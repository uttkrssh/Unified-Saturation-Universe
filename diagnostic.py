import subprocess

# We are including 'mPk' (Matter Power Spectrum) and 'z_max_pk'
ini_content = """h = 0.6732
omega_b = 0.02237
omega_cdm = 1e-15
Omega_Lambda = 0.0
A_s = 2.1e-9
n_s = 0.965
tau_reio = 0.054
qf_A = 0.68
qf_B = 0.32
qf_alpha = 0.0005
qf_viscosity = 0.005
output = tCl, pCl, lCl, mPk
lensing = yes
z_max_pk = 0.0
P_k_max_h/Mpc = 10.0
spectra_verbose = 3
"""

# Force strict Linux formatting
with open("diagnostic_test.ini", "w", newline='\n') as f:
    f.write(ini_content)

print("Executing CLASS Engine...\n")

# Run the engine and capture EVERY channel (stdout and stderr)
run = subprocess.run(["./class", "diagnostic_test.ini"], capture_output=True, text=True)

print("=== ENGINE STANDARD OUTPUT (Last 20 Lines) ===")
if run.stdout.strip():
    lines = run.stdout.strip().split('\n')
    for line in lines[-20:]:
        print(line)
else:
    print("[No Standard Output - The engine was completely silent]")

print("\n=== ENGINE ERROR LOG ===")
if run.stderr.strip():
    print(run.stderr)
else:
    print("[No Errors Found]")
