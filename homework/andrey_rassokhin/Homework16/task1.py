import os
import csv
import mysql.connector as mysql
import dotenv

dotenv.load_dotenv()

query = '''
select s.name,s.second_name,
g.title as group_title, b.title as book_title,
s2.title as subject_title, l.title as lesson_title,
m.value as mark_value
from students s
join `groups` g
on s.group_id = g.id
join books b
on s.id = b.taken_by_student_id
join marks m
on s.id = m.student_id
join lessons l
on l.id  = m.lesson_id
join subjets s2
on s2.id = l.subject_id
'''


def work_with_db(query):
    db = mysql.connect(
        user=os.getenv('DB_USER'),
        passwd=os.getenv('DB_PASSW'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT'),
        database=os.getenv('DB_NAME')
    )
    cursor = db.cursor(dictionary=True)
    db.commit()
    cursor.execute(query)
    data = cursor.fetchall()
    db.close()
    return data


def path_from_file(*path):
    my_path = os.path.dirname(__file__)
    homework_dir_path = os.path.dirname(os.path.dirname(my_path))
    eu_file_path = os.path.join(homework_dir_path, *path)
    return eu_file_path


def work_with_file(path, data):
    with open(path, newline='') as csv_file:
        file_data = csv.DictReader(csv_file)
        for raw in file_data:
            if raw not in data:
                print(f'Такой строки нет в БД: {raw}')


result_query = work_with_db(query)
path = path_from_file('eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')
work_with_file(path, result_query)
