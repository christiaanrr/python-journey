import random

class Thief(object):
    sneaky = True

    def __init__(self, name, sneaky = True, **kwargs):
        self.name = name
        self.sneaky = sneaky

        for key, value in kwargs.items():
            setattr(self, key, value)

    def pickpocket(self):
        return bool(random.randint(0,1))

    def hide(self, light_level):
        return self.sneaky and light_level < 10