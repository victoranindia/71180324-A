# Victor Anindia
# 71180324
# Universitas Kristen Duta Wacana

# Soal Modular Programming

# Dilan berencana pergi liburan bersama Milea pada akhir pekan ini. Namun Dilan masih kebingungan tentang konversi mata uang yang akan digunakan. Bantulah Dilan agar dapat mengkonversi mata uang dari IDR ke USD, IDR ke JPY, dan juga IDR ke SGD. (Kurs USD 14.000, JPY 133, SGD 10.750)

# Input
    # Mau konversi ke mana? USD, JPY, SGD
    # (float) angka rupiah yang ingin dikonversi -> rupiah

# Process
    # hasil = 0

    # def convert(idr, rate):
        # return idr/rate

    # if matauang=='usd':
    #   nama = "USD"
    #   hasil = convert(rupiah, 14000)
    # elif matauang=='jpy':
    #   nama = "JPY"
    #   hasil = convert(rupiah, 133)
    # else:
    #   nama = "SGD"
    #   hasil = convert(rupiah, 10750)

# Output
# print("Uang Dilan sebesar Rp. %f jika dikonversi ke dalam %s menjadi %f" %(rupiah, nama, hasil))


#Source code program
# Input
print("Konversi Rupiah ke USD/JPY/SGD")
print("1. IDR/USD")
print("2. IDR/JPY")
print("3. IDR/SGD")
pil = input("Masukkan pilihan (USD/JPY/SGD)")
rupiah = float(input("Masukkan uang dalam rupiah: "))

# Proses
hasil = 0

def convert(idr, rate):
    return idr/rate

if pil.upper()=='USD':
    hasil = convert(rupiah,14000)
elif pil.upper()=='JPY':
    hasil = convert(rupiah,133)
else:
    hasil = convert(rupiah,10750)

# Output
print("Uang Dilan sebesar Rp. %f jika dikonversi ke dalam %s menjadi %f" %(rupiah, pil.upper(), hasil))