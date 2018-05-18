#!/usr/bin/env python2
import time
import webbrowser
import datetime
option= '''
Press 1 : to search every word
Press 2 :to image search only
Press 3 :to print url of each website
Press 4 :current time and date
press 5 : open default web  browser
press 6 : all network ip
press 7 : enter url and check owner name
'''
print option
ch=raw_input()
if ch=='1':
	search_data=raw_input("enter data :  ")
	strip_data=search_data.strip()
	split_data=final_data.split()
	for i in split_data :
         webbrowser.open_new_tab('https://www.google.com/search?q='+i)
if ch=='4':
         t=datetime.datetime.now()
	 print("current date and time : ")
	 print(t.strftime("%y-%m-%d %H:%M:%S"))
if ch=='5':
	 webbrowser.get('firefox').open('youtube.come')

else:
	print "no chance.."
