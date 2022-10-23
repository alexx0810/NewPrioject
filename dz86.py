import random

def make_choise(bot=False):
    if bot:
        return random.choise('rps')
    else:
        return input('выберите предмет r p s')