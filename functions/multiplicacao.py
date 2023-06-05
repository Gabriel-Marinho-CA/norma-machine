import lerarquivo

__multiplicacao = lerarquivo.ler_arquivo('./multiplicacao.txt')

def get():
    return tuple(__multiplicacao.values())