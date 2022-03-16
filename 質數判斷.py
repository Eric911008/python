
"""

判斷是否為質數

"""
            
    
            
num = int(input("請輸入一個數字: "))    
if num > 1:
   
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"不是質數")
           print(i,"x",num//i,"=",num)
           break
       else:
           print(num,"是質數")
           break
       
else:
   print(num,"不是質數")
