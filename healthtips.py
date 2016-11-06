from bs4 import BeautifulSoup
import urllib3
import urllib2 
import requests
import re
import csv

count=2;
for count in range(2,32):
	url='http://www.healthline.com/health-news'+'?condition=Addiction'+'#grid'

	out_file=open('tips.csv','a')
	file=csv.writer(out_file)

	page=requests.get(url)

	bs=BeautifulSoup(page.text)
	dlist=[]
	div_items= bs.find_all('div',attrs={'class':'listing_new_info_div left'})
	for div in div_items:
	 
	 a_name=div.find('a') 
	 doctor_name=a_name.text

	 '''
	 div_items_speciality=div.find('div',attrs={'class':'info_left_new margin-bottom padding-top5 clear'})
	 
	 
	 speciality = div_items_speciality.find('div',attrs={'class':'left info_details'}).text

	 div_items_clinic=div.find('div',attrs={'class':'info_left_new margin-bottom padding-top clear'})
	 clinic = div_items_clinic.find('div',attrs={'class':'left info_details'}).text

	 div_items_address=div.find('div',attrs={'class':'info_left_new margin-bottom padding-top5 clear'})
	 address = div_items_address.find('div',attrs={'class':'left info_details'}).text

	 doc=[doctor_name,speciality,clinic,address]
	 dlist.append(doc)

	 print (doctor_name) 
	  



	     
	 print (speciality)   
	 print (clinic)  
	 print (address)   
	'''
	 c=0
	 div_all=div.find_all('div',attrs={'class':'left info_details'})
	 for d in div_all:
	  
	  if c==0:
	     speciality=d.text
	  elif c==1:
	     clinic=d.text
	  else:
	     address=d.text
             pin_code= address[-6:]
	  c=c+1
	 doc=[doctor_name,speciality,clinic,address,pin_code]
	 dlist.append(doc)
	for row in dlist:
		file.writerow([item.encode('utf-8') for item in row]) 


	out_file.close()
      
                
