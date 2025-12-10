# Simulation Plan: Ahmed Body Validation

## Objective
Validate OpenFOAM v13 RANS turbulence models against experimental data (Ahmed et al., 1984) to establish a baseline for automotive aerodynamic CFD.

## Status: Completed !
*   **Simulation:** Successfully converged (500 iterations).
*   **Mesh:** 238k cells, non-orthogonality < 47 (Mesh OK).
*   **Visualization:** Velocity fields and pressure contours captured.

## Case Setup
*   **Geometry:** Standard Ahmed Body (Length = 1.044m)
*   **Slant Angle:** 25°
*   **Domain:**
    *   Inlet: 2L upstream
    *   Outlet: 5L downstream
    *   Cross-section: Large enough to minimize blockage effects

## Physics & Solver (OpenFOAM v13)
*   **Solver:** `foamRun` (incompressibleFluid module) - *Supersedes `simpleFoam`*
*   **Turbulence Model:** `kOmegaSST`
*   **Inlet Velocity:** 40 m/s
*   **Reynolds Number:** Re ≈ 4.3 x 10^6
*   **Wall Functions:** Used for `k`, `omega`, and `nut` (Standard wall functions)

## Mesh Strategy
*   **Tool:** `snappyHexMesh`
*   **Base Mesh:** `blockMesh` (Background grid)
*   **Refinement:**
    *   Box refinement around the car
    *   Surface-based refinement (Level 3-4)
    *   Feature edge extraction (`surfaceFeatures`)
*   **Final Mesh Stats:** ~238,000 cells

## Validation Targets
| Parameter | Experimental | CFD Target | Status |
| :--- | :--- | :--- | :--- |
| Drag Coeff (25°) | 0.285 | ± 5% | Pending Calculation |
| Lift Coeff | - | Monitor | Pending Calculation |