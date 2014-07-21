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

names = pd.read_table('out.log', sep=',', header=None, names=real_names)

names_without = names.drop(['accountcode', 'uniqueid'], axis=1)

frame = DataFrame(names_without)
tz_counts = frame['src'].value_counts()
tz_counts[:20]

tz_counts[:10].plot(kind='barh', rot=0)
