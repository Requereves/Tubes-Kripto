aset = []
portofolio = [] #Buat nyimpen koin user

saldo = 0
riwayat_trans = []

# CEK SALDO
def ceksaldo():
    print(f"Saldo Kamu sekarang adalah: Rp {saldo}")

# TOP UP SALDO DOMPET (fitur baru)
def topupsaldo(saldo_sekarang):
    print("\nTop Up Dompet")
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
    print("Daftar Coin/Aset di Market")

    if len(aset) == 0:
        print("Belum ada aset, tambah dulu di menu 7.")
    else:
        for i in range(len(aset)):
            print(f"{i+1}. {aset[i]['nama']} ({aset[i]['simbol']})")
            print(f" Harga: Rp {aset[i]['harga']}")
            print(f" Market Cap: {aset[i]['market']}")

# BUAT NYARI NAMA ASET PAKE SEQUENTIAL
def sequen_nama(cari_nama):
    for i in range(len(aset)):
        if aset[i]['nama'].lower() == cari_nama.lower():
            return i
    return -1 

# BUAT CARI ASET NYA SESUAI HARGA / MARKET CAP
def cariaset():
    print("\nCek aset kripto")
    print("1. Harga")
    print("2. Market Cap")
    print("3. Nama Aset")
    pilihan = input("Cek mana? ")

    if pilihan == '1':
        select_harga()
        cekaset()
    elif pilihan == '2':
        market_cap()
        cekaset()
    elif pilihan == '3':
        nama = input("Masukkan nama yang yang mau dicari: ")
        hasil = sequen_nama(nama)

        if hasil != -1:
            print("\nASETNYA")
            print(f"Nama    :{aset[hasil]['nama']}")
            print(f"Simbol  :{aset[hasil]['simbol']}") 
            print(f"Harga   :Rp {aset[hasil]['harga']}") 
            print(f"Market  :{aset[hasil]['market']}") 
        else:
            print("Aset tidak ditemukan")
    else:
        print("Pilihan tidak ada")
        return

# LOGIKA BUAT CARI ASET HARGA PAKE SELECTION SORT
def select_harga():
    n = len(aset)

    for i in range(n):
        idx = i

        for j in range(i + 1, n):
            if aset[j]['harga'] > aset[idx]['harga']:
                idx = j
        aset[i], aset[idx] = aset[idx], aset[i]

    print("\nData diurutkan berdasarkan harga Tertinggi")

# LOGIKA BUAT CARI MARKET CAP PAKE INSERTION SORT
def market_cap():
    for i in range(1, len(aset)):
        k = aset[i]
        j = i - 1
        # ngurutin dari Market Cap terbesar ke terkecil
        while j >= 0 and aset[j]['market'] < k['market']:
            aset[j + 1] = aset[j]
            j -= 1
        aset[j + 1] = k
    
    print("\nData diurutkan berdasarkan Market Cap Tertinggi")

def jualaset():
    print("Jual aset (belum dibikin)")

# FITUR BELI ASET (fitur baru)
def beliaset(saldo_sekarang):
    print("\nBeli Aset Kripto")
    if len(aset) == 0:
        print("Belum ada koin di market. Tambah aset dulu dari menu 7.")
        return saldo_sekarang
        
    cekaset()
    nama_beli = input("\nMasukkan nama koin yang mau dibeli: ")
    hasil = sequen_nama(nama_beli)
    
    if hasil != -1:
        harga_koin = aset[hasil]['harga']
        print(f"Harga 1 keping {aset[hasil]['nama']}: Rp {harga_koin}")
        jumlah = int(input("Mau beli berapa keping? "))
        
        total_bayar = harga_koin * jumlah
        
        # Cek saldony cukup/ga buat beli
        if saldo_sekarang >= total_bayar:
            saldo_sekarang -= total_bayar
            print(f"Sip! Kamu berhasil beli {jumlah} {aset[hasil]['simbol']} seharga Rp {total_bayar}.")
            print(f"Sisa saldo sekarang: Rp {saldo_sekarang}")
            
            # Catet transaksinya
            riwayat_trans.append(f"Beli Aset: {jumlah} {aset[hasil]['nama']} (-Rp {total_bayar})")
            
            # Masukin koinnya ke portofolio user
            sudah_punya = False
            for p in portofolio:
                if p['nama'].lower() == aset[hasil]['nama'].lower():
                    p['jumlah'] += jumlah
                    sudah_punya = True
                    break
            
            # bikin data baru di portofolio kalo belum punya
            if not sudah_punya:
                portofolio.append({
                    "nama": aset[hasil]['nama'],
                    "simbol": aset[hasil]['simbol'],
                    "jumlah": jumlah
                })
        else:
            print(f"saldonya ga cukup oi. Total belanjanya Rp {total_bayar}, saldo kamu cuma Rp {saldo_sekarang}.")
    else:
        print("Koin ga ketemu, pastikan namanya sesuai yang ada di daftar ya.")
        
    return saldo_sekarang

def tambahaset():
    nama = input("Masukkan Nama Aset: ")
    simbol = input("Masukkan Simbol Aset: ")
    harga = int(input("Masukkan Harga Aset: "))
    if harga < 0:
        print("Harga ga bs dibawah 0")
    market = int(input("Masukkan Harga Market: "))
    if market < 0:
        print("Harga market ga bisa dibawah 0")

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
        # Nampilin portofolio koin yang udah dibeli user
        if len(portofolio) > 0:
            print("Koin yang kamu punya:")
            for p in portofolio:
                print(f"- {p['jumlah']} keping {p['nama']} ({p['simbol']})")
    elif pil == 2:
        saldo = topupsaldo(saldo)
    elif pil == 3:
        cekaset()
    elif pil == 4:
        jualaset()
    elif pil == 5:
        saldo = beliaset(saldo)
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
