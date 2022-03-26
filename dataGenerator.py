import data_names
import random
from random import choice


def generate_username():
    name = str(choice(data_names.names))
    prefix = choice(["x", "xx", "e", "o", "a", "v", ""])
    suffix = str(random.randint(1, 9))
    number = str(random.randint(1, 9))
    number2 = str(random.randint(1, 9))
    return prefix + name + suffix + number + number2


def generate_password():
    name = str(choice(data_names.names))
    prefix = choice(["A", "B", "C", "D", "E", "F", "G"])
    suffix = choice(["bbb", "xxx", "vvv"])
    number = str(random.randint(1, 9))
    return prefix + name + suffix + number


