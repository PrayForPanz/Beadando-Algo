import timeit
from main import numb_list
import matplotlib.pyplot as plt

def idomeres(func, list, ismetles = 30000):
    return timeit.timeit(lambda: func(list.copy()), number = ismetles)

from buborek_rendezes_egy   import buborek_rendezes_egy
from buborek_rendezes_ketto import buborek_rendezes_ketto
from buborek_rendezes_harom  import buborek_rendezes_harom

print("\Teljesítmény ellenőrzés folyamatban (buborékok)...")

ismetles = 30000
bubor_ido_egy = idomeres(buborek_rendezes_egy, numb_list, ismetles)
bubor_ido_ketto = idomeres(buborek_rendezes_ketto, numb_list, ismetles)
bubor_ido_harom = idomeres(buborek_rendezes_harom, numb_list, ismetles)

print(f"Buborék rendezés [első alak] futási ideje:, {bubor_ido_egy:.5f}s")
print(f"Buborék rendezés [második alak] futási ideje:, {bubor_ido_ketto:.5f}s")
print(f"Buborék rendezés [harmadik alak] futási ideje:, {bubor_ido_harom:.5f}s")

values = [bubor_ido_egy, bubor_ido_ketto, bubor_ido_harom]
labels = ["Buborék[1]", "Buborék[2]", "Buborék[3]"]

fig, ax = plt.subplots(figsize=(6,4))
bars = ax.bar(labels, values)
ax.set_title('Buborék rendezések futási ideje')
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