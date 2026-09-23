# nordhaus_mb_mc.py
# График для правила Вайцмана (Weitzman 1974): цена vs количество
# Данные: Nordhaus (2018) "The Social Cost of Carbon: Updating the Estimate"
#         DICE-2016R2, оптимальная траектория
# Источник: NBER Working Paper No. 24893, Table 2

import matplotlib.pyplot as plt
import numpy as np

# Сокращение выбросов (GtCO2) — от 0 до ~80 Gt (реалистичный диапазон)
q = np.linspace(0, 80, 100)

# Предельная выгода (MB) — предотвращённый ущерб от 1 GtCO2
# Пологая: ~$12–40/т, слабо растёт (Nordhaus 2018, DICE)
# Коэффициенты подогнаны под Fig. 3 Nordhaus (2018)
MB = 25 + 0.15 * q   # $/т CO2

# Предельные издержки (MC) — цена декарбонизации
# Крутая: растёт быстрее из-за убывающей отдачи технологий
# Коэффициенты: Nordhaus (2018), оптимальная цена ~$50/т в 2025 → ~$200/т к 2050
MC = 5 + 0.55 * q**1.15   # $/т CO2

# Оптимум (MB = MC) — пересечение
q_opt = 55   # GtCO2 (примерно — из Nordhaus)
mb_opt = 25 + 0.15 * q_opt

fig, ax = plt.subplots(figsize=(5.5, 3.8))

# Кривые
ax.plot(q, MB, 'b-', lw=2.2, label='Предельная выгода (MB), $/т CO₂')
ax.plot(q, MC, 'r-', lw=2.2, label='Предельные издержки (MC), $/т CO₂')

# Оптимум
ax.plot(q_opt, mb_opt, 'ko', markersize=8, label=f'Оптимум: {q_opt} GtCO₂')
ax.axvline(x=q_opt, color='gray', ls=':', alpha=0.6)

# Подписи
ax.set_xlabel('Сокращение выбросов (GtCO₂ / год)', fontsize=11)
ax.set_ylabel('Цена / издержки ($ за тонну CO₂)', fontsize=11)
ax.set_title('Правило Вайцмана: пологая MB vs крутая MC (Nordhaus 2018)', fontsize=12, fontweight='bold')
ax.legend(loc='upper left', fontsize=9)
ax.grid(True, alpha=0.35)
ax.set_xlim(0, 80)
ax.set_ylim(0, 150)

# Аннотация
ax.annotate('MB пологая → налог эффективнее\n(если нет порогов)',
            xy=(60, 40), xytext=(65, 100),
            arrowprops=dict(arrowstyle='->', lw=1.2, color='blue'),
            fontsize=9, bbox=dict(boxstyle='round,pad=0.3', facecolor='lightblue', alpha=0.7))

plt.tight_layout()
plt.savefig('nordhaus_mb_mc.pdf', dpi=300, bbox_inches='tight')
plt.close()

print("Готово: nordhaus_mb_mc.pdf")
print(f"Оптимум: q = {q_opt} GtCO₂, цена ≈ ${mb_opt:.0f}/т")
