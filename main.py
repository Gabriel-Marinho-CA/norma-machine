from operacoes import Operacoes
from functions import soma, multiplicacao, fatorial

def main():
    # === MENU STAT--- #
    print("\n1 - Somar")
    print("2 - Multiplicação")
    print("3 - Fatorial")
    print("0 - Sair")

    # === MENU END--- #

    while True:

        op = input("\nDigite sua opção: ")

        if op == '0':
            print("Saiu")
            exit()

        elif op == '1':
            print("\nDigite os valores de A e B:\n")

            # testa se o input é positivo e guarda os valores dos registradores

            while True:
                try:
                    inputUser = int(input("Digite o value de A: "))
                    assert (inputUser > 0)
                    break
                except:
                    print("Apenas valores positivos")

            A = Operacoes(inputUser)

            while True:
                try:
                    inputUser = int(input("Digite o value de B: "))
                    assert (inputUser > 0)
                    break
                except:
                    print("Apenas valores positivos")

            B = Operacoes(inputUser)
            C = Operacoes(0)
            D = Operacoes(0)

            # Pega as instrucoes do .txt
            instrucoes = soma.get()
            break
        elif op == '2':
            print("\n\nDigite os valores de A e B:\n ")
            while True:
                try:
                    inputUser = int(input("Digite o value de A: "))
                    assert (inputUser > 0)
                    break
                except:
                    print("Apenas valores positivos")

            A = Operacoes(inputUser)

            while True:
                try:
                    inputUser = int(input("Digite o value de B: "))
                    assert (inputUser > 0)
                    break
                except:
                    print("Apenas valores positivos")

            B = Operacoes(inputUser)
            C = Operacoes(0)
            D = Operacoes(0)
            instrucoes = multiplicacao.get()
            break

        elif op == '3':
            print("\nDigite os valores de A\n")
            while True:
                try:
                    inputUser = int(input("Digite o value de A: "))
                    assert (inputUser >= 0)
                    break
                except:
                    print("Apenas valores positivos")

            A = Operacoes(inputUser)
            B = Operacoes(0)
            C = Operacoes(0)
            D = Operacoes(0)
            instrucoes = fatorial.get()
            break
        else:
            print("Escolha uma das opções válidas")

    arrInstrucoes = []
    for coluna in instrucoes:
        # Cria as instrucoes, quebrando as colunas, e montando o array separando elas
        arrInstrucoes += [
            [
                coluna[0],
                coluna[1],
                coluna[2],
                coluna[3],
                coluna[4]
            ]
        ]

    i = 0

    print("\nInicio\n-> (({},{},{},{}),{})"
          .format(
              A.value,
              B.value,
              C.value,
              D.value,
              i
          ))

    while i < len(arrInstrucoes):
        try:

            if arrInstrucoes[i][1] == 'ADD':

                # Relaciona a string á variavel e executa os attr relacionados a ela

                getattr(locals()[arrInstrucoes[i][2]], 'ADD')()

                i = arrInstrucoes[i][3]
                i -= 1

                print("(({},{},{},{}),{})"
                      .format(
                          A.value,
                          B.value,
                          C.value,
                          D.value,
                          i
                      ))

            elif arrInstrucoes[i][1] == 'SUB':
                getattr(locals()[arrInstrucoes[i][2]], 'SUB')()
                i = arrInstrucoes[i][3]
                i -= 1

                print("(({},{},{},{}),{})"
                      .format(
                          A.value,
                          B.value,
                          C.value,
                          D.value,
                          i
                      ))
            elif arrInstrucoes[i][1] == 'ZER':

                i = arrInstrucoes[i][3] if (
                    getattr(locals()[arrInstrucoes[i][2]], 'ZER')() == 1) else arrInstrucoes[i][4]

                i -= 1
                print("(({},{},{},{}),{})"
                      .format(
                          A.value,
                          B.value,
                          C.value,
                          D.value,
                          i
                      ))

        except:
            print("\nOs valores dos registradores são:")
            print("A: ", A.value)
            print("B: ", B.value)
            print("C: ", C.value)
            print("D: ", D.value)


main()

while True:
    op = input("Deseja rodar o programa novamente? [s/n] ")
    if op == 'n':
        print("\n Fim do programa!")
        break
    elif op == 's':
        main()
    else:
        print("Escolha uma opção válida")
