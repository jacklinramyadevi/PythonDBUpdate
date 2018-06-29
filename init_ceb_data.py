# _*_ coding:utf-8 _*_
"""
Created on 2018/06/05
@author: lwx
"""
#%%
import pymysql as pym
import datetime
import json



class CEB_INFO():

    def __init__(self):
        self.conn = None
        self.ceb_card_list = []
        self.bankCode = 'CEB'
        self.bankId = 8

    def conn_db(self):
        if not self.conn:
            self.conn = pym.connect(host='192.168.100.63', port=3306, user='root', passwd='123456',db='cm_xl_earth',charset='UTF8')
        return self.conn

    def init_bank_id(self):
        cursor = self.conn.cursor()

        sql = 'select * from bank_info where BANK_CODE=\'{bankCode}\''.format(bankCode=self.bankCode)
        print('sql:',sql)
        try:
            cursor.execute(sql)

            results = cursor.fetchall()
            for row in results:
                self.bankId = row[0]
                print('bankId:',self.bankId)
                break

        except:
            print('select exception')

    def insert_pcr_item(self,bankCode,nameProvince,idProvince,nameCity,idCity,nameArea,idArea,localCode):
        cursor = self.conn.cursor()

        datetimenowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        sql = 'insert into bank_city_code (BANK_CODE, PROVINCE,PROVINCE_CODE,CITY,CITY_CODE,AREA,AREA_CODE,LOCAL_CODE,STATUS,CRT_TM,LMT_TM) values(\'{bankCode}\',\'{nameProvince}\',\'{idProvince}\',\'{nameCity}\',\'{idCity}\',\'{nameArea}\',\'{idArea}\',\'{localCode}\',\'{status}\',\'{crtTime}\',\'{lmtTime}\')'.format(bankCode=bankCode  \
        ,nameProvince=nameProvince,idProvince=idProvince,nameCity=nameCity,idCity=idCity,nameArea=nameArea,idArea=idArea,localCode=localCode,status=1, crtTime=datetimenowTime,lmtTime=datetimenowTime)
        cursor.execute(sql)

        sql = 'insert into BANK_COMPANY_CODE (BANK_CODE, PROVINCE,PROVINCE_CODE,CITY,CITY_CODE,AREA,AREA_CODE,LOCAL_CODE,STATUS,CRT_TM,LMT_TM) values(\'{bankCode}\',\'{nameProvince}\',\'{idProvince}\',\'{nameCity}\',\'{idCity}\',\'{nameArea}\',\'{idArea}\',\'{localCode}\',\'{status}\',\'{crtTime}\',\'{lmtTime}\')'.format(bankCode=bankCode  \
        ,nameProvince=nameProvince,idProvince=idProvince,nameCity=nameCity,idCity=idCity,nameArea=nameArea,idArea=idArea,localCode=localCode,status=1, crtTime=datetimenowTime,lmtTime=datetimenowTime)
        cursor.execute(sql)

        print('insert_pcr_item...')

        self.conn.commit()


    def insert_card_type(self,bankId,creditID,creditType,creditName,urlPic,baseInfo,privillageInfo):
        cursor = self.conn.cursor()

        datetimenowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        sql = 'insert into CREDIT_TYPE_INFO (BANK_ID, CARD_TYPE_CODE,CREDIT_CARD_TYPE,CREDIT_CARD_NAME,CREDIT_CARD_PIC,CREDIT_BASE_INFO,CREDIT_PRIVILEGE_INFO,STATUS,CRT_TM,LMT_TM) values({bankId},\'{creditID}\',\'{creditType}\',\'{creditName}\',\'{urlPic}\',\'{baseInfo}\',\'{privillageInfo}\',\'{status}\',\'{crtTime}\',\'{lmtTime}\')'.format(bankId=bankId  \
        ,creditID=creditID,creditType=creditType,creditName=creditName,urlPic=urlPic,baseInfo=baseInfo,privillageInfo=privillageInfo,status=1, crtTime=datetimenowTime,lmtTime=datetimenowTime)

        print('SQL-->',sql)
        cursor.execute(sql)
        self.conn.commit()

    def insert_bank_city(self,bankCardCode,bankCityCode,provinceName,cityName,areaName):
        cursor = self.conn.cursor()

        datetimenowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        sql = 'insert into BANK_CITY_INFO (CARD_TYPE_CODE, BANK_CITY_CODE,PROVINCE,CITY,AREA,CRT_TM,LMT_TM) values(\'{bankCardCode}\',\'{bankCityCode}\',\'{provinceName}\',\'{cityName}\',\'{areaName}\',\'{crtTime}\',\'{lmtTime}\')'.format(bankCardCode=bankCardCode  \
        ,bankCityCode=bankCityCode,provinceName=provinceName,cityName=cityName,areaName=areaName, crtTime=datetimenowTime,lmtTime=datetimenowTime)

        print('SQL-->',sql)
        cursor.execute(sql)
        self.conn.commit()

    def delete_pcr_info(self,bankCode):
        cursor = self.conn.cursor()
        sql = 'delete from bank_city_code where BANK_CODE=\'{bankCode}\''.format(bankCode=bankCode)
        print('delete_pcr_info SQL-->',sql)
        cursor.execute(sql)
        self.conn.commit()

    def delete_cardtype_info(self,bankId):
        cursor = self.conn.cursor()
        sql = 'delete from CREDIT_TYPE_INFO where BANK_ID={bankId}'.format(bankId=bankId)
        print('delete_cardtype_info SQL-->',sql)
        cursor.execute(sql)
        self.conn.commit()        

    def delete_bank_city_info(self,bankCode):
        cursor = self.conn.cursor()
        sql = 'delete from BANK_CITY_INFO where BANK_CITY_CODE like \'{bankCode}%\''.format(bankCode=bankCode)
        print('delete_bank_city_info SQL-->',sql)
        cursor.execute(sql)
        self.conn.commit()      

    def load_pcr_info(self,filename):

        self.delete_pcr_info('CEB')

        cmb_index = 0
        with open(filename,'r',encoding='UTF-8') as f:
            jstr = json.loads(f.read())
            p_index = 0
            print(len(jstr))
            for p in range(len(jstr)):
                pName = jstr[p]['pn']
                pCity = jstr[p]['c']
                pId = jstr[p]['pid']
                pc_index = 0
                for ci in range(len(pCity)):
                    pc_index = pc_index + 1
                    cityName = pCity[ci]['cityName']
                    cityId = pCity[ci]['cityId']
                    #print('cname:',cname,'  h:',ch,'  cm:',cm)
                    cregion = pCity[ci]['area']
                    r_index = 0
                    for ri in range(len(cregion)):
                        areaName = cregion[ri]['areaName']
                        areaId = cregion[ri]['areaId']

                        province = pName
                        cityCode = ''
                        for rowi in range(len(self.jitem)):
                            pnn = self.jitem[rowi]['provinceName'].replace('省','').replace(' ','')
                            cnn = self.jitem[rowi]['cityName'].replace('市','').replace(' ','')
                            rnn = self.jitem[rowi]['areaName'].replace('区','').replace(' ','')
                            rnn = rnn.replace('县','')
                            if len(cnn)!=0 and len(rnn) != 0:
                                if pnn in province and cnn in cityName and rnn in areaName:
                                    cityCode = self.jitem[rowi]['cityCode']
                                    #print(len(cnn),',',len(rnn),'-',cnn,'-')
                                    #print('***************',pName, ' ----- ',str(pId), ' ----- ',cityName, ' ----- ',str(cityId), ' ----- ',areaName, ' ----- ',str(areaId), ' ----- ',cityCode)
                                    
                                    self.insert_pcr_item('CEB',pName,str(pId),cityName,str(cityId),areaName,str(areaId),cityCode)
                                    break


    def load_support_city(self,filename):

        self.delete_bank_city_info('CEB')

        with open(filename,'r',encoding='UTF-8') as f:
            jstr = json.loads(f.read())
            #print(jstr)
            cmb_index = 0
            for p in range(len(jstr)):
                city_item = jstr[p]

                for citem in range(len(self.ceb_card_list)):
                    cmb_index = cmb_index + 1
                    bankCardCode = self.ceb_card_list[citem]['creditID']
                    self.insert_bank_city(bankCardCode,'CEB_'+str(cmb_index),city_item['provinceName'],city_item['cityName'],city_item['areaName'])

    def load_card_type(self,filename):
        print(filename)

        self.delete_cardtype_info(self.bankId)

        self.ceb_card_list.clear()

        with open(filename,'r',encoding='UTF-8') as f:
            jstr = json.loads(f.read())
            p_index = 0
            #print(jstr)
            #print(type(jstr))
            #print(len(jstr))
            for p in range(len(jstr)):
                p_index = p_index + 1
                creditID = jstr[p]['creditID']
                if('creditType' in jstr[p]):
                    creditType = jstr[p]['creditType']
                else:
                    creditType = ''
                creditName = jstr[p]['card_name']
                urlPic = jstr[p]['urlPic']
                baseInfo = jstr[p]['base_info']
                privillageInfo = ''
                if('privillageInfo' in jstr[p]):
                    privillageInfo = jstr[p]['privillageInfo']

                card_type_item = {}
                card_type_item['creditID'] = creditID#+'_'+creditType
                card_type_item['creditType'] = creditType
                card_type_item['creditName'] = creditName
                self.ceb_card_list.append(card_type_item)
                
                #self.insert_card_type(self.bankId,creditID,creditType,creditName,urlPic,baseInfo,privillageInfo)
                
            print(self.ceb_card_list)


    def load_pt_city(self,filename):
        with open(filename,'r',encoding='UTF-8') as f:
            self.jitem = json.loads(f.read())

            return self.jitem                         


if __name__ == '__main__':
    ceb = CEB_INFO()

    ceb.conn_db()

    ceb.init_bank_id()
    
    ceb.load_card_type('F:\\Jacklin\\creditcard\\DB\\ceb_Card_listnew.json')#Finished
    #ceb.load_support_city('F:\\Jacklin\\creditcard\\DB\\ceb_support_city.json')

    #ceb.load_pt_city('F:\\Jacklin\\creditcard\\DB\\pt_city_info.json')#Finished

    #ceb.load_pcr_info('F:\\Jacklin\\creditcard\\DB\\ceb_pcr_info.json')#Finished

    


#%%