class ArgumentoInvalidoError(Exception):
    pass


def calcular_fatorial(numero):
    try:
        if not isinstance(numero, int) or numero < 0:
            raise ArgumentoInvalidoError("Argumento inválido")

        fatorial = 1
        for i in range(1, numero + 1):
            fatorial *= i
        return fatorial
    except ArgumentoInvalidoError as e:
        return str(e)


print(calcular_fatorial(5))
print(calcular_fatorial(-3))
print(calcular_fatorial(3.5))
