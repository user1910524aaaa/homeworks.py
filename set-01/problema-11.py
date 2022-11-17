print()
print('Numarati cuvintele dintr-un text. \n')

print('Introduceti textul de la tastatura:')

text = input()
lista_cuvinte = []
temp = ''
numarator = 0

# parcurgem fiecare caracter al textului in parte
for caracter in text:
    numarator += 1
    # in cazul in care caracterul nu este spatiu
    if caracter != ' ':
        # daca caracterul nu este spatiu, il adaugam la sfarsitul valorii variabilei temporare
        temp += caracter
        # in cazul in care suntem la ultimul caracter din text, 
        # adaugam in lista si ultimul cuvant stocat in variabila temp
        if numarator == len(text):
            lista_cuvinte.append(temp)
    else: 
        # in cazul in care caracterul este spatiu   
        # adaugam in lista de cuvinte valoarea variabilei temporare, care detine ultimul cuvant format,
        # inainte ca sa intre in bucla caracterul pentru spatiu
        lista_cuvinte.append(temp)
        # resetam valoarea variabilei temporare
        temp = ''

print(f'In textul introdus anterior sunt {len(lista_cuvinte)} cuvinte.')

