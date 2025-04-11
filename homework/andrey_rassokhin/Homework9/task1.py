import datetime


def transformation_from_python():
    date = 'Jan 15, 2023 - 12:05:33'
    python_date = datetime.datetime.strptime(date, '%b %d, %Y - %H:%M:%S')
    return python_date


def output_full_month():
    month = transformation_from_python().month
    month_transform = datetime.datetime(2023, month, 15).strftime('%B')
    return month_transform


def transformation_from_human():
    date = transformation_from_python().strftime('%d.%m.%Y, %H:%M')
    return date


print(transformation_from_python())
print(output_full_month())
print(transformation_from_human())
