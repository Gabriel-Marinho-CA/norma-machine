import lerarquivo

__soma = lerarquivo.ler_arquivo('./soma.txt')

def get():
    return tuple(__soma.values())