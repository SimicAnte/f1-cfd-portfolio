# Study Brief: Front Wing in Ground Effect

## Introduction
This project investigates the sensitivity of downforce (Cl) and drag (Cd) as a wing profile approaches the ground plane, a critical phenomenon in F1 front wing design.

## The Physics (Ground Effect)
As the ride height (h) decreases, we expect:
1.  **Force Enhancement:** Downforce increases due to flow acceleration between the suction side and the ground (Venturi effect).
2.  **Stall Phenomenon:** At a critical height (h/c), the boundary layer on the suction side separates due to adverse pressure gradients, causing a sharp loss in downforce ("force reduction phenomenon").

## Simulation Matrix
*   **Airfoil:** NACA 4412 (High lift cambered profile)
*   **Chord (c):** 0.25m
*   **Test Heights (h):**
    *   h = 100mm (Free stream reference)
    *   h = 50mm
    *   h = 20mm
    *   h = 10mm (Expected separation onset)

## Post-Processing Goals
*   Plot Cl vs. Ride Height (h/c).
*   Visualize surface pressure coefficients (Cp) on the ground plane.
*   Visualize velocity streamlines to identify separation bubbles at low ride heights.
