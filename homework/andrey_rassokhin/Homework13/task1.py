import os
import datetime


my_path = os.path.dirname(__file__)
homework_dir_path = os.path.dirname(os.path.dirname(my_path))
eu_file_path = os.path.join(homework_dir_path, 'eugene_okulik', 'hw_13', 'data.txt')


def working_with_file(path_to_file):
    with open(path_to_file, 'r', encoding='utf-8') as data_file:
        # Подумал, что можно сделать через обычный цикл т.к известно кол-во строк в файле
        for line in data_file.readlines():
            date = datetime.datetime.strptime(line[3:29], '%Y-%m-%d %H:%M:%S.%f')
            if int(line[0]) == 1:
                delta = datetime.timedelta(days=7)
                new_date = date + delta
                print(new_date)
            elif int(line[0]) == 2:
                day_of_the_week = datetime.datetime.strftime(date, '%A')
                print(day_of_the_week)
            elif int(line[0]) == 3:
                date_now = datetime.datetime.now()
                result_date = date_now - date
                print(result_date)


working_with_file(eu_file_path)
