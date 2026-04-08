# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 16:14:42 2026

@author: 12921
"""
ps=0
ups=0
grade_list=[]
while True:
    grade=input('输入成绩(输入q结束)')
    if grade=='q':
        break
    try:
        grade=float(grade)
        if grade<0 or grade>100:
            print('请重新输入')
            continue
    except:
        print('请重新输入')
        continue
    grade_list.append(grade)
    if grade>=60:
        ps+=1
    else:
        ups+=1
if grade_list==[]:
    print('无结果')
else:
    print(f'最高分为{max(grade_list):.2f}')
    print(f'最低分为{min(grade_list):.2f}')
    print(f'平均分为{sum(grade_list)/len(grade_list):.2f}')
    print(f'及格人数为{ps}')
    print(f'不及格人数为{ups}')




def input_grade():
    grade=input('输入成绩(输入q结束)')
    if grade=='q':
        return grade
    try:
        grade=float(grade)
        if grade<0 or grade>100:
            print('请重新输入')
            return 'j'
        return grade
    except:
        print('请重新输入')
        return 'j'
    
def count_pass_fail(grade):
    if grade>=60:
        return True
    else:
        return False
    
    
def show_result(grade_list, ps, ups):
    if grade_list==[]:
        print('无结果')
    else:
        print(f'最高分为{max(grade_list):.2f}')
        print(f'最低分为{min(grade_list):.2f}')
        print(f'平均分为{sum(grade_list)/len(grade_list):.2f}')
        print(f'及格人数为{ps}')
        print(f'不及格人数为{ups}')
        
ps=0
ups=0
grade_list=[]
while True:  
    out=input_grade()    
    if out=='j':
        continue
    elif out=='q':
        break
    else:
        grade_list.append(out)
        if count_pass_fail(out):
            ps+=1
        else:
            ups+=1
show_result(grade_list, ps, ups)

        
        
    
    



    
