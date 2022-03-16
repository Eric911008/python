"""

test 5
"""

import json 
import sys
import numpy as np
import matplotlib.pyplot as plt
grades = dict()
student_average = {}
grade = []

def add_grade() :
    student_id = input("請輸入學號: ")
    hw1 = int(input("請輸入作業一成績: "))
    hw2 = int(input("請輸入作業二成績: "))
    hw3 = int(input("請輸入作業三成績: "))
    mean_score = ((hw1 + hw2 + hw3) / 3)
    txt = f"{mean_score:.2f}"
    y = float(txt)
    grades[student_id] = [hw1, hw2, hw3, y]
    print(f'{student_id} 成績新增完成 !')
    
def export_grades() :
    file = open ("score.json", "w")
    json.dump(grades, file)
    file.close()
    print("成績匯出完成 !")
    
def sort_scores_by_mean() :
    for index, value in grades.items() :
        avr_grade = value[3]
        student_average[index] = avr_grade
    sort = sorted(student_average.items(), key = lambda x : x[1], reverse = True)
    print('**' * 20)
    for i in sort:
        print(i[0], i[1])
        
def show_all_scores() :
    for key, value in grades.items() :
        grade_1 = value[0]
        grade_2 = value[1]
        grade_3 = value[2]
        average_grade = value[3]  
        print(f"學號: {key}, 作業一: {grade_1}, 作業二: {grade_2}, 作業三: {grade_3}, 平均: {average_grade}")
        
def show_student_grades() :  
    wantsort = input("是否排序成績 (Y/N)")      
    if wantsort == 'y' or wantsort == "Y" :
        sort_scores_by_mean()
    else :
        show_all_scores()
        
def grades_bar ():
    plt.title("Average")
    plt.bar(student_average.keys(),student_average.values())
    plt.show()



       

while True:
    print("\n")
    print("**" * 20)
    print("1.新增成績")
    print("2.匯出成績")
    print("3.顯示全體成績")
    print("4.繪製成圖表")
    x = int(input("請輸入要執行的動作: "))
    if x == 1 :
        add_grade()
    elif x == 2 :
        export_grades()
    elif x == 3 :
        show_student_grades()
    elif x == 4:
        grades_bar()
        
        
        
        