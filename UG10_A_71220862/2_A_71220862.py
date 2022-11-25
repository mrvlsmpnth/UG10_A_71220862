print ("==== Selamat datang di Toko Andi Tersenyum, selamat belanja ====")

x = int(input( "Total belanja :Rp. "))
y = a-a*2/100
z = a-a*5/100
d = a-(a*10/100)

if x >= 1000000 :
    print (" Biaya yang harus dibayar setelah diskon adalah : ", d)
elif x >= 500000 :
    print (" Biaya yang harus dibayar setelah diskon adalah : ", z)
elif x >= 100000 :
    print (" Biaya yang harus dibayar setelah diskon adalah : ", y)
else :
    print (" Tidak ada diskon ! Maka yang anda bayarkan adalah : ", x)