def guess_the_number(x):
    while True:
        a = input('Введите цифру: ')
        if int(a) == x:
            print('Поздравляю! Вы угадали!')
            break
        else:
            print('попробуйте снова')


guess_the_number(5)
