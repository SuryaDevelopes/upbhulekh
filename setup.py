import requests
import sortjanpads as j
import googletrans
import District
import Tehsil
import InputUser
import Village
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

console=Console()
def getDistrict():
    c=0
    for i in j.janpads:
        c+=1
        console.print(str(c)+'.',i,style="bold")
    dis=int(input("Enter District: "))
    code=list(j.janpads.values())[dis-1]
    name=list(j.janpads.keys())[list(j.janpads.values()).index(code)]
    district=District.District(name,code)
    return district


def getTehsil(district):
    c=0
    teh=district.getTehsils()
    for i in teh:
        c+=1
        console.print(str(c)+'.',i.get('tehsil_name_english'),style="bold white")
    t_in=int(input("Enter Tehsil: "))
    index=t_in-1
    code=teh[index].get('tehsil_code_census')
    nhindi=teh[index].get('tehsil_name')
    neng=teh[index].get('tehsil_name_english')
    tehsil=Tehsil.Tehsil(nhindi,code,neng,district)
    return tehsil

def getVillage(district,tehsil,idx=0):
    c=0
    vill=tehsil.getVillages()
    if(idx==0):
        for i in vill:
            c+=1
            console.print(str(c)+'.',i.get('vname_eng'),style="bold magenta")
        v_in=int(input("Enter Village: "))
        index=v_in-1
    else:
        index=idx
    code=vill[index].get('village_code_census')
    nhindi=vill[index].get('vname')
    neng=vill[index].get('vname_eng')
    tehname=vill[index].get('pname')
    chakb=vill[index].get('flg_chakbandi')
    surv=vill[index].get('flg_survey')
    pargana=vill[index].get('pargana_code_new')
    village=Village.Village(nhindi,code,neng,tehname,chakb,surv,pargana,tehsil)
    return village


def getData(name,village):
    udata=village.searchName(name)
    return udata


def printPrettyData(district,tehsil,village,serdata):
    table=Table(title=f":{district.getName()} > {tehsil.getName()} > {village.getName()}")
    table.add_column("Name",style="cyan")
    table.add_column("Father's Name",style="green")
    for i in serdata:
        table.add_row(str(i.get('name')),str(i.get('father')))
    console.print(table)

def askChoice():
    ch=int(input("1. Search In One Village\n2. Search In All Villages\nEnter: "))
    return ch


def main():
    inputuser=InputUser.InputUser()
    district=getDistrict()
    tehsil=getTehsil(district)
    inputuser.askName()
    ask=askChoice()
    if(ask==1):
        village=getVillage(district,tehsil)
        serverdata=getData(inputuser.getHindiName(),village)
        printPrettyData(district,tehsil,village,serverdata)
    elif(ask==2):
        vill=tehsil.getVillages()
        for i in range(tehsil.getVillageCount()):
            village=getVillage(district,tehsil,i)
            serverdata=getData(inputuser.getHindiName(),village)
            printPrettyData(district,tehsil,village,serverdata)





if(__name__=='__main__'):
    main()





