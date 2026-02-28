Unified Saturation Universe: A Quantum Fluid Approach🌌
Overview 

This repository contains a modified version of the Cosmic Linear Anisotropy Solving System (CLASS). The project introduces the Unified Saturation Universe theory, which models the early universe as a macroscopic quantum fluid rather than a collection of discrete particles.By modifying the core C-based Boltzmann equations within CLASS, this model simulates how quantum pressure and density saturation points affect the Cosmic Microwave Background (CMB) and the growth of large-scale structures.🛠 Features & ModificationsTo implement this theory, I performed the following modifications to the public CLASS source code:
background.c: Modified the background evolution to include a custom energy-momentum tensor for the quantum fluid, altering the Hubble expansion history $H(z)$.

perturbations.c: Implemented scale-dependent sound speed $c_s(k)$ to model quantum pressure. This effectively suppresses small-scale power, addressing the "Missing Satellites Problem" in standard $\Lambda$CDM.

input.c: Added new input parameters for fluid viscosity and saturation density limits to allow for easy testing of different cosmological scenarios.

🧪 Scientific Theory: Unified Saturation unlike standard Cold Dark Matter (CDM), which is pressureless, the Unified Saturation model assumes:
Superfluid Properties: The early universe plasma exhibits zero-viscosity flow.
Density Saturation: A non-singular evolution of the scale factor by enforcing a maximum density threshold via quantum effects.
BEC Analogy: Treating dark matter as a Bose-Einstein Condensate to explain the "core-cusp" problem in galactic centers.

🚀 Installation & UsageTo run this modified version, you must have a C compiler and the standard CLASS dependencies installed.
Bash 

# Clone the repository
git clone https://github.com/uttkrssh/Unified-Saturation-Universe.git

# Navigate to the directory
cd Unified-Saturation-Universe

# Compile the modified C code
make class

# Run with the quantum fluid parameter file
./class explanatory_quantum_fluid.ini

📊 Results: The following plots illustrate the difference between the standard $\Lambda$CDM model and the Unified Saturation model:
CMB Power Spectrum: Notable shifts in the higher-order acoustic peaks.
Matter Power Spectrum: Significant suppression of power at $k > 10 \text{ h/Mpc}$.

📚 References: CLASS: Cosmic Linear Anisotropy Solving System - Blas, Lesgourgues, and Tram (2011) Unified Saturation Model - Independent Research Paper (2025)
