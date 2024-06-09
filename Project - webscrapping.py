#!/usr/bin/env python
# coding: utf-8

# In[35]:


pip install requests


# In[36]:


pip install beautifulsoup4


# In[37]:


import requests


# In[38]:


import re


# In[39]:


from bs4 import BeautifulSoup


# In[25]:


path = 'https://www.coursera.org/learn/python-crash-course/'
#add / at the end for default index page in case of error


# In[26]:


page = requests.get(path)


# In[27]:


print (page)


# In[28]:


soup = BeautifulSoup(page.text, 'html.parser')


# In[29]:


txt = str(soup)


# In[30]:


print(txt)


# In[31]:


result = re.findall(r'(\d+,?\d+,?\d+)</span></strong> already enrolled',txt)
#\d matches a number, \d+ for more than one number matching, ? means optional towads left side,


# In[32]:


print (result)


# In[47]:


#pip install requests
#pip install beautifulsoup4
#import requests
#import re
#from bs4 import BeautifulSoup
#path = 'https://www.edx.org/learn/python/ibm-python-basics-for-data-science?index=product&queryID=5b20e89b71cef69e72d57865e7819695&position=1&results_level=first-level-results&term=python+basics+for+data+science&objectID=course-381a0046-5d78-4790-8776-74620d59f48e&campaign=Python+Basics+for+Data+Science&source=edX&product_category=course&placement_url=https%3A%2F%2Fwww.edx.org%2Fsearch/'
#page = requests.get(path)
#print (page)
#soup = BeautifulSoup(page.text, 'html.parser')
#txt = str(soup)
#print(txt)
#result = re.findall(r'(\d+,?\d+,?\d+) already enrolled',txt)
#print (result)


# In[62]:


#pip install requests
#pip install beautifulsoup4
#import requests
#import re
#from bs4 import BeautifulSoup
#path = 'https://www.udemy.com/course/100-days-of-code/?couponCode=ST20MT50724/'
#page = requests.get(path)
#print (page)
#soup = BeautifulSoup(page.text, 'html.parser')
#txt = str(soup)
#print(txt)
#result = re.findall(r'(\d.\d) out of 5</span><span',txt)
#print (result)


# In[3]:


url = 'https://www.bbc.com/news'
response = requests.get(url)
print (response)
soup = BeautifulSoup(response.text, 'html.parser')

print(txt)
h2_headings = soup.find_all('h2',('data-testid':'card-headline', 'class': 'sc-4fedabc7-3 zTZri')) #h2 k beech mein jo hai print krdo
for heading in h2_headings:
    print (heading.text.strip())
#str mein convert nai krna coz soup understands h2 heading



# In[2]:


import requests
import re
from bs4 import BeautifulSoup

url = [
    'https://www.coursera.org/learn/python-for-applied-data-science-ai',
    'https://www.coursera.org/learn/python-crash-course',
    'https://www.coursera.org/professional-certificates/google-it-automation',
    'https://www.coursera.org/specializations/python-3-programming',
    'https://www.coursera.org/learn/data-analysis-with-python',
    'https://www.coursera.org/learn/get-started-with-python',
    'https://www.coursera.org/learn/programming-in-python',
    'https://www.coursera.org/learn/python-basics',
    'https://www.coursera.org/learn/programming-in-python',
    'https://www.coursera.org/learn/python-programming-fundamentals',
    'https://www.udemy.com/course/100-days-of-code/?couponCode=LETSLEARNNOW'#diff string so need diff code
]

for path in url:
    page = requests.get(path)
    print(page)
    soup = BeautifulSoup(page.text, 'html.parser')
    txt = str(soup)
    result = re.findall(r'(\d+,?\d+)</span></strong> already enrolled', txt)
    if result:
        print(f"Number of students enrolled in {path}: {result[0]}")
    else:
        print(f"Unable to find enrollment data for {path}")



# In[16]:


import requests
from bs4 import BeautifulSoup
url= 'https://edition.cnn.com'
response = requests.get(url)
soup= BeautifulSoup(response.text,'html.parser')
h2_headings = soup.find_all('h2',('data-editable':'headline', 'class': 'container__headline-text'))
from headings in h2_headings:
    print(heading.text.strip())


# In[5]:


#without copy pasting URLs
import requests
from bs4 import BeautifulSoup
import re
url ='https://www.coursera.org/search?query=python'
response= requests.get(url)
soup= BeautifulSoup (response.text, 'html.parser')
mystring= str(soup)
#Regular exp pattern to search for the desired string
#+ means 1 or more * means 0 or more
pattern = r'"(https://www\.coursera\.org/[a-zA-Z0-9/-]+python[a-zA-Z0-9/-]*)"'
#search for the pattern in string
matches = re.findall(pattern, mystring)
for link in matches:
    print(link)


# In[9]:


from bs4 import BeautifulSoup
import re
url ='https://www.coursera.org/search?query=python'
response= requests.get(url)
soup= BeautifulSoup (response.text, 'html.parser')
mystring= str(soup)
#Regular exp pattern to search for the desired string
#+ means 1 or more * means 0 or more
pattern = r'"(https://www\.coursera\.org/[a-zA-Z0-9/-]+python[a-zA-Z0-9/-]*)"'
#search for the pattern in string
matches = re.findall(pattern, mystring)
for link in matches:
    print(link)
urllist=list(dict.fromkeys(matches))
list1=[]
for url in urllist:
    print(url)
    page= requests.get(url)
    soup= BeautifulSoup(page.text, 'html.parser')
    txt= str(soup)
    result= re.findall(r'(\d+,?\d+,?\d+)</span></strong> already enrolled',txt)
    list1.append(result)
    print(result)


# In[ ]:




