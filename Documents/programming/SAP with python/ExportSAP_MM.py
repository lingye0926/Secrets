# encoding:utf-8

import SAPConn
import codecs
import os

'''
使用此代码从sap导出文件到C:\Users\cwang2\Documents\py36_SAP 中，再使用export_SAP_MM.py 对原始数据进行匹配处理，生成最终文件。
'''

def save2maratemp(data, filename):
    filepath = 'C:\Users\cwang2\Documents\py36_SAP'
    full_path = os.path.join(filepath, filename)
    with codecs.open(full_path, "w", encoding="utf-8") as f:
        for line in data:
            f.writelines(line[0] + '\r\n')
    f.close()

def add2maratemp(data, filename):
    filepath = 'C:\Users\cwang2\Documents\py36_SAP'
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

MARAConn = SAPConn.Callse16()
MARAConn.logon('PRP')
MARAConn.addMF()
MARAConn.set_table('MARA')
'''
MATNR	Material
BISMT	old Matl no.
BRAND_ID	Brand
ERSDA	Created
LAEDA	Last Chg.
MEINS	Unit
BRGEW	Gross
NTGEW	Net
GEWEI	WeightUnit
VOLUM	Volume
VOLEH	VolumeUnit
WHSTC	Storage Temp
MSTAV	xchain
ETIAG	Initiative
'''
MARA_fields = ['MATNR', 'BISMT','BRAND_ID', 'ERSDA', 'LAEDA',  'MEINS', 'BRGEW', 'NTGEW', 'GEWEI', 'VOLUM', 'VOLEH', 'WHSTC', 'MSTAV', 'ETIAG']
MARAConn.set_fields(MARA_fields)
# MARAConn.set_queries("BRAND_ID = 'SU'")
Brandlist = ['3P','AV','AL','BJ','BR','CE','DV','FL','GN','HW','IS','KT','MI','NB','PR','RD','RO','SA','SG','SI','SU','VT','US',]
MARAConn.set_queries("ETIAG <> ''")
MARAConn.set_batch_queries_or("BRAND_ID", Brandlist[:1], len(Brandlist[:1]))
data1 = MARAConn.excute()
header = MARAConn.getfieldsdesc()

MARAConn = None
MARA_FULL = header + data1
data1 = None
save2maratemp(MARA_FULL, 'MARA.txt')

Brandlist = ['AL','AV','BJ','BR','CE','DV','FL','GN','HW','IS','KT','MI','NB','PR','RD','RO','SA','SG','SI','SU','VT','US',]
for brand in Brandlist:
    print(brand)
    MARAConn = SAPConn.Callse16()
    MARAConn.logon('PRP')
    MARAConn.addMF()
    MARAConn.set_table('MARA')
    MARA_fields = ['MATNR', 'BISMT','BRAND_ID', 'ERSDA', 'LAEDA',  'MEINS', 'BRGEW', 'NTGEW', 'GEWEI', 'VOLUM', 'VOLEH', 'WHSTC', 'MSTAV', 'ETIAG']
    MARAConn.set_fields(MARA_fields)
    # MARAConn.set_queries("BRAND_ID = 'SU'")

    MARAConn.set_queries("ETIAG <> ''")
    MARAConn.set_queries("BRAND_ID = " + "'" + brand + "'")
    data2 = MARAConn.excute()
    if data2 is not None:
        add2maratemp(data2, 'MARA.txt')
    MARAConn = None
    data2 = None

# MARA_DF = pd.read_csv("C:\Users\cwang2\Documents\py36_SAP\MARA.txt" ,sep='\t', encoding='utf-8', header=0)

# MARA_CLEAN = splitlist(MARA_FULL)
# MARA_DF = pd.DataFrame(MARA_CLEAN[1:])
# MARA_DF.columns = MARA_CLEAN[0]

TEMPConn = SAPConn.Callse16()
TEMPConn.logon('PRP')
TEMPConn.addMF()
TEMPConn.set_table('TWHSTCT')
TEMP_Fields = ['WHSTC', 'TEXT']
TEMPConn.set_fields(TEMP_Fields)
TEMPConn.set_queries("LANGU = 'E'")
data = TEMPConn.excute()
header = TEMPConn.getfieldsdesc()
TEMP_FULL = header + data
TEMPConn = None
save2maratemp(TEMP_FULL, 'TEMP.txt')

