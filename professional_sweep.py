import os
import subprocess
import shutil
import glob
import numpy as np
from concurrent.futures import ProcessPoolExecutor

# ==============================================================================
# 1. SETTINGS
# ==============================================================================
SWEEP_DIR = "output_sweep"
TOTAL_UNIVERSES = 1000
# We use a broad range for viscosity and alpha to capture the full physics
VISC_RANGE = (0.0, 10.0) 
ALPHA_RANGE = (0.0001, 0.1)

BASE_INI = """
h = 0.6732
omega_b = 0.02237
omega_cdm = 1e-15
Omega_Lambda = 0.0
A_s = 2.1e-9
n_s = 0.965
tau_reio = 0.054
gauge = newtonian
output = tCl
"""

# ==============================================================================
# 2. GENERATOR LOGIC
# ==============================================================================
def setup_environment():
    if os.path.exists(SWEEP_DIR):
        shutil.rmtree(SWEEP_DIR)
    os.makedirs(SWEEP_DIR)

def run_universe(index):
    # Use random sampling to explore the 2D parameter space efficiently
    visc = np.random.uniform(*VISC_RANGE)
    alpha = np.random.uniform(*ALPHA_RANGE)
    
    run_id = f"uni_{index:04d}_v{visc:.2f}_a{alpha:.4f}"
    root_path = f"{SWEEP_DIR}/{run_id}_"
    ini_path = f"{SWEEP_DIR}/{run_id}.ini"
    
    # Injected Quantum Fluid Equations
    ini_content = BASE_INI + f"""
qf_A = 0.6847
qf_B = 0.3153
qf_alpha = {alpha}
qf_viscosity = {visc}
root = {root_path}
"""
    with open(ini_path, "w") as f:
        f.write(ini_content)
    
    try:
        # Running CLASS
        subprocess.run(["./class", ini_path], stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, check=True)
        return True
    except:
        return False

# ==============================================================================
# 3. EXECUTION
# ==============================================================================
if __name__ == '__main__':
    setup_environment()
    print(f"🚀 Launching Parallel Factory: Generating {TOTAL_UNIVERSES} Universes...")
    
    success_count = 0
    # Change max_workers to match your CPU cores (e.g., 4, 8, or 16)
    with ProcessPoolExecutor(max_workers=None) as executor:
        results = list(executor.map(run_universe, range(TOTAL_UNIVERSES)))
        success_count = sum(results)
            
    print(f"\n✅ Done! {success_count}/{TOTAL_UNIVERSES} universes simulated successfully.")
    print(f"Check the '{SWEEP_DIR}' folder for your .dat files.")