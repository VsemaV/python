def thesaurus(*names):
    names_list = {}
    for name in names:
        key = name[0].capitalize()
        if key not in names_list:
            names_list[key] = []
        names_list[key].append(name)
    print(names_list)


thesaurus('Аня', 'Марина', 'Виталий', 'Борис', 'Ярослава', 'Алина')
