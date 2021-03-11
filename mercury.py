#!/usr/bin/python
     #importing all the modules 
import os
import socket
banner="""

####################################################################################################
#                                   							   	   #
#	---	 ---  										   #
#	|  \    /  |               -------               --       --   -------     --     --       #
#	|   \  /   |    ------	  |	  |     ------	|  |    |  |  |	      |	  |  |	 |  |	   #
#	| |\ \/ /| |   /      \   |  |-----    /      | |  |    |  |  |   |----   |  |   |  |      #
#	| | \  / | |  /	  ---  \  |  \	\     /	   ---  |  |    |  |  |	  \  \    |   ---   |      #
#       | |  \/	 | |  \   -----/  |  |\  \    \    \--  |   ----   |  |   |\  \    ---   ---       #
#       | |	 | |   \          |  | \  \    \      | |          |  |   | \  \      |  |         #
#	|-|	 |-|	------	  |--|  \--\    ------  |----------|  |-- |  \--\     |__|         #
#                                                                               		   #
####################################################################################################
#												   #
#                            ---FOOTPRINTING AUTOMATION---                                         #
#											           # 
#												   #
#												   #	
####################################################################################################
 		#             -developed by TM-Deadleaf               #                                
   		#	                                              #
	        #						      #
		#######################################################						      


"""
menu="""

      [+] \033[4mChoose An Option\033[0m
      _________________________________________________
     |                                                |
     |  [1] TCP Scan               		      |
     |  [2] UDP SCAN                                  |
     |  [3] Traceroute                                |
     |  [4] WHois lookup                              |
     |  [5] DNS Lookup                                |
     |  [6] Reverse dns lookup                        |
     |  [7] GEOip location                            |
     |  [8] HTTP headers                              |
     |	[9] Banner Grab                               |
     |                                                |
     +------------------------------------------------+                                            
     |  [N]:New Target             [X]:Exit           | 
     |                                                |
     +------------------------------------------------+

"""
print(banner)
def ping():
	global domain
	global IP
	domain = input("Enter Target Address [Example.com / IP]: ")
	try:	
		IP = socket.gethostbyname(domain)
	except socket.gaierror or requests.ConnectionError:
		print("\n\033[0;31m[*] Invalid Target Address\033[0m\n")
		ping()
	else:	
		response = os.system("ping -c 1 " + domain)
		if response == 0:
			print("\n\033[0;31m[-] Target is Live,Ready For Action\033[0m")
			print(menu)
		else:
			print("\n\033[0;31m[!] Oops!! Target is not Live\033[0m\n")
			ping()
def Exit():
	while True :
		cond = input("Are you sure (y/n) : ")
		if cond == str('y'or 'Y'):
			exit()	
		elif cond == str('n' or 'N'):
			os.system("clear")
			print(logo)
			ping()			
			option()
		else:
			print("\n\033[0;31m[!] Invalid Input\033[0m\n")

def option():
	opt=input("[+] Select An Option: ")
	if opt==str('e'or'E'):
		Exit()

	elif opt==str('n'or 'N'):
		ping()
		option()
	elif opt=='1':
		os.system("clear")
		os.system("curl https://api.hackertarget.com/nmap/?q="+domain)
		x=input("\n[+] press enter for menu:")
		print(menu)
		option()
	elif opt=='2':
		os.system("clear")
		os.system("curl https://api.hackertarget.com/udp-port-scan/?q="+domain)
		x=input("\n[+] press enter for menu:")
		print(menu)
		option()
	elif opt=='3':
		os.system("clear")
		os.system("curl https://api.hackertarget.com/mtr/?q="+domain)
		x=input("\n[+] press enter for menu:")
		print(menu)
		option()
	elif opt=='4':
		os.system("clear")
		os.system("curl https://api.hackertarget.com/whois/?q="+domain)	
		x=input("\n[+] press enter for menu:")
		print(menu)
		option()
	elif opt=='5':
		os.system("clear")
		os.system("curl https://api.hackertarget.com/dnslookup/?q="+domain)
		x=input("\n[+] press enter for menu:")
		print(menu)
		option()

	elif opt=='6':
		os.system("clear")
		os.system("curl https://api.hackertarget.com/reversedns/?q="+domain)
		x=input("\n[+] press enter for menu:")
		print(menu)
		option()
	elif opt=='7':
		os.system("clear")
		os.system("curl https://api.hackertarget.com/geoip/?q="+domain)
		x=input("\n[+] press enter for menu:")
		print(menu)
		option()
	elif opt=='8':
		os.system("clear")
		os.system("curl https://api.hackertarget.com/httpheaders/?q="+domain)
		x=input("\n[+] press enter for menu:")
		print(menu)
		option()
	elif opt=='9':
		os.system("clear")
		os.system("curl https://api.hackertarget.com/bannerlookup/?q="+domain)
	else:
		print("\033[0;31m[!] Invalid Input\033[0m")
		option()
if __name__ == "__main__":
	ping()	
	option()
	



		













































































