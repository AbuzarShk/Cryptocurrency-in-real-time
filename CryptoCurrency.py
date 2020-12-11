#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import time


# In[2]:


url = 'https://www.google.com/search?q=bitcoin+price'

HTML = requests.get(url)

soup = BeautifulSoup(HTML.text, 'html.parser')

print(soup.prettify())


# In[3]:


#<div class="BNeawe iBp4i AP7Wnd">

def get_crypto_price(coin):
    url = 'https://www.google.com/search?q='+coin+'+price'

    HTML = requests.get(url)

    soup = BeautifulSoup(HTML.text, 'html.parser')

    text = soup.find('div', attrs={'class':'BNeawe iBp4i AP7Wnd'}).find('div', attrs={'class':'BNeawe iBp4i AP7Wnd'}).text
    
    return text


# In[4]:


price = get_crypto_price('litecoin')



print(price)


# In[7]:


def main():
    last_price = -1
    while True:
        crypto = 'bitcoin'
        price = get_crypto_price(crypto)
        if price != last_price:
            print(crypto+' price: ',price)
            
            last_price = price
        time.sleep(1)


# In[ ]:


main()


# In[ ]:





# In[ ]:




