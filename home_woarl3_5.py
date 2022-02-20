import random
from random import choice


def pop_random(name):
    return name.pop(random.randrange(len(name)))


def get_jokes(number=1, repeat=True):
    """Generates jokes
    :param number: amount of jokes
    :param repeat: responsible for word repeat
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    index = 0
    while index < number:
        if repeat:
            print(choice(nouns), choice(adverbs), choice(adjectives))
        else:
            print(pop_random(nouns), pop_random(adverbs), pop_random(adjectives))
        index += 1


get_jokes(5, repeat=False)
