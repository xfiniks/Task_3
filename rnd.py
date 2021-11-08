import random
import string


def generate_random_int(minim, maxim):
    return random.randint(minim, maxim)


def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string