# TEMP_CLEAN = splitlist(TEMP_FULL)
# TEMP_DF = pd.DataFrame(TEMP_CLEAN[1:])
# TEMP_DF.columns = ['Warehouse Storage Condition', 'Storage Description']
# # 存储温度ID和描述整合
# NEW_MARA_DF = pd.merge(MARA_DF,TEMP_DF,how="left", on='Warehouse Storage Condition')
# NEW_MARA_DF = pd.DataFrame(NEW_MARA_DF)
# NEW_MARA_DF = NEW_MARA_DF.iloc[:, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 14, 12, 13]]

BRANDConn = SAPConn.Callse16()
BRANDConn.logon('PRP')
BRANDConn.addMF()
BRANDConn.set_table('WRF_BRANDS_T')
BRAND_Fields = ['BRAND_ID', 'BRAND_DESCR']
BRANDConn.set_fields(BRAND_Fields)
BRANDConn.set_queries("LANGUAGE = 'E'")
data = BRANDConn.excute()
header = BRANDConn.getfieldsdesc()
BRAND_FULL = header + data
BRANDConn = None
save2maratemp(BRAND_FULL, 'BRAND.txt')

# BRAND_CLEAN = splitlist(BRAND_FULL)
# BRAND_DF = pd.DataFrame(BRAND_CLEAN[1:])
# BRAND_DF.columns = BRAND_CLEAN[0]
#
# NEW_MARA_DF = pd.merge(NEW_MARA_DF,BRAND_DF,how="left", on='Brand')
# NEW_MARA_DF = pd.DataFrame(NEW_MARA_DF)
# NEW_MARA_DF = NEW_MARA_DF.iloc[:, [0, 1, 2, 15, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]]

MVKEConn = SAPConn.Callse16()
MVKEConn.logon('PRP')
MVKEConn.addMF()
MVKEConn.set_table('MVKE')
MVKE_Fields = ['PMATN', 'VMSTA', 'MATNR'] # pricing ref, dchain
MVKEConn.set_fields(MVKE_Fields)
MVKEConn.set_queries("VKORG = '2118'")
data = MVKEConn.excute()
header = MVKEConn.getfieldsdesc()
MVKE_FULL = header + data
MVKEConn = None
save2maratemp(MVKE_FULL, 'MVKE.txt')
# MVKE_CLEAN = splitlist(MVKE_FULL)
# MVKE_DF = pd.read_csv("C:\Users\cwang2\Documents\py36_SAP\MVKE.txt" ,sep='\t', encoding='utf-8', header=0)



MARCConn = SAPConn.Callse16()
MARCConn.logon('PRP')
MARCConn.addMF()
MARCConn.set_table('MARC')
MARC_Fields = ['MFRGR', 'MATNR'] # 运输温度
MARCConn.set_fields(MARC_Fields)
MARCConn.set_queries("WERKS = 'CN01'")
data = MARCConn.excute()
header = MARCConn.getfieldsdesc()
MARC_FULL = header + data
MARCConn = None
save2maratemp(MARC_FULL, 'MARC.txt')
# MARC_CLEAN = splitlist(MARC_FULL)
# MARC_DF = pd.read_csv("C:\Users\cwang2\Documents\py36_SAP\MARC.txt" ,sep='\t', encoding='utf-8', header=0)


MFRGRConn = SAPConn.Callse16()
MFRGRConn.logon('PRP')
MFRGRConn.addMF()
MFRGRConn.set_table('TMFGT')
MFRGR_Fields = ['MFRGR', 'BEZEI']
MFRGRConn.set_fields(MFRGR_Fields)
MFRGRConn.set_queries("SPRAS = '1'")
data = MFRGRConn.excute()
header = MFRGRConn.getfieldsdesc()
MFRGR_FULL = header + data
MFRGRConn = None
save2maratemp(MFRGR_FULL, 'MFRGR.txt')
#
# MFRGR_CLEAN = splitlist(MFRGR_FULL)
# MFRGR_DF = pd.DataFrame(MFRGR_CLEAN[1:])
# MFRGR_DF.columns = ['Material freight group', 'MFG Description']

# 存储温度ID和描述整合
# NEW_MARC_DF = pd.merge(MARC_DF,MFRGR_DF, how='left', on='Material freight group')
# NEW_MARC_DF = pd.DataFrame(NEW_MARC_DF)
#
# FULL_DATA_1 = pd.merge(NEW_MARA_DF, MVKE_DF, how='left', on='Material Number')
# FULL_DATA = pd.merge(FULL_DATA_1, NEW_MARC_DF, how='left', on='Material Number')
# FULL_DATA.to_csv(r'C:\Users\cwang2\Documents\B2B Integration\Data\latest\SAP_MM.txt', sep='\t', encoding='utf-8', index=False, header=False)



