import random


def gen_plus_minus():
    sign = '+'
    a = random.randint(0, 100)
    b = random.randint(-99, 100)
    if b <= 0:
        sign = ''
    text = str(a) + sign + str(b) + '='
    result = str(a + b)
    return text, result


def gen_multiply():
    a = random.randint(1, 10)
    b = random.randint(1, 10)

    text = str(a) + '*' + str(b) + '='
    result = str(a * b)
    return text, result


if __name__ == '__main__':
    print(gen_plus_minus())
    print(gen_multiply())
