class Book:
    material = 'бумага'
    text = True

    def __init__(self, title: str, author: str, pages: int, isbn: int, reserved: bool):
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reserved = reserved

    '''
    Изначально не понял, как описать метод с if-ом. Пришлось гуглить, применил магический метод __str__,
    все сработало,но так и не понял каким образом. Можете объяснить подробнее,
    почему нужно в данном случае применять его, а нельзя просто создать обычный метод внутри класса.
    '''

    def __str__(self):
        if self.reserved:
            return (f'Название: {self.title}, Автор: {self.author}, '
                    f'страниц: {self.pages}, материал: {self.material}, зарезервирована')
        else:
            return (f'Название: {self.title}, Автор: {self.author}, '
                    f'страниц: {self.pages}, материал: {self.material}')


class SchoolBooks(Book):

    def __init__(self, title: str, author: str, pages: int, isbn: int, reserved: bool, item: str, group: str,
                 exercise: bool):
        super().__init__(title, author, pages, isbn, reserved)
        self.item = item
        self.group = group
        self.exercise = exercise

    def __str__(self):
        if self.reserved:
            return (f'Название: {self.title}, Автор: {self.author}, '
                    f'страниц {self.pages}, предмет: {self.item}, '
                    f'класс: {self.group}, зарезервирована ')
        else:
            return (f'Название: {self.title}, Автор: {self.author}, '
                    f'страниц {self.pages}, предмет: {self.item}, '
                    f'класс: {self.group}')


first_book = Book('Преступление и наказание', 'Ф.М.Достоевский', 672, 4587, False)
second_book = Book('Гарри Поттер', 'Дж.К.Роулинг', 120, 9863, False)
third_book = Book('1984', 'Д.Оруэлл', 120, 10589, False)
fourth_book = Book('Властелин колец', 'Дж.Р.Р.Толкиен', 752, 1574, True)
fifth_book = Book('Сильмариллион', 'Дж.Р.Р.Толкиен', 448, 8217, False)

first_textbook = SchoolBooks('Математика для старшей школы', 'М.В.Ломоносов', 100, 4178, False, 'Алгебра', '11Б', True)
second_textbook = SchoolBooks('История древней Греции', 'Геродот', 90, 74936, True, 'История', '9А', True)
third_textbook = SchoolBooks('Вокруг света за 80 дней', 'Жюль Верн', 256, 99874, False, 'Окружающий мир', '6В', True)

print(first_book)
print(second_book)
print(third_book)
print(fourth_book)
print(fifth_book)
print(90 * '-')
print(first_textbook)
print(second_textbook)
print(third_textbook)
