class ListaInvalidaError(Exception):
    pass


def soma_lista(lista):
    try:
        if not all(isinstance(item, (int, float)) for item in lista):
            raise ListaInvalidaError("Lista inválida")
        return sum(lista)
    except ListaInvalidaError as e:
        return str(e)


# Exemplos de uso:
print(soma_lista([1, 2, 3, 4]))
print(soma_lista([1, "a", 3]))
