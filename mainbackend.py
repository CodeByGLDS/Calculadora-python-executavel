def calculo(num1, num2, operacao):
    operacoes = {
        "soma": lambda: num1 + num2,
        "subtracao": lambda: num1 - num2,
        "multiplicacao": lambda: num1 * num2,
        "divisao": lambda: num1 / num2,
        "potencia": lambda: num1 ** num2,
        "resto": lambda: num1 % num2
    }

    func = operacoes.get(operacao)

    if func:
        try:
            return func()
        except ZeroDivisionError:
            return "Erro: divisão por zero"
    else:
        return "Erro Interno"
