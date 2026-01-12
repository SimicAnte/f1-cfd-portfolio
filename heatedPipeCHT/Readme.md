# Heated Pipe Conjugate Heat Transfer (CHT) Benchmark


> **Note to Reviewers:** I am currently finalizing the post-processing and documentation for this case study. The complete Analysis Report (PDF) and flow visualizations will be available by **January 15th**.


**Turbulent thermohydraulic validation case (Re ≈ 40,000)** demonstrating conjugate heat transfer (fluid-solid coupling) for industrial cooling applications using OpenFOAM.

![Simulation Preview](https://via.placeholder.com/800x400?text=Insert+Paraview+Screenshot+Here)
*(Add a slice view of Temperature or Velocity magnitude here)*

## Project Overview
This project validates a high-fidelity turbulent pipe flow simulation with coupled heat transfer against standard engineering correlations (**Dittus-Boelter**). It was developed to demonstrate proficiency in:
- **Conjugate Heat Transfer (CHT):** Simultaneous solution of fluid thermodynamics and solid thermal conduction.
- **Turbulence Modeling:** Correct application of the **$k-\omega$ SST** model with **compressible wall functions** (`alphatJayatilleke`) for accurate near-wall heat transfer.
- **Structured Meshing:** High-quality **O-Grid hexahedral meshing** with `blockMesh` (L/D = 50) to capture entrance length effects.
- **Validation:** Achieving **<11% deviation** from theoretical benchmarks, accurately capturing thermally developing flow physics.

## Physics & Methodology

| Parameter | Value | Description |
|-----------|-------|-------------|
| **Fluid** | Water | Incompressible, Turbulent ($Re \approx 40,000$, $Pr \approx 6.6$) |
| **Solid** | Steel | 2mm thick wall, constant heat flux ($q'' \approx 12 kW/m^2$) |
| **Solver** | `chtMultiRegionFoam` | Transient PIMPLE solver for multi-region heat transfer |
| **Turbulence** | $k-\omega$ SST | Selected for superior near-wall resolution vs $k-\epsilon$ |
| **Mesh** | 800k Cells | Full O-Grid, $L=5m$, $y^+ < 5$ (Resolved Boundary Layer) |

### Key Challenges Solved
1. **Laminar-to-Turbulent Transition:** Overcame initial solver limitations where `momentumTransport` defaulted to laminar, correcting the setup to fully activate the $k-\omega$ SST turbulence budget.
2. **Wall Functions:** Implemented `compressible::alphatJayatillekeWallFunction` to correctly model the thermal sublayer for high-Prandtl number fluids (Water).
3. **Entrance Length Effects:** Extended the domain to **50 Diameters (5m)** to capture the transition from developing to fully developed thermal flow.

## Results & Validation

The simulation results were validated against the **Dittus-Boelter correlation** ($Nu = 0.023 Re^{0.8} Pr^{0.4}$).

| Metric | Simulation Result | Theoretical Target | Deviation |
|--------|------------------:|-------------------:|----------:|
| **Wall Heat Flux** ($q_{wall}$) | $12,001 \ W/m^2$ | $12,000 \ W/m^2$ | N/A (BC) |
| **Wall Temp** ($T_{wall}$) | $301.71 \ K$ | - | - |
| **Bulk Temp** ($T_{bulk}$) | $300.11 \ K$ | - | - |
| **Heat Transfer Coeff** ($h$) | **$7,500 \ W/m^2K$** | **$6,790 \ W/m^2K$** | **+10.5%** |

**Physics Note:** The +10% deviation is physically expected. The Dittus-Boelter correlation assumes *fully developed* flow ($L/D > 60$). Our domain ($L/D = 50$) includes the thermal entrance region where the boundary layer is thinner and heat transfer is naturally higher, raising the average $h$.

## 📂 Repository Structure
```bash
├── case/                   # OpenFOAM simulation case (v13/v2306 compatible)
│   ├── system/             # Mesh (blockMeshDict) and Solver settings
│   ├── constant/           # Physics properties (Water, Steel, Turbulence)
│   └── 0/                  # Initial Boundary Conditions (U, p, T, k, omega)
├── automation/             # (Optional) Python scripts for parametric sweeps
└── validation/             # Validation data and comparison charts
