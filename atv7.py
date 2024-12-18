class ArgumentoInvalidoError(Exception):
    pass


def contar_vogais(texto):
    try:
        if not isinstance(texto, str):
            raise ArgumentoInvalidoError("Argumento inválido")

        vogais = "aeiouAEIOU"
        return sum(1 for char in texto if char in vogais)
    except ArgumentoInvalidoError as e:
        return str(e)


# Exemplos de uso:
print(contar_vogais("Olá Mundo"))
print(contar_vogais(123))
print(contar_vogais(["a", "e"]))
