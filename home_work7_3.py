import os
import shutil
my_dir = 'home_work7_3'
if not os.path.exists(my_dir):
    os.mkdir(my_dir)

folder = r'C:\projects\python\my_project'
files = []


for address, dirs, files_walk in os.walk(folder):
    for file in files_walk:
        if '.html' in file:
            files.append(os.path.join(address, file))
for path in files:
    folder = os.path.join(my_dir, os.path.basename(os.path.dirname(path)))
    if not os.path.exists(folder):
        os.mkdir(folder)
    save_path = os.path.join(folder, os.path.basename(path))
    shutil.copy(path, save_path)
