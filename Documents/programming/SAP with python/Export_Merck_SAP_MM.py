# encoding:utf-8

import SAPConn
import codecs
import os

'''
使用此代码从sap导出文件到C:\Users\cwang2\Documents\py36_SAP 中，再使用export_SAP_MM.py 对原始数据进行匹配处理，生成最终文件。
'''

def save2maratemp(data, filename):
    filepath = 'C:\Users\cwang2\Documents\py36_SAP\MM_DATA'
    full_path = os.path.join(filepath, filename)
    with codecs.open(full_path, "w", encoding="utf-8") as f:
        for line in data:
            f.writelines(line[0].replace('\n', '').replace('"', "") + '\r\n')
    f.close()

def add2maratemp(data, filename):
    filepath = 'C:\Users\cwang2\Documents\py36_SAP\MM_DATA'
    full_path = os.path.join(filepath, filename)
    with codecs.open(full_path, "a", encoding="utf-8") as f:
        for line in data:
            f.writelines(line[0] + '\r\n')
    f.close()

def splitlist(sqllist):
    outputlist = []
    for i in sqllist:
        outputlist.append(map(unicode.strip, i[0].split('\t')))
    return outputlist

def exportMARA():
    MARAConn = SAPConn.Callse16()
    MARAConn.logon('MERCK')
    MARAConn.addMF()
    MARAConn.set_table('MARA')

    '''
    MATNR	Material
    BISMT	old Matl no.
    NORMT   PKG
    ERSDA	Created
    LAEDA	Last Chg.
    MEINS	Unit
    BRGEW	Gross
    NTGEW	Net
    GEWEI	WeightUnit
    VOLUM	Volume
    VOLEH	VolumeUnit
    MSTAV	xchain
    TRAGR   shipping condition
    RAUBE   storage condition
    EXTWG   SBU
    ZZA_ECNUM   EC NUMBER
    ZZA_TEXT4   MDM CODE
    ZZA_TEXT5   GPH
    ZZA_TEXT    short description
    '''

    MARA_fields = ['MATNR', 'BISMT', 'NORMT', 'ERSDA', 'LAEDA',  'MEINS', 'BRGEW', 'NTGEW', 'GEWEI', 'VOLUM', 'VOLEH', 'MSTAV', 'TRAGR', 'RAUBE', 'EXTWG', 'ZZA_ECNUM', 'ZZA_TEXT4', 'ZZA_TEXT5', 'ZZA_TEXT']
    MARAConn.set_fields(MARA_fields)
    data1 = MARAConn.excute()
    header = MARAConn.getfieldsdesc()
    MARAConn = None
    MARA_FULL = header + data1
    data1 = None
    save2maratemp(MARA_FULL, 'MM_MARA.txt')

# Brandlist = ['AL','AV','BJ','BR','CE','DV','FL','GN','HW','IS','KT','MI','NB','PR','RD','RO','SA','SG','SI','SU','VT','US',]

#
# MARAConn = SAPConn.Callse16()
# MARAConn.logon('MERCK')
# MARAConn.addMF()
# MARAConn.set_table('MARA')
# MARA_fields = ['MATNR', 'BISMT','BRAND_ID', 'ERSDA', 'LAEDA',  'MEINS', 'BRGEW', 'NTGEW', 'GEWEI', 'VOLUM', 'VOLEH', 'WHSTC', 'MSTAV', 'ETIAG']
# MARAConn.set_fields(MARA_fields)
# # MARAConn.set_queries("BRAND_ID = 'SU'")
#
# MARAConn.set_queries("ETIAG <> ''")
# MARAConn.set_queries("BRAND_ID = " + "'" + brand + "'")
# data2 = MARAConn.excute()
# if data2 is not None:
#     add2maratemp(data2, 'MARA.txt')
# MARAConn = None
# data2 = None

# MARA_DF = pd.read_csv("C:\Users\cwang2\Documents\py36_SAP\MARA.txt" ,sep='\t', encoding='utf-8', header=0)

# MARA_CLEAN = splitlist(MARA_FULL)
# MARA_DF = pd.DataFrame(MARA_CLEAN[1:])
# MARA_DF.columns = MARA_CLEAN[0]

# Storage condition
def exportT142T():
    T142TConn = SAPConn.Callse16()
    T142TConn.logon('MERCK')
    T142TConn.addMF()
    T142TConn.set_table('T142T')
    T142T_Fields = ['RAUBE', 'RBTXT']
    T142TConn.set_fields(T142T_Fields)
    T142TConn.set_queries("SPRAS = 'EN'")
    data = T142TConn.excute()
    header = T142TConn.getfieldsdesc()
    T142T_FULL = header + data
    T142TConn = None
    save2maratemp(T142T_FULL, 'MM_T142T.txt')

