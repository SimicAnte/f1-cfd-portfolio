# Heated Pipe Conjugate Heat Transfer (CHT) Benchmark

**Automated thermohydraulic validation case (Re=40k)** demonstrating conjugate heat transfer (fluid-solid coupling) for nuclear cooling applications using OpenFOAM.

## Project Overview
This project validates a turbulent pipe flow simulation with coupled heat transfer against standard engineering correlations (Dittus-Boelter). It demonstrates:
- **Conjugate Heat Transfer (CHT)**: Solving fluid thermodynamics and solid conduction simultaneously.
- **Structured Meshing**: High-quality O-Grid hexahedral mesh generation using `blockMesh`.
- **Automation**: Python-driven parametric sweeps for Reynolds number sensitivity.
- **Validation**: Comparison of Nusselt number ($Nu$) and heat transfer coefficient ($h$) against theoretical benchmarks.

## Physics & Methodology
| Parameter | Value | Description |
|-----------|-------|-------------|
| **Fluid** | Water | Incompressible, Turbulent ($Re \approx 40,000$) |
| **Solid** | Steel | 2mm thick wall, constant heat flux ($q'' = 10 kW/m^2$) |
| **Solver** | `chtMultiRegionFoam` | Transient PIMPLE solver for multi-region heat transfer |
| **Turbulence** | $k-\omega$ SST | Accurate near-wall heat transfer prediction |
| **Mesh** | O-Grid | 2-Region (Fluid/Solid), fully hexahedral |

### Key Physics Captured
1. **Thermal Boundary Layer**: Resolved with near-wall refinement ($y^+ < 5$).
2. **Solid Conduction**: Radial heat conduction through the pipe wall.
3. **Fluid-Solid Coupling**: Implicit temperature and heat flux matching at the interface using `turbulentTemperatureCoupledBaffleMixed` boundary condition.

## Repository Structure
- `case/`: OpenFOAM simulation case files (v13 compatible).
  - `system/blockMeshDict`: Parametric O-grid mesh definition.
  - `0/`: Initial boundary conditions for Fluid (U, p, T) and Solid (T).
- `automation/`: Python scripts for running parametric sweeps.
- `validation/`: Jupyter notebooks comparing simulation results to Dittus-Boelter.

## Usage
### 1. Mesh Generation
The mesh uses a multi-block O-grid strategy to avoid centerline singularities and ensure orthogonal cells.
```bash
cd case
blockMesh
splitMeshRegions -cellZones -overwrite
checkMesh