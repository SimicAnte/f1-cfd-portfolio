# F1 Aerodynamics & CFD Portfolio
**Author:** Ante Šimić | **Role:** Engineering Physicist & DevOps Engineer

## Overview
This repository documents my work in Computational Fluid Dynamics (CFD) using OpenFOAM, with a focus on motorsport aerodynamics. As an engineer with a background in both **Physics** and **DevOps**, my goal is not just to run simulations, but to build **automated and scalable workflows** that accelerate the aerodynamic design cycle.

## Project Roadmap

### 1. Ahmed Body Validation Study (In Progress)
**Objective:** Validate OpenFOAM settings against standard wind tunnel experimental data.
- **Solver:** `simpleFoam` (Steady-state RANS, k-omega SST turbulence model)
- **Methodology:**
    - Mesh independence study (Coarse: 2M, Medium: 4M, Fine: 8M cells)
    - Validation at 25° and 35° slant angles
    - Comparison of Drag Coefficient (Cd) vs. Ahmed (1984) experimental data
- **Current Status:** Mesh generation pipeline setup.

### 2. Automated Parametric Wing Analysis (Planned)
**Objective:** Demonstrate Python automation for CFD batch processing.
- **Goal:** Eliminate manual case setup for routine parameter sweeps.
- **Toolchain:** Python + Bash + OpenFOAM.
- **Workflow:**
    1. Python script modifies Angle of Attack (AoA) in `blockMeshDict` / CAD.
    2. Automatically generates mesh and executes solver.
    3. Extracts Lift (Cl) and Drag (Cd) coefficients.
    4. Plots L/D polar curves automatically.

### 3. Front Wing Ground Effect Study (Planned)
**Objective:** Analyze the sensitivity of front wing downforce to ride height changes.
- **Focus:** Simulating the "ground effect" phenomenon critical to F1 performance.
- **Test Matrix:** Ride heights of 20mm, 40mm, 60mm, 80mm.
- **Post-Processing:** Visualization of pressure distribution and wing tip vortices using ParaView.

---
*This portfolio is actively updated. Code and case files will be pushed as validation stages are completed.*
