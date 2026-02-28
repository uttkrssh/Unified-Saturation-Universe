import os
import subprocess
import re

# The surgical micro-viscosity grid
nu_grid = [0.005, 0.05, 0.1, 0.2]

# The baseline configuration
ini_template = """h = 0.6732
omega_b = 0.02237
omega_cdm = 1e-15
Omega_Lambda = 0.0
A_s = 2.1e-9
n_s = 0.965
tau_reio = 0.054
qf_A = 0.68
qf_B = 0.32
qf_alpha = 0.0005
output = mPk, tCl, lCl
lensing = yes
P_k_max_h/Mpc = 10.0
z_max_pk = 0.0
spectra_verbose = 2
"""

print("=== STARTING RAW C-EXECUTABLE SWEEP ===\n")

for nu in nu_grid:
    # Notice the newline='\n' - this completely blocks the Windows formatting bug!
    with open("sweep_temp.ini", "w", newline='\n') as f:
        f.write(ini_template)
        f.write(f"qf_viscosity = {nu}\n\n") # Double newline at the end to satisfy the parser
    
    print(f"Firing engine for qf_viscosity = {nu} ...")
    
    # Run the C-executable and capture the terminal output
    process = subprocess.run(["./class", "sweep_temp.ini"], capture_output=True, text=True)
    
    # Hunt for the sigma8 value in the output
    match = re.search(r'sigma8=([\d\.]+)', process.stdout)
    
    if match:
        sig8 = float(match.group(1))
        print(f"--> Extracted sigma_8: {sig8:.4f}")
        
        # The S_8 Tension "Goldilocks" Check
        if 0.75 <= sig8 <= 0.81:
            print("    *** S_8 TENSION TARGET HIT! ***")
    else:
        print("--> ERROR: Could not find sigma_8 in output.")
        print("    Tail of output:", process.stdout[-300:])
        if process.stderr:
            print("    Error output:", process.stderr)
            
    print("-" * 40)

# Clean up
if os.path.exists("sweep_temp.ini"):
    os.remove("sweep_temp.ini")
    
print("\nSweep Complete.")
