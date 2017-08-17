import random

class Character(object):
    def __init__(self, name, **kwargs):
        self.name = name

        for key, value in kwargs.items():
            setattr(self, key, value)

class Thief(Character):
    sneaky = True

    def pickpocket(self):
        return bool(random.randint(0,1))

    def hide(self, light_level):
        return self.sneaky and light_level < 10