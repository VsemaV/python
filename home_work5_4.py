user_numbers = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result = [user_numbers[index] for index in range(1, len(user_numbers)) if user_numbers[index] > user_numbers[index-1]]
print(result)
