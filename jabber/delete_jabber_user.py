# -*- coding: utf-8 -*-

import codecs
import subprocess


ls_output = subprocess.call('ejabberdctl registered-users localhost', shell=True, stderr=None)

print(ls_output)


f = codecs.open("users.txt", "r", "utf-8")


def list_users():
    print('ejabberdctl registered-users localhost')


def pretty(dict):
     print repr(dict).decode("unicode-escape")


list_users()

users_list = []

while True:
    line = f.readline()
    if not line:
        print('выхожу из цикла')
        f.close()
        break
    else:
        users_list.append(line)

pretty(users_list)
