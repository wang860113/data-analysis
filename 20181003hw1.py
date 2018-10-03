#!/usr/bin/env python
# coding: utf-8

# In[1]:


fruits = ['蘋果','香蕉','橘子','哈密瓜','西瓜','水蜜桃','葡萄','芭樂','木瓜','梨子']
print('=====1=====')
print(fruits)

print('=====2=====')
print(fruits[4])

print('=====3=====')
print(fruits[len(fruits)-1])

print('=====4=====')
print(fruits[2:6])

print('=====5=====')
Pickfruit=fruits.pop(2)
print(Pickfruit,'\n')
print(fruits)

print('=====6=====')
fruits.insert(1,'蜜桃')
print(fruits)

print('=====7=====')
fruits.append('非洲甜橙')
print(fruits)

print('=====8=====')
country=['亞州','非洲','美洲']
fruits.extend(country)
print('extend complete')

print('=====9=====')
print(fruits)


# In[ ]:




