# Victor Anindia
# 71180324
# Universitas Kristen Duta Wacana

# Soal String
# Abhay merasakan kesulitan jika harus berurusan dengan angka terutama jika angka tersebut mewakili uang dalam bentuk USD. Sebagai teman yang baik, bantulah Abhay agar setiap kalimat yang dia lihat mengandung uang dalam bentuk USD dapat dikonversi ke dalam bentuk rupiah.

# Input
    # String -> Adam membeli sebuah mouse gaming seharga $56.33 dan sebuah RAM seharga $20
# Process
    # tempList = inputan.split(' ')
    # temp = ""
    # for kata in tempList:
    #   if kata[0]=='$':
    #       nilai = float(kata[1:])
    #       hasil = nilai * 14000
    #       uang = "Rp. "+str(hasil)
    #       temp+=uang
    #   else:
    #      temp+=kata
    #   temp+=" "  
    #  
# Output
    # print(temp)
    # String -> Adam membeli sebuah mouse gaming seharga Rp. xx dan sebuah RAM seharga Rp. xy

#Source code program
# Input
inputUser = input("Masukkan kalimat yang ingin diubah: ")
# Proses
tempList = inputUser.split(' ')
temp = ""
for kata in tempList:
    if kata[0]=='$':
        nilai = float(kata[1:])
        hasil = nilai * 14000
        uang = "Rp. "+str(hasil)
        temp+=uang
    else:
        temp+=kata
    temp+=" "  
# Output
print(temp)
