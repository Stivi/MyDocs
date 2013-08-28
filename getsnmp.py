import codecs
import os
import sys
import subprocess

# открывает utf-8 строку как cp1251

s = "РњР°Р»Р°СЏ РјРѕС‰РЅРѕСЃС‚СЊ"
u = unicode(s, "utf-8", errors='ignore')
print u
Малая мощность

keys = u'-v 1 -c public MSK-VPS-MFP 1.3.6.1.4.1.1347.43.18.2.1.2.1.1'
cmd = u'C:\\Users\\ssv\\Documents\\Programs\\net-snmp\\usr\\bin\\snmpget.exe'
cmd = cmd + ' ' + keys
PIPE = subprocess.PIPE

def give_status_print():
    keys = u'-v 1 -c public MSK-VPS-MFP 1.3.6.1.4.1.1347.43.18.2.1.2.1.1'
    cmd = u'C:\\Users\\ssv\\Documents\\Programs\\net-snmp\\usr\\bin\\snmpget.exe'
    cmd = cmd + ' ' + keys
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


