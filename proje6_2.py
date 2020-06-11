import random
import time
class Bilgisayar():
    def __init__(self,b_ses=50,b_durum="Kapalı",b_uyglar=["Masaüstü","Hesap Makinesi","Sayı Tahmin Oyunu"],b_uyg="Masaüstü",b_sifre="12345"):
        self.b_ses = b_ses
        self.b_durum = b_durum
        self.b_uyglar = b_uyglar
        self.b_sifre = b_sifre
        self.b_uyg = b_uyg
    def bilgisayar_ac(self,sifre):          
        if sifre == self.b_sifre:
            print("Bilgisayar Açılıyor...")
            time.sleep(3)
            self.b_durum = "Açık"
            print("Bilgisayara hoşgeldiniz...")
        else :
            print("Şifreniz yanlış lütfen doğru giriniz.")
    def bilgisayar_kapat(self):
        print("Bilgisayar Kapatılıyor...")
        time.sleep(3)
        self.b_durum = "Kapalı"
        print("Bilgisayar Kapandı.")
    def uygulama_degistir(self):
        print("Mevcut uygulamalar: {}".format(self.b_uyglar))
        print("Seçili uygulama: {}".format(self.b_uyg))
        sayi = int(input("Lütfen uygulama seçiniz (Örneğin Masaüstü'ne gitmek için 1'i tıklayınız."))
        self.b_uyg = self.b_uyglar[sayi-1]
        print("Mevcut uygulama: {}".format(self.b_uyg))
    def uygulama_ekle(self,uyg_ismi):
        print("{} uygulaması indiriliyor".format(uyg_ismi))
        time.sleep(3)
        self.b_uyglar.append(uyg_ismi)
        print("{} uygulaması başarıyla bilgisayara yüklendi.".format(uyg_ismi))
    def ses_ayar(self):
        i = 0
        while True:
            if i == 0 :
                print("Mevcut Ses Düzeyi : {}".format(self.b_ses))
                ses = int(input("Sesi kaç derece yapmak istiyorsunuz.Alabileceği değerler 0 ile 100 arasındadır'0 ve 100 dahildir.'"))
                if ses>100:
                    print("Yanlış değer girildi. Lütfen daha düşük bir değer giriniz.")
                elif ses<0:
                    print("Yanlış değer girildi. Lütfen daha yüksek bir değer giriniz.")
                else :
                    self.b_ses = ses
                    print("Mevcut Ses Düzeyi : {}".format(self.b_ses))
                i += 1
            else:
                cevap = input("Lütfen tekrar ses ayarı için herhangi bir tuşa, Çıkmak için 'q'ya tıklayınız.")
                if cevap=="q":
                    print("Ses ayarlarından çıkılıyor...")
                    time.sleep(1.5)
                    print("Ses Düzeyi Güncellendi : {}".format(self.b_ses))
                    print("Ses ayarlarından çıktınız.")
                    break
                else :
                    print("Mevcut Ses Düzeyi : {}".format(self.b_ses))
                    ses = int(input("Sesi kaç derece yapmak istiyorsunuz.(Alabileceği değerler 0 ile 100 arasındadır'0 ve 100 dahildir.')"))
                    if ses>100:
                        print("Yanlış değer girildi. Lütfen daha düşük bir değer giriniz.")
                    elif ses<0:
                        print("Yanlış değer girildi. Lütfen daha yüksek bir değer giriniz.")
                    else :
                        self.b_ses = ses
                        print("Mevcut Ses Düzeyi : {}".format(self.b_ses))
    def sifre_degis(self,yeni_sif):
        self.b_sifre = yeni_sif
        print("Şifreniz değiştirildi")
    def hesap_makinesi(self):
        self.b_uyg = "Hesap Makinesi"
        print("""
        ****************************
        Hoşgeldiniz

        Hesap Makinesi Programı İçerisinde Kullanılabilir İşlemler:

        1.Toplama(x + y)

        2.Çıkarma(x - y)

        3.Çarpma(x * y)

        4.Bölme(x : y)

        5.Faktöryel Alma(x!)

        6.Sinüs Hesaplama(sinx)

        7.Kosinüs Hesaplama(cosx)

        8.Tanjant Hesaplama(tanx)

        9.Kotanjant Hesaplama(cotx)

        10.Üslü Sayı Hesaplama(x^y)

        11.EBOB Hesaplama(EBOB(x,y))

        12.EKOK Hesaplama(EKOK(x,y))
        ****************************
        """)
        import time
        import math
        def ebob(sayi1,sayi2):
            liste = list()
            ebob=0
            if sayi1>sayi2:
                for x in range(1,sayi2+1):
                    if ((sayi1%x==0)and(sayi2%x==0)):
                        liste.append(x)
                liste.sort(reverse=True)
                ebob=liste[0]
                print("{} ve {} sayılarının en büyük ortak böleni {} sayısıdır.".format(sayi1,sayi2,ebob))
            elif sayi1==sayi2:
                print("{} ve {} sayılarının en büyük ortak böleni {} sayısıdır.".format(sayi1,sayi2,sayi1))
            else :
                for x in range(1,sayi1+1):
                    if ((sayi1%x==0)and(sayi2%x==0)):
                        liste.append(x)
                liste.sort(reverse=True)
                ebob=liste[0]
                print("{} ve {} sayılarının en büyük ortak böleni {} sayısıdır.".format(sayi1,sayi2,ebob))
        def topla(*a):
            toplam = 0
            for x in a:
                toplam += x
            return toplam
        def carp(*a):
            carpım = 1
            for x in a:
                carpım += x
            return carpım
        def ekok(sayi1,sayi2):
            liste = list()
            ebob=0
            ekok=0
            if sayi1>sayi2:
                for x in range(1,sayi2+1):
                    if ((sayi1%x==0)and(sayi2%x==0)):
                        liste.append(x)
                liste.sort(reverse=True)
                ebob=liste[0]
                ekok=(sayi1/ebob)*(sayi2/ebob)
                print("{} ve {} sayılarının en küçük ortak katı {} sayısıdır.".format(sayi1,sayi2,ekok))
            elif sayi1==sayi2:
                print("{} ve {} sayılarının en küçük ortak katı {} sayısıdır.".format(sayi1,sayi2,sayi1))
            else :
                for x in range(1,sayi1+1):
                    if ((sayi1%x==0)and(sayi2%x==0)):
                        liste.append(x)
                liste.sort(reverse=True)
                ebob=liste[0]
                ekok=(sayi1/ebob)*(sayi2/ebob)
                print("{} ve {} sayılarının en küçük ortak katı {} sayısıdır.".format(sayi1,sayi2,ekok))
        while True:
            islem = input("Hangi işlemi yapmak istiyorsunuz.(Çıkmak için lütfen 'q' ya basınız.)")
            if islem == "q":
                print("Program sonlandırılıyor...")
                time.sleep(1)
                break
            elif islem == "1":
                saysay=input("Kaç tane sayı kullanacaksınız")
                if saysay=="2":
                    sayı1 = int(input("Sayı - 1 : "))
                    sayı2 = int(input("Sayı - 2 : "))
                    print("{} + {} = {}".format(sayı1,sayı2,topla(sayı1,sayı2)))
                elif saysay=="3":
                    sayı1 = int(input("Sayı - 1 : "))
                    sayı2 = int(input("Sayı - 2 : "))
                    sayı3 = int(input("Sayı - 3 : "))
                    print("{} + {} + {} = {}".format(sayı1,sayı2,sayı3,topla(sayı1,sayı2,sayı3)))
                elif saysay=="4":
                    sayı1 = int(input("Sayı - 1 : "))
                    sayı2 = int(input("Sayı - 2 : "))
                    sayı3 = int(input("Sayı - 3 : "))
                    sayı4 = int(input("Sayı - 4 : "))
                    print("{} + {} + {} + {} = {}".format(sayı1,sayı2,sayı3,sayı4,topla(sayı1,sayı2,sayı3,sayı4)))
                elif saysay=="5":
                    sayı1 = int(input("Sayı - 1 : "))
                    sayı2 = int(input("Sayı - 2 : "))
                    sayı3 = int(input("Sayı - 3 : "))
                    sayı4 = int(input("Sayı - 4 : "))
                    sayı5 = int(input("Sayı - 5 : "))
                    print("{} + {} + {} + {} + {} = {}".format(sayı1,sayı2,sayı3,sayı4,sayı5,topla(sayı1,sayı2,sayı3,sayı4,sayı5)))
                else:
                    print("Geçersiz işlem...\nHizmet veremiyoruz...")
            elif islem == "3":
                saysay=input("Kaç tane sayı kullanacaksınız")
                if saysay=="2":
                    sayı1 = int(input("Sayı - 1 : "))
                    sayı2 = int(input("Sayı - 2 : "))
                    print("{} * {} = {}".format(sayı1,sayı2,carp(sayı1,sayı2)))
                elif saysay=="3":
                    sayı1 = int(input("Sayı - 1 : "))
                    sayı2 = int(input("Sayı - 2 : "))
                    sayı3 = int(input("Sayı - 3 : "))
                    print("{} * {} * {} = {}".format(sayı1,sayı2,sayı3,carp(sayı1,sayı2,sayı3)))
                elif saysay=="4":
                    sayı1 = int(input("Sayı - 1 : "))
                    sayı2 = int(input("Sayı - 2 : "))
                    sayı3 = int(input("Sayı - 3 : "))
                    sayı4 = int(input("Sayı - 4 : "))
                    print("{} * {} * {} * {} = {}".format(sayı1,sayı2,sayı3,sayı4,carp(sayı1,sayı2,sayı3,sayı4)))
                elif saysay=="5":
                    sayı1 = int(input("Sayı - 1 : "))
                    sayı2 = int(input("Sayı - 2 : "))
                    sayı3 = int(input("Sayı - 3 : "))
                    sayı4 = int(input("Sayı - 4 : "))
                    sayı5 = int(input("Sayı - 5 : "))
                    print("{} * {} * {} * {} * {} = {}".format(sayı1,sayı2,sayı3,sayı4,sayı5,carp(sayı1,sayı2,sayı3,sayı4,sayı5)))
                else:
                    print("Geçersiz işlem...\nHizmet veremiyoruz...")
            elif islem == "2":
                sayı1 = int(input("Sayı - 1 : "))
                sayı2 = int(input("Sayı - 2 : "))
                print("{} - {} = {}".format(sayı1,sayı2,sayı1-sayı2))
            elif islem == "4":
                sayı1 = int(input("Sayı - 1 : "))
                sayı2 = int(input("Sayı - 2 : "))
                print("{} : {} = {}".format(sayı1,sayı2,sayı1/sayı2))
            elif islem == "5":
                sayı = int(input("Sayı giriniz : "))
                print(math.factorial(sayı))
            elif islem == "6":
                sayı = int(input("Sayı giriniz : "))
                print(math.sin(sayı))
            elif islem == "7":
                sayı = int(input("Sayı giriniz : "))
                print(math.cos(sayı))
            elif islem == "8":
                sayı = int(input("Sayı giriniz : "))
                print(math.tan(sayı))
            elif islem == "9":
                sayı = int(input("Sayı giriniz : "))
                a=math.tan(sayı)
                b=1/a
                print(b)
            elif islem == "10":
                sayı1 = int(input("Tabandaki Sayı : "))
                sayı2 = int(input("Üsdeki Sayı : "))
                print("{} ^ {} = {}".format(sayı1,sayı2,sayı1**sayı2))
            elif islem == "11":
                as1=int(input("1.sayıyı giriniz."))
                as2=int(input("2.sayıyı giriniz."))
                ebob(as1,as2)
            elif islem == "12":
                as1=int(input("1.sayıyı giriniz."))
                as2=int(input("2.sayıyı giriniz."))
                ekok(as1,as2)
            else :
                print("Geçersiz işlem...")
        self.b_uyg = "Masaüstü"
    def sayi_tahmin(self):
        self.b_uyg = "Sayı Tahmin Oyunu"
        sayi = random.randint(1,100)
        a = 0
        while a != 5:
            isay=int(input("1 ile 100 arasındaki sayıyı bulunuz"))
            if sayi == isay:
                print("Doğru sayıyı {}. hakkınızda buldunuz bilgisayarın sayısı {} sayısıydı.".format(a+1,sayi))
                break
            elif isay > sayi and isay>0 and 101>isay :
                print("Daha düşük birsayı giriniz.")
                a += 1
                print("Kalan Hakkınız : {}".format(5-a))
            elif sayi > isay and isay>0 and 101>isay :
                print("Daha yüksek bir sayı giriniz")
                a += 1
                print("Kalan Hakkınız : {}".format(5-a))
            else :
                print("Doğru aralıkta bir sayı giriniz")
                a += 1
                print("Kalan Hakkınız : {}".format(5-a))
        if a==5:
            print("Maalesef sayıyı bulamadınız.  :(\nSayı {} sayısıydı.".format(sayi))
        else :
            print("Güle Güle...")
        self.b_uyg = "Masaüstü"
    def __str__(self):
        return "Bilgisayarın Durumu: {}\nUygulamalar: {}\nSes Düzeyi: {}\nSeçili Olan Uygulama: {}".format(self.b_durum,self.b_uyglar,self.b_ses,self.b_uyg)
    def __len__(self):
        return len(self.b_uyglar)
