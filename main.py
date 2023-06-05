#!/usr/local/bin/python
# encoding: utf-8
from operacoes import Operacoes
from functions import soma, multiplicacao, fatorial


def main():
    print("\n1 - Somar")
    print("2 - Multiplicação")
    print("3 - Fatorial")
    print("0 - Sair")

    while True:
        option = input("\nDigite sua opção: ")
        if option == '0':
            print("Saiu")
            exit()
        elif option == '1':
            print("\nDigite os valores de A e B:\n")

            while True:
                try:
                    temp = int(input("Digite o valor de A: "))
                    assert (temp > 0)
                    break
                except:
                    print("Apenas valores positivos")

            A = Operacoes(temp)

            while True:
                try:
                    temp = int(input("Digite o valor de B: "))
                    assert (temp > 0)
                    break
                except:
                    print("Apenas valores positivos")

            B = Operacoes(temp)
            C = Operacoes(0)
            D = Operacoes(0)
            program = soma.get()
            break
        elif option == '2':
            print("\n\nDigite os valores de A e B:\n ")
            while True:
                try:
                    temp = int(input("Digite o valor de A: "))
                    assert (temp > 0)
                    break
                except:
                    print("Apenas valores positivos")

            A = Operacoes(temp)

            while True:
                try:
                    temp = int(input("Digite o valor de B: "))
                    assert (temp > 0)
                    break
                except:
                    print("Apenas valores positivos")

            B = Operacoes(temp)
            C = Operacoes(0)
            D = Operacoes(0)
            program = multiplicacao.get()
            break

        elif option == '3':
            print("\nDigite os valores de A\n")
            while True:
                try:
                    temp = int(input("Digite o valor de A: "))
                    assert (temp >= 0)
                    break
                except:
                    print("Apenas valores positivos")

            A = Operacoes(temp)
            B = Operacoes(0)
            C = Operacoes(0)
            D = Operacoes(0)
            program = fatorial.get()
            break
        else:
            print("Escolha uma das opções válidas")

    instructions = []
    for linha in program:
        instructions += [[linha[0], linha[1], linha[2], linha[3], linha[4]]]
    i = 0

    print("\nInicio\n-> (({},{},{},{}),{})".format(A.value,
          B.value, C.value, D.value, i))
    while i < len(instructions):
        try:
            if instructions[i][1] == 'ADD':
                if instructions[i][2] == 'A':
                    A.add()
                elif instructions[i][2] == 'B':
                    B.add()
                elif instructions[i][2] == 'C':
                    C.add()
                else:
                    D.add()
                i = instructions[i][3]
                i -= 1
                print("(({},{},{},{}),{})".format(
                    A.value, B.value, C.value, D.value, i))
            elif instructions[i][1] == 'SUB':
                if instructions[i][2] == 'A':
                    A.sub()
                elif instructions[i][2] == 'B':
                    B.sub()
                elif instructions[i][2] == 'C':
                    C.sub()
                else:
                    D.sub()
                i = instructions[i][3]
                i -= 1
                print("(({},{},{},{}),{})".format(
                    A.value, B.value, C.value, D.value, i))
            elif instructions[i][1] == 'ZER':
                if instructions[i][2] == 'A':
                    i = instructions[i][3] if (
                        A.zer()) == 1 else instructions[i][4]
                elif instructions[i][2] == 'B':
                    i = instructions[i][3] if (
                        B.zer()) == 1 else instructions[i][4]
                elif instructions[i][2] == 'C':
                    i = instructions[i][3] if (
                        C.zer()) == 1 else instructions[i][4]
                else:
                    i = instructions[i][3] if (
                        D.zer()) == 1 else instructions[i][4]
                i -= 1
                print("(({},{},{},{}),{})".format(
                    A.value, B.value, C.value, D.value, i))
        except IndexError:
            print("\nOs valores dos registradores são:")
            print("A: ", A.value)
            print("B: ", B.value)
            print("C: ", C.value)
            print("D: ", D.value)


if __name__ == '__main__':
    main()
    while True:
        option = input("Deseja rodar o programa novamente? [Y/N] ")
        if option == 'N' or option == 'n':
            print("\n Fim do programa!")
            break
        elif option == 'Y' or option == 'y':
            main()
        else:
            print("Escolha uma opção válida")
