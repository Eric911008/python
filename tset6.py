"""

test 6
"""

import json 
import sys
import numpy as np
import matplotlib.pyplot as plt
grades = dict()
student_average = {}
grade = []

class Student():
    def __init__(self,ID,G1,G2,G3):
        self.ID = ID
        self.G1 = G1
        self.G2 = G2
        self.G3 = G3
    
    def showgrade(self): 
        
        print(f"student id:{self.ID}")
        print(f"grade 1:{self.G1}")
        print(f"grade 2:{self.G2}")
        print(f"grade 3:{self.G3}")
        
    def exportjson(self) :  
        
        Dict = {}
        Dict[self.ID] = [self.G1 , self.G2 , self.G3]
        J1 = json.dumps(Dict)
        print(J1)
        print("成績匯出完成 !")
    def searchgrade(self):
        
        ans = input("是否排序成績 (Y/N)")
        if ans == "y":
            print(f"student id:{self.ID}")
            print(f"grade 1:{self.G1}")
            print(f"grade 2:{self.G2}")
            print(f"grade 3:{self.G3}")
        elif ans == "n":

             print(f"學號:{self.ID}",f"作業一:{self.G1}",f"作業二:{self.G2}",f"作業三:{self.G3}")
        else:
            print("no such option")
            
    def Exit(self):        
        print("結束!")
        
class Grade():
    
    @staticmethod
    
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
           
    @staticmethod
    def export_grades() :
        file = open ("score.json", "w")
        json.dump(grades, file)
        file.close()
        print("成績匯出完成 !")
    
    @staticmethod 
    def sort_scores_by_mean() :
        for index, value in grades.items() :
            avr_grade = value[3]
            student_average[index] = avr_grade
        sort = sorted(student_average.items(), key = lambda x : x[1], reverse = True)
        print('**' * 20)
        for i in sort:
            print(i[0], i[1])
            
    @staticmethod      
    def show_all_scores() :
        for key, value in grades.items() :
            grade_1 = value[0]
            grade_2 = value[1]
            grade_3 = value[2]
            average_grade = value[3]  
            print(f"學號:{key},作業一:{grade_1},作業二:{grade_2},作業三:{grade_3},平均:{average_grade}")
            
    @staticmethod  
    def show_student_grades() :  
        wantsort = input("是否排序成績 (Y/N)")      
        if wantsort == 'y' or wantsort == "Y" :
            Grade.sort_scores_by_mean()
        else :
            Grade.show_all_scores()
            
    @staticmethod       
    def grades_bar ():
        plt.title("Average")
        plt.bar(student_average.keys(),student_average.values())
        plt.show()
      
"""
while True:
    print("\n")
    print("**" * 20)
    print("1.新增成績")
    print("2.匯出成績")
    print("3.顯示全體成績")
    print("4.繪製成圖表")
    x = int(input("請輸入要執行的動作: "))
    if x == 1 :
        Grade.add_grade()
    elif x == 2 :
        Grade.export_grades()
    elif x == 3 :
        Grade.show_student_grades()
    elif x == 4:
        Grade.grades_bar()
"""        
student1 = Student(4110029026,80,90,100)  
student1.showgrade()
student1.exportjson()
student1.searchgrade()      
        
        