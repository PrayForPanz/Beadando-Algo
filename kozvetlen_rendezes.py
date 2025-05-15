from main import numb_list

# print("\nTeljes lista rendezésének folyamata (Közvetlen rendezés):")

def kozvetlen_rendezes(numb_list):
    for i in range(0, len(numb_list) - 1):
        for j in range(i + 1, len(numb_list)):
            if numb_list[j] < numb_list[i]:
                temp = numb_list[j]
                numb_list[j] = numb_list[i]
                numb_list[i] = temp
        # print(f"Folyamat ({i + 1}): ", numb_list) # Olyan gyors, hogy nincs értelme leírnom
    return numb_list

# print("\nKözvetlen rendezés: ", kozvetlen_rendezes(numb_list))