class ArquivoInvalidoError(Exception):
    pass


def abrir_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
        return conteudo
    except FileNotFoundError:
        raise ArquivoInvalidoError("Arquivo inválido")


nome_arquivo = input("Digite o nome do arquivo: ")

try:
    conteudo = abrir_arquivo(nome_arquivo)
    print("Conteúdo do arquivo:")
    print(conteudo)
except ArquivoInvalidoError as e:
    print(e)
