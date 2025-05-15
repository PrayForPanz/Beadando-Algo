import main
from main import numb_list

def buborek_rendezes_ketto(numb_list):
    # print("\nTeljes lista rendezésének folyamata (Buborék rendezés [második alakja]):")
    i = 1
    csere = True
    while i <= len(numb_list) - 1 and csere:
        csere = False
        for j in range(0, len(numb_list) - i):
            if numb_list[j] > numb_list[j + 1]:
                temp = numb_list[j]
                numb_list[j] = numb_list[j + 1]
                numb_list[j + 1] = temp
                # print(f"Folyamat ({j + 1}): ", numb_list)
                csere = True
        i += 1
    return numb_list

# print("\nTeljes rendezett lista (Buborék rendezés):", buborek_rendezes_ketto(numb_list))