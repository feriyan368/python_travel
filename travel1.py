travel = ['Bus Besar', 'Bus Sedang', 'Travel']
tujuan = ['Bali', 'Jogja', 'Banyuwangi']
lama = [7, 10, 14]

while True:
    #index kendaraan
    print('==== Paket Wisata Promo ====')
    for i in range(0, len(travel)):
        print(f'{i+1}.{travel[i]}')
    pilihan = int(input('Silahkan Pilih Transportasi : '))
    print('==== Tujuan ====')
    #index tujuan
    for k in range(0, len(tujuan)):   
        print(f'{k+1}.{tujuan[k]}')
    tuju = int(input('Silahkan Pilih Tujuan : '))
    # Index lama
    print('==== Lama ====')
    for l in range(0, len(lama)):
        print(f'{l+1}.{lama[l]} Hari')
    lam = int(input('Silahkan Pilih Lama : '))
    print('====================')
    print(f'Transport : {travel[pilihan-1]}')
    print(f'Tujuan : {tujuan[tuju-1]}')
    print(f'Selama : {lama[lam-1]} Hari')
    print('Selamat Jalan')
    print('====================')
    lanjut = input('Apakah Mau Beli Paket Wisata Lagi y/n d')
    if lanjut == 'y' or lanjut == 'Y':
        continue
    else:
        break
