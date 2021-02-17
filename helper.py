import random


def operation(level=1):

    if level == 1:
        op = random.choice(['+', '-'])
        a = random.randint(0, 10)
        b = random.randint(0, 10)
        r = a+b
        if op == '-':
            if b>a:
                b = random.randint(0, a)
            r = a-b
        cuenta = '{}{}{}'.format(a,op,b)
        return cuenta, r
    elif level == 2:
        op = random.choice(['+', '-', '*'])
        a = random.randint(-10, 20)
        b = random.randint(-10, 20)
        r = a+b
        if op == '-': r = a-b
        if op == '*':
            a = random.randint(-10, 10)
            b = random.randint(-10, 10)
            r = a*b
        cuenta = '{}{}{}'.format(a, op, b)
        return cuenta, r
    else:
        op = random.choice(['+', '-', '*', '/'])
        a = random.randint(-100, 100)
        b = random.randint(-100, 100)
        r = a+b
        if op == '-': r = a - b
        elif op == '*':
            a = random.randint(-20, 20)
            b = random.randint(-10, 10)
            r = a * b
        elif op == '/':
            a = random.randint(0, 100)
            b = random.randint(1, 10)
            r = int(a/b)
        cuenta = '{}{}{}'.format(a, op, b)
        return cuenta, r

