# numbers_list = []
# number = 0
# while number <= 20:
#     if number % 2 != 0:
#         numbers_list.append(number ** 3)
#     number += 1
numbers_list = [number ** 3 for number in range(1, 1001) if number % 2 == 1]
print(numbers_list)
result = 0
for index in numbers_list:
    number_sum = index
    sum_check = 0
    while index > 0:
        digit = index % 10
        sum_check += digit
        index //= 10
    if sum_check % 7 == 0:
        result += number_sum
print(result)

# каждому элементу списка добавить 17 и заново вычислить сумму
result = 0
for index in numbers_list:
    index += 17
    number_sum = index
    sum_check = 0
    while index > 0:
        digit = index % 10
        sum_check += digit
        index //= 10
    if sum_check % 7 == 0:
        result += number_sum
print(result)
