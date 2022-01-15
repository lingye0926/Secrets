# encoding:utf-8
from win32com.client import Dispatch
import codecs
import math
import win32gui
import win32con
import time
from multiprocessing import Process

class Callva05():
    def __init__(self):
        self.R3 = Dispatch("SAP.Functions")
        self.__queries = []
        self.__queries_or = []
        self.__batch_queries_or = None
        self.__or_values = []
        self.__PRE_Config = {'System': 'PRE',
                             'SystemID': 'PRE", "ERP - PRE [Production EMEA/ROW - Login Default]',
                             'client': '100',
                             'user': 'lye',
                             'ApplicationServer': '141.247.199.103',
                             'Password': 'lingye3EDC',
                             'Language': 'ZH'}
        self.__URP_Config = {'System': 'URP',
                             'SystemID': 'SAPNext - URP [ ERP Quality ] HANA',
                             'client': '100',
                             'user': 'cwang2',
                             'ApplicationServer': '172.16.30.30',
                             'Password': 'wyq123456789',
                             'Language': 'EN'}
        self.__PRP_Config = {'System': 'PRP',
                             'SystemID': 'SAPNext - PRP [ ERP Production ] HANA',
                             'client': '100',
                             # 'user': 'cwang2',
                             'user': 'lye',
                             'ApplicationServer': 'sapprpap1.sial.com',
                             # 'Password': 'wyq1234567890-',
                             'Password': '3EDC6yhn.*',
                             'Language': 'EN'}

    def get_conn(self, conn):
        self.R3 = conn

    def logon(self, sys='PRE'):
        if sys == 'PRE':
            sys_config = self.__PRE_Config
        if sys == 'URP':
            sys_config = self.__URP_Config
        if sys == 'PRP':
            sys_config = self.__PRP_Config
        self.R3.Connection.System = sys_config['System']
        self.R3.Connection.SystemID = sys_config['SystemID']
        self.R3.Connection.client = sys_config['client']
        self.R3.Connection.user = sys_config['user']
        self.R3.Connection.ApplicationServer = sys_config['ApplicationServer']
        self.R3.Connection.Password = sys_config['Password']
        self.R3.Connection.Language = sys_config['Language']
        # self.R3.Connection.Autologon = 1
        # R3.Connection.Codepage = '8400' # 8400 = simplified Chinese
        self.R3.Connection.Logon(0, 0)
        # while win32gui.FindWindowEx(win32gui.FindWindowEx(0, 0, "#32770", u'SAP Logon 在 PRE'), 0, "Button", u'确定(&O)') == 0:
        #     pass
        # win32gui.SendMessage(
        #     win32gui.FindWindowEx(win32gui.FindWindowEx(0, 0, "#32770", u'SAP Logon 在 PRE'), 0, "Button", u'确定(&O)'),
        #     win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, 0)
        # win32gui.SendMessage(
        #     win32gui.FindWindowEx(win32gui.FindWindowEx(0, 0, "#32770", u'SAP Logon 在 PRE'), 0, "Button", u'确定(&O)'),
        #     win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, 0)

    # def logon(self):
    #     process = []
    #     p1 = Process(target=self.logonprocess)
    #     p1.start()
    #     process.append(p1)
    #     p2 = Process(target=self.monitorLogon)
    #     p2.start()
    #     process.append(p2)

    def addMF(self, ModuleFunction="BAPI_SALESORDER_GETLIST"):
        self.MyFunc = self.R3.Add(ModuleFunction)
        self.CustomerNB = self.MyFunc.exports("CUSTOMER_NUMBER")
        self.SalesOrg = self.MyFunc.exports("SALES_ORGANIZATION")
        self.Material = self.MyFunc.exports("MATERIAL")
        self.dateFrom = self.MyFunc.exports("DOCUMENT_DATE")
        self.dateTo = self.MyFunc.exports("DOCUMENT_DATE_TO")
        self.SOList = self.MyFunc.tables("SALES_ORDERS")
        self.__CustomerNB = ''
        self.__SalesOrg = ''
        self.__dateFrom = ''
        self.__dateTo = ''
        self.__Material = ''
        self.__QIndex = 1  # where条件索引，用来判断是否是第一行
        self.__FIndex = 1  # 字段索引，传递到table中
        self.__result = False


        # 初始化参数，移除原有表中的数据，防止再次请求数据叠加
        while self.SOList.rows.count > 0:
            self.fields.rows.removeall()

    def set_CustomerNB(self, customerNB):
        '''设置SOLDTO'''
        self.__CustomerNB = unicode(customerNB)

    def __addCustomerNB__(self):
        self.CustomerNB.Value = self.__CustomerNB

    def set_SalesOrg(self, SalesOrg='1390'):
        '''设置SalesOrg'''
        self.__SalesOrg = SalesOrg

    def __addSalesOrg__(self):
        self.SalesOrg.Value = self.__SalesOrg

    def set_Material(self, Material):
        '''设置SalesOrg'''
        self.__Material = Material

    def __addMaterial__(self):
        self.Material.Value = self.__Material

    def set_dateFrom(self, dateFrom):
        '''设置SalesOrg'''
        self.__dateFrom = dateFrom

    def __adddateFrom__(self):
        self.dateFrom.Value = self.__dateFrom

    def set_dateTo(self, dateTo):
        self.__dateTo = dateTo

    def __adddateTo__(self):
        self.dateTo.Value = self.__dateTo



    def excute(self):
        '''将所有设置的参数汇总并执行'''
        if self.__SalesOrg != '':
            self.__addSalesOrg__()
        if self.__CustomerNB != '':
            self.__addCustomerNB__()
        if self.__Material != '':
            self.__addMaterial__()
        if self.__dateFrom != '':
            self.__adddateFrom__()
        if self.__dateTo != '':
            self.__adddateTo__()
        self.MyFunc.CALL
        return self.SOList.data

    def getfieldsdesc(self):
        returnfields = ''
        if self.__result:
            for field in self.fields.data:
                if returnfields == u'':
                    returnfields = field[4]
                else:
                    returnfields  = returnfields + '\t' + field[4]
        return (returnfields,),


