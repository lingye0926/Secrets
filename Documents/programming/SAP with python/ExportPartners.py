import SAPConn
import codecs
import pandas as pd
#
# fields = ['VBELN']
# newconn = SAPConn.Callse16()
# newconn.logon()
# newconn.addMF()
# newconn.set_table('VBAK')
# newconn.set_fields(fields)
# newconn.set_queries("VKORG = '1390'")
# newconn.set_queries("ERDAT >= '2013/01/01' AND ERDAT <= '2017/03/09'")
# data = newconn.excute()
# header = newconn.getfieldsdesc()
# fulldata = header + data

# with codecs.open("C:\Users\cwang2\PycharmProjects\SAPConnection\Temp.txt", 'w', encoding='utf-16') as f:
#     for d in fulldata:
#         try:
#             f.writelines(d[0] + '\n')
#         except:
#             pass
#     f.close()

flist = codecs.open("C:\Users\cwang2\PycharmProjects\SAPConnection\Temp.txt",encoding='utf-16').readlines()
fields = ['VBELN', 'PARVW', 'KUNNR']
newconn = SAPConn.Callse16()
newconn.logon()
newconn.addMF()
newconn.set_table('VBPA')
newconn.set_fields(fields)
newconn.set_queries("LAND1 = 'CN'")
newconn.set_queries("PARVW = 'RG' OR PARVW = 'RE' OR PARVW = 'WE'")
newconn.set_batch_queries_or('VBELN', flist, 800)
data = newconn.excute()
header = newconn.getfieldsdesc()
fulldata = header + data
with codecs.open("C:\Users\cwang2\PycharmProjects\SAPConnection\Temp2.txt", 'w', encoding='utf-16') as f:
    for d in fulldata:
        try:
            f.writelines(d[0] + '\n')
        except:
            pass
    f.close()