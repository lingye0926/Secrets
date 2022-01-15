# encoding:utf-8
from win32com.client import Dispatch
import codecs
import numpy as np
import time
import pandas


class Callse16():
    def __init__(self):
        self.R3 = Dispatch("SAP.Functions")
        self.__QIndex__ = 1
        self.__FIndex__ = 1

    def logon(self):
        self.R3.Connection.System = "PRE"
        self.R3.Connection.SystemID = "ERP - PRE [Production EMEA/ROW - Login Default]"
        self.R3.Connection.client = "100"
        self.R3.Connection.user = "CWANG2"
        self.R3.Connection.ApplicationServer = "141.247.199.112"
        self.R3.Connection.Password = "wyq12345"
        self.R3.Connection.Language = "ZH"
        # R3.Connection.Codepage = '8400' # 8400 = simplified Chinese
        self.R3.Connection.Logon(0, True)

    def addMF(self, ModuleFunction="RFC_READ_TABLE"):
        self.MyFunc = self.R3.Add(ModuleFunction)
        self.oParam1 = self.MyFunc.exports("QUERY_TABLE")
        self.oParam2 = self.MyFunc.tables("OPTIONS")
        self.oParam3 = self.MyFunc.tables("FIELDS")
        self.oParam4 = self.MyFunc.tables("DATA")
        self.oParamD = self.MyFunc.exports("DELIMITER")
        self.oParamD.value = '\t'

    def addtable(self, Tablename):
        self.oParam1.value = Tablename

    def addquery(self, Query, logic='AND'):
        if self.__QIndex__ == 1:
            self.oParam2.AppendGridData(self.__QIndex__, 1, 1, Query)
            self.__QIndex__ += 1
        else:
            self.oParam2.AppendGridData(1, 1, 1, logic + ' ' + Query)
            self.__QIndex__ += 1

    def addfields(self, fieldnames):
        for fieldname in fieldnames:
            self.oParam3.AppendGridData(self.__FIndex__, 1, 1, fieldname)
            self.__FIndex__ += 1

    def excute(self):
        self.MyFunc.CALL
        if self.MyFunc:
            return self.oParam4.data
        else:
            return False

#获取表的表头
def gettablelabel(tableName, fields):
    conn = Callse16()
    conn.logon()
    conn.addMF()
    conn.addtable('DDFTX')
    conn.addfields(['FIELDNAME', 'SCRTEXT_L'])
    conn.addquery("TABNAME = '" + tableName + "' AND DDLANGUAGE = '1'")
    data = conn.excute()
    fieldheader = ''
    for field in fields:
        for item in data:
            if item[0].split('\t')[0].strip() == field:
                if fieldheader == '':
                    fieldheader = fieldheader + item[0].split('\t')[1].strip()
                else:
                    fieldheader = fieldheader + '\t' + item[0].split('\t')[1].strip()
    return (fieldheader,)


if __name__ == '__main__':
    header = gettablelabel('ZVS09', ['BISMT', 'MATKL', 'ZCOMTYP', 'LAEDA'])
    newsapconn = Callse16()
    newsapconn.logon()
    newsapconn.addMF()
    newsapconn.addtable('ZVS09')
    newsapconn.addfields(['BISMT', 'MATKL', 'ZCOMTYP', 'LAEDA'])
    newsapconn.addquery("ZCLAND = 'CN'")
    # newsapconn.addquery("VMSTA = 'ZC'")
    data = newsapconn.excute()
    fulldata = (header,) + data
    soldtoData = []
with codecs.open(r'C:\Users\cwang2\Documents\B2B Integration\Data\latest\ZVS09Fin_utf16.txt', 'w', 'utf-16') as f:
    for line in fulldata:
        try:
            textwrite = line[0]
            text = line[0].split('\t')
            if len(text) == 1:
                textwrite = textwrite + '\t' + ' ' + '\t' + ' '
            if len(text) == 2:
                textwrite = textwrite + '\t' + ' '
            f.writelines(textwrite + '\r\n')
        except:
            print(line[0])
    f.close()
