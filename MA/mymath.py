import random


def gen_plus_minus(a1, a2, b1, b2):
    sign = '+'
    a = random.randint(a1, a2+1)
    b = random.randint(b1, b2+1)
    if b <= a:
        sign = random.choice('-+')
    text = str(a) + sign + str(b) + '='
    if sign == '+': result = str(a + b)
    else: result = str(a - b)
    return text, result


def gen_multiply(a1, a2, b1, b2):
    a = random.randint(a1, a2+1)
    b = random.randint(b1, b2+1)

    text = str(a) + '*' + str(b) + '='
    result = str(a * b)
    return text, result

def gen_division(a1, a2, b1, b2):
    a = random.randint(a1, a2+1)
    b = random.randint(b1, b2+1)
    result = str(a * b)

    text = result + '/' + str(a) + '='

    return text, str(b)


if __name__ == '__main__':
    print(gen_plus_minus(0, 1, 0, 1))
    print(gen_multiply(0, 1, 0, 1))
    print(gen_division(0, 1, 0, 1))
