# Victor Anindia
# 71180324
# Universitas Kristen Duta Wacana

# Soal Struktur Kontrol Perulangan

# Milea mendapat tugas dari gurunya untuk menuliskan barisan bilangan prima pada suatu interval. Sebagai teman yang baik, kamu akhirnya memutuskan untuk membuatkan program sesuai dengan kebutuhannya tersebut.


# Input
    # Interval = awal, akhir
    # awal = inputan user (int)
    # akhir = inputan user (int)
    # awal = 5
    # akhir = 15

# Process
    # for int i = awal, i<akhir+1, i++:
    #   if i > 1:
    #       for int j = 2, j<i,j++:
    #           if i % j == 0:
    #               break -> terdapat faktor lain selain bilangan 1 dan bilangan itu sendiri
    #       else:
    #           print(i)
    #   else:
    #       diemin
# Output
    # print -> 5, 7, 11, 13

#Source code program
# Input
print("Bilangan prima pada suatu interval")
awal = int(input("Masukkan angka awal dari interval: "))
akhir = int(input("Masukkan angka akhir dari interval: "))

# Proses
print("Bilangan prima pada interval %d hingga %d adalah " %(awal, akhir))
for i in range(awal, akhir+1):
    if i > 1:
        for j in range(2, i):
            if (i%j)==0:
                break
        else:
            print(i)
# Output
