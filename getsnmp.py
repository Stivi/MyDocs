# -*- coding: utf-8 -*-

import subprocess


def kyocera_status_print(devicename):
    """kyocera_status_print('  MSK-MENEDG-MFP1   ')"""
    args = [u'C:\\Users\\ssv\\Documents\\Programs\\net-snmp\\usr\\bin\\snmpget.exe', u'-O Tav -v 1 -c public', u'1.3.6.1.4.1.1347.43.18.2.1.2.1.1']
    devicename = devicename.strip()
    devicename = unicode(devicename, 'cp1251')
    args.insert(2, devicename)
    cmd = ' '.join(args)
    PIPE = subprocess.PIPE
    p = subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=subprocess.STDOUT)
    while True:
        s = p.stdout.read()
        u = unicode(s, 'utf-8', errors='ignore')
        if not s:
            break
        print u,


def main():
    kyocera_status_print.__doc__


if __name__ == '__main__':
    main()
