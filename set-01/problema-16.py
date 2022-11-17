print()
print('Afisati caracterele unice dintr-un text. \n')

print('Introduceti textul de la tastatura:')
text = input()
caractere_unice = []

text = text.lower()

for caracter in text:
    if caracter == ' ' or caracter == '-':
        continue
    else:
        if text.count(caracter) < 2:
            caractere_unice.append(caracter)
            
print('Elementele care se repeta: ', ', '.join(str(caracter) for caracter in caractere_unice))
