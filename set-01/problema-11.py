print()
print('Numarati cuvintele dintr-un text. \n')

print('Introduceti textul de la tastatura:')
text = input()

lista_cuvinte = []
tmp = ''
for caracter in text:
    if caracter == ' ':
        lista_cuvinte.append(tmp)
        tmp = ''
    else:
        tmp += caracter

# for last word
if tmp:
    lista_cuvinte.append(tmp)

print(lista_cuvinte)
print(f'In textul introdus anterior sunt {len(lista_cuvinte)} cuvinte.')

