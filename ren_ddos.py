import os
import time
from colorama import Fore, Back, Style

def tampilkan_menu():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
    print(Fore.CYAN + "="*40)
    print(Fore.GREEN + "   === MENU KEREN DDOS ===")
    print(Fore.CYAN + "="*40)
    print(Fore.YELLOW + "1. " + Fore.MAGENTA + "DDOS_V1")
    print(Fore.YELLOW + "2. " + Fore.MAGENTA + "DDOS_V2")
    print(Fore.YELLOW + "3. " + Fore.MAGENTA + "DDOS_V3")
    print(Fore.YELLOW + "4. " + Fore.MAGENTA + "DDOS_V2 (Shell Script)")
    print(Fore.RED + "5. " + Fore.WHITE + "Keluar")
    print(Fore.CYAN + "="*40)

def efek_loading():
    loading = ["[     ]", "[=    ]", "[==   ]", "[===  ]", "[==== ]", "[=====]"]
    for i in loading:
        print(Fore.WHITE + i, end="\r")
        time.sleep(0.2)

def pilih_menu():
    while True:
        tampilkan_menu()
        pilihan = input(Fore.GREEN + "Pilih menu (1/2/3/4/5): ")

        if pilihan == '1':
            print(Fore.YELLOW + "Memulai DDOS_V1...")
            efek_loading()
            os.system("python ddosv1_op.py")
        elif pilihan == '2':
            print(Fore.YELLOW + "Memulai DDOS_V2...")
            efek_loading()
            os.system("python ddosv2_op.py")
        elif pilihan == '3':
            print(Fore.YELLOW + "Memulai DDOS_V3...")
            efek_loading()
            os.system("python ddosv3_op.py")
        elif pilihan == '4':
            print(Fore.YELLOW + "Memulai DDOS_V2 (Shell Script)...")
            efek_loading()
            os.system("bash test.sh")
        elif pilihan == '5':
            print(Fore.RED + "Keluar dari program...")
            time.sleep(1)
            break
        else:
            print(Fore.RED + "Pilihan tidak valid, coba lagi.")
            time.sleep(1)

if __name__ == "__main__":
    pilih_menu()
