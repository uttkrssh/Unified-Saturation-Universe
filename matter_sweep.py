import os
import subprocess
import re

# ==============================================================================
# 1. DEFINE THE PARAMETER GRID & BASE INI
# ==============================================================================
nu_grid = [0.005, 0.05, 0.1, 0.2]

# Notice we set spectra_verbose = 2 so CLASS prints sigma8 to the terminal
ini_template = """
h = 0.6732
omega_b = 0.02237
omega_cdm = 1e-15
Omega_Lambda = 0.0
A_s = 2.1e-9
n_s = 0.965
tau_reio = 0.054

qf_A = 0.68
qf_B = 0.32
qf_alpha = 0.0005

output = tCl, pCl, lCl, mPk
lensing = yes
P_k_max_h/Mpc = 10.0
z_max_pk = 0.0

spectra_verbose = 2
root = output/vqf_sweep_
"""

print("=== STARTING RAW C-EXECUTABLE SWEEP ===\n")

# ==============================================================================
# 2. RUN THE SWEEP LOOP
# ==============================================================================
for nu in nu_grid:
    # A. Write the temporary .ini file
    with open("sweep_temp.ini", "w") as f:
        f.write(ini_template)
        f.write(f"qf_viscosity = {nu}\n")
    
    print(f"Firing engine for qf_viscosity = {nu} ...")
    
    # B. Command the OS to run the CLASS C-executable
    # capture_output=True intercepts all the text CLASS prints to the terminal
    process = subprocess.run(["./class", "sweep_temp.ini"], capture_output=True, text=True)
    
    # C. Hunt for sigma8 in the terminal output using Regular Expressions
    # CLASS typically prints: "sigma8=0.8123..." or "sigma_8=..."
    match = re.search(r'sigma8=([\d\.]+)', process.stdout)
    
    if match:
        sig8 = float(match.group(1))
        print(f"--> Extracted sigma_8: {sig8:.4f}")
        
        # The S_8 Tension "Goldilocks" Check
        if 0.75 <= sig8 <= 0.81:
            print( "    *** S_8 TENSION TARGET HIT! ***")
    else:
        print(sig8, "--> ERROR: Could not find sigma_8 in output.")
        # If it fails, this will print the error CLASS threw (e.g., a typo in variable names)
        print("    Tail of CLASS output:", process.stdout[-500:])
    print("-" * 40)

# Clean up the temporary file
if os.path.exists("sweep_temp.ini"):
    os.remove("sweep_temp.ini")
    
print("\nSweep Complete.")