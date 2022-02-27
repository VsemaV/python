user_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

unique_numbers = set()
for number in user_list:
    if number not in unique_numbers:
        unique_numbers.add(number)
    else:
        unique_numbers.discard(number)
unique_numbers_order = [number for number in user_list if number in unique_numbers]

print(unique_numbers_order)
