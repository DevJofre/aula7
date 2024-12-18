def criar_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'x') as arquivo:
            arquivo.write("Este é um novo arquivo.")
        print(f"Arquivo '{nome_arquivo}' criado com sucesso.")
    except FileExistsError:
        print(f"Erro: O arquivo '{nome_arquivo}' já existe.")


nome_arquivo = input("Digite o nome do arquivo para criar: ")

criar_arquivo(nome_arquivo)
