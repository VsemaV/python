# get_sign - функция для получения знака первого символа, чтобы отличать числа
def get_sign(number):
    if number[0] in '+-':
        return number[0]

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

index = 0
while index < len(my_list):
    sign = get_sign(my_list[index])
    # isdigit() возвращает True, если все символы в строке являются цифрами
    if my_list[index].isdigit() or (sign and my_list[index][1:].isdigit()):
        if sign:
            # zfill добавляет слева 0 до указанной в него длины
            my_list[index] = sign + my_list[index][1:].zfill(2)
        else:
            my_list[index] = my_list[index].zfill(2)

        my_list.insert(index, '"')
        my_list.insert(index + 2, '"')
        index += 2

    index += 1

print(' '.join(my_list))