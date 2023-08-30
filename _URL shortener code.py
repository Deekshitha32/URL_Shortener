#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests

def shorten_url(api_key, long_url, custom_name):
    base_url = "https://cutt.ly/api/api.php"
    
    params = {
        "key": api_key,
        "short": long_url,
    }
    
    if custom_name:
        params["name"] = custom_name
    
    response = requests.get(base_url, params=params).json()
    
    if response["url"]["status"] == 7:
        shortened_url = response["url"]["shortLink"]
        return shortened_url
    else:
        return None

def main():
    api_key = "f5a49894fc654968b74b10019e1929a842b9d"  
    
    long_url = input('Enter the long URL: ')
    custom_name = input('Enter a custom name (optional): ')
    
    shortened_url = shorten_url(api_key, long_url, custom_name)
    
    if shortened_url:
        print("Shortened URL:", shortened_url)
    else:
        print("URL shortening failed.")

if _name_ == "_main_":
    main()

