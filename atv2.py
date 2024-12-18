from datetime import datetime


class DataInvalidaError(Exception):
    pass


def verificar_data(data_str):
    try:
        datetime.strptime(data_str, "%d/%m/%Y")
        return "Data válida"
    except ValueError:
        raise DataInvalidaError("Data inválida")


data_usuario = input("Digite uma data no formato 'dd/mm/aaaa': ")

try:
    resultado = verificar_data(data_usuario)
    print(resultado)
except DataInvalidaError as e:
    print(e)
