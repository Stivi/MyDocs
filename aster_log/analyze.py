import gzip
aster_log = gzip.open('aste/Master.csv-20140727.gz', 'rb')

from pandas import DataFrame, Series
import pandas as pd
%pylab inline

real_names = ['accountcode',
         'src',
         'dst',
         'dcontext',
         'clid',
         'channel',
         'dstchannel',
         'lastapp',
         'lastdata',
         'start',
         'answer',
         'end',
         'duration',
         'billsec',
         'disposition',
         'amaflags',
         'userfield',
         'uniqueid']

#TODO
#1.Рисовать на графике отдельно внутренние, отдельно внешние (дата)
names = pd.read_table(aster_log, sep=',', header=None, names=real_names)
names_without = names.drop(['accountcode', 'uniqueid'], axis=1)


# An indication of what happened to the call.
# This may be NO ANSWER, FAILED, BUSY, ANSWERED, or UNKNOWN.
answer_counts = names_without['disposition'].value_counts()
answer_counts[:10]


# The last dialplan application that was executed.
lastapp_counts = names_without['lastapp'].value_counts()
lastapp_counts[:10]


# The destination context for the call.
dcontext_counts = names_without['dcontext'].value_counts()
dcontext_counts[:10]
