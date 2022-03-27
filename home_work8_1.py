import re
EMAIL = re.compile(r'([a-z0-9]+)@([a-z0-9]+\.[a-z]+)')


def email_parse(email):
    found_info = EMAIL.findall(email)
    print(found_info)
    if found_info and found_info[0]:
        name, addr = found_info[0]
    else:
        raise ValueError(f'wrong email: {email}')
    return name, addr

print(email_parse('19someone19@geekbrains13.ru'))
print(email_parse('someonegeekbrains.ru'))
