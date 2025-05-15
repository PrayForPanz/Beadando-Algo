import timeit
from main import numb_list
import matplotlib.pyplot as plt

def idomeres(func, list, ismetles = 30000):
    return timeit.timeit(lambda: func(list.copy()), number = ismetles)

from kozvetlen_rendezes import kozvetlen_rendezes
from minimum_rendezes import minimum_rendezes

print("\nTeljesítmény ellenőrzés folyamatban (közvetlen, minimum)...")

ismetles = 30000
kozv_ido = idomeres(minimum_rendezes, numb_list, ismetles)
min_ido = idomeres(kozvetlen_rendezes, numb_list, ismetles)

print(f"Buborék rendezés [első alak] futási ideje:, {kozv_ido:.5f}s")
print(f"Buborék rendezés [második alak] futási ideje:, {min_ido:.5f}s")

values = [kozv_ido, min_ido]
labels = ["Közvetlen", "Minimum"]

fig, ax = plt.subplots(figsize=(6,4))
bars = ax.bar(labels, values)
ax.set_title('Közvetlen és Minimum rendezések futási ideje')
ax.set_ylabel('Idő (másodperc) összesen')

for bar in bars:
    bar_height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width()/2,
        bar_height,
        f"{bar_height:.4f}",
        ha='center',
        va='bottom'
    )

plt.tight_layout()
plt.show()