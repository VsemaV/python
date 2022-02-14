persent_list = []
for number in range(1, 101):
    persent_list.append(number)
for number in persent_list:
    if number % 10 == 1:
        print('{} процент'.format(number))
    elif 2 <= number % 10 <= 4:
        print('{} процента'.format(number))
    else:
        print('{} процентов'.format(number))
