aset = []

saldo = 100000
riwayat_trans = []

# CEK SALDO
def ceksaldo():
    print(f"Saldo Kamu sekarang adalah: {saldo}")

# CEK ASET / LIST ASET YANG ADA
def cekaset():
    print("")
    print("Daftar Coin/Aset")

    for i in range(len(aset)):
        print(f"{i+1}. {aset[i]['nama']} ({aset[i]['simbol']})")
        print(f" Harga: {aset[i]['harga']}")
        print(f" Market Cap: {aset[i]['market']}")


# BUAT NYARI NAMA ASET PAKE SEQUENTIAL
def sequen_nama(cari_nama):
    for i in range(len(aset)):
        if aset[i]['nama'].lower() == cari_nama.lower():
            return i
    return -1 

# BUAT CARI ASET NYA SESUAI HARGA / MARKET CAP
def cariaset():
    print("Cek aset kripto")
    print("1. Harga")
    print("2. Market Cap")
    print("3. Nama Aset")
    pilihan = input("Cek mana? ")

    if pilihan == '1':
        select_harga()
    elif pilihan == '2':
        market_cap()
    elif pilihan == '3':
        nama = input("Masukkan nama yang yang mau dicari: ")
        hasil = sequen_nama(nama)

        if hasil != -1:
            print("ASETNYA")
            print(f"Nama    :{aset[hasil]['nama']}")
            print(f"Simbol  :{aset[hasil]['simbol']}") 
            print(f"Harga  :{aset[hasil]['harga']}") 
            print(f"market  :{aset[hasil]['market']}") 
    else:
        print("Pilihan tidak ada")
        return

    
    cekaset()



# LOGIKA BUAT CARI ASET HARGA PAKE SELECTION SORT
def select_harga():
    n = len(aset)

    for i in range(n):
        idx = i

        for j in range(i + 1, n):
            if aset[j]['harga'] > aset[idx]['harga']:
                idx = j
        aset[i], aset[idx] = aset[idx], aset[i]

    print("Data diurutkan berdasarkan harga Tertinggi")



def market_cap():
    print("ini buat cek market cap pake insertion")

def jualaset():
    print("Jual aset")

def beliaset():
    print("Beli Aset")

def tambahaset():
    nama = input("Masukkan Nma Aset: ")
    simbol = input("Masukkan Simbol Aset: ")
    harga = int(input("Masukkan Harga Aset: "))
    market = int(input("Masukkan Harga Market: "))

    data_baru = {
        "nama": nama,
        "simbol": simbol,
        "harga": harga,
        "market": market
    }

    aset.append(data_baru)
    print("Aset baru berhasil ditambahkan")

def riwayat():
    if len(riwayat_trans) == 0:
        print("ga ada aset")
        for i in riwayat_trans:
            print(i)

while True:
    print("")
    print("========================")
    print("MENU UTAMA")
    print("1.Cek Saldo")
    print("2.Cek Aset")
    print("3.Jual Aset Kripto")
    print("4.Beli Kripto")
    print("5.Cek Riwayat")
    print("6.Tambah Aset")
    print("7.Cari Aset")
    print("8.Keluar")
    print("========================")
    print()

    pil = int(input("Pilih no berapa: "))

    if pil == 1:
        ceksaldo()
    elif pil == 2:
        cekaset()
    elif pil == 3:
        jualaset()
    elif pil == 4:
        beliaset()
    elif pil == 5:
        riwayat()
    elif pil == 6:
        tambahaset()
    elif pil == 7:
        cariaset()
    elif pil == 8:
        print("BYEE")
        break
    else:
        print("Pilihan tidak ada")