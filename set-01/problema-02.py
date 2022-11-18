print()
print('Cititi un text de la tastatura si inlocuiti un carcater cu un alt caracter si apoi afisati rezultatul. \n')
print('introduceti un text:')
text = input()

print('Introduceti numarul pozitiei din text al caracterului pe care vreti sa-l inlocuiti')
# indexul pozitiei - 1, deoarece numaratoarea indexurilor caracterelor intr-un sir incepe de la 0
pozitie_carcater = int(input()) - 1

print('Introduceti caracterul nou')
caracter_nou = input()

# textul pana la numarul pozitiei alese din text + caracterul nou introdus + textul de la numarul pozitiei alese din text
# EXEMPLU:

# text = 'ana are mere' 

# numar total caractere: 12

# indexuri de pozitie: 0-11 => 
# => text[0]='a', text[1]='n', t[2]='a', text[3]=' ', text[4]='a', text[5]='r', text[6]='e', text[7] =' ', text[8]='m', 
# text[9]='e', text[10]='r', text[11]='e

# pozitie_carcater = int(input()) - 1 => 9 - 1 => pozitie_caracter = 8 => text[8]='m'

# caracter_nou = 'p'

# text_nou = text[:8] + 'p' + text[8 + 1:] => text_nou = 'ana are ' + 'p' + 'ere' => 'ana are pere'

text_nou = text[:pozitie_carcater] + caracter_nou + text[pozitie_carcater + 1:]
print(text_nou)