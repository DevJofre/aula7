def acessar_elemento(lista, indice):
    try:
        return lista[indice]
    except IndexError:
        return "Erro: Índice fora dos limites da lista."


minha_lista = ["maçã", "banana", "uva", "laranja"]

try:
    indice = int(input("Digite o índice do elemento que deseja acessar: "))
    elemento = acessar_elemento(minha_lista, indice)
    print(f"Elemento acessado: {elemento}")
except ValueError:
    print("Erro: O índice deve ser um número inteiro.")
