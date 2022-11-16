print()
print('Cititi un text de la tastatura si inlocuiti un carcater cu un alt caracter si apoi afisati rezultatul. \n')
print('introduceti un text:')
text = input()

print('Introduceti numarul pozitiei din text al caracterului pe care vreti sa-l inlocuiti')
# numarul pozitiei - 1, deoarece numaratoarea indexurilor intr-un sir incepe de la 0
numar_carcater = int(input()) - 1

print('Introduceti caracterul nou')
caracter_nou = input()

# textul pana la numarul pozitiei alese din text + caracterul nou introdus + textul de la numarul pozitiei alese din text
text_nou = text[:numar_carcater] + caracter_nou + text[numar_carcater + 1:]
print(text_nou)