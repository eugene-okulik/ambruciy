def repeat_me(func):
    def wrapper(text, count):
        for i in range(count):
            func(text)
            print('')
    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count=2)

# Дополнительное задание


def repeater(count):
    def repeat_me(func):
        def wrapper(text):
            for i in range(count):
                func(text)
                print('')
        return wrapper
    return repeat_me


@repeater(count=2)
def example(text):
    print(text)


example('Test')
