from googletrans import Translator
class InputUser:

    def __init__(self):
        self.name=''

    def askName(self):
        self.name=str(input("Enter Name: "))

    def getName(self):
        return self.name

    def getHindiName(self):
        t=Translator()
        hname=t.translate(self.name,'hi').text
        return hname
