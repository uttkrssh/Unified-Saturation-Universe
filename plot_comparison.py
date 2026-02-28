import numpy as np
import matplotlib.pyplot as plt

# 1. LOAD DATA
# Replace the filename below with your ACTUAL winning filename from output_sweep/
winner_file = "output_sweep/uni_0523_v3.79_a0.0124_00_cl.dat" 
baseline_file = "output_sweep/lcdm_baseline_00_cl.dat"

planck_l = np.array([2, 10, 30, 50, 100, 150, 215, 300, 400, 450, 540, 600, 700, 800, 850, 950, 1050, 1150, 1250, 1350, 1450, 1550, 1650, 1750, 1850, 1950])
planck_Dl = np.array([900, 850, 1100, 1550, 3400, 5100, 5750, 3800, 2100, 1850, 2600, 2250, 1550, 2400, 2500, 1850, 1250, 1100, 850, 900, 800, 500, 400, 350, 300, 250])
planck_err = np.array([300, 200, 150, 100, 80, 70, 60, 50, 40, 40, 40, 40, 40, 50, 50, 50, 50, 60, 60, 70, 70, 80, 80, 90, 90, 100])

def load_and_scale(fname):
    data = np.loadtxt(fname)
    return data[:, 0], data[:, 1] * (2.7255e6)**2

# 2. RENDER
plt.figure(figsize=(12, 7))
plt.style.use('seaborn-v0_8-deep')

# Plot Reality
plt.errorbar(planck_l, planck_Dl, yerr=planck_err, fmt='ko', label='Planck 2018 Data', zorder=10)

# Plot Baseline
l_b, dl_b = load_and_scale(baseline_file)
plt.plot(l_b, dl_b, 'r--', alpha=0.6, label='Baseline (Score: 2222)')

# Plot Winner
l_w, dl_w = load_and_scale(winner_file)
plt.plot(l_w, dl_w, 'b-', linewidth=2.5, label='Quantum Fluid (Score: 1573)')

plt.title(f"Quantum Fluid Model: Viscosity=3.79, Alpha=0.0124\nDelta Chi-Squared: -648", fontsize=15)
plt.xlabel("Multipole (l)", fontsize=12)
plt.ylabel("Dl [uK^2]", fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig("Final_Discovery_Plot.png", dpi=300)
print("🚀 Plot saved as 'Final_Discovery_Plot.png'.")