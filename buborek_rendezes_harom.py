import main
from main import numb_list

def buborek_rendezes_harom(numb_list):
    # print("\nTeljes lista rendezésének folyamata (Buborék rendezés [harmadik alakja]):")
    i = 1
    while i <= len(numb_list) - 1:
        csereHely = 0
        for j in range(0, len(numb_list) - i):
            if numb_list[j] > numb_list[j + 1]:
                temp = numb_list[j]
                numb_list[j] = numb_list[j + 1]
                numb_list[j + 1] = temp
                csereHely = j
                # print(f"Folyamat ({j + 1}): ", numb_list)
        i = len(numb_list) - csereHely
    return numb_list

# print("\nTeljes rendezett lista (Buborék rendezés [harmadik alakja]):", buborek_rendezes_harom(numb_list))