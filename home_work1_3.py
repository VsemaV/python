persent_list = []
for number in range(1, 101):
    persent_list.append(number)
for number in persent_list:
    if 4 < number % 100 <= 20:
        print('{} процентов'.format(number))
    elif number % 10 == 1:
        print('{} процент'.format(number))
    elif 1 < number % 10 < 5:
        print('{} процента'.format(number))
    else:
        print('{} процентов'.format(number))
