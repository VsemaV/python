def numbers_generator(max_number):
   for number in range(1, max_number + 1, 2):
       yield number


max_number = int(input('Введите число: '))
numbers_list = numbers_generator(max_number)
print(next(numbers_list))
print(next(numbers_list))
print(next(numbers_list))


numbers_list2 = (number for number in range(1, max_number + 1, 2))


print(next(numbers_list2))
print(next(numbers_list2))
print(next(numbers_list2))
