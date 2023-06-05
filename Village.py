import requests

from dataurl import URL
class Village:
    def __init__(self,vname,vcode,vengname,pname,flg_chakbandi,flg_survey,pargana_code,tehsil):
        self.vname=vname
        self.vcode=vcode
        self.engname=vengname
        self.tname=pname
        self.chakbandi=flg_chakbandi
        self.survey=flg_survey
        self.parganacode=pargana_code
        self.tehsil=tehsil

    def getCode(self):
        return self.vcode


    def getHindiName(self):
        return self.vname
    
    def getName(self):
        return self.engname

    def getTehsilName(self):
        return self.tname

    def getChakbandiStatus(self):
        return self.chakbandi

    def getSurveyStatus(self):
        return self.survey

    def getNewParganaCode(self): 
        return self.parganacode

    def getTehsil(self):
        return self.tehsil

    def searchName(self,name):
        fasli='वर्तमान फसली'
        d_ta={'name':name,'act':'sbname','vcc':self.vcode,'fasli-code-value':999,'fasli-name-value':fasli}
        resp=requests.post(URL,data=d_ta).json()
        return resp

    def toVillageObj(data):
        vname=data.get('vname')
        vcode=data.get('vcode')
        veng=data.get('vname_eng')
        tname=data.get('pname')
        chak=data.get('flg_chakbandi')
        sur=data.get('flg_survey')
        par=data.get('pargana_code_new')
        return (vname,vcode,veng,tname,chak,sur,par)

