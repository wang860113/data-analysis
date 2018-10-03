#!/usr/bin/env python
# coding: utf-8

# In[1]:


classmate = [("林威豪","台北市"),("黃安安","高雄市"),("林湘琦","台中市"),("陳遠見","台南市"),("林萊萱","台中市"),("許志祥","台北市"),("呂姍姍","嘉義市"),("張柏凱","桃園市")]
newclassmate=classmate.copy();
pick=list();
newpick=[]
print("=========")
for i in range(0,len(classmate)):
 print(classmate[i][0],classmate[i][1]);
print("=========")
for j in range(0,len(classmate)):
  if(classmate[j][1] == "台北市"):
    del newclassmate[j];
    pick.append(classmate[j]);

print(pick)

print("=========")
for k in range(0,len(newclassmate)):
  print("第",k+1,"位同學",newclassmate[k][0],":家住",newclassmate[k][1]);
print("======teacher skill=====")
for member in classmate:
  if member[1] =='台北市':
    temp=classmate.pop(classmate.index(member))
    newpick.append(temp)
print(newpick)


# In[ ]:




