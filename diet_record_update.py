# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 19:26:00 2026

@author: 12921
"""

def input_intake():
    state=True
    while state:
        protein =input("输入蛋白质(按q退出记录) ")
        if protein=='q':
            state=False
            break
        try:
            protein=float(protein)
        except:
            print('重新输入蛋白质')
            continue
        if protein<0:
            print('输入有误 重新输入')
            continue
    while state:   
        carbs =input("输入碳水(按q退出记录) ")
        if carbs=='q':
            state=False
            break
        try:
            carbs=float(carbs)
        except:
            print('重新输入碳水')
            continue
        if carbs<0:
            print('输入有误 重新输入')
            continue
    while state:     
        fat =input("输入脂肪(按q退出记录) ")
        if fat=='q':
            state=False
            break
        try:
            fat=float(fat)
        except:
            print('重新输入脂肪')
            continue
        if fat<0:
            print('输入有误 重新输入')
            continue
    if state==False:
        return []
    return [protein,carbs,fat]


def print_record(list):
    for i in range  (len(list)):
        print(list[i])
        
        
def conclusion(list):
    p,c,f=0,0,0
    for i in range (len(list)):
        p+=list[i][0]
        c+=list[i][1]
        f+=list[i][2] 
    return p,c,f

list=[]
while True:
    ipt=input('1.添加一条饮食记录\n2.查看所有记录（逐条打印）\n3.查看总摄入（全部加起来）\n4.清空\n5.退出')
    try:
        ipt=int(ipt)
    except:
        print('输入不合法 重新输入')
        continue
    if ipt<1 or ipt>5:
        print('输入不合法 重新输入')
        continue
    if ipt==1:
        data = input_intake()
        if data != []:
            list.append(data)
    elif ipt==2:
        print_record(list)
    elif ipt==3:
        p1,c1,f1=conclusion(list)
        print(f'蛋白质总摄入{p1}')
        print(f'碳水总摄入{c1}')
        print(f'脂肪总摄入{f1}')
    elif ipt==4:
        list=[]
    else:
        break