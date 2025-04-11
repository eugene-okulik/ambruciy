def hot_day():
    temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27,
                    22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]
    return list(filter(lambda x: x > 28, temperatures))


def average_temperature():
    average = sum(hot_day()) / len(hot_day())
    return round(average, 2)


print(f'Новые жаркие дни: {hot_day()}')
print(f'Самая высокая температура: {max(hot_day())}')
print(f'Самая низкая температура: {min(hot_day())}')
print(f'Средная температура: {average_temperature()}')
