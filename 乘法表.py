
"""
method 1
"""

for i in range(1, 10): 
    for j in range(1, 10):
        if j == 9:
          print("\t", i*j) # j == 9時，換行
        else:
          print("\t", i*j, end ="") # j < 9時，不換行
          
"""
method 2
"""        
         
for i in range(1,10):
    for j in range(1,10):
        product = i * j
        print("%d * %d = %d\t" % (i , j , product) , end="") 
        
          
          
          
          
          
          
          
          
