def ler_arquivo(filename):
    with open(filename, 'r') as file:
        linhas = file.readlines()

    fatorial = {}
    for linha in linhas:
        partes = linha.strip().split()
        numero = int(partes[0].replace(':', ''))
        comando = partes[1]
        variavel = partes[2]
        value1 = int(partes[3])
        value2 = int(partes[4])
        instrucao = (numero, comando, variavel, value1, value2)
        fatorial[numero] = instrucao
    return fatorial
