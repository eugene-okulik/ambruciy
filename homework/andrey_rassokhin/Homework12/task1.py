class Flowers:
    petals = True

    def __init__(self, name: str, color: str, price: int, freshness: str, stem_length: int, quantity: int):
        self.name = name
        self.color = color
        self.price = price
        self.freshness = freshness
        self.stem_length = stem_length
        self.quantity = quantity


class Rose(Flowers):
    life_span = 5

    def __init__(self, name: str, color: str, price: int,
                 freshness: str, stem_length: int,
                 quantity: int, spikes: bool):
        super().__init__(name, color, price, freshness, stem_length, quantity)
        self.spikes = spikes

    def __repr__(self):
        return (f'Название цветка: {self.name}, Цвет: {self.color}, Стоимость: {self.price}, '
                f'Свежесть: {self.freshness}, Длина стебля: {self.stem_length} см, Кол-во цветов: {self.quantity}, '
                f'Наличие шипов: {self.spikes}')


class Tulips(Flowers):
    life_span = 7

    def __init__(self, name: str, color: str, price: int,
                 freshness: str, stem_length: int,
                 quantity: int, field: bool):
        super().__init__(name, color, price, freshness, stem_length, quantity)
        self.field = field

    def __repr__(self):
        return (f'Название цветка: {self.name}, Цвет: {self.color}, Стоимость: {self.price}, '
                f'Свежесть: {self.freshness}, Длина стебля: {self.stem_length} см, Кол-во цветов: {self.quantity}, '
                f'Полевые цветы: {self.field}')


class Peonies(Flowers):
    life_span = 4

    def __init__(self, name: str, color: str, price: int,
                 freshness: str, stem_length: int,
                 quantity: int, country: str):
        super().__init__(name, color, price, freshness, stem_length, quantity)
        self.country = country

    def __repr__(self):
        return (f'Название цветка: {self.name}, Цвет: {self.color}, Стоимость: {self.price}, '
                f'Свежесть: {self.freshness}, Длина стебля: {self.stem_length} см, Кол-во цветов: {self.quantity}, '
                f'Страна производителя: {self.country}')


class Bouquet:

    def __init__(self):
        self.flowers = []

    def create_bouquet(self, flower):
        self.flowers.append(flower)

    def price_in_bouquet(self):
        return f'Стоимость букета: {sum(flower.price * flower.quantity for flower in self.flowers)} руб.'

    def time_of_fading(self):
        time_of_fading = (sum(flower.life_span for flower in self.flowers))/len(self.flowers)
        return f'Время увядания: {round(time_of_fading, 2)} дней.'

    def sort_for_freshness(self):
        # Пришлось долго разбираться, с лямбда функцией в ключе.
        sort = sorted(self.flowers, key=lambda flower: flower.freshness)
        # Про list-comprehension вообще забыл
        return [flower.name for flower in sort]

    def sort_for_price(self):
        sort = sorted(self.flowers, key=lambda flower: flower.price)
        return [flower.name for flower in sort]

    def sort_for_color(self):
        sort = sorted(self.flowers, key=lambda flower: flower.color)
        return [flower.name for flower in sort]

    def sort_for_stem_length(self):
        sort = sorted(self.flowers, key=lambda flower: flower.stem_length)
        return [flower.name for flower in sort]

    def search_flowers(self, life_span):
        for flower in self.flowers:
            if flower.life_span == life_span:
                return f'Цветок в букете с таким временем жизни: {flower.name}'
        else:
            return 'Цветка с таким временем жизни нет'

    # Декоратор для текса о составе букета
    def add_text(func):
        def wrapper(self):
            print('Букет состоит из: ')
            func(self)
        return wrapper

    @add_text
    def print_flower(self):
        for flower in self.flowers:
            print(
                f'Цветок: {flower.name}, '
                f'Цена: {flower.price}, '
                f'Кол-во: {flower.quantity}')


red_rose = Rose('Красная Роза', 'Красный', 150, 'Свежие', 50, 5, True)
yellow_tulips = Tulips('Желтые тюльпаны', 'Желтый', 100, 'Позавчерашние', 30, 3, True)
french_peonies = Peonies('Пионы', 'Белый', 300, 'Неделя', 40, 5, 'Франция')

print(red_rose)
print(yellow_tulips)
print(french_peonies)

# Создали экземпляр класса, чтобы использоваеть его методы?
bouquet = Bouquet()
bouquet.create_bouquet(red_rose)
bouquet.create_bouquet(yellow_tulips)
bouquet.create_bouquet(french_peonies)

bouquet.print_flower()
print(bouquet.price_in_bouquet())
print(bouquet.time_of_fading())
print(f'Сортировка по стоимости: {bouquet.sort_for_price()}')
print(f'Сортировка по свежести: {bouquet.sort_for_freshness()}')
print(f'Сортировка по цвету: {bouquet.sort_for_color()}')
print(f'Сортировка по длине стебля: {bouquet.sort_for_stem_length()}')
print(bouquet.search_flowers(5))
