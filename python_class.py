#!/usr/bin/env python
# coding: utf-8

# In[1]:


a="pakISTan zinDA bAAD"
print(a)


# In[2]:


a.capitalize()# inline hay yani real data change nhi hoga aur print k liya shift+enter


# In[3]:


a.lower() # inline hay


# In[4]:


a.upper() #inline


# In[5]:


print(a) # check karain real data change nahi howa


# In[6]:


a.title()


# In[7]:


print(a.title()) # is tarah bhi likh saktay hain


# In[8]:


a.format()


# In[9]:


help(print) # print ki command ki help yani is function ki detail


# In[10]:


a.casefold()


# In[11]:


print(a.casefold())


# In[12]:


print(a.lower())


# In[13]:


print(a.center())


# In[14]:


a.center()


# In[20]:


a="""
*******PIAC********
Saylani Welfare Trust 
name = Muhammed Naveed
father's name = Muhammed Haroon
Roll # = 00458"""
print(a)


# In[21]:


a


# In[35]:


name="Muhamed Naveed"
father_name = "Muhammed Haroon"
roll_no = 742

a="""
*******PIAC********
Saylani Welfare Trust 
name :{}
father's name :{}
Roll # :{}
"""

print(a.format(name, father_name, roll_no))


# In[33]:


print(name)


# In[38]:


a=input("Enter Your Name= ")


# In[39]:


name=input("Enter Your Name")
father_name = input("Enter your Father Name")
roll_no = input("Enter your Roll number")

a="""
*******PIAC********
Saylani Welfare Trust 
name :{}
father's name :{}
Roll # :{}
"""

print(a.format(name, father_name, roll_no))


# In[41]:


number=45+65
number


# In[42]:


number=45-64
number


# In[43]:


number=45/85
number


# In[46]:


#% is a modulus yani divide k baad bachi howi value
number=2%5
number


# number=45//85
# number

# In[47]:


number=45//85
number


# In[48]:


4/2


# In[49]:


4//2 #double divide point k baad k result ko ignore karay ga


# In[50]:


4/3


# In[51]:


4//3


# In[52]:


4*3 # yay simple multiply karay ga


# In[53]:


4**3 # aur yay power hay yani 4 ki power 3 , yani 4 ko 3 martaba multiple karna hay


# In[55]:


# = ka matlab hay porani value ko bhol jao new value ko yaad rakho
# += ka matlab hay porani value may new vale ko joor do
a=("naveed")
a+=("haroon")
print(a)


# In[56]:


# -= ka matlab hay poani value say new ko minus kar day ga
# *= ka matlab hay porani value say new ko multiply kar day ga
# /= ka matlab hay porani valus say new ko divide kar day ga
# %= ka matlab hay porani value ap ka modulus lay ga new value k sath aur is ko return kar day ga variable may
n=5
n+=6
print(n)


# In[57]:


n-=2
print(n)


# In[58]:


n*=3
n


# In[59]:


n/=3
n


# In[60]:


n*=3
n


# In[61]:


n//=3
n


# In[62]:


n%=3
n


# In[63]:


n+=8
n%=3
n


# In[ ]:


# if ya else ki command k liyay logical operator use hotay hain example ==,<,>,<=,>=,!=
# == do value ko compare karwanay k liyay hay aur single = value define karnay k liyay hay
# != is ka matlab not equal to
# and , or  yay bhe operator hain, and saray sahi hon to , or agar aik bhi sahi ho to


# In[74]:


2+6*8/5(2*3) # complex equation is may pamdas tareqa istimal hoga


# In[75]:


2+6*8/5


# In[76]:


f="pakistan"
print(f)


# In[77]:


f="china"
print(f)


# In[79]:


f*=6
f


# In[80]:


f+="pakistan"
f


# In[81]:


5==5


# In[82]:


5<=5


# In[83]:


6<=5


# In[84]:


5>=6


# In[85]:


6>=5


# In[86]:


5==5 and 6==6 and 5>=4


# In[87]:


5==5 and 6==6 and 5>=6


# In[88]:


5==5 or 6==6 or 5>=4


# In[96]:


a="naveed"
b="haroon"
c=5
a+b


# In[98]:


a="naveed"
b="haroon"
c=45
a+b+str(c)


# In[99]:


a="1"
b="1"
a+b


# In[100]:


int(a)+int(b)


# In[ ]:


# ab control flow    if, else, elif , 2 say ziyada logic k liyay elif use hota hay


# In[ ]:


if logic:
    true value
else:
    false value


# In[ ]:


if logic1:
    true value 1
elif logic 2:
    true value2
elif logic 3:
    true value 3
else:
    false value
    


# In[ ]:





# In[ ]:


if logic1 and logic2 and logic3:
    value true
else:
    value false


# In[101]:


name = input("Enter your name")
if name == "qasim":
    print("teacher")
else:
    print("student")


# In[102]:


name = input("Enter your name")
if name == "qasim":
    print("teacher")
else:
    print("student")


# In[103]:


name = input("Enter your name")
if name == "qasim":
    print("teacher")
else:
    print("student")


# In[ ]:


# yani case sensitive hay


# In[105]:


name = input("Enter your name")
if name.lower() == "qasim":
    print("teacher")
else:
    print("student")


# In[106]:


per = 70
if per >=0:
    print("Fail")
elif per >=35:
    print("Grade F")
elif per >=50:
    print("Grade D")
elif per >=70:
    print("Grade A")
elif per >=90:
    print("Grade A")


# In[109]:


per = 70
if per >=0 and per <35:
    print("Fail")
elif per >=35 and per <50:
    print("Grade F")
elif per >=50 and per <70:
    print("Grade D")
elif per >=70 and per <90:
    print("Grade A")
elif per >=90:
    print("Grade A")


# In[118]:


# list bana , list edit able hote hay aur tupple non editable
names=["naveed","kashif","huzaifa","jibran"]
names


# In[119]:


print(names)


# In[120]:


names[2]="imran"
print(names)


# In[137]:


names=[]
while True:
    a=input("names")
    if a!="x":
        names.append(a)
    else:
        break


# In[ ]:




