aset = []

saldo = 0
riwayat_trans = []
dompet = {} #variabel dompet buat nyimpen aset user

#Fitur baru cek saldo 
def cek_saldo():
    global saldo
    print(f"\nSaldo Rupiah Kamu sekarang adalah: Rp {saldo}")
    print("Aset Kripto di Dompet:")
    if len(dompet) == 0:
        print(" - Belum ada aset di dompet")
    else:
        for sim, jum in dompet.items():
            print(f" - {sim} : {jum} koin")

    #Fitur Baru Tambah Saldo 
    print("\nOpsi Dompet:")
    print("1. Top Up / Deposit Saldo Rupiah")
    print("2. Kembali ke Menu Utama")
    opsi = input("Pilih (1/2): ")

    if opsi == '1':
        tambah_saldo = float(input("Masukkan nominal Deposit: Rp "))
        if tambah_saldo <= 0:
            print("Nominal deposit harus lebih dari 0!")
        else:
            saldo += tambah_saldo
            riwayat_trans.append(f"DEPOSIT: Saldo masuk Rp {tambah_saldo}")
            print(f"Deposit berhasil! Saldo kamu sekarang menjadi: Rp {saldo}")
    elif opsi == '2':
        return
    else:
        print("Pilihan tidak ada.")

#Cek aset yang ada di market
def cek_aset():
    print("\nDaftar Coin/Aset")
    if len(aset) == 0:
        print("Belum ada aset.")
        return

    for i in range(len(aset)):
        print(f"{i+1}. {aset[i]['nama']} ({aset[i]['simbol']})")
        print(f"   Harga: {aset[i]['harga']}")
        print(f"   Market Cap: {aset[i]['market']}")

#Nyari nama aset pake sequential search
def sequen_nama(cari_nama):
    for i in range(len(aset)):
        if aset[i]['nama'].lower() == cari_nama.lower() or aset[i]['simbol'].lower() == cari_nama.lower():
            return i
    return -1 

#Buat cari aset berdasarkan harga/mcap/nama
def cari_aset():
    print("\nCek aset kripto")
    print("1. Harga")
    print("2. Market Cap")
    print("3. Nama Aset")
    pilihan = input("Cek mana? ")

    if pilihan == '1':
        select_harga()
    elif pilihan == '2':
        market_cap()
    elif pilihan == '3':
        nama = input("Masukkan nama yang mau dicari: ")
        hasil = sequen_nama(nama)

        if hasil != -1:
            print("\nASET DITEMUKAN")
            print(f"Nama    : {aset[hasil]['nama']}")
            print(f"Simbol  : {aset[hasil]['simbol']}") 
            print(f"Harga   : {aset[hasil]['harga']}") 
            print(f"Market  : {aset[hasil]['market']}") 
        else:
            print("Aset tidak ditemukan.")
    else:
        print("Pilihan tidak ada")
        return

    #tampilin list urutan kalo user memilih 1 atau 2
    if pilihan in ['1', '2']:
        cek_aset()

#Logika harga pake selection sort
def select_harga():
    n = len(aset)
    for i in range(n):
        idx = i
        for j in range(i + 1, n):
            if aset[j]['harga'] > aset[idx]['harga']:
                idx = j
        aset[i], aset[idx] = aset[idx], aset[i]

    print("Data diurutkan berdasarkan harga Tertinggi")

#Logika mcap pake insertion sort
def market_cap():
    for i in range(1, len(aset)):
        key = aset[i]
        j = i - 1
        #ngurutin dari Market Cap terbesar ke terkecil
        while j >= 0 and aset[j]['market'] < key['market']:
            aset[j + 1] = aset[j]
            j -= 1
        aset[j + 1] = key
        
    print("Data diurutkan berdasarkan Market Cap Tertinggi") #insertion sort