# TEMP_CLEAN = splitlist(TEMP_FULL)
# TEMP_DF = pd.DataFrame(TEMP_CLEAN[1:])
# TEMP_DF.columns = ['Warehouse Storage Condition', 'Storage Description']
# # 存储温度ID和描述整合
# NEW_MARA_DF = pd.merge(MARA_DF,TEMP_DF,how="left", on='Warehouse Storage Condition')
# NEW_MARA_DF = pd.DataFrame(NEW_MARA_DF)
# NEW_MARA_DF = NEW_MARA_DF.iloc[:, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 14, 12, 13]]


def exportTIGRT():
    # SHIPPING CONDITION
    TTGRTConn = SAPConn.Callse16()
    TTGRTConn.logon('MERCK')
    TTGRTConn.addMF()
    TTGRTConn.set_table('TTGRT')
    TTGRT_Fields = ['TRAGR', 'VTEXT']
    TTGRTConn.set_fields(TTGRT_Fields)
    TTGRTConn.set_queries("SPRAS = 'E'")
    data = TTGRTConn.excute()
    header = TTGRTConn.getfieldsdesc()
    BRAND_FULL = header + data
    BRANDConn = None
    save2maratemp(BRAND_FULL, 'MM_ShippingCondition.txt')

# BRAND_CLEAN = splitlist(BRAND_FULL)
# BRAND_DF = pd.DataFrame(BRAND_CLEAN[1:])
# BRAND_DF.columns = BRAND_CLEAN[0]
#
# NEW_MARA_DF = pd.merge(NEW_MARA_DF,BRAND_DF,how="left", on='Brand')
# NEW_MARA_DF = pd.DataFrame(NEW_MARA_DF)
# NEW_MARA_DF = NEW_MARA_DF.iloc[:, [0, 1, 2, 15, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]]
def exportMVKE():
    MVKEConn = SAPConn.Callse16()
    MVKEConn.logon('MERCK')
    MVKEConn.addMF()
    MVKEConn.set_table('MVKE')
    '''
    VMSTA   DCHAIN
    ZZE_TEXT2 Chinese Name
    '''
    MVKE_Fields = ['ZZE_TEXT2', 'VMSTA', 'MATNR'] # pricing ref, dchain
    MVKEConn.set_fields(MVKE_Fields)
    MVKEConn.set_queries("VKORG = '6102'")
    data = MVKEConn.excute()
    header = MVKEConn.getfieldsdesc()
    MVKE_FULL = header + data
    MVKEConn = None
    save2maratemp(MVKE_FULL, 'MM_MVKE.txt')
# MVKE_CLEAN = splitlist(MVKE_FULL)
# MVKE_DF = pd.read_csv("C:\Users\cwang2\Documents\py36_SAP\MVKE.txt" ,sep='\t', encoding='utf-8', header=0)

def exportSBUDes():
    # SBU description
    TWEWTConn = SAPConn.Callse16()
    TWEWTConn.logon('MERCK')
    TWEWTConn.addMF()
    TWEWTConn.set_table('TWEWT')
    TWEWT_Fields = ['EXTWG', 'EWBEZ']
    TWEWTConn.set_fields(TWEWT_Fields)
    TWEWTConn.set_queries("SPRAS = 'E'")
    data = TWEWTConn.excute()
    header = TWEWTConn.getfieldsdesc()
    TWEWT_FULL = header + data
    TWEWTConn = None
    save2maratemp(TWEWT_FULL, 'MM_TWEW.txt')

def exportMARC():
    MARCConn = SAPConn.Callse16()
    MARCConn.logon('MERCK')
    MARCConn.addMF()
    MARCConn.set_table('MARC')
    '''
    CASNR CAS
    ZZC_MECOM   if displayed on website
    ZZC_PECOM   if displayed price on website
    ZZC_TEXT2   BU
    ZZC_TEXT3   BF
    ZZC_LEADT   lead time
    ZZC_PACKS   pack size on the website
    ZZC_PRODC    product code
    '''
    MARC_Fields = ['CASNR', 'ZZC_TEXT2', 'ZZC_TEXT3', 'ZZC_MECOM', 'ZZC_PECOM', 'ZZC_LEADT', 'ZZC_PACKS', 'ZZC_PRODC', 'MATNR']
    MARCConn.set_fields(MARC_Fields)
    MARCConn.set_queries("WERKS = '6101'")
    data = MARCConn.excute()
    header = MARCConn.getfieldsdesc()
    MARC_FULL = header + data
    MARCConn = None
    save2maratemp(MARC_FULL, 'MM_MARC.txt')

if __name__ == '__main__':
    exportMARA()
    exportMARC()
    exportMVKE()
    exportSBUDes()
    exportT142T()
    exportTIGRT()


