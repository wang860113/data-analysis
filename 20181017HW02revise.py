allname=[]
allword=[]
allhour=[]

while True:
  name,words,hours=input("請輸入姓名,字數/小時,時數\n").split(' ')
  stop=input("不在輸入請按n,繼續請按y\n")
  words=int(words)
  hours=int(hours)
  allname.append(name)
  allword.append(words)
  allhour.append(hours)
  
  if stop=='n':
    break
  elif stop=='y':
    continue
  elif stop!='y':
    print('錯誤的輸入')
  elif stop!='n':
    print('錯誤的輸入')
  


allmoney=list(map(lambda a,b:((a/200)*10)*b,allword,allhour))
print('='*20)
print('姓名','\t','薪水')
for i in range(len(allname)):
  print(allname[i],'\t',allmoney[i])