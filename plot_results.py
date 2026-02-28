import matplotlib.pyplot as plt
import numpy as np

# Load the Quantum Fluid data - updated with the correct filename
# Column 0: multipole l, Column 1: TT power spectrum
try:
    data = np.loadtxt('output/test_quantum_fluid00_cl.dat')
    l = data[:,0]
    tt = data[:,1]

    plt.figure(figsize=(10, 6))

    # Plotting the Temperature (TT) Spectrum
    # Using a raw string r'' to fix the LaTeX math warning
    plt.plot(l, tt, label='Quantum Fluid Model', color='#1f77b4', linewidth=2)

    plt.yscale('linear')
    plt.xlabel('Multipole Moment ($l$)', fontsize=12)
    plt.ylabel(r'$D_l^{TT} [\mu K^2]$', fontsize=12)
    plt.title('CMB Temperature Power Spectrum\nUnified Saturation Universe', fontsize=14)
    plt.legend()
    plt.grid(True, which='both', linestyle='--', alpha=0.5)

    plt.savefig('quantum_fluid_spectrum.png', dpi=300)
    print("Success! Your discovery plot is saved as 'quantum_fluid_spectrum.png'.")

except FileNotFoundError:
    print("Error: Could not find 'output/test_quantum_fluid00_cl.dat'.")
    print("Check your 'output/' folder to verify the exact filename.")
