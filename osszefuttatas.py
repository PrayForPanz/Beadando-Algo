import main
from main import numb_list , merge_list
from buborek_rendezes_harom import buborek_rendezes_harom

temp_list = []

def osszefuttatas(numb_list , merge_list , temp_list):
    temp_list.clear()

    numb_list_sort = buborek_rendezes_harom(numb_list) 
    merge_list_sort = buborek_rendezes_harom(merge_list)

    i = 0
    j = 0
    while i < len(numb_list_sort) and j < len(merge_list_sort):
        if numb_list_sort[i] < merge_list_sort[j]:
            temp_list.append(numb_list_sort[i])
            i += 1
        else:
            if numb_list_sort[i] > merge_list_sort[j]:
                temp_list.append(merge_list_sort[j])
                j += 1
            else:
                temp_list.append(numb_list_sort[i])
                i += 1
                temp_list.append(merge_list_sort[j])
                j += 1
        print(f"Folyamat ({j + 1}): ", temp_list)
    
    print()
    print(temp_list)
    while i < len(numb_list_sort):
        temp_list.append(numb_list_sort[i])
        i += 1
    while j < len(merge_list_sort):
        temp_list.append(merge_list_sort[j])
        j += 1
    return temp_list

print("\nTeljes rendezett lista (Összefuttatás):", osszefuttatas(numb_list , merge_list , temp_list))