import main
from main import numb_list
from main import merge_list

temp_list = []

def osszefuttatas(numb_list, mege_list, temp_list):
    numb_list_i = 0
    merge_list_i = 0
    while numb_list_i < len(numb_list) and merge_list_i < len(mege_list):
        if numb_list[numb_list_i] < mege_list[merge_list_i]:
            temp_list.append(numb_list[numb_list_i])
            numb_list_i += 1
        else:
            if numb_list[numb_list_i] > merge_list[merge_list_i]:
                temp_list.append(merge_list[merge_list_i])
                merge_list_i += 1
            else:
                temp_list.append(numb_list[numb_list_i])
                numb_list_i += 1
                temp_list.append(merge_list[merge_list_i])
                merge_list_i += 1
        print(f"Folyamat ({merge_list_i}): ", temp_list)
    
    print()
    print(temp_list)
    while numb_list_i < len(numb_list):
        temp_list.append(numb_list[numb_list_i])
        numb_list_i += 1
    while merge_list_i < len(merge_list):
        temp_list.append(merge_list[merge_list_i])
        merge_list_i += 1
    return temp_list

print("\nTeljes rendezett lista (Összefuttatás):", osszefuttatas(numb_list, merge_list, temp_list))