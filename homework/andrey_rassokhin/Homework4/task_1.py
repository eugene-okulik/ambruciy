my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': ['red', 'green', 'blue', 'grey', 'white'],
    'dict': {
        'name': 'Иван',
        'second_name': 'Иванов',
        'age': '35',
        'city': 'Mocsow',
        'gender': 'man'
    },
    'set': {1, 10, 100, 1000, 1000},
 }

print(f"Последний элемент словаря {my_dict['tuple'][-1]}")
my_dict['list'].append('black')
my_dict['list'].pop(1)
my_dict['dict']['i am a tuple'] = True
my_dict['dict'].pop('age')
my_dict['set'].add(10000)
my_dict['set'].remove(10)
print(f'Итоговый вывод словаря {my_dict}')
