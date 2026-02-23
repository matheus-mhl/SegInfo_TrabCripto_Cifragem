import sys #Módulo que permite que o programa acesse informações do sistemas

def carregar_arquivo(nome):
    try:
        with open(nome, "r", encoding="utf-8") as f:
            return f.read()
    except:
        print("Erro ao abrir arquivo.")
        return None

def salvar_arquivo(nome_original, metodo, conteudo):
    novo_nome = nome_original.replace(".txt", f"_{metodo}.txt")
    with open(novo_nome, "w", encoding="utf-8") as f:
        f.write(conteudo)
    print(f"\nArquivo criptografado '{novo_nome}' salvo com sucesso!")

def inverter_mensagem(msg):
    return msg[::-1]

def deslocar_mensagem(msg, deslocamento):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    resultado = ""

    for c in msg:
        if c.lower() in alfabeto:
            indice = alfabeto.index(c.lower())
            novo_indice = (indice + deslocamento) % 26
            nova_letra = alfabeto[novo_indice]

            if c.isupper():
                nova_letra = nova_letra.upper()

            resultado += nova_letra
        else:
            resultado += c

    return resultado

def carregar_alfabeto(nome_arquivo):
    with open(nome_arquivo, "r") as f:
        linhas = f.read().splitlines()
        return linhas[0], linhas[1]

def substituir_mensagem(msg, arquivo_alfabeto):
    original, substituto = carregar_alfabeto(arquivo_alfabeto)
    resultado = ""

    for c in msg:
        if c.lower() in original:
            i = original.index(c.lower())
            nova = substituto[i]
            if c.isupper():
                nova = nova.upper()
            resultado += nova
        else:
            resultado += c

    return resultado

def menu():
    print("\nEscolha o método de cifragem:")
    print("1 - Inversão")
    print("2 - Deslocamento")
    print("3 - Substituição")
    print("4 - Sair")
    return input("Opção: ")

def main():
    print("=== Seja bem-vindo ao cifrador criptográfico Senac Br Cripto ===\n")

    if len(sys.argv) > 1:
        nome_arquivo = sys.argv[1]
    else:
        nome_arquivo = input("Digite o nome do arquivo (.txt): ")

    mensagem = carregar_arquivo(nome_arquivo)
    if mensagem is None:
        return

    print("\nMensagem original:\n")
    print(mensagem)

    while True:
        opcao = menu()

        if opcao == "1":
            resultado = inverter_mensagem(mensagem)
            salvar_arquivo(nome_arquivo, "inversao", resultado)
            print("\nMensagem cifrada:\n", resultado)

        elif opcao == "2":
            deslocamento = int(input("Informe o fator de deslocamento: "))
            resultado = deslocar_mensagem(mensagem, deslocamento)
            salvar_arquivo(nome_arquivo, "deslocamento", resultado)
            print("\nMensagem cifrada:\n", resultado)

        elif opcao == "3":
            print("\nEscolha o alfabeto:")
            print("1 - alfabeto1.txt")
            print("2 - alfabeto2.txt")
            escolha = input("Opção: ")

            arquivo = "alfabeto1.txt" if escolha == "1" else "alfabeto2.txt"

            resultado = substituir_mensagem(mensagem, arquivo)
            salvar_arquivo(nome_arquivo, "substituicao", resultado)
            print("\nMensagem cifrada:\n", resultado)

        elif opcao == "4":
            print("\nObrigado por utilizar o cifrador criptográfico Senac Br Cripto!")
            print("Até a próxima e programe com $eguranç@!")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()