import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# --- Parameters ---
RESULTS_FILE = "sweep_results.csv"
Pr = 7.0 # Prandtl number for Water

def dittus_boelter(Re):
    # Nu = 0.023 * Re^0.8 * Pr^0.4
    return 0.023 * (Re**0.8) * (Pr**0.4)

def main():
    try:
        # Load Data
        df = pd.read_csv(RESULTS_FILE)
        
        # Calculate Theoretical Nu for comparison
        Re_range = np.linspace(min(df['Target_Re'])*0.9, max(df['Target_Re'])*1.1, 100)
        Nu_theory = dittus_boelter(Re_range)
        
        # Plotting
        plt.figure(figsize=(8, 6))
        
        # Plot Theory Line
        plt.plot(Re_range, Nu_theory, 'k--', label="Dittus-Boelter Correlation", linewidth=2)
        
        # Plot CFD Points
        plt.plot(df['Target_Re'], df['Nu_cfd'], 'ro', label="OpenFOAM CFD", markersize=8, markeredgecolor='k')
        
        # Formatting
        plt.title("Nusselt Number Validation: CFD vs Theory", fontsize=14)
        plt.xlabel("Reynolds Number (Re)", fontsize=12)
        plt.ylabel("Nusselt Number (Nu)", fontsize=12)
        plt.grid(True, which='both', linestyle='--', alpha=0.7)
        plt.legend(fontsize=12)
        
        # Save Plot
        plt.tight_layout()
        plt.savefig("validation_plot.png", dpi=300)
        print("Plot saved as 'validation_plot.png'")
        
        # Print Comparison Table
        print("\n--- Validation Summary ---")
        print(f"{'Re':<10} | {'Nu CFD':<10} | {'Nu Theory':<10} | {'Error %':<10}")
        print("-" * 46)
        for _, row in df.iterrows():
            Re_val = row['Target_Re']
            Nu_c = row['Nu_cfd']
            Nu_t = dittus_boelter(Re_val)
            err = abs(Nu_c - Nu_t)/Nu_t * 100
            print(f"{int(Re_val):<10} | {Nu_c:<10.2f} | {Nu_t:<10.2f} | {err:<10.2f}")

    except FileNotFoundError:
        print(f"Error: Could not find {RESULTS_FILE}. Run the sweep script first.")

if __name__ == "__main__":
    main()
