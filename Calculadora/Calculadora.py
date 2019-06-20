def operacoes():
    n1 = float(input('Digite primeiro número: '))  # Recebe primeiro número.
    s = str(input('Digite um dos sinais: + - x / '))  # Recebe Sinal.
    n2 = float(input('Digite segundo número: '))  # Recebe segundo número.

    if s == '+':  # Efetua operação de soma.
        print('Resultado : ', n1 + n2)

    elif s == '/':  # Efetua operação de divisão.
        print('Resultado : ', n1 / n2)

    elif s == '-':  # Efetua operação de subtração.
        print('Resultado : ', n1 - n2)

    elif s == 'x':  # Efetua operação de multiplicação.
        print('Resultado : ', n1 * n2)

    else:  # Erro no operador.
        print('Operador digitado não foi identificado.')

    repetidor()  # Chama função para repetir ou encerrar aplicação.


def repetidor():
    reiniciar = input('Deseja calcular novamente?' +
                      'Digite Y para sim e N para não: ')  # Valida repetição.

    if reiniciar.upper() == 'Y':  # Repete aplicação.
        operacoes()

    elif reiniciar.upper() == 'N':  # Finaliza aplicação.
        print('Obrigado! Até breve =)')

    else:
        repetidor()


operacoes()
