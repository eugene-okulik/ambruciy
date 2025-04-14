PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''


def price(data):
    new_list = PRICE_LIST.split()
    edit_list = [x.rstrip('р') for x in new_list]
    key = [x for x in edit_list[::2]]
    value = [int(x) for x in edit_list[1::2]]
    new_dict = dict(zip(key, value))
    return new_dict


print(price(PRICE_LIST))