class Callse16():
    def __init__(self):
        self.R3 = Dispatch("SAP.Functions")
        self.__queries = []
        self.__queries_or = []
        self.__batch_queries_or = None
        self.__or_values = []
        self.__PRE_Config = {'System': 'PRE',
                         'SystemID': u"ERP - PRE [Production EMEA/ROW - Login Default]",
                         'client': '100',
                         'user': 'cwang2',
                         'ApplicationServer': '3',
                         'Password': 'wyq12349',
                         'Language': 'ZH'}
        self.__URP_Config = {'System': 'URP',
                         'SystemID': 'SAPNext - URP [ ERP Quality ] HANA',
                         'client': '100',
                         'user': 'cwang2',
                         'ApplicationServer': '172.16.30.30',
                         'Password': 'wyq123456789',
                         'Language': 'EN'}
        self.__PRP_Config = {'System': 'PRP',
                         'SystemID': u'SAPNext - PRP [ ERP Production ] HANA',
                         'client': '100',

                         'user': 'NZHANG',
                         'ApplicationServer': 'sapprpap1.sial.com',

                         'Password': 'zhangb03',
                         'Language': 'EN'}

        self.__PTR_Config = {'System': 'PTR',
                             'SystemID': u'SAPNext - PTR [ GTS Production ] HANA',
                             'client': '100',
                             'user': 'gchen',
                             'ApplicationServer': 'sapptrap1.sial.com',
                             'Password': 'gchen000',
                             'Language': 'EN'}
        self.__MERCK_Config = {'System': 'P95',
                             'SystemID': u'P95 - Merck ERP EMERALD Asia Production System',
                             'client': '300',
                             'user': 'M177222',
                             'ApplicationServer': 'mdap95.merckgroup.com',
                             'Password': 'Sh@nghai04',
                             'Language': 'EN'}
    def get_conn(self, conn):
        self.R3 = conn

    def monitorLogon(self):
        while win32gui.FindWindowEx(win32gui.FindWindowEx(0, 0, "#32770", u'SAP Logon 在 PRE'), 0, "Button",
                                    u'确定(&O)') == 0:
            pass
        win32gui.SendMessage(
            win32gui.FindWindowEx(win32gui.FindWindowEx(0, 0, "#32770", u'SAP Logon 在 PRE'), 0, "Button", u'确定(&O)'),
            win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, 0)
        win32gui.SendMessage(
            win32gui.FindWindowEx(win32gui.FindWindowEx(0, 0, "#32770", u'SAP Logon 在 PRE'), 0, "Button", u'确定(&O)'),
            win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, 0)

    def logon(self, sys='PRE'):
        if sys == 'PRE':
            sys_config = self.__PRE_Config
        if sys == 'URP':
            sys_config = self.__URP_Config
        if sys == 'PRP':
            sys_config = self.__PRP_Config
        if sys == 'PTR':
            sys_config = self.__PTR_Config
        if sys == 'MERCK':
            sys_config = self.__MERCK_Config
        self.R3.Connection.System = sys_config['System']
        self.R3.Connection.SystemID = sys_config['SystemID']
        self.R3.Connection.client = sys_config['client']
        self.R3.Connection.user = sys_config['user']
        self.R3.Connection.ApplicationServer = sys_config['ApplicationServer']
        self.R3.Connection.Password = sys_config['Password']
        self.R3.Connection.Language = sys_config['Language']
        self.R3.Connection.Codepage = '8400' # 8400 = simplified Chinese
        self.R3.Connection.Logon(0, 1)
        # while win32gui.FindWindowEx(win32gui.FindWindowEx(0, 0, "#32770", u'SAP Logon 在 PRE'), 0, "Button", u'确定(&O)') == 0:
        #     pass
        # win32gui.SendMessage(
        #     win32gui.FindWindowEx(win32gui.FindWindowEx(0, 0, "#32770", u'SAP Logon 在 PRE'), 0, "Button", u'确定(&O)'),
        #     win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, 0)
        # win32gui.SendMessage(
        #     win32gui.FindWindowEx(win32gui.FindWindowEx(0, 0, "#32770", u'SAP Logon 在 PRE'), 0, "Button", u'确定(&O)'),
        #     win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, 0)

    # def logon(self):
    #     process = []
    #     p1 = Process(target=self.logonprocess)
    #     p1.start()
    #     process.append(p1)
    #     p2 = Process(target=self.monitorLogon)
    #     p2.start()
    #     process.append(p2)

    def addMF(self, ModuleFunction="RFC_READ_TABLE"):
        self.MyFunc = self.R3.Add(ModuleFunction)
        self.tb = self.MyFunc.exports("QUERY_TABLE")
        self.opt = self.MyFunc.tables("OPTIONS")
        self.fields = self.MyFunc.tables("FIELDS")
        self.data = self.MyFunc.tables("DATA")
        self.delimiter = self.MyFunc.exports("DELIMITER")
        self.__QIndex = 1  # where条件索引，用来判断是否是第一行
        self.__FIndex = 1  # 字段索引，传递到table中
        self.__result = False


        # 初始化参数，移除原有表中的数据，防止再次请求数据叠加
        while self.fields.rows.count > 0:
            self.fields.rows.removeall()
        while self.opt.rows.count > 0:
            self.opt.rows.removeall()
        while self.data.rows.count > 0:
            self.data.rows.removeall()
        self.delimiter.value = '\t'

    def set_table(self, tablename):
        '''设置需要读取的SE16表'''
        self.__tablename = unicode(tablename)

    def __addtable__(self):
        self.tb.value = self.__tablename

    def set_queries(self, queries, logic='AND'):
        '''设置需要查询的条件，不包含单个field的多条件'''
        self.__queries.append([unicode(queries), unicode(logic)])

    def __addquery__(self):
        for query in self.__queries:
            if self.__QIndex == 1:
                self.opt.AppendGridData(self.__QIndex, 1, 1, query[0].upper())
                self.__QIndex += 1
            else:
                self.opt.AppendGridData(1, 1, 1, query[1] + ' ' + query[0].upper())
                self.__QIndex += 1

    def set_batch_queries_or(self, batch_field, batch_queries_or, batch_nb):
        '''如果因为超时需要分批查询，将需要分批查询的字段和条件放在此参数中'''
        self.__batch_queries_or = [unicode(batch_field), batch_queries_or, unicode(batch_nb)]

    def set_queries_or(self, field, queries_or):
        '''将不需要分批查询的or条件放在此参数中'''
        self.__queries_or.append([field, queries_or])

    def ___split_or_value__(self):
        # 将需要分批处理的条件根据分批处理的数量分开
        field = self.__batch_queries_or[0] # 字段
        or_value_inputs = self.__batch_queries_or[1] # 原始的or条件
        batch_number = self.__batch_queries_or[2] # 需要分几批处理
        each_number_per_batch = math.ceil(len(or_value_inputs) / float(batch_number)) # 每批处理的数量
        lineArr = []
        for index, or_value_input in enumerate(or_value_inputs):
            if index == len(or_value_inputs) - 1: # 如果是最后个，则不考虑此批次的数量，全部传入数组
                lineArr.append(unicode(or_value_input))
                self.__or_values.append([field, lineArr])
            else:
                if (index + 1) % each_number_per_batch == 0: # 如果是每批处理的最后一个，则将此批作为一个整体数组传入总数组
                    lineArr.append(unicode(or_value_input))
                    self.__or_values.append([field, lineArr])
                    lineArr = []
                else: # 如果此条件不是此批的最后一个，则传入改批的数组
                    lineArr.append(unicode(or_value_input))

    def __addquery_or__(self):
        '''将or条件加入option table中'''
        for queries_or in self.__queries_or:
            field = queries_or[0]
            inputdatas = queries_or[1]
            or_index = 1 # 初始化or条件索引
            for inputdata in inputdatas: # 逐条处理条件
                if inputdata.find("*") >= 0: # 如果条件中有星号，则认为需要模糊查询
                    inputdata = "'" + inputdata.replace('*', '%').upper() + "'" # 将*替换成%，以便RFC方法可以识别
                    calLogic = 'like' # 模糊查询使用like
                else:
                    inputdata = "'" + inputdata.upper() + "'"
                    calLogic = '=' # 精确查询使用等号
                if or_index == 1:  #  第一个or条件需要加上左括号
                    if self.__QIndex == 1: # 所有where条件的第一个不需要加and，否则需要加上and
                        self.opt.AppendGridData(1, 1, 1, "(" + field + ' ' + calLogic + ' ' +inputdata)
                        or_index += 1
                    else:
                        self.opt.AppendGridData(1, 1, 1, "AND (" + field + ' ' + calLogic + ' ' + inputdata)
                        or_index += 1
                else:
                    self.opt.AppendGridData(1, 1, 1, 'OR ' + field + ' ' + calLogic + ' ' + inputdata)
                    or_index += 1
            self.opt.AppendGridData(1, 1, 1, ')') # 最后加上右括号

    def set_fields(self, fields):
        '''设置需要返回在字段，fields为数组，返回的字段的排序和数组顺序一致'''
        self.__fields  = fields

    def __addfields__(self):
        for fieldname in self.__fields:
            Findex_1 = (self.__FIndex - 1) % 5 + 1
            Findex_2 = int(math.ceil(self.__FIndex / 5.0))
            # AppendGridData第一个参数的index最大为5，超过5，向第二个参数进一位
            self.fields.AppendGridData(Findex_1, Findex_2, 1, fieldname)
            self.__FIndex += 1

    def excute(self):
        '''将所有设置的参数汇总并执行'''
        if self.__batch_queries_or is not None:
            alldata = ()
            tmp_queries_ors = self.__queries_or[:]
            self.___split_or_value__()
            b_nb = 1
            #  分批执行
            for each_batch in self.__or_values:
                self.addMF()
                self.__queries_or = []
                for tmp_queries_or in tmp_queries_ors:
                    self.set_queries_or(tmp_queries_or[0], tmp_queries_or[1])
                self.set_fields(self.__fields)
                self.set_table(self.__tablename)
                self.__addfields__()
                self.__addtable__()
                self.__addquery__()
                self.set_queries_or(each_batch[0], each_batch[1])
                self.__addquery_or__()
                self.MyFunc.CALL
                if self.MyFunc:
                    print("分批工作正在处理中，已处理完的批数")
                    print(b_nb)
                    try:
                        print(len(self.data.data))
                    except:
                        print('No data')
                    b_nb += 1
                    self.__result = True
                    if self.data.data is not None:
                        alldata = alldata + self.data.data
                else:
                    self.__result = False
            return alldata
        else:
            self.__addfields__()
            self.__addtable__()
            self.__addquery__()
            self.__addquery_or__()
            self.MyFunc.CALL
            if self.MyFunc:
                self.__result = True
                if self.data.data is not None:
                    return self.data.data
                else:
                    print(self.MyFunc.exception)
                    return None
            else:
                self.__result = False
                return False

    def getfieldsdesc(self):
        returnfields = ''
        if self.__result:
            for field in self.fields.data:
                if returnfields == u'':
                    returnfields = field[4]
                else:
                    returnfields  = returnfields + '\t' + field[4]
        return (returnfields,),

