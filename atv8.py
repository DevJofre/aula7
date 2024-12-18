class ListaInvalidaError(Exception):
    pass


def ordenar_strings(lista):
    try:
        if not all(isinstance(item, str) for item in lista):
            raise ListaInvalidaError("Lista inválida")

        return sorted(lista)
    except ListaInvalidaError as e:
        return str(e)


print(ordenar_strings(["banana", "maçã", "uva"]))
print(ordenar_strings(["cachorro", "gato", 123]))
print(ordenar_strings(["laranja", "abacaxi", "morango"]))
