# Victor Anindia
# 71180324
# Universitas Kristen Duta Wacana

# Soal Struktur Kontrol Percabangan

# KulMa.com adalah sebuah website e-commerce yang khusus menjual buah kurma ke seluruh penjuru Indonesia. Saat ini KulMa sedang memberikan promosi dan diskon ongkos kirim bagi para pembeli yang memenuhi kriteria sebagai berikut:
# Gratis ongkir untuk pengiriman ke Jawa dan Bali dengan minimal pembelian 3 pack kurma. 
# Gratis ongkir untuk pengiriman ke Kalimantan dan Sumatera dengan minimal pembelian 6 pack kurma.
# Untuk pulau lainnya, gratis ongkir diberikan apabila melakukan pembelian minimal 10 pack kurma.
# Selain itu, KulMa juga akan memberikan potongan harga untuk pembelian pack di atas 5 buah yaitu sebesar 8% dari harga aslinya yaitu Rp. 40.000

# Input
    # pulau mana?
    # berapa pack?
# Process
    # if pulau tujuan == (jawa || bali):
        # if pack >= 3:
            # Gratis ongkir
    # elif pulau tujuan == (kalimantan || sumatera):
        # if pack >= 6:
            # Gratis ongkir
    # else:
        # if pack >= 10:
            # Gratis ongkir
    # if pack > 5:
        # Diskon 8%
# Output
    #  print -> pembelian x pack kurma ke pulau y akan dikenai biaya Rp. z saja
    #  print -> pembelian x pack kurma ke pulau y akan dikenai biaya Rp. z + ongkir

#Source code program
# Input
pulau = input("Pulau tujuan: ")
pack = int(input("Beli berapa pack? "))

# Proses
ongkir = False
total = 0
if pulau == "jawa" or pulau == "bali":
    if pack >= 3:
        ongkir = True
elif pulau == "kalimantan" or pulau == "sumatera":
    if pack >= 6:
        ongkir = True
else:
    if pack >= 10:
        ongkir = True
if pack > 5:
    total = pack*40000-(0.08*(pack*40000))   
else:
    total = pack*40000     
# Output 
if ongkir:
    print("Pembelian %d pack kurma ke pulau %s akan dikenai biaya Rp. %d saja" % (pack, pulau, total))
else:
    print("Pembelian %d pack kurma ke pulau %s akan dikenai biaya Rp. %d + ongkir" % (pack, pulau, total))  

