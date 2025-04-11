import random


def salary_with_bonus():
    salary = input('Какая у вас зарплата?\n')
    bonus = random.choice([True, False])
    if bonus:
        new_salary = int(salary) + random.randrange(1000, 10000, 1000)
        print(f"{salary}, {bonus} - '${new_salary}'")
    else:
        print(f"{salary}, {bonus} - '${salary}'")


salary_with_bonus()
