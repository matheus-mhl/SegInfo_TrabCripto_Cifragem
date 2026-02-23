# === CIFRADOR SIMPLES ===

def inverter(msg):
    return msg[::-1]

def deslocamento(msg, n):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    resultado = ""

    for letra in msg:
        if letra.lower() in alfabeto:
            pos = alfabeto.index(letra.lower())
            nova = alfabeto[(pos + n) % 26]

            if letra.isupper():
                nova = nova.upper()

            resultado += nova
        else:
            resultado += letra

    return resultado

def substituicao(msg, original, novo):
    resultado = ""

    for letra in msg:
        if letra.lower() in original:
            i = original.index(letra.lower())
            nova = novo[i]

            if letra.isupper():
                nova = nova.upper()

            resultado += nova
        else:
            resultado += letra

    return resultado


# ===== PROGRAMA PRINCIPAL =====

arquivo = input("Digite o nome do arquivo: ")

with open(arquivo, "r", encoding="utf-8") as f:
    mensagem = f.read()

print("\nMensagem original:\n", mensagem)

print("\nEscolha o método:")
print("1 - Inverter")
print("2 - Deslocamento")
print("3 - Substituição")

opcao = input("Opção: ")

if opcao == "1":
    resultado = inverter(mensagem)

elif opcao == "2":
    n = int(input("Valor do deslocamento: "))
    resultado = deslocamento(mensagem, n)

elif opcao == "3":
    with open("alfabeto1.txt") as f:
        linhas = f.read().splitlines()
    resultado = substituicao(mensagem, linhas[0], linhas[1])

else:
    print("Opção inválida")
    exit()

novo_nome = arquivo.replace(".txt", "_cifrado.txt")

with open(novo_nome, "w", encoding="utf-8") as f:
    f.write(resultado)

print("\nMensagem cifrada:\n", resultado)
print("\nArquivo salvo como:", novo_nome)