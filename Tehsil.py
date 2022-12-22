class Tehsil:
    
    def __init__(self,tname,tcode,tengname):
        self.tname=tname
        self.tcode=tcode
        self.tengname=tengname

    def getHindiName(self):
        return self.tname

    def getName(self):
        return self.tengname

    def getCode(self):
        return self.tcode
