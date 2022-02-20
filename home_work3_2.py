def num_translate(number):
    list_translate = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }
    return list_translate.get(number, None)


user_number = input('Введите число на английском: ')
if user_number.istitle():
    if num_translate(user_number.lower()):
        print(f'{user_number.capitalize()} - {num_translate(user_number.lower()).capitalize()}')
    else:
        print(f'{user_number.capitalize()} - {num_translate(user_number.lower())}')
else:
    print(f'{user_number} - {num_translate(user_number)}')
