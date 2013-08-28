import codecs
import os
import sys
import subprocess


def give_status_print(devicename):
    args = [u'C:\\Users\\ssv\\Documents\\Programs\\net-snmp\\usr\\bin\\snmpget.exe', u'-O Tav -v 1 -c public', u'1.3.6.1.4.1.1347.43.18.2.1.2.1.1']
    args.insert(2, devicename.strip())
    cmd = ' '.join(args)
    PIPE = subprocess.PIPE
    p = subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=subprocess.STDOUT)
    while True:
        s = p.stdout.read()
        u = unicode(s, 'utf-8', errors='ignore')
        if not s:
            break
        print u,


def new_func(mystring):
    snmpbin = [u'dir', '/Q', '/N']
    snmpbin.insert(1, mystring)
    p = subprocess.Popen(snmpbin, shell=True, stdin=PIPE, stdout=PIPE, stderr=subprocess.STDOUT)
    while True:
        s = p.stdout.read()
        if not s:
            break
        print s,
