duration = int(input('Введите промежуток времени в секундах: '))
seconds = duration % 60
minet = (duration // 60) % 60
hour = ((duration // 60) // 60) % 24
day = ((duration // 60) // 60) // 24
if minet == 0 and hour == 0 and day == 0:
    print('{} сек'.format(seconds))
elif hour == 0 and day == 0:
    print('{} мин {} сек'.format(minet, seconds))
elif day == 0:
    print('{} час {} мин {} сек'.format(hour, minet, seconds))
else:
    print('{} дн {} час {} мин {} сек'.format(day, hour, minet, seconds))
