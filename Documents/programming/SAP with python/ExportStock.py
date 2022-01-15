# coding:utf-8
import SAPConn
import codecs
import LoginNEXT
import requests
import json
import codecs
import pandas as pd
import codecs
import zipfile
from requests.adapters import HTTPAdapter
import numpy as np
import os
import openpyxl
import shutil
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

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

    def writeDELheader(self, filepath1):
        with codecs.open(filepath1, 'wb', 'utf-16') as f:
            f.writelines('Material' + '\t')
            f.writelines('Del_Quantity' + '\r\n')
            f.close()

    def writeSOheader(self, filepath1):
        with codecs.open(filepath1, 'wb', 'utf-16') as f:
            f.writelines('Material' + '\t')
            f.writelines('SO_Quantity' + '\r\n')
            f.close()


    def writeDELdata(self, filepath1, dataList):
        with codecs.open(filepath1, 'ab', 'utf-16') as f:
            for d in dataList:
                try:
                    self.writefile(f, d['Material'])
                    if d['ActualDeliveryQuantity'] is None:
                        f.writelines('' + '\r\n')
                    else:
                        f.writelines(d['ActualDeliveryQuantity'] + '\r\n')
                except:
                    print(d)
        f.close()

    def writeSOdata(self, filepath1, dataList):
        with codecs.open(filepath1, 'ab', 'utf-16') as f:
            for d in dataList:
                try:
                    self.writefile(f, d['MATNR'])
                    if d['BMENG_DIM'] is None:
                        f.writelines('' + '\r\n')
                    else:
                        f.writelines(d['BMENG_DIM'] + '\r\n')
                except:
                    print(d)
        f.close()



    def ReadNEXT_Del(self):

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
        filepath1 = r'C:\Users\cwang2\Documents\WUXI\Open_DEL_QTY.txt'

        self.writeDELheader(filepath1)
        while len(sjson) > 0:
            url2 = "https://sappweb.sial.com/hanaprp/sial/sapnext/sd/Services/CustomerService.xsodata/OpenDeliveryeport?$skip=" + str(
                start) + "&$top=" + str(
                end) + "&$select=Material,ActualDeliveryQuantity&$filter=%20(SAPClient%20eq%20%27100%27%20and%20((((tolower(ActualGoodsMovementDate)%20eq%20tolower(%27%27)%20or%20ActualGoodsMovementDate%20eq%20null%20or%20tolower(ActualGoodsMovementDate)%20eq%20tolower(%2700000000%27))))))"
            print('processing:' + str(start))
            sapcontent2 = sapsession.get(url2, headers=headers, cookies=self.Requests_cookie, verify=False)
            try:
                sjson = json.loads(sapcontent2.content)['d']['results']
                self.writeDELdata(filepath1, sjson)
            except:
                print(sapcontent2.content)

            # Alldata = sjson + Alldata
            start = start + 20000


    def ReadNEXT_SO(self):
        headers = {"Accept": "application/json",
                   "Connection": "keep-alive",
                   "MaxDataServiceVersion": "2.0",
                   "DataServiceVersion": "2.0",
                   "Accept-Encoding": "gzip, deflate",
                   "Content-Type": "application/json",
                   "Host": "sappweb.sial.com",
                   "Accept-Language": "en",
                   "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.76 Safari/537.36"}
        adapter = HTTPAdapter(max_retries=20)  # 增加重试次数，防止由于网络原因造成的中断
        sapsession = requests.session()
        sapsession.mount('http://', adapter)
        sapsession.mount('https://', adapter)

        Alldata = []
        sjson = ['1']  # 初始化值，使其len 不等于0
        start = 0  # 初始值，从0开始读取
        end = 20000  # 每次读取最多20000条记录
        filepath1 = r'C:\Users\cwang2\Documents\WUXI\Open_SO_QTY.txt'

        self.writeSOheader(filepath1)
        while len(sjson) > 0:
            url2 = "https://sappweb.sial.com/hanaprp/sial/sapnext/sd/Services/SDSalesDocItemKPI.xsodata/SDSalesDocItemInputParams(P_EXCHANGECURRENCY='EUR',P_EXCHANGETYPE='EURX')/Results?$skip=" + str(
                start) + "&$top=" + str(
                end) + "&$select=MATNR,BMENG_DIM&$filter=%20((VBTYP%20eq%20%27C%27%20and%20MANDT%20eq%20%27100%27%20and%20(GBSTA%20eq%20%27A%27%20or%20GBSTA%20eq%20%27B%27)%20and%20(OMENG_DIM%20ne%20null))%20and%20((((tolower(WERKS)%20eq%20tolower(%27CN01%27)%20and%20tolower(PlantName)%20eq%20tolower(%27Shanghai%20Warehouse%27))))%20and%20((LABST_DIM%20gt%200M))))"
            print('processing:' + str(start))
            sapcontent2 = sapsession.get(url2, headers=headers, cookies=self.Requests_cookie, verify=False)
            try:
                sjson = json.loads(sapcontent2.content)['d']['results']
                self.writeSOdata(filepath1, sjson)
            except:
                print(sapcontent2.content)

            # Alldata = sjson + Alldata
            start = start + 20000


