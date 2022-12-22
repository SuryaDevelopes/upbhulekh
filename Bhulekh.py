import requests
class Bhulekh:
    def __init__(self):
        self.URL="https://upbhulekh.gov.in/public/public_ror/action/public_action.jsp"


    def loadTehsil(self,code):
        d_ta={'act':"fillTehsil", 'district_code':code}
        resp=requests.post(self.URL,data=d_ta)
        return resp
    
    def loadVillage(self,dcode,tcode):
        d_ta={'act':"fillVillage", 'district_code': dcode, 'tehsil_code':tcode}
        resp=requests.post(self.URL,data=d_ta)
        return resp

    def loadFasli(self,vcode):
        d_ta={'act':"fillfasliyear",'village_code':vcode}
        resp=requests.post(self.URL,data=d_ta)
        return resp

    def searchVillage(self,dcode,tcode,query):
        d_ta={'act':"searchVillage", 'district_code': dcode, 'tehsil_code':tcode, 'query':query}
        resp=requests.post(self.URL,data=d_ta)
        return resp
    
    def searchName(self,name,vcode):
        fasli='वर्तमान फसली'
        d_ta={'name':name,'act':'sbname','vcc':vcode,'fasli-code-value':999,'fasli-name-value':fasli}
        resp=requests.post(self.URL,data=d_ta)
        return resp
