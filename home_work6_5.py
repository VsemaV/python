import sys
from itertools import zip_longest
users, hobby, out = sys.argv[1:]
with open(out, 'w', encoding='utf-8') as result:
    with open(users) as users:
        with open(hobby) as hobby:
            num_lines_users = sum(1 for line in users)
            num_lines_hobby = sum(1 for line in hobby)

            if num_lines_users < num_lines_hobby:
                exit(1)

            users.seek(0)
            hobby.seek(0)
            for line_user, line_hobby in zip_longest(users, hobby):
                result.write(f'{line_user.strip().replace(";", " ")}: '
                             f'{line_hobby.strip() if line_hobby is not None else line_hobby}\n')
