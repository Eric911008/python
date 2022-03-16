
"""

append scores to a list and calculate its average

"""

score  = []

total = inscore = 0

while inscore != -1 :
    inscore = int(input("請輸入學生成績:"))
    score.append(inscore)
     
for i in range(0 , len(score)-1):
    total += score[i]
    average = total / (len(score)-1)
        
print("--" * 25)    
print("共有 %d 位學生" % (len(score)-1))   
print("總分 : %d 分 ， 平均成績: %5.2f 分" % (total , average))  

    