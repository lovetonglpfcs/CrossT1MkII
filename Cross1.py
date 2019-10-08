from random import randint
from os import system

#กำหนดตัวที่เก็บความถี่ Array = 0
def init(CT):
    for r in range(5):
        CT.append([])
        for c in range(5):
            CT[r].append([])
            CT[r][c]=0

#กำหนด Array ที่รับข้อมูล โดยเริ่มต้นที่รับอายุ 1-3
def EnterData(TData):
    for r in range(150):
        TData.append([])
        for c in range(5):
            TData[r].append([])
            #TData[r][c]=int(input("Enter Age : "))
            TData[r][c]=randint(18,60)
            if c == 0:
                if TData[r][0] < 21:
                    TData[r][0]=1
                elif TData[r][0] < 40:
                    TData[r][0]=2
                else:
                    TData[r][0]=3
#เลือกเมนู /พร้อมเคลียหน้าจอ
def ChooseOptions():
    global Option1,Option2
    system('cls')
    print("="*55)
    print(" 0.")
    print(" 1.")
    print(" 2.")
    print(" 3.")
    print("="*55)
    while not(Option1 > -1 and Option1) < 5:
        Option1 = int(input("Enter Option1 : "))
    Option2 = Option1
    while Option1 != 0 and (Option1 == Option2 or Option2 < 0 or Option2 > 4):
        Option2 = int(input("Enter Option2 : "))
        
def Calc(TData,CT):
    global Option1,Option2
    RMAX = 0
    CMAX = 0
    for r in range(150):
        R = TData(r,Option1)
        C = TData(r,Option2)
        CT[R][C] = CT[R][C] + 1
        if R > RMAX:
            RMAX=R
        if C > CMAX:
            CMAX = C

def report(CT):
    global RMAX,CMAX
    print("\nAverage of days absent.")
    print("="*((CMAX*5)+11))
    print(f"|{'Heading':>9}|",end="")
    for c in range(CMAX):
        print(f"{c+1:>4}|",end="")
    print()
    print(f"|{'Heading':>9}|",end="")
    for c in range(CMAX):
        print(f"{' ':>4}|",end="")
    print()
    print("="*((CMAX*5)+11))
    for r in range(RMAX):
        print(f"|{r+1:>9}|",end="")
        for c in range(CMAX):
            print(f"{CT[r][c]:>4}|",end="")
        print()
    print("="*((CMAX*5)+11))

#main
Option1 = 6
Option2 = 0
CT = []
TData = []
init(CT)
EnterData(TData)
ChooseOptions()
while Option1 > 0:
    Calc(TData,CT)
    report(CT)
    init(CT)
    ChooseOptions()
