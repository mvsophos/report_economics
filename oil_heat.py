# oil_sector_pie.py
import matplotlib.pyplot as plt

# EIA 2023: U.S. petroleum consumption by sector (million barrels per day)
# https://www.eia.gov/totalenergy/data/monthly/
sectors = ['Транспорт', 'Промышленность', 'Жилой/коммерч.', 'Электроэнергия']
values  = [68.0, 26.5, 9.5, 3.0]          # % of total (≈100%)
colors  = ['#b8860b', '#4682b4', '#d62728', '#2ca02c']

fig, ax = plt.subplots(figsize=(4, 3))
wedges, texts, autotexts = ax.pie(
    values, labels=sectors, autopct='%1.0f%%',
    colors=colors, startangle=140, pctdistance=0.85
)
for t in autotexts:
    t.set_fontsize(9)
    t.set_fontweight('bold')
ax.set_title('Нефть: конечное потребление по секторам (EIA 2023)', fontsize=11)
plt.tight_layout()
plt.savefig('oil_sector_pie.pdf', dpi=300)
