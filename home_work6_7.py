import sys
edit_idx, new_val = sys.argv[1:]
with open('bakery.csv', 'r+', encoding='utf-8') as f:
    tmp_file = open('bakery.tmp', 'w+')
    change = False
    for i, line in enumerate(f, 1):
        if i == int(edit_idx):
            tmp_file.write(f'{new_val}\n')
            change = True
        else:
            tmp_file.write(line)
    if not change:
        exit('error')
    tmp_file.seek(0)

    f.truncate(0)
    for line in tmp_file:
        f.write(line)
    tmp_file.close()
