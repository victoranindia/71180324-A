# Victor Anindia
# 71180324
# Universitas Kristen Duta Wacana

# Soal

# Abhay adalah pemain baru di game travian. Dia kesusahan karena satuan waktu yang digunakan pada game tersebut adalah second (detik). Bantulah Abhay untuk membuat program yang dapat mengkonversi satuan detik pada game tersebut menjadi satuan hari, jam, menit, dan detik. Supaya Abhay dapat tahu kapan serangan musuh akan datang.

# Input
# Inputannya adalah detik (int)
# inputan = 1443201 detik
# Process
    # 1 hari = 86400 detik
    # 1 jam = 3600 detik
    # 1 menit = 60 detik
    # 1 detik = 1 detik
    # Hari = inputan // 86400
    # inputan = inputan % 86400
    # Jam = inputan // 3600
    # inputan = inputan % 3600
    # Menit = inputan // 60
    # inputan = inputan % 60
    # Detik = inputan // 1
# Output
    # print -> serangan musuh akan datang dalam x hari, y jam, z menit, a detik
     
#Source code program
# Input
waktu = int(input("Masukkan detik yang ingin dikonversi: "))

# Proses
hari = waktu // 86400
waktu = waktu % 86400
jam = waktu // 3600
waktu = waktu % 3600
menit = waktu // 60
waktu = waktu % 60
detik = waktu

# Output 
print("Serangan musuh akan datang dalam %d hari, %d jam, %d menit, %d detik lagi..." % (hari, jam, menit, detik))
  

