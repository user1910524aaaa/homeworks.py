print()
print('Calculati deviatia standard a unei liste de numere. \n')


print('introduceti de la tastatura numarul de elemente pe care lista il va avea lista:')
numar_elemente = int(input())
lista = []

print('introduceti elementele listei:')
for i in range(numar_elemente):
    print(f'lista[{i}] = ', end=' ')
    element = int(input())
    lista.append(element)
    
print('Lista: ', lista, '\n')


ecuatie_calcul_deviatie_esantion = float((sum((x-(sum(lista) / len(lista)))**2 for x in lista) / (len(lista)-1))**0.5)
ecuatie_calcul_deviatie_populatie = float((sum((x-(sum(lista) / len(lista)))**2 for x in lista) / len(lista))**0.5)

print('Ecuatia deviatiei standard pe un esantion: ', ecuatie_calcul_deviatie_esantion)
print('Ecuatia deviatiei standard a populatiei: ', ecuatie_calcul_deviatie_populatie)