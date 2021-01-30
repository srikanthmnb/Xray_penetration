## This simulates the incident X-ray penetration depth and transmittivity as a function of Qz for vapor-liquid (water) interface.
## Srikanth Nayak

import numpy as np
from matplotlib import pyplot as plt

#X-ray energy
Energy = 17300 #eV
hc = 1.23984193* 1E4 #eV A
wavelength = hc/Energy
k = 2*np.pi/wavelength

#Material properties for water at 17.3keV
delta = 7.7057e-7 
beta=5.7821e-10

Q_critical = 2*k*(2*delta)**0.5
b_mu = (2*k/Q_critical)**2 * beta

Q = np.linspace(0.01,0.035,250)
q = Q/Q_critical
q_prime = (q**2 -1 + 2j * b_mu)**0.5
t_q = 2*q/(q+q_prime)
penetration_depth = 1/Q_critical/np.imag(q_prime)
I_transmitted = np.absolute(t_q) ** 2

fig, ax1 = plt.subplots(figsize=[5,4])
color = 'tab:red'
ax1.set_xlabel(r'$Q, \AA^{-1}$', fontsize=14)
ax1.set_ylabel(r'$t_{f}^2$', color=color, fontsize=14)
ax1.plot(Q, I_transmitted, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel(r'Penetration depth, $\AA$', color=color, fontsize = 14)  # we already handled the x-label with ax1
ax2.plot(Q, penetration_depth, color=color)
ax2.tick_params(axis='y', labelcolor=color)
ax2.set_yscale('log')

fig.tight_layout()  # otherwise the right y-label is slightly clipped
fig.savefig('xray_penetration.jpg', bbox_inches = 'tight')
