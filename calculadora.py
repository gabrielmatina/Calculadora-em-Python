def Calculadora():
    operacao = int(input(
        "Selecione o número da operação desejada:\n\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n\nDigite sua opção (1/2/3/4): "))
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    if int(operacao) == 1:
        resultado = num1 + num2
        print(num1, '+', num2, '=', resultado)
    elif int(operacao) == 2:
        resultado = num1 - num2
        print(num1, '-', num2, '=', resultado)
    elif int(operacao) == 3:
        resultado = num1 * num2
        print(num1, 'x', num2, '=', resultado)
    elif int(operacao) == 4:
        resultado = num1 / num2
        print(num1, '/', num2, '=', int(resultado))
    elif int(operacao) > 4:
        print("Operação inválida")
    elif int(operacao) < 1:
        print("Operação inválida")
    else:
        Calculadora()
    Repetir()


def Repetir():
    novocalculo = int(
        input("Deseja fazer uma nova operação? \n\n1 - Sim\n2 - Não\n"))
    if novocalculo == 1:
        Calculadora()
    elif novocalculo == 2:
        print("Até breve")
    else:
        Repetir()


Calculadora()
