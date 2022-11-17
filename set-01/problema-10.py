print()
print('Afisati in ordine inversa o lista de numere. \n')


print('introduceti de la tastatura numarul de elemente pe care lista il va avea lista:')
numar_elemente = int(input())
lista = []

print('introduceti elementele listei:')
for i in range(numar_elemente):
    print(f'lista[{i}] = ', end=' ')
    element = int(input())
    lista.append(element)
    
print('Lista originala: ', lista)


inversa_listei = []
for value in lista:
  inversa_listei = [value] + inversa_listei
print('Inversa listei : ', inversa_listei)