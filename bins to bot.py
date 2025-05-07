import random,requests,os;from user_agent import generate_user_agent;from requests import get


TOKEN = input('\x1b[1;31m   𝑇\x1b[1;32m 𝑂 \x1b[1;33m 𝐾 \x1b[1;34m 𝐸 \x1b[1;36m 𝑁 \x1b[1;35m ♕ : ')
ID = input('\n\x1b[1;31m   𝐼  \x1b[1;34m𝐷 \x1b[1;32m   : ')

god,bad=0,0

def cl(zh):
 api_url="https://bins.antipublic.cc/bins/"+zh

 response=requests.get(api_url)
 if response.status_code == 200:
  return 'ok'
 else:
  return 'bad'

def dato(zh):
 api_url = get("https://bins.antipublic.cc/bins/"+zh).json()
#ok
 #{'bin': '505194', 'brand': 'MAESTRO', 'country': 'US', 'country_name': 'UNITED STATES', 'country_flag': '🇺🇸', 'country_currencies': ['USD', 'USN', 'USS'], 'bank': None, 'level': None, 'type': 'DEBIT'}
 brand=api_url["brand"]
 card_type=api_url["type"]
 level=api_url["level"]
 bank=api_url["bank"]
 country_name=api_url["country_name"]
 country_flag=api_url["country_flag"]
 cp = f'''
⌯ 𝑵𝑬𝑾 𝑩𝑰𝑵 BOkachoda 🤣⌯ 
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
• ɪɴғᴏʀᴍᴀᴛɪᴏɴѕ ʙɪɴ 
⌯ ʙɪɴ : {zh}
⌯ ᴄᴏụɴᴛʀʏ : {country_name} {country_flag}
⌯ ɴᴇᴛᴡᴏʀᴋ : {level}
⌯ ʙʀᴀɴᴅ : {brand}
⌯ ᴛʏᴘᴇ : {card_type}

• ʙᴀɴᴋ 
⌯ ɴᴀᴍᴇ : {bank}
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
• Tlg : @soNGPY
'''
 requests.post(f'''https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ID}&text=''' + cp)
 return cp



def data(bini):
    try:
     head = {
        'appCodeName': 'Mozilla',
        'appName': 'Netscape',
        'appVersion': generate_user_agent(),
        'buildID': None,
        'oscpu': 'Intel Mac OS X 10_8_1',
        'platform': 'Macintosh; Intel Mac OS X 10_8_1',
        'product': 'Gecko',
        'productSub': '20030107',
        'userAgent': generate_user_agent(),
        'vendor': 'Google Inc.',
        'vendorSub': '' }
     k = requests.get('https://lookup.binlist.net/'+bini,headers=head)
     name = k.json()['country']['name']
     emoji = k.json()['country']['emoji']
     scheme = k.json()['scheme']
     type = k.json()['type']
     brand = k.json()['brand']
     bank_name = k.json()['bank']['name']
     txt_ruks = f'''
⌯ 𝑵𝑬𝑾 𝑩𝑰𝑵 𝑲𝑰𝑳𝑾𝑨 ⌯ 
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
• ɪɴғᴏʀᴍᴀᴛɪᴏɴѕ ʙɪɴ 
⌯ ʙɪɴ : {bini}
⌯ ᴄᴏụɴᴛʀʏ : {name} {emoji}
⌯ ɴᴇᴛᴡᴏʀᴋ : {scheme}
⌯ ʙʀᴀɴᴅ : {brand}
⌯ ᴛʏᴘᴇ : {type}

• ʙᴀɴᴋ 
⌯ ɴᴀᴍᴇ : {bank_name}
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
• Tlg : @sonGPY '''
     requests.post(f'''https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ID}&text=''' + txt_ruks)
     return txt_ruks
     
    except:
     return 'bad'
while True:
 gh='123456789'
 sc=['51','41','50','40']
 z="".join(random.choice(gh)for i in range(4))
 zh=random.choice(sc)+z
 bin=zh
 if 'ok' in str(cl(zh)):
    data(zh)
    if 'bad' in str(data(zh)):
     god+=1
     dato(zh)
    else:
     bad+=1
 else:
  bad+=1
 ki=f'''\033[1;36m•-•-•-•-•-•-•-•-•-•-•-•-
\033[1;36m¦\033[1;33m - \033[1;38;5;48m- ViP -  Tools BIN \033[1;36m    ¦
\033[1;36m•-•-•--•-•-•-•-•-•-•-
¦ \033[1;38;5;48m- Good BIN -> {god}            \033[1;36m    ¦
\033[1;36m•-•--•-•-•-•-•-•-•-•-
¦ \033[1;31m- Bad BIN -> {bad}   \033[1;36m              ¦
\033[1;36m•-•-•--•-•-•-•-•-•-•-
¦ - Check BIN -> \033[1;39m{zh}     \033[1;36m           ¦
\033[1;36m•-•-•-•--•-•-•-•-
\033[1;36m¦\033[1;33m - \033[1;38;5;48mProgrammer M O H -> @SONGPY    \033[1;36m   ¦-•-•-
\033[1;36m¦\033[1;33m - \033[1;38;5;48mTele admin  -> @SONGPY \033[1;36m ¦
\033[1;36m•-•'''
 os.system('clear')
 print(ki)