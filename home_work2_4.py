my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for name_list in my_list:
    name_list_part = name_list.split(' ')
    print(f'Привет, {name_list_part[-1].capitalize()}!')

