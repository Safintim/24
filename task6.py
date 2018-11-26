def summation(num1, num2):
    num1 = list(reversed(num1))
    num2 = list(reversed(num2))

    if len(num1) >= len(num2):
        number2, number1 = num2, num1
    else:
        number1, number2 = num2, num1

    for i in range(len(number2)):
        temp = int(number1[i]) + int(number2[i])
        number1[i] = temp % 10
        memory = temp // 10
        if memory and i + 1 == len(number1):
            number1.append(0)

        if memory:
            number1[i+1] = int(number1[i+1]) + memory

    return ''.join(str(i) for i in reversed(number1))


def multiplication(n, m):
    n = str(n)
    total = '0'
    for i in range(m):
        total = summation(n, total)

    return int(total)


def factorial(n):
    t = 1
    for i in range(0, n):
        t = multiplication(t, i + 1)
        yield t
