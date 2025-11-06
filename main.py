while True:
    nome = input("Digite seu nome: ")

    if nome.strip() == "":
        print("Erro! O nome não pode ficar vazio.\n")
        continue
    elif any(char.isdigit() for char in nome):
        print("Erro! O nome não pode conter números.\n")
        continue
    else:
        break

while True:
    try:
        idade = int(input("Digite sua idade: "))
        break
    except ValueError:
        print("Erro! Digite apenas números para a idade.\n")

print("\nDados cadastrados com sucesso!")
print(f"Nome: {nome}")
print(f"Idade: {idade}")