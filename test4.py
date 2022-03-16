
"""
Created on Wed Oct 27 16:30:28 2021

成績系統
"""

student = {}
while True:
    print("1.新增學生成績")
    print("2.搜尋學生成績")
    print("3.顯示所有學生成績 ")
    print("4.結束")
    x = int(input("*請輸入要執行的選項:"))
    if x == 1:
        student_ID = input("請輸入學號: ")
        student_name = input("請輸入姓名: ")
        grade_1 = input("grade 1:")
        grade_2 = input("grade 2:")
        grade_3 = input("grade 3:")
        student[student_ID] = [grade_1, grade_2, grade_3]
        print("成績新增完成!")
        print("-" * 25)       
    elif x == 2:
        number_2 = input("請輸入學號: ")
        if number_2 in student:
            student_grade1 = (student.get(number_2))[0]
            print("grade 1= ", student_grade1)            
            student_grade2 = (student.get(number_2))[1]
            print("grade 2= ", student_grade2)
            student_grade3 = (student.get(number_2))[2]
            print("grade 3= ", student_grade3)          
            print("-" * 25)
        else:
            print("請輸入正確的學號!")
            print("-" * 25)
    elif x == 3:      
        for key, value in student.items():              
            print("student_ID", key)
            print("grade 1", value[0])
            print("grade 2", value[1])
            print("grade 3", value[2])
            print("-" * 25)
    elif x== 4:
        print("結束")
        break     
    else:
        print("沒有這個選項!")
        print("-" * 25)
        
    
    
        
        
            
            


