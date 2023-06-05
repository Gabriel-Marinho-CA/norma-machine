import lerarquivo

__fatorial = lerarquivo.ler_arquivo('./fatorial.txt')

def get():
    return tuple(__fatorial.values())