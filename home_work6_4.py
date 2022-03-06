from itertools import zip_longest

with open('task6_4.txt', 'w', encoding='utf-8') as result:
    with open('user.csv') as users:
        with open('hobby.csv') as hobby:
            num_lines_users = sum(1 for line in users)
            num_lines_hobby = sum(1 for line in hobby)

            if num_lines_users < num_lines_hobby:
                exit(1)

            users.seek(0)
            hobby.seek(0)
            for line_user, line_hobby in zip_longest(users, hobby):
                result.write(f'{line_user.strip().replace(";", " ")}: '
                             f'{line_hobby.strip() if line_hobby is not None else line_hobby}\n')