#Fitur baru jual aset kripto (bisa jual koin cuyy)
def jual_aset():
    global saldo
    if len(dompet) == 0:
        print("Dompet kosong, tidak ada aset yang bisa dijual.")
        return

    cek_saldo()
    keyword = input("\nMasukkan Nama/Simbol koin yang mau dijual: ")
    idx = sequen_nama(keyword)

    if idx == -1:
        print("Koin tersebut sudah tidak ada di market!")
        return

    koin = aset[idx]
    simbol = koin['simbol']

    #Cek apakah simbol ini ada di dompet user
    punya_koin = False
    for s in dompet.keys():
        if s.lower() == simbol.lower():
            simbol = s # Samakan kapitalisasi huruf dengan yang ada di dompet
            punya_koin = True
            break
            
    if not punya_koin:
        print("Kamu ga punya koin itu di dompet!")
        return

    harga_sekarang = koin['harga']
    jumlah_dimiliki = dompet[simbol]

    print(f"Harga {simbol} saat ini: {harga_sekarang}")
    print(f"Jumlah koin Anda: {jumlah_dimiliki}")

    jumlah_jual = float(input("Masukkan jumlah koin yang mau dijual: "))

    if jumlah_jual <= 0 or jumlah_jual > jumlah_dimiliki:
        print("Jumlah jual ga valid atau koin kamu ga cukup!")
    else:
        total_dapat = jumlah_jual * harga_sekarang
        saldo += total_dapat
        dompet[simbol] -= jumlah_jual

        if dompet[simbol] == 0:
            del dompet[simbol]

        riwayat_trans.append(f"JUAL: {jumlah_jual} {simbol} (Dapat Rp {total_dapat})")
        print(f"Berhasil menjual! Saldo bertambah Rp {total_dapat}")

#Fitur baru beli aset kripto (bisa beli koin cuyy)
def beli_aset():
    global saldo
    if len(aset) == 0:
        print("Portofolio masih kosong. Silakan tambah aset terlebih dahulu.")
        return

    cek_aset()
    keyword = input("\nMasukkan Nama atau Simbol koin yang mau dibeli: ")
    idx = sequen_nama(keyword)

    if idx == -1:
        print("Koin tidak ditemukan di market")
        return

    koin = aset[idx]
    print(f"\nKamu memilih: {koin['nama']} ({koin['simbol']})")
    print(f"Harga saat ini: {koin['harga']}")
    print(f"Saldo Kamu: {saldo}")

    print("\nOpsi Pembelian:")
    print("1. Beli berdasarkan jumlah koin")
    print("2. Beli berdasarkan Budget")
    opsi = input("Pilih (1/2): ")
    

    if opsi == '1':
        jumlah = float(input("Masukkan jumlah koin yang mau dibeli: "))
        total_harga = jumlah * koin['harga']
    elif opsi == '2':
        total_harga = float(input("Masukkan nominal Rupiah untuk membeli: "))
        jumlah = total_harga / koin['harga']
    else:
        print("Pilihan tidak ada.")
        return
    

    if total_harga > saldo:
        print(f"Saldo tidak cukup! Kamu butuh {total_harga}")
    elif jumlah <= 0:
        print("Jumlah beli ga valid!")
    else:
        saldo -= total_harga
        simbol = koin['simbol']
        
        
        if simbol in dompet:
            dompet[simbol] += jumlah
        else:
            dompet[simbol] = jumlah
            
            
        riwayat_trans.append(f"BELI: {jumlah} {simbol} (Biaya Rp {total_harga})")
        print(f"Berhasil membeli {jumlah} {simbol}!")

#Tambah aset baru ke market
def tambah_aset():
    nama = input("Masukkan Nama Aset: ")
    simbol = input("Masukkan Simbol Aset: ")
    harga = int(input("Masukkan Harga Aset: "))
    market = int(input("Masukkan Market Cap: "))

    data_baru = {
        "nama": nama,
        "simbol": simbol,
        "harga": harga,
        "market": market
    }
    

    aset.append(data_baru)
    print("Aset baru berhasil ditambahkan")

#Fitur baru riwayat transaksi
def riwayat():
    if len(riwayat_trans) == 0:
        print("Ga ada riwayat transaksi")
    else: 
        print("\n--- RIWAYAT TRANSAKSI ---")
        for i in riwayat_trans:
            print(i)
            

#Main menu
while True:
    print("\n========================")
    print("MENU UTAMA")
    print("1. Cek Saldo & Dompet") 
    print("2. Cek market")
    print("3. Jual Aset Kripto")
    print("4. Beli Kripto")
    print("5. Cek Riwayat")
    print("6. Tambah Aset")
    print("7. Cari/Urutkan Aset")
    print("8. Keluar")
    print("========================")
    print()

    pil = int(input("Pilih no berapa: "))

    if pil == 1:
        cek_saldo()
    elif pil == 2:
        cek_aset()
    elif pil == 3:
        jual_aset()
    elif pil == 4:
        beli_aset()
    elif pil == 5:
        riwayat()
    elif pil == 6:
        tambah_aset()
    elif pil == 7:
        cari_aset()
    elif pil == 8:
        print("BYEE")
        break
    else:
        print("Pilihan tidak ada")

    input("\nTeken Enter buat balik ke menu")