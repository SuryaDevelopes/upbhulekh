class Village:
    def __init__(self,vname,vcode,vengname,pname,flg_chakbandi,flg_survey,pargana_code):
        self.vname=vname
        self.vcode=vcode
        self.engname=vengname
        self.tname=pname
        self.chakbandi=flg_chakbandi
        self.survey=flg_survey
        self.parganacode=pargana_code

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


