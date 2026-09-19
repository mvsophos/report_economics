import matplotlib.pyplot as plt
import numpy as np

years = np.array([1998, 2000, 2002, 2004, 2006, 2008])
ratio = np.array([0.62, 0.58, 0.38, 0.34, 0.30, 0.32])

fig, ax = plt.subplots(figsize=(5, 3.5))
ax.plot(years, ratio, 'o-', color='#1f77b4', linewidth=2, markersize=6,
        label='Observed / Natural flow (Murray–Darling)')
ax.axhline(y=0.32, color='#d62728', linestyle='--', linewidth=2,
           label='Cap (1995) — median 1998–2008')
ax.set_xlabel('Year')
ax.set_ylabel('Observed / Natural flow')
ax.set_title('Murray River at Swan Hill: flow reduction during Millennium Drought')
ax.legend()
ax.grid(True, alpha=0.3)
ax.set_ylim(0.25, 0.7)
plt.tight_layout()
plt.savefig('murray_flow_ratio.pdf', dpi=300)
