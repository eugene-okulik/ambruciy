def add_text(func):
    def wrapper(text):
        func(text)
        print('')
        print('finished')
    return wrapper


@add_text
def example(text):
    print(text)


example('print me')
