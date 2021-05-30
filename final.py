def eserKaydet():
    print("Kayıt Ekleme Sistemine Hoş Geldiniz...")
    f = open('final.txt','a')
    eserAdi = input('Eser Adını Giriniz.')
    eserYazar = input("Eserin Yazarını Giriniz.")
    eserYayınevi = input("Eserin Yayınevi Bilgisini Giriniz.")
    eserBasımtarihi = input("Eserin Basım Tarihini Yıl Olarak Giriniz. ")
    eserIsbn = input("Eserin ISBN Bilgilerini Giriniz.")

    f.write(eserAdi +','+ eserYazar +','+ eserYayınevi +','+ eserBasımtarihi +','+ eserIsbn + "\n")
    f.close()

def eserListe():
    infile = open('final.txt' , 'r')
    for line in infile.readlines():
        print(line)
        infile.close()


islemSec = ["ekle" , "listele" , "çıkış"]
while islemSec:
    girilen = input("Lütfen Eser eklemek için 'ekle' , Eser listelemek için 'listele' , Çıkmak için ise 'çıkış' yazınız \n")
    if girilen == islemSec[0]:
        eserKaydet()
    elif girilen == islemSec[1]:
        eserListe()
    elif girilen == islemSec[2]:
        break

