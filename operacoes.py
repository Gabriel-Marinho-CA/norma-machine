class Operacoes(object):
    value = 0

    def __init__(self, value):
        self.value = value

    def ADD(self):
        self.value += 1

    def SUB(self):
        if (self.ZER()) != 1:
            self.value -= 1
        else:
            self.value = 0

    def ZER(self):
        return 1 if self.value == 0 else 0
