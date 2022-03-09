import os

dir_my_project = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}

for key, values in dir_my_project.items():
    for val in values:
        dir_set = os.path.join(key, val)
        if not os.path.exists(dir_set):
            os.makedirs(dir_set)
