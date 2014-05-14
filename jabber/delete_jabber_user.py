# -*- coding: utf-8 -*-

import codecs
import subprocess


subprocess.call('ejabberdctl registered-users localhost > users.txt', shell=True)

f = codecs.open("users.txt", "r", "utf-8")

users_list = []

while True:
    line = f.readline()
    if not line:
        f.close()
        print('Загружен список пользователей.')
        break
    else:
        users_list.append(line)


delete_user = "belyaev_aleksey_evgenievich"


for user in users_list:
    commands = " ejabberdctl delete-rosteritem " + user.strip() + " localhost " + delete_user.strip() + " localhost"
    subprocess.call(commands, shell=True)
    print('Done for user: ' + user.strip())
