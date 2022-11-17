print('cititi un text si numarati cate vocale contine.')
print('introduceti un text:')
text = input()

text_litere_mici = text.lower()

numar_vocale = 0

for litera in text_litere_mici:
    if (litera == 'a' or litera == 'e' 
        or litera == 'i'  or litera == 'o' 
        or litera == 'u' or litera == 'ă' 
        or litera =='â' or litera == 'î'):
        numar_vocale += 1

print(f'in textul urmator: {text_litere_mici}, sunt {numar_vocale} vocale')