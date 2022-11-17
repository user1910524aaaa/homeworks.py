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
    # in cazul in care caracterul este spatiu
    if caracter == ' ':
        # adaugam valoarea variabilei temporare in lista de cuvinte
        lista_cuvinte.append(temp)
        # resetam valoarea variabilei temporare
        temp = ''
    else:
        # daca caracterul nu este spatiu, il adaugam la sfarsitul valorii variabilei temporare
        temp += caracter
        # in cazul in care suntem la ultimul caracter din text, 
        # adaugam in lista si ultimul cuvant stocat in variabila temp
        if numarator == len(text):
            lista_cuvinte.append(temp)

print(f'In textul introdus anterior sunt {len(lista_cuvinte)} cuvinte.')

