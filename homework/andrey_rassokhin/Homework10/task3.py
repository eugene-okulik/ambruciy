def result(func):
    def wrapper(first, second):
        operation = ''
        if first < 0 or second < 0:
            operation = '*'
        elif first > second:
            operation = '-'
        elif first == second:
            operation = '+'
        elif first < second:
            operation = '/'
        return func(first, second, operation)
    return wrapper


@result
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second


first = int(input('Введите первую цифру: '))
second = int(input('Введите вторую цифру: '))
print(calc(first, second))