bilgisayar = Bilgisayar()
bcdefg=""
adssd=0
while bcdefg != "q" and adssd != 3:
    hak = 0
    while hak!=3:
        print("Kalan Hakkınız: {}".format(3-hak))
        sif = input("Bilgisayarı açmak için şifreyi giriniz.")
        bilgisayar.bilgisayar_ac(sif)
        if bilgisayar.b_durum =="Açık":
            break
        else:
            hak += 1

    if bilgisayar.b_durum == "Açık":
        print("""
        Yapılabilecek işlemler
        
        1.Bilgisayarı Kapat

        2.Kullanılabilir Uygulamalar Listesi

        3.Ses Ayarları

        4.Uygulama Ekle

        5.Uygulama Değiştir

        6.Uygulama Sayısı

        7.Şifre Değiştir

        """)
        while True:
            giris = input("İşlem seçiniz")
            if giris == "1":
                bilgisayar.bilgisayar_kapat()
                break
            elif giris == "2":
                print(bilgisayar.b_uyglar)
                print("Uygulama sayısı {}".format(len(bilgisayar)))
            elif giris == "3":
                bilgisayar.ses_ayar()
            elif giris == "4":
                uygis = input("Uygulama ismini giriniz.")
                bilgisayar.uygulama_ekle(uygis)
            elif giris == "5":
                bilgisayar.uygulama_degistir()
                if bilgisayar.b_uyg == "Hesap Makinesi":
                    bilgisayar.hesap_makinesi()
                elif bilgisayar.b_uyg == "Sayı Tahmin Oyunu":
                    bilgisayar.sayi_tahmin()
                elif bilgisayar.b_uyg == "Masaüstü":
                    print("Masaüstü açık.")
                else :
                    print("Seçilen uygulamanın dosyaları mevcut değil.(Sadece adı var.)")
            elif giris == "6":
                print("Uygulama sayısı {}".format(len(bilgisayar)))
            elif giris == "7":
                sifrey=input("Geçerli işlem için lütfen mevcut şifreyi girin.")
                if sifrey == bilgisayar.b_sifre:
                    abc=input("Değiştirilecek şifreyi girin")
                    bilgisayar.sifre_degis(abc)
                else:
                    print("Hatalı şifre")
                    continue
            else:
                print("Hatalı işlem girildi")
        continue
    else :
        print("Hiçbir işlem yapamazsınız. Lütfen önce bilgisayarı açınız.")
        bcdefg = input("Tekrar şifreyi denemek için herhangi bir tuşa , Bilgisayar kapalı kalsın istiyorsanız 'q' ya basınız")
        adssd += 1
print("Artık şifreyi deneyemezsiniz.")

        

        































































        
    