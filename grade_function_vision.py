# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 16:55:25 2026

@author: 12921
"""

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
# while True:  
#     out=input_grade()    
#     if out=='j':
#         continue
#     elif out=='q':
#         break
#     else:
#         grade_list.append(out)
#         if count_pass_fail(out):
#             ps+=1
#         else:
#             ups+=1
# show_result(grade_list, ps, ups)

while True:
    move=input('1.录入成绩\n2.查看所有成绩\n3.查看统计结果\n4.退出程序')
    try:
        move=int(move)
    except:
        print('输入有误 请重新输入')
        continue
    if move>4 or move<1:
        print('输入有误 请重新输入')
        continue
    else:
        if move==1:
            out=input_grade()    
            if out=='j':
                continue
            elif out=='q':
                continue
            else:
                grade_list.append(out)
                if count_pass_fail(out):
                    ps+=1
                else:
                    ups+=1
        if move==2:
            for i in grade_list:
                print(i)
        if move==3:
            show_result(grade_list, ps, ups)
        if move==4:
            break
            
        
