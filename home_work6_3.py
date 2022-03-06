from itertools import zip_longest
import json


out_dict = {}
with open('user.csv') as users:
    with open('hobby.csv') as hobby:
        num_lines_users = sum(1 for line in users)
        num_lines_hobby = sum(1 for line in hobby)

        if num_lines_users < num_lines_hobby:
            exit(1)

        users.seek(0)
        hobby.seek(0)
        for line_user, line_hobby in zip_longest(users, hobby):
            out_dict[line_user.strip().replace(";", " ")] = line_hobby.strip() if line_hobby is not None else line_hobby

with open('task6_3.json', 'w', encoding='utf-8') as result:
    json.dump(out_dict, result, ensure_ascii=False)
print(out_dict)
