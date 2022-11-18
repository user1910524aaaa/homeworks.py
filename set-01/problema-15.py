print()
print('Verificati daca doua cuvinte sunt anagrame. \n')

print('Introduceti primul cuvant:', end=' ')
cuvantul1 = input()
print('Introduceti cel de-al doilea cuvant:', end=' ')
cuvantul2 = input()


# convertim literele ambelor cuvinte in litere mici, pentru a le putea compara 
cuvantul1 = cuvantul1.lower()
cuvantul2 = cuvantul2.lower()

# preluarea caracterelor din cele doua cuvinte in doua liste distincte
cuvantul1_sortat_crescator = [x for x in cuvantul1]
cuvantul2_sortat_crescator = [x for x in cuvantul2]


# verificam daca ambele cuvinte au acelasi numar de caractere
if(len(cuvantul1) == len(cuvantul2)):
    
    # ordonam in ordine alfabetica caracterele primului cuvant cu ajutorul algoritmului bubble sort
    # cuvantul1_sortat_crescator = sorted(cuvantul1)
    temp = ''
    for i in range(0, len(cuvantul1)):
        for j in range(0, len(cuvantul1)):
            if cuvantul1_sortat_crescator[j] > cuvantul1_sortat_crescator[i]:
                temp = cuvantul1_sortat_crescator[i]
                cuvantul1_sortat_crescator[i] = cuvantul1_sortat_crescator[j]
                cuvantul1_sortat_crescator[j] = temp
    
    # ordonam in ordine alfabetica caracterele celui de-al doilea cuvant cu ajutorul algoritmului bubble sort
    # cuvantul2_sortat_crescator = sorted(cuvantul2)            
    temp = ''
    for i in range(0, len(cuvantul2)):
        for j in range(0, len(cuvantul2)):
            if cuvantul2_sortat_crescator[j] > cuvantul2_sortat_crescator[i]:
                temp = cuvantul2_sortat_crescator[i]
                cuvantul2_sortat_crescator[i] = cuvantul2_sortat_crescator[j]
                cuvantul2_sortat_crescator[j] = temp

    # # verificam daca listele de caractere sortate crescator sunt la fel
    if(cuvantul1_sortat_crescator == cuvantul2_sortat_crescator):
        print(cuvantul1 + ' si ' + cuvantul2 + ' sunt anagrame.')
    else:
        print(cuvantul1 + ' si ' + cuvantul2 + ' nu sunt anagrame.')
else:
    print(cuvantul1 + ' si ' + cuvantul2 + ' nu sunt anagrame.')