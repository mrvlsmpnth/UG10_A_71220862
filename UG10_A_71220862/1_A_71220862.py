a =input("Masukkan nama mahasiswa:")
b =input("Masukkan NIM-nya:")
c = int(b[2:4])
d = int(b[0:2])
if c == 20 or c== 22 or c==21 and d==71  :
    print(a,"Merupakan Mahasiswa Informatika angkatan 20 hingga 22")
else :
    print(a,"bukan mahasiswa informatika angkatan 20 hingga 22")