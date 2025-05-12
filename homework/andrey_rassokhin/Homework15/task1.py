import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

insert_query_student = "INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, NULL)"
values = [
    ('Джонни', 'Депп')
]

cursor.executemany(insert_query_student, values)
student_id = cursor.lastrowid

insert_query_group = "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)"
values = [
    ('Актеры', 'Май 2025', 'Май 2025')
]
cursor.executemany(insert_query_group, values)
group_id = cursor.lastrowid

update_query_student = "UPDATE students SET group_id = %s where id = %s"

cursor.execute(update_query_student, (group_id, student_id))

insert_query_books = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
values = [
    ('Актерское мастерство', student_id),
    ('История кинематографа', student_id)
]

cursor.executemany(insert_query_books, values)

insert_query_subjets = "INSERT INTO subjets (title) VALUES (%s)"
values = [
    # Зачем запятая после в скобочках?Без нее не работает
    ('Актерское мастерство',),
    ('История кинематографа',)
]

sub_ids = []
for value in values:
    cursor.execute(insert_query_subjets, value)
    sub_id = cursor.lastrowid
    sub_ids.append(sub_id)

subjets_id_1 = sub_ids[0]
subjets_id_2 = sub_ids[1]


insert_query_lessons = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
values = [
    ('Понедельник', subjets_id_1),
    ('Среда', subjets_id_1),
    ('Понедельник', subjets_id_2),
    ('Среда', subjets_id_2)
]

les_ids = []
for value in values:
    cursor.execute(insert_query_lessons, value)
    les_id = cursor.lastrowid
    les_ids.append(les_id)

les_id_1 = les_ids[0]
les_id_2 = les_ids[1]
les_id_3 = les_ids[2]
les_id_4 = les_ids[3]

insert_query_marks = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
values = [
    ('4', les_id_1, student_id),
    ('5', les_id_2, student_id),
    ('4', les_id_3, student_id),
    ('5', les_id_4, student_id)
]

cursor.executemany(insert_query_marks, values)

select_marks_student = '''
SELECT value
from marks
where student_id = %s
'''
cursor.execute(select_marks_student, (student_id,))
print(cursor.fetchall())

select_books_student = '''
select title
from books
where taken_by_student_id = %s
'''

cursor.execute(select_books_student, (student_id,))
print(cursor.fetchall())

select_all_info_student = '''
select s.name as 'Имя', s.second_name as 'Фамилия',
g.title as 'Группа', g.start_date as 'Дата начала',g.end_date as 'Дата окончания',
b.title as 'Название книги', m.value as 'Оценка',
l.title as 'День проведения занятия', s2.title as 'Предмет'
from students s
join `groups` g
on s.group_id = g.id
join books b
on s.id = b.taken_by_student_id
join marks m
on s.id = m.student_id
join lessons l
on m.lesson_id = l.id
join subjets s2
on l.subject_id = s2.id
where s.id = %s
'''

cursor.execute(select_all_info_student, (student_id,))
print(cursor.fetchall())

db.commit()

db.close()
