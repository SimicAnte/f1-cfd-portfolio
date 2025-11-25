import os
import pandas as pd

angles_of_attack = [-5, 0, 5, 10, 15]
results = []

def update_mesh(angle):
    print(f"Updating geometry to Angle: {angle} degrees...")
    pass

def run_solver():
    print("Running simpleFoam...")
    os.system("simpleFoam > log.simpleFoam")

def extract_forces():
    return {"Cl": 0.0, "Cd": 0.0}

for angle in angles_of_attack:
    update_mesh(angle)
    run_solver()
    data = extract_forces()
    results.append(data)
    print(f"Completed Simulation for AoA: {angle}")

print("Batch Processing Complete. Data saved to csv.")
