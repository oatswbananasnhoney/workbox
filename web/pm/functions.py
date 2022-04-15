def time_of_day(h):
    if h>=7 and h<12:
        return 'Доброе утро'
    elif h>=12 and h<18:
        return 'Добрый день'
    elif h>=18 and h<21:
        return 'Добрый вечер'
    elif h>=21:
        return 'Доброй ночи'  
    elif h>24 and h<7:
        return 'Доброй ночи'