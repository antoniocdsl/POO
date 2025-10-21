#questão 1
lista = [10,20,30,40,50]
print(lista)

#questão 2 

print('primeiro elemento:',lista[0])
print('elemento do meio:',lista[2])
print('último elemento:',lista[-1])

#questão 3

lista[1] = 25
print(lista)

#questão 4

novo_numero = int(input('digite um número para adicionar na lista:'))
lista.append(novo_numero)
print('lista após adicionar novo número:',lista)

#questão 5

remover = int(input('digite um número da lista para remover:'))

if remover in lista:
    lista.remove(remover)
    print('lista após remover o número:', lista)
else:
    print('número não encontrado na lista.')



