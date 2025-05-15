import main
from main import numb_list

def koktel_rendezes(numb_list):
    # print("\nTeljes lista rendezésének folyamata (Koktél rendezés):")
    start = 0
    end = len(numb_list) - 1
    for i in range(0, len(numb_list)):
        for j in range(start, end):
            if numb_list[j] > numb_list[j + 1]:
                temp = numb_list[j]
                numb_list[j] = numb_list[j + 1]
                numb_list[j + 1] = temp
                # print(f"Folyamat ({j + 1}): ", numb_list)
        end -= 1
        for k in range(end, start, -1):
            if numb_list[k] < numb_list[k - 1]:
                temp = numb_list[k]
                numb_list[k] = numb_list[k - 1]
                numb_list[k - 1] = temp
                # print(f"Folyamat ({k + 1}): ", numb_list)
        start += 1
    return numb_list

# print("\nTeljes lista rendezésének folyamata (Koktél rendezés):", koktel_rendezes(numb_list))