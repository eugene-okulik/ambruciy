def result_text(text):
    location = text.index(':') + 1
    print(f'Итоговый результат = {int(text[location:]) + 10}')


result_text('результат операции: 42')
result_text('результат операции: 54')
result_text('результат работы программы: 209')
result_text('результат: 2')
