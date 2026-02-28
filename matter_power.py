import os
import subprocess
import numpy as np
import matplotlib.pyplot as plt

# Your winning parameters
VISC = 3.79
ALPHA = 0.0124

def run_matter_spectrum():
    run_id = "matter_check"
    ini_path = f"{run_id}.ini"
    root_path = f"output_sweep/{run_id}_"
    
    # We add 'mPk' to the output to get the Matter Power Spectrum
    ini_content = f"""
h = 0.6732
omega_b = 0.02237
omega_cdm = 1e-15
Omega_Lambda = 0.0
A_s = 2.1e-9
n_s = 0.965
tau_reio = 0.054
gauge = newtonian
output = tCl, mPk
P_k_max_h/Mpc = 1.0
z_max_pk = 0
qf_A = 0.6847
qf_B = 0.3153
qf_alpha = {ALPHA}
qf_viscosity = {VISC}
root = {root_path}
"""
    with open(ini_path, "w") as f:
        f.write(ini_content)
    
    print("🚀 Simulating Matter Power Spectrum...")
    subprocess.run(["./class", ini_path], check=True)
    
    # CLASS outputs matter power spectrum in a file ending in pk.dat
    pk_file = f"{root_path}00_pk.dat" 
    data = np.loadtxt(pk_file)
    return data[:, 0], data[:, 1] # k (h/Mpc), P(k)

# Execute and Plot
k, pk = run_matter_spectrum()

plt.figure(figsize=(10, 6))
plt.loglog(k, pk, color='forestgreen', linewidth=2)
plt.title(f"Matter Power Spectrum: Visc={VISC}, Alpha={ALPHA}", fontsize=14)
plt.xlabel("Wavenumber k [h/Mpc]", fontsize=12)
plt.ylabel("P(k) [(Mpc/h)^3]", fontsize=12)
plt.grid(True, which="both", ls="-", alpha=0.2)
plt.savefig("Matter_Power_Spectrum.png", dpi=300)
print("✅ Matter Power Spectrum saved as 'Matter_Power_Spectrum.png'.")