import os
import subprocess
import shutil
import re

# --- Configuration ---
CASE_DIR = "../case"
RESULTS_FILE = "sweep_results.csv"

# Physics Parameters
D_PIPE = 0.02828    # Hydraulic Diameter [m] (Based on 14.14mm radius)
RHO = 1000.0        # Density [kg/m3]
MU_BULK = 0.000855  # Viscosity at 300K [Pa.s]
TARGET_RE = [20000, 40000, 60000] # The Sweep Target Reynolds Numbers

def calculate_velocity(Re):
    # Re = (rho * U * D) / mu  ->  U = (Re * mu) / (rho * D)
    return (Re * MU_BULK) / (RHO * D_PIPE)

def update_velocity_file(velocity):
    """Edit 0/fluid/U to set the new inlet velocity"""
    u_file = os.path.join(CASE_DIR, "0/fluid/U")
    with open(u_file, 'r') as f:
        content = f.read()
    
    new_val = f"uniform (0 0 {velocity:.4f})"
    
    content = re.sub(r'uniform\s*\(\s*0\s+0\s+[\d\.]+\s*\)', new_val, content)
    
    with open(u_file, 'w') as f:
        f.write(content)
    print(f" --> Updated U to {velocity:.4f} m/s")

def clean_case():
    """Remove result directories to ensure a fresh run"""
    print(" --> Cleaning case...")
    subprocess.run("rm -rf [1-9]* postProcessing", shell=True, cwd=CASE_DIR)

def run_solver():
    """Runs the OpenFOAM solver"""
    print(" --> Running chtMultiRegionFoam ...")

    with open(os.path.join(CASE_DIR, "solver.log"), "w") as log:
        subprocess.run(["chtMultiRegionFoam"], cwd=CASE_DIR, stdout=log, stderr=log)

def extract_data(Re):
    """Read postProcessing files to get Q_wall and T_wall"""
    try:
        # 1. Get Heat Flux (Last value)
        flux_file = os.path.join(CASE_DIR, "postProcessing/fluid/calcHeatFlux/0/wallHeatFlux.dat")
        with open(flux_file, 'r') as f:
            lines = [l for l in f.readlines() if not l.startswith('#')]
            # Format: Time patch min max Q q
            last_line = lines[-1].split()
            q_wall = float(last_line[5])

        # 2. Get Wall Temp (Last value)
        temp_file = os.path.join(CASE_DIR, "postProcessing/fluid/avgWallTemp/0/surfaceFieldValue.dat")
        with open(temp_file, 'r') as f:
            lines = [l for l in f.readlines() if not l.startswith('#')]
            # Format: Time value
            last_line = lines[-1].split()
            T_wall = float(last_line[1])
            
        # 3. Get Inlet/Outlet Temp (for Bulk)
        bulk_file = os.path.join(CASE_DIR, "postProcessing/fluid/inletOutletTemp/0/surfaceFieldValue.dat")
        with open(bulk_file, 'r') as f:
            lines = [l for l in f.readlines() if not l.startswith('#')]
            last_line = lines[-1].split()
            # If average of inlet/outlet is one column:
            T_bulk = float(last_line[1])

        return q_wall, T_wall, T_bulk

    except Exception as e:
        print(f"  ERROR reading results: {e}")
        return None, None, None

def main():
    # Initialize results file
    with open(RESULTS_FILE, 'w') as f:
        f.write("Target_Re,Velocity,q_wall,T_wall,T_bulk,h_cfd,Nu_cfd\n")

    print("=== Starting Parametric Sweep ===")
    
    for Re in TARGET_RE:
        U = calculate_velocity(Re)
        print(f"\n--- Running Case: Re = {Re} (U = {U:.4f} m/s) ---")
        
        clean_case()
        update_velocity_file(U)
        run_solver()
        
        q, Tw, Tb = extract_data(Re)
        
        if q is not None:
            h_cfd = q / (Tw - Tb)
            k_fluid = 0.613 # Thermal conductivity at ~300K
            Nu_cfd = (h_cfd * D_PIPE) / k_fluid
            
            print(f"  -> Result: Nu = {Nu_cfd:.2f}")
            
            with open(RESULTS_FILE, 'a') as f:
                f.write(f"{Re},{U},{q},{Tw},{Tb},{h_cfd},{Nu_cfd}\n")
        else:
            print("  -> Failed to extract data.")

    print("\n=== Sweep Complete. Data saved to sweep_results.csv ===")

if __name__ == "__main__":
    main()
