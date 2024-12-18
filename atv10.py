def converter_para_string(numero):
    try:
        numero_str = str(numero)
        return numero_str
    except Exception as e:
        return f"Erro: {e}"


try:
    numero = int(input("Digite um número inteiro: "))
    numero_str = converter_para_string(numero)
    print(f"O número convertido para string é: {numero_str}")
except ValueError:
    print("Erro: O valor digitado não é um número inteiro válido.")
