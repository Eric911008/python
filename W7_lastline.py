# 讀出檔案最後一行字的四種方法

f = open(filename, 'r')

#readlines()列印出全部檔案後，看最後一行
for line in f.readlines():
    print(line)

#readline()以無窮迴圈讀檔案，只記錄當下讀到的一行
while True:
    line=f.readline()
    if not line:
        break
    lastline=line
print(lastline)


#直接走訪檔案物件，讀出檔案每一行，只記錄當下讀到的一行
for line in f:
    lastline=line
print(lastline)


#直接走訪檔案物件，讀出檔案每一行
for line in f:
    pass
print(line)   

f.close()
    







    
    









