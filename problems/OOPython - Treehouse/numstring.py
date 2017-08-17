class NumString(object):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)