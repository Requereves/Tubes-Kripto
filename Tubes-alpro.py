

aset = []

saldo = 100000
riwayat_trans = []

# CEK SALDO
def ceksaldo():
    print(f"Saldo Kamu sekarang adalah: {saldo}")

# TOP UP SALDO DOMPET (fitur baru)
def topupsaldo(saldo_sekarang):
    print("Top Up Dompet")
    nominal = int(input("Mau top up saldo berapa? Rp "))
    
    if nominal > 0:
        saldo_sekarang += nominal
        print(f"Top up Rp {nominal} berhasil.")
        print(f"Saldo kamu sekarang: Rp {saldo_sekarang}")
        riwayat_trans.append(f"Top Up Saldo: +Rp {nominal}")
    else:
        print("Nominalnya ga valid, masukin angka yang bener ya.")
        
    return saldo_sekarang

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
            print(f"Harga   :{aset[hasil]['harga']}") 
            print(f"market  :{aset[hasil]['market']}") 
        else:
            print("Aset tidak ditemukan")
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
    for i in range(1, len(aset)):
        k = aset[i]
        j = i - 1
        #ngurutin dari Market Cap terbesar ke terkecil
        while j >= 0 and aset[j]['market'] < k['market']:
            aset[j + 1] = aset[j]
            j -= 1
        aset[j + 1] = k

def jualaset():
    print("Jual aset (belum dibikin)")

def beliaset():
    print("Beli Aset (belum dibikin)")

def tambahaset():
    nama = input("Masukkan Nama Aset: ")
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
        print("Belum ada transaksi nih.")
    else:
        for i in riwayat_trans:
            print(i)

while True:
    print("")
    print("========================")
    print("MENU UTAMA")
    print("1. Cek Saldo")
    print("2. Top Up Saldo")
    print("3. Cek Aset")
    print("4. Jual Aset Kripto")
    print("5. Beli Kripto")
    print("6. Cek Riwayat")
    print("7. Tambah Aset")
    print("8. Cari Aset")
    print("9. Keluar")
    print("========================")
    print()

    pil = int(input("Pilih no berapa: "))

    if pil == 1:
        ceksaldo()
    elif pil == 2:
        saldo = topupsaldo(saldo)
    elif pil == 3:
        cekaset()
    elif pil == 4:
        jualaset()
    elif pil == 5:
        beliaset()
    elif pil == 6:
        riwayat()
    elif pil == 7:
        tambahaset()
    elif pil == 8:
        cariaset()
    elif pil == 9:
        print("BYEE")
        break
    else:
        print("Pilihan tidak ada")

