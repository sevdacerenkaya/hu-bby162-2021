file = open("Adres.txt" ,"w")
file.write("Isim\n")
file.write("Soyisim\n")
file.write("E-posta\n")


file = open("Adres.txt" ,"r")
veri = file.read()
print(veri)