for a in range(1, 101):
    if a % 3 == 0 and a % 5 == 0:
        print('FuzzBuzz')
    elif a % 5 == 0:
        print('Buzz')
    elif a % 3 == 0:
        print('Fuzz')
    else:
        print(a)
