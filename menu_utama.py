import os,time
from colorama import Fore,Back,Style
def tampilkan_menu():A='=';os.system('cls'if os.name=='nt'else'clear');print(Fore.CYAN+A*40);print(Fore.GREEN+'   === MENU REN9999 DDOS ===');print(Fore.CYAN+A*40);print(Fore.YELLOW+'1. '+Fore.MAGENTA+'DDOS_V1');print(Fore.YELLOW+'2. '+Fore.MAGENTA+'DDOS_V2');print(Fore.YELLOW+'3. '+Fore.MAGENTA+'DDOS_V3');print(Fore.YELLOW+'4. '+Fore.MAGENTA+'DDOS_V2 (Shell Script)');print(Fore.RED+'5. '+Fore.WHITE+'Keluar');print(Fore.CYAN+A*40)
def efek_loading():
	A=['[     ]','[=    ]','[==   ]','[===  ]','[==== ]','[===== ]','[======  ]','[======= ]','[========]']
	for B in A:print(Fore.WHITE+B,end='\r');time.sleep(.2)
def pilih_menu():
	while True:
		tampilkan_menu();A=input(Fore.GREEN+'Pilih menu (1/2/3/4/5): ')
		if A=='1':print(Fore.YELLOW+'Memulai DDOS_V1...');efek_loading();os.system('python ddosv1_op.py')
		elif A=='2':print(Fore.YELLOW+'Memulai DDOS_V2...');efek_loading();os.system('python ddosv2_op.py')
		elif A=='3':print(Fore.YELLOW+'Memulai DDOS_V3...');efek_loading();os.system('python ddosv3_op.py')
		elif A=='4':print(Fore.YELLOW+'Memulai test...');efek_loading();os.system('bash test.sh')
		elif A=='5':print(Fore.RED+'Keluar dari program...');time.sleep(1);break
		else:print(Fore.RED+'Pilihan tidak valid, coba lagi.');time.sleep(1)
if __name__=='__main__':pilih_menu()
