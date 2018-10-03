
# coding: utf-8

# In[27]:


Book = ["國文","英文","數學","財務","工程","歷史","公民","地理","物理","化學","地科","線性代數","機率論","電路學","電子學"]
print("=====1=====")
print(Book);
print("=====2=====")
print(Book[7]);
print("=====3=====")
print(Book[0],Book[14]);
print("=====4=====")
print(Book[9:12]);
print("=====5=====")
sbook=list();
sbook1=Book.pop(14);
sbook2=Book.pop(13);
sbook=sbook1+sbook2;
print(sbook);
print(Book);
print("=====6=====")
Book.insert(4,"作業研究")
print(Book);
print("=====7=====")
country = ["台灣","日本","韓國","美國","加拿大"]
print(country);
print("=====8=====")
Book.extend(country)
print(Book);

