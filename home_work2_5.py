prise_list = [60.55, 54.4, 487, 20.78, 85, 56.2, 120, 73.2, 99.99, 1]


# A
result = []
for prise in prise_list:
    ruble = int(prise // 1)
    coins = int(round(prise - ruble, 2) * 100)

    if coins == 0:
        result.append(f'{ruble} руб {coins}{coins} коп')
    else:
        result.append(f'{ruble} руб {coins} коп')
print(', '.join(result))


# B
prise_list = [60.55, 54.4, 487, 20.78, 85, 56.2, 120, 73.2, 99.99, 1]
print(id(prise_list))
prise_list.sort()
print(prise_list)
print(id(prise_list))


# C
prise_list = [60.55, 54.4, 487, 20.78, 85, 56.2, 120, 73.2, 99.99, 1]
print(sorted(prise_list, reverse=True))


# D
prise_list = [60.55, 54.4, 487, 20.78, 85, 56.2, 120, 73.2, 99.99, 1]
prise_list.sort()
print(prise_list[-3:])
