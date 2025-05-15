import main
from main import numb_list

def buborek_rendezes_egy(numb_list):
    # print("\nTeljes lista rendezésének folyamata (Buborék rendezés [első alakja]):")
    for j in range(1, len(numb_list) - 1):
        for i in range(0, len(numb_list) - j):
            if numb_list[i] > numb_list[i + 1]:
                temp = numb_list[i]
                numb_list[i] = numb_list[i + 1]
                numb_list[i + 1] = temp
                # print(f"Folyamat ({i + 1}): ", numb_list)
    return numb_list

# print("\nTeljes lista rendezésének folyamata (Buborék rendezés):", buborek_rendezes_egy(numb_list))