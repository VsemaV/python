import itertools

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А'
]

# result = ((tutors[index], klasses[index]) for index in range(len(tutors)))
# print(type(result))
# print(next(result))

for index in itertools.zip_longest(tutors, klasses):
    print(index)
