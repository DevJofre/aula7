# Escreva uma função que recebe dois números como argumentos e retorna a divisão do primeiro pelo segundo. Use um bloco try/except para tratar o caso em que o segundo número é zero e lance uma exceção personalizada com a mensagem "Divisão por zero não permitida".

class DivisaoPorZeroError(Exception):
    pass


def dividir(numerador, denominador):
    try:
        if denominador == 0:
            raise DivisaoPorZeroError("Divisão por zero não permitida")
        return numerador / denominador
    except DivisaoPorZeroError as e:
        return str(e)


print(dividir(10, 2))
print(dividir(10, 0))
