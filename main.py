#   II. Beadandó feladat - Levelező
#   Adatszerkezetek és algoritmusok gyakorlat
#   1. Feladat:
#   •       Hozzon létre egy 100 elemű listát, amely 1 és 1000 közötti random számokat tartalmaz. Az elemeket a Python beépített random könyvtára segítségével generálja, így garantáltan különbözőek lesznek.
#   2. Feladat:
#   •       Implementálja a közvetlen rendezés és a minimum rendezés algoritmusát!
#   3. Feladat:
#   •       Vizsgálja meg, a közvetlen rendezés és a minimum rendezés algoritmusának a futási idejét a random generált listán.
#   •       Végezze el a rendezést 30000 alkalommal mindkét algoritmussal, majd mérje meg és összegezze mind a két algoritmus futási idejét az összes iteráció figyelembevételével.
#   •       A futási időt a Python time moduljával tudja mérni. A mérések után hasonlítsa össze a két algoritmus teljesítményét a matplotlib könyvtár segítségével.
#   4. Feladat:
#   •       Implementálja a buborékrendezés és a koktélrendezés algoritmusát.
#   •       Implementálja a javított buborékrendezés 1-es és 2-es változatát. Ezek a változatok bizonyos esetekben hatékonyabbak a klasszikus buborékrendezésnél, mivel korán leállhatnak, ha a lista már rendezett.
#   5. Feladat:
#   •       Vizsgálja meg a buborékrendezés és a javított buborékrendezések futási idejét a random generált listán.
#   •       Végezze el a rendezést 30000 alkalommal mind a három algoritmussal, majd mérje meg és összegezze mind a három algoritmus futási idejét az összes iteráció figyelembevételével.
#   •       A futási időt a Python time moduljával tudja mérni. A mérések után hasonlítsa össze a három algoritmus teljesítményét a matplotlib könyvtár segítségével.
#   6. Feladat:
#   •       Implementálja és hajtsa végre az összefuttatás algoritmusát.

#első feladat
import random

numb_list = random.sample(range(1, 1000), 5)
def numb_List_elemei():
    for i in numb_list:
        print(numb_list.index(i), ". elem: ", i)
        
print("\nTeljes lista: ", numb_list)

merge_list = random.sample(range(1, 1000), 5)
def numb_List_elemei_ossze():
    for i in merge_list:
        print(merge_list.index(i), ". elem: ", i)

print("\nTeljes lista: ", merge_list)