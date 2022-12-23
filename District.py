from dataurl import URL
import requests
import Bhulekh
class District:

    def __init__(self,name,code):
        self.name=name
        self.code=code

    def getName(self):
        return self.name

    def getCode(self):
        return self.code

    def getTehsils(self):
        d_ta={'act':"fillTehsil", 'district_code':self.code}
        resp=requests.post(URL,data=d_ta).json()
        return resp