def SAP_sotck():
    fields = ['MATNR', 'LABST']
    conn = SAPConn.Callse16()
    conn.logon('PRP')
    conn.addMF()
    conn.set_table('MARD')
    conn.set_fields(fields)
    conn.set_queries("WERKS = 'CN01'")
    conn.set_queries("LGORT = 'L001'")
    conn.set_queries("LABST  <> '0.000'")

    data = conn.excute()
    header = conn.getfieldsdesc()
    fulldata = header + data
    with codecs.open(r'C:\Users\cwang2\Documents\WUXI\stock.txt', 'w', 'utf-16') as f:
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

class loginLN():
    # 使用selenium模拟登陆
    def __init__(self, username, password):
        self.__LoginURL = "https://www.uploadcatalog.com/p/#/login"
        self.__username = username
        self.__password = password
        self.__driver = webdriver.Chrome("C:\Users\cwang2\Documents\GoogleChromeDriver\V237\chromedriver.exe")
        self.__sess = requests.session()

    def Get_Login_Cookies(self):

        # driver.set_window_position(-100000, 0)

        self.__driver.get('https://www.uploadcatalog.com/logout')
        self.__driver.get(self.__LoginURL)
        wait = WebDriverWait(self.__driver, 10)

        username = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        password = wait.until(EC.presence_of_element_located((By.NAME, "password")))
        submit = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/form/button')))
        username.send_keys(self.__username)
        password.send_keys(self.__password)
        submit.send_keys(Keys.RETURN)

    def getparams(self):
        uploadurl = 'https://www.uploadcatalog.com/p/#/catalogUpload/uploadProduct'
        sleep(2)
        self.__driver.get(uploadurl)
        wait = WebDriverWait(self.__driver, 10)

        batchid_ele = wait.until(EC.presence_of_element_located((By.NAME, "batchId")))
        batchid = batchid_ele.get_attribute('value')

        companyid_ele = wait.until(EC.presence_of_element_located((By.NAME, "companyId")))
        companyid = companyid_ele.get_attribute('value')

        cookies = self.__driver.get_cookies()
        cookiedict = {}
        # 获取cookie
        for cookie in cookies:
            cookiedict[cookie['name']] = cookie['value']
        self.__driver.close()
        Requests_cookie = requests.utils.cookiejar_from_dict(cookiedict)

        return {"companyid": companyid,
                "batchid": batchid,
                "cookies": Requests_cookie}

    def uploadfiles(self, params, filepath, filename):
        addfileurl = 'https://www.uploadcatalog.com/excel/chemical/upload'
        folder = filepath.decode('utf-8')
        filename = filename
        companyId = params['companyid']
        batchId = params['batchid']
        cookies = params['cookies']

        with open(os.path.join(folder, filename), 'rb') as openedfile:
            files = [('type', ('', 'PACKAGE_CHEMICAL')),
                     ('companyId', ('', companyId)),
                     ('batchId', ('', batchId)),
                     ('file',(filename, openedfile, 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'))]
            res = self.__sess.post(addfileurl, files=files, cookies=cookies, verify=False)

        print(res.content)
        finishuploadurl = 'https://www.uploadcatalog.com/excel/finish?batchId=' + batchId + '&type=PACKAGE_CHEMICAL&companyId=' + companyId
        headers = {'Accept': 'application/json, text/plain'}
        # finshpl = {'batchId':	batchId,
        #             'type':	'PRODUCT_CHEMICAL',
        #             'companyId':	companyId}

        result = self.__sess.post(finishuploadurl, cookies=cookies, headers=headers, verify=False)
        print(result.content)

def GenerateExcel(filepath, filename, template, stock_df):
    chemical_file = os.path.join(filepath, filename)
    product_df = pd.read_excel(chemical_file, sheetname='Sheet1', header=0, skiprows=[1])
    Fin_stock = pd.merge(product_df, stock_df, how='left', left_on='ProductId', right_on='Material')
    Fin_stock['PackageStockLocation'] = 'CN-SH'
    Fin_stock['PackageStockQuantity'] = Fin_stock['ATP']
    Fin_stock['LNCost'] = ''
    Fin_stock = Fin_stock.iloc[:, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
    Fin_stock = Fin_stock.fillna(0)

    dst_file = os.path.join(filepath, 'Stock_' + filename)
    shutil.copy(template, dst_file)
    book = openpyxl.load_workbook(dst_file)

    pdWriter = pd.ExcelWriter(dst_file, engine='openpyxl')
    pdWriter.book = book

    # for ws in book.worksheets:
    #     if ws.title == sheetname:
    #         pdWriter.sheets = dict((ws.title, ws) for ws in book.worksheets)
    pdWriter.sheets = dict((ws.title, ws) for ws in book.worksheets)
    Fin_stock.to_excel(pdWriter, sheet_name="Sheet1", index=False, header=False, startrow=2)
    pdWriter.save()

if __name__ == '__main__':
    NEXT = ReadMM()
    NEXT.LoginNEXT()
    NEXT.ReadNEXT_Del()
    NEXT.ReadNEXT_SO()
    SAP_sotck()


    stock_DF = pd.read_csv(r"C:\Users\cwang2\Documents\WUXI\stock.txt", sep='\t', encoding='utf-16', header=0)
    stock_DF.columns = ['Material', 'Quantity']
    Del_qty_DF = pd.read_csv(r"C:\Users\cwang2\Documents\WUXI\Open_DEL_QTY.txt", sep='\t', encoding='utf-16', header=0)
    SO_qty_DF = pd.read_csv(r"C:\Users\cwang2\Documents\WUXI\Open_SO_QTY.txt", sep='\t', encoding='utf-16', header=0)

    stock_DF = stock_DF.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    stock_DF["Material"] = stock_DF["Material"].apply(lambda x: x.lstrip("0") if x.isdigit() else x)
    Del_qty_DF["Material"] = Del_qty_DF["Material"].apply(lambda x: x.lstrip("0") if x.isdigit() else x)
    SO_qty_DF["Material"] = SO_qty_DF["Material"].apply(lambda x: x.lstrip("0") if x.isdigit() else x)
    NEW_STOCK_DF = pd.merge(stock_DF, Del_qty_DF, how="left", on='Material')
    NEW_STOCK_DF = pd.merge(NEW_STOCK_DF, SO_qty_DF, how="left", on='Material')
    NEW_STOCK_DF = NEW_STOCK_DF.fillna(0)
    NEW_STOCK_DF.insert(4, "ATP", 0)

    for index, item in enumerate(np.array(NEW_STOCK_DF)):
        atp_qty = int(item[1]) - int(item[2]) - int(item[3])
        if atp_qty < 0:
            atp_qty = 0
        NEW_STOCK_DF['ATP'][index] = atp_qty

    chemical_product_filepath = 'C:\Users\cwang2\Documents\B2B Integration\Customers\Wuxi Apptec\Labnetwork\Chemical\Upload_PKG'
    chemical_product_filename = 'VAT16_20180502_OUT20180119_Chemical_PKG_0.xlsx'
    template = 'C:\Users\cwang2\Documents\B2B Integration\Customers\Wuxi Apptec\Labnetwork\Chemical\package_template.xlsx'
    # 将dataframe转为excel 文件名为原文件名加stock_前缀
    GenerateExcel(chemical_product_filepath, chemical_product_filename, template, NEW_STOCK_DF)
    # 上传
    wuxi = loginLN('cheney.wang@sial.com', 'sigma123')
    wuxi.Get_Login_Cookies()
    sel = wuxi.getparams()
    wuxi.uploadfiles(sel, chemical_product_filepath, "Stock_" + chemical_product_filename)



