import os
files = []
for address, dirs, files_walk in os.walk('./'):
    for file in files_walk:
        file_path = os.path.join(address, file)
        files.append(os.stat(file_path).st_size)

max_size = max(files)

i = 1
out_dict = {}

for _ in range(len(str(max_size))):
    i *= 10
    out_dict[i] = 0

for file in files:
        out_dict[10 ** len(str(file))] += 1

print(out_dict)
