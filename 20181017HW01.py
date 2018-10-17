import math
import time

name=['林姍','王志祥','李明立','黃婷婷','張文智','陳怡君','王凱群','林曉曉']
high=[155,175,172,162,180,158,170,156]
weigth=[45,85,68,52,72,48,80,70]
student=[]
BMI=[]
for i in range(len(name)):
  student.append(name[i])
  student.append(high[i])
  student.append(weigth[i])
print(student)
print('='*50)
print('請以下同學注意飲食')
print('姓名',' ','BMI')

for i in range(0,len(student),3):
  high=student[i+1]
  weigth=student[i+2]
  T=weigth/((high/100)**2)
  T=round(T,2)#小數點第2位
  BMI.append(T) 
  if(T>27):
    print(student[i],T)
print(BMI)
