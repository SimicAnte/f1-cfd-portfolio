# Simulation Plan: Ahmed Body Validation

## Objective
Validate OpenFOAM RANS turbulence models against experimental data (Ahmed et al., 1984).

## Case Setup
*   **Geometry:** Standard Ahmed Body (Length = 1.044m)
*   **Slant Angles:** 25° (Attached flow) and 35° (Separated flow)
*   **Domain:**
    *   Inlet: 2L upstream
    *   Outlet: 5L downstream
    *   Height/Width: Sufficient to keep blockage < 5%

## Physics & Solver
*   **Solver:** `simpleFoam` (Steady-state incompressible)
*   **Turbulence Model:** `kOmegaSST` (Standard for external aero)
*   **Inlet Velocity:** 40 m/s
*   **Reynolds Number:** Re ≈ 4.29 x 10^6

## Mesh Strategy
*   **Tool:** `snappyHexMesh`
*   **Layering:** 5 prism layers (Expansion ratio 1.2) to resolve boundary layer
*   **Target y+:** 30 < y+ < 300 (Wall functions)

## Validation Targets
| Parameter | Experimental | Target CFD |
| :--- | :--- | :--- |
| Drag Coeff (25°) | 0.285 | ± 5% |
| Drag Coeff (35°) | 0.250 | ± 5% |
