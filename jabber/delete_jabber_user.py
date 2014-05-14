# -*- coding: utf-8 -*-

import codecs
import subprocess


f = codecs.open("users.txt", "r", "utf-8")

users_list = []

while True:
    line = f.readline()
    if not line:
        f.close()
        print('выхожу из цикла')
        break
    else:
        users_list.append(line)


delete_user = "medvedev_vladimir_olegovich"

for user in users_list:
    print(" ejabberdctl delete-rosteritem " + user.strip() + " localhost " + delete_user.strip() + " localhost")
    print(' done for user: ' + user.strip())