'''
class batchjob(Callse16):
    def __init__(self):
        Callse16.R3 = Dispatch("SAP.Functions")
        self.__or_values = []

    def split_or_value(self, or_value_inputs, batch_number):
        each_number_per_batch = math.ceil(len(or_value_inputs) / batch_number)
        lineArr = []
        for index, or_value_input in enumerate(or_value_inputs):
            if index == len(or_value_inputs) - 1:
                lineArr.append(or_value_input)
                self.__or_values.append(lineArr)
            else:
                if (index + 1) % each_number_per_batch == 0:
                    lineArr.append(or_value_input)
                    self.__or_values.append(lineArr)
                    lineArr = []
                else:
                    lineArr.append(or_value_input)

    def batch_execute(self, field):
        for or_value in self.__or_values:
            Callse16.addquery_or(field, or_value)
'''
def gettablelabel(tableName, fields, SAPconn=None):
    """
    DO NOT USE ANY MORE
    """
    conn = Callse16()
    if SAPconn is None:
        conn.logon()
    else:
        conn.get_conn(SAPconn)
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
    fields = ['MATNR', 'ZZMAT_SBU', 'ZZMAT_GPH']
    tablename = 'MARA'
    # header = gettablelabel(tablename, fields)
    newsapconn = Callse16()
    newsapconn.logon()
    newsapconn.addMF()
    newsapconn.set_table(tablename)
    newsapconn.set_fields(fields)
    # newsapconn.set_queries("VKORG = '1390'")
    # newsapconn.set_queries_or('KTOKD', ['0001', '0002'])
    qlist = []
    for line in open('qList.txt').readlines():
        qlist.append(unicode(line.replace('\n', '')))

    newsapconn.set_batch_queries_or('PRDHA', qlist, 36)
    # newsapconn.addquery("MATNR = 'S7653-250G'", 'OR')
    # newsapconn.addquery("PARVW = 'E0'")
    data = newsapconn.excute()
    header = newsapconn.getfieldsdesc()
    fulldata = header + data
    soldtoData = []
    with codecs.open(r'C:\Users\cwang2\PycharmProjects\SAPConnection\SBU.txt', 'w', 'utf-16') as f:
        for line in fulldata:
            try:
                textwrite = line[0]
                # text = line[0].split('\t')
                # if len(text) == 1:
                #     textwrite = textwrite + '\t' + '\t'
                # if len(text) == 2:
                #     textwrite = textwrite + '\t'
                f.writelines(textwrite + '\r\n')
            except:
                print(line[0])
        f.close()


