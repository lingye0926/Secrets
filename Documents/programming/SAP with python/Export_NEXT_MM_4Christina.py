# coding:utf-8
import LoginNEXT
import requests
import json
import codecs
import os
import shutil
import datetime
import pandas as pd
import codecs
import zipfile
import grequests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

class ReadMM():
    def __init__(self):
        self.Requests_cookie = ''

    def LoginNEXT(self):
        # 使用selenium模拟登陆
        Login = LoginNEXT.loginNEXT()
        self.Requests_cookie = Login.Get_Login_Cookies()

    def writefile(self, fileOBJ, linestr):
        if linestr is None:
            fileOBJ.writelines('' + '\t')
        else:
            fileOBJ.writelines(linestr.replace('"', '').strip() + '\t') # 去除双引号，防止pandas读取文件时出现错误

    def writeheader(self, filepath1, filepath2): # 写入2个文件，第一个是非SMI的数据，第二个是SMI的数据，由于一个产品可能有多个SMI
        with codecs.open(filepath1, 'wb', 'utf-16') as f:
            f.writelines('Material' + '\t')
            f.writelines('CAS' + '\t')
            f.writelines('GPH' + '\t')
            f.writelines('Currency' + '\t')
            f.writelines('DGIndicatorID' + '\t')
            f.writelines('DGProfile' + '\t')
            f.writelines('SBU' + '\t')
            f.writelines('SBUDescription' + '\t')
            f.writelines('HierarchyID' + '\t')
            f.writelines('Hierarchy' + '\t')
            f.writelines('IndustrySectorID' + '\t')
            f.writelines('IndustrySector' + '\t')
            f.writelines('ListPrice' + '\r\n')
            f.close()

        with codecs.open(filepath2, 'wb', 'utf-16') as f:
            f.writelines('Material' + '\t')
            f.writelines('SMI_ID' + '\t')
            f.writelines('SMI' + '\r\n')

            f.close()

    def writedata(self, filepath1, filepath2, dataList):
        with codecs.open(filepath1, 'ab', 'utf-16') as f:
            for d in dataList:
                try:
                    self.writefile(f, d['MATNR'])
                    self.writefile(f, d['NORMT'])
                    self.writefile(f, d['ZZMGPH'])
                    self.writefile(f, d['KONWA'])
                    self.writefile(f, d['PROFL'])
                    self.writefile(f, d['PROFLD'])
                    self.writefile(f, d['ZZMSBU'])
                    self.writefile(f, d['ZZMSBU_DESC_SBU'])
                    self.writefile(f, d['PRDHA'])
                    self.writefile(f, d['VTEXT'])
                    self.writefile(f, d['MBRSH'])
                    self.writefile(f, d['MBBEZ'])
                    if d['KBETR'] is None:
                        f.writelines('' + '\r\n')
                    else:
                        f.writelines(d['KBETR'] + '\r\n')
                except:
                    pass
        f.close()

        with codecs.open(filepath2, 'ab', 'utf-16') as f:
            for d in dataList:
                try:
                    self.writefile(f, d['MATNR'])

                    self.writefile(f, d['SMI'])
                    if d['BEZEK'] is None:
                        f.writelines('' + '\r\n')
                    else:
                        f.writelines(d['BEZEK'].strip() + '\r\n')

                except:
                    pass
            f.close()

    def ReadNEXT(self):

        headers = {"Accept": "application/json",
                   "Connection": "keep-alive",
                   "MaxDataServiceVersion": "2.0",
                   "DataServiceVersion": "2.0",
                   "Accept-Encoding": "gzip, deflate",
                   "Content-Type": "application/json",
                   "Host": "sappweb.sial.com",
                   "Accept-Language": "en",
                   "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.76 Safari/537.36"}
        adapter = HTTPAdapter(max_retries=20) # 增加重试次数，防止由于网络原因造成的中断
        sapsession = requests.session()
        sapsession.mount('http://', adapter)
        sapsession.mount('https://', adapter)

        Alldata = []
        sjson = ['1']  # 初始化值，使其len 不等于0
        start = 0  #初始值，从0开始读取
        end = 20000 #每次读取最多20000条记录
        filepath1 = r'C:\Users\cwang2\Documents\B2B Integration\Customers\Christina\NEXT_MM.dat'
        filepath2 = r'C:\Users\cwang2\Documents\B2B Integration\Customers\Christina\NEXT_SMI_MM.dat'
        # backuppath = r'C:\Users\cwang2\Documents\B2B Integration\Data\Historical_data\Price\RMB'
        self.writeheader(filepath1, filepath2)
        # counturl = 'https://sappweb.sial.com/hanaprp/sial/sapnext/mdg/material/odata/MasterDataGovernance.xsodata/MaterialsInbox?$skip=' + \
        #            '0&$top=0&$inlinecount=allpages&$select=MATNR,NORMT,ZZMGPH,KONWA,PROFL,PROFLD,ZZMSBU,ZZMSBU_DESC_SBU,PRDHA,VTEXT,MBRSH,MBBEZ,SMI,BEZEK,KBETR&$filter=%20((((MTART%20eq%20%27FERT%27%20or%20MTART%20eq%20%27HALB%27%20or%20MTART%20eq%20%27KMAT%27%20or%20MTART%20eq%20%27ZRCH%27%20or%20MTART%20eq%20%27ZVAR%27%20or%20MTART%20eq%20%27ZVFT%27%20or%20MTART%20eq%20%27ZRCH%27%20or%20MTART%20eq%20%27ZPC%27%20or%20MTART%20eq%20%27ZMTO%27%20or%20MTART%20eq%20%27FGTR%27)%20and%20MANDT%20eq%20%27100%27))%20and%20(((tolower(KZKFG)%20ne%20tolower(%27X%27)))))'
        # countContent = sapsession.get(counturl, headers=headers, cookies=self.Requests_cookie, verify=False)
        # countsjson = json.loads(countContent.content)['d']['__count']
        # pagecount = int(countsjson / 20000)  + 1

        while len(sjson) > 0:
            url2 = "https://sappweb.sial.com/hanaprp/sial/sapnext/mdg/material/odata/MasterDataGovernance.xsodata/MaterialsInbox?$skip=" + str(
                start) + "&$top=" + str(
                end) + "&$select=MATNR,NORMT,ZZMGPH,KONWA,PROFL,PROFLD,ZZMSBU,ZZMSBU_DESC_SBU,PRDHA,VTEXT,MBRSH,MBBEZ,SMI,BEZEK,KBETR&$filter=%20((((MTART%20eq%20%27FERT%27%20or%20MTART%20eq%20%27HALB%27%20or%20MTART%20eq%20%27KMAT%27%20or%20MTART%20eq%20%27ZRCH%27%20or%20MTART%20eq%20%27ZVAR%27%20or%20MTART%20eq%20%27ZVFT%27%20or%20MTART%20eq%20%27ZRCH%27%20or%20MTART%20eq%20%27ZPC%27%20or%20MTART%20eq%20%27ZMTO%27%20or%20MTART%20eq%20%27FGTR%27)%20and%20MANDT%20eq%20%27100%27)))"
            print('processing:' + str(start))
            sapcontent2 = sapsession.get(url2, headers=headers, cookies=self.Requests_cookie, verify=False)
            try:
                sjson = json.loads(sapcontent2.content)['d']['results']
                self.writedata(filepath1, filepath2, sjson)
            except:
                print(sapcontent2.content)

            # Alldata = sjson + Alldata
            start = start + 20000
        # backupfile = os.path.join(backuppath, "ListPrice_" + datetime.datetime.today().strftime('%Y%m%d') + '.txt')
        # shutil.copy(filepath1, backupfile)


if __name__ == '__main__':
    mm = ReadMM()
    mm.LoginNEXT()
    mm.ReadNEXT()

    MM = pd.read_csv(r'C:\Users\cwang2\Documents\B2B Integration\Customers\Christina\NEXT_MM.dat' ,sep='\t', encoding='utf-16', header=0)
    MM = MM.drop_duplicates()
    MM_SMI = pd.read_csv(r'C:\Users\cwang2\Documents\B2B Integration\Customers\Christina\NEXT_SMI_MM.dat', sep='\t', encoding='utf-16', header=0)
    MM_SMI = MM_SMI.drop_duplicates()
    MM.to_csv(r'C:\Users\cwang2\Documents\B2B Integration\Customers\Christina\NEXT_MM_2.dat', sep='\t', encoding='utf-8', index=False, header=False)
    MM_SMI.to_csv(r'C:\Users\cwang2\Documents\B2B Integration\Customers\Christina\NEXT_SMI_MM_2.dat', sep='\t', encoding='utf-8',
              index=False, header=False)

    print(MM)
