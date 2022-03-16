
"""
while迴圈計算班級成績

"""

total = person = score = 0

while (score != -1):          # enter -1 to claculate result
    person += 1
    total += score
    score = int(input("請輸入第 %d 位學生的成績: " % person))
    
average = total / (person -1) 
print("本班總成績 : %d 分 ， 平均成績 : %5.2f 分" % (total,average)) 
     