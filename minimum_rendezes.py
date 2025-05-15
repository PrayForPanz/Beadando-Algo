import main
from main import numb_list

# print("\nTeljes lista rendezésének folyamata (Minimum rendezés):")

def minimum_rendezes(numb_list):
    for i in range(0, len(numb_list)-1):
        minI = i
        for j in range(i + 1, len(numb_list)):
            if numb_list[j] < numb_list[minI]:
                minI = j
        if minI != i:
            temp = numb_list[minI]
            numb_list[minI] = numb_list[i]
            numb_list[i] = temp
            # print(f"Folyamat ({i+1}): ", numb_list) # 30mp - 45mp között történik meg a kiíratásokkal együtt
    return numb_list

# print("\nMinimum rendezés: ", minimum_rendezes(numb_list))