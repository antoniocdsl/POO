
valores = []  

while True:
    valor = float(input("Digite um valor: "))
    
    if valor == -1:
        break  
    
    valores.append(valor)  

print("\n" + "="*50)

# letra a)
quantidade = len(valores)
print(f"a) Quantidade de valores lidos: {quantidade}")

# letra b) 
print(f"b) Valores na ordem original: ", end="")
for valor in valores:
    print(f"{valor:.1f} ", end="")
print()  

# letra c)
print("c) Valores na ordem inversa:")
for i in range(len(valores)-1, -1, -1):
    print(f"   {valores[i]:.1f}")

# letra d)
soma = sum(valores)
print(f"d) Soma dos valores: {soma:.1f}")

# letra e)
if quantidade > 0:
    media = soma / quantidade
    print(f"e) Média dos valores: {media:.2f}")
else:
    media = 0
    print("e) Média dos valores: 0 (nenhum valor foi digitado)")

# letra f)
acima_media = 0
for valor in valores:
    if valor > media:
        acima_media += 1
print(f"f) Valores acima da média: {acima_media}")

# letra g) 
abaixo_sete = 0
for valor in valores:
    if valor < 7:
        abaixo_sete += 1
print(f"g) Valores abaixo de sete: {abaixo_sete}")

# letra h) 
print("h) Programa finalizado! grato por usar!")
print("="*50)