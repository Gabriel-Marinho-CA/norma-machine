class Operacoes(object):
    value = 0

    def __init__(self, value):
        self.value = value

    def add(self):
        self.value += 1

    def sub(self):
        if (self.zer()) != 1:
            self.value -= 1
        else:
            self.value = 0

    def zer(self):
        return 1 if self.value == 0 else 0
