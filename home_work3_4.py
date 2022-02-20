def thesaurus(*names):
    surnames_list = {}
    for surname in names:
        key_surname = surname.split(' ')[1][0]
        if key_surname not in surnames_list:
            surnames_list[key_surname] = []
        surnames_list[key_surname].append(surname)

    for name in surnames_list:
        index = 0
        names_list = {}
        while index < len(surnames_list[name]):
            key_name = surnames_list[name][index][0]
            if key_name not in names_list:
                names_list[key_name] = []
            names_list[key_name].append(surnames_list[name][index])
            index += 1
        surnames_list[name] = names_list
    print(surnames_list)


thesaurus("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
