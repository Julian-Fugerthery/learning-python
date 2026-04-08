# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 11:18:32 2026

@author: scyjh15
"""
l=[]
while True:
    w=input('输入体重(按q退出)')
    if w=='q':
        break
    try:
        w=float(w)
    except:
        print('重新输入')
        continue
    h=input('输入身高')
    try:
        h=float(h)
    except:
        print('重新输入')
        continue
    if h<=0:
        print('重新输入')
        continue
    bmi=w/h**2
    l.append(bmi)
    if bmi<18.5:
        print('偏瘦')
    elif bmi<24:
        print('正常')
    elif bmi<28:
        print('偏胖')
    else:
        print('超重')
    
if l==[]:
    print('无结果')
else:
    print(f'最大bmi{max(l)},最小bmi{min(l)},平均值{sum(l)/len(l)}')