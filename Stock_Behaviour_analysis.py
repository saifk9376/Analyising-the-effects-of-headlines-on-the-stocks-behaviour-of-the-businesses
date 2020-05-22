# -*- coding: utf-8 -*-
"""
Created on Thu May 21 00:51:59 2020

@author: SAIF KHAN
"""
#### This code has been made to analyse the effects of news headlines through sentiment metrics in the 'finviz.com' and its impacts on the busiensses stocks####

###Importing the necessary libraries###
import os, time
import certifi
import pycurl as pycurl
from io import BytesIO

path = ('./Stock_Analysis/')
file_list = os.listdir('./Stock_Analysis')
try:
    os.mkdir('./Stock_Analysis')
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s " % path)

#####Deleting Files from the specificied folder######
now = time.time()

for file in file_list:
    # if os.stat(os.path.join(path, filename)).st_mtime < now - 7 * 86400:
    if os.path.getmtime(os.path.join(path, file)) < now - 7 * 86400:
        if os.path.isfile(os.path.join(path, file)):
            print(file)
            os.remove(os.path.join(path , file))

##Getting the user inputs##            
company_stocklist = []
url_stocklist = []
nof_cmpny = int(input('Provide the no of companies to further analyse: '))
for cmpny in range(nof_cmpny):
  cmpny_stock_name = input('Provide the stock name of the companies: ')
  company_stocklist.append(cmpny_stock_name.upper())
  site_url = 'https://finviz.com/quote.ashx?t='
  url_stocklist.append(site_url+cmpny_stock_name)
  
print(url_stocklist[0])

sites_data = {}

for index in range(nof_cmpny):
 try:
    website_input_url = url_stocklist[index]
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, website_input_url)
    c.setopt(c.WRITEDATA, buffer)
    c.setopt(c.CAINFO, certifi.where())
    c.perform()
    c.close()
    body = buffer.getvalue()
    sites_data[company_stocklist[index]] = body.decode('utf8')
 except (RuntimeError, TypeError, NameError):
    print ('Website not found')
    
for i in range(nof_cmpny):
    write_to_file = open(path + company_stocklist[i]+'.html', 'w')
    write_to_file.write(sites_data[company_stocklist[i]])
    write_to_file.close()
 
###Importing libraries for scraping the loaded pages to get the headlines about companies###
from bs4 import BeautifulSoup
    
html_pages = {}

for page_name in os.listdir('./Stock_Analysis'):
    page_path = f'./Stock_Analysis/{page_name}'
    page_file = open(page_path, 'r')
    html_data = BeautifulSoup(page_file, "lxml")
    # The .html file contains a 'news-table' section that holds all the news headlines
    html_page = html_data.find(id="news-table")
    # Adding the pages to our dictionary
    html_pages[page_name] = html_page























######buffer = BytesIO()
##c = pycurl.Curl()
#c.setopt(c.URL, site_url)
#c.setopt(c.WRITEDATA, buffer)
##c.setopt(c.CAINFO, certifi.where())
#c.perform()
#c.close()
#body = buffer.getvalue()
#ody.decode('utf8')

#for index in range(nof_cmpny):
#try:website_input_urls = body(url_stocklist[index])#########balls you made a function here....irreplacable mistake#################
#except (RuntimeError, TypeError, NameError):
#print ('Website not found')




            
# Website Downloader
##def url_downloader(url):
##byte_obj = BytesIO() 
##curl = pycurl.Curl() 
##curl.setopt(curl.URL, url)
##curl.setopt(curl.WRITEDATA, byte_obj)
##curl.perform() 
##curl.close()
    # Get the content stored in the BytesIO object (in byte characters) 
    ##get_body = byte_obj.getvalue()
    # Decode the bytes stored in get_body to HTML and print the result 
    ##return get_body.decode('utf8')          


            
##########file_path = './html_files/'
###file_list = os.listdir('./html_files')
###for file in file_list:
    ###os.remove(file_path + file)############