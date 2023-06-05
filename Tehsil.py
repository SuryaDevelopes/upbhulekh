import requests
import Village
from dataurl import URL
class Tehsil:
    
    def __init__(self,tname,tcode,tengname,district):
        self.tname=tname
        self.tcode=tcode
        self.tengname=tengname
        self.district=district
        self.villagecount=0

    def getHindiName(self):
        return self.tname

    def getName(self):
        return self.tengname

    def getCode(self):
        return self.tcode

    def getDistrict(self):
        return self.district

    def getVillageCount(self):
        return self.villagecount

    def getVillages(self):
        d_ta={'act':"fillVillage", 'district_code': self.district.getCode(), 'tehsil_code':self.tcode}
        resp=requests.post(URL,data=d_ta).json()
        self.villagecount=len(resp)
        return resp


