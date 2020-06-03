#Standart Zaman Hesaplama
Rakam = [("0"),("1"),("2"),("3"),("4"),("5"),("6"),("7"),("8"),("9")]
Yasaklar = [","]
b=1
i=0
x=0
liste = []
liste_top = 0.0
#Veri Girişi Sütun
while True:
    sutun_sayisi = input("Kaç adet gözlem zamanınız var: \n")
    q = list(sutun_sayisi)
    q1= ''.join(q[0:1])
    if q1 not in Rakam:
        print("Sayı girişi yapınız.\n")
    else:
        break
#Veri Girişi Satır
while True:
    satir_sayisi = input ("Kaç adet gözlem yapılacak eleman var: \n")
    q = list(satir_sayisi)
    q1= ''.join(q[0:1])
    if q1 not in Rakam:
        print("Sayı girişi yapınız.\n")
    else:
        break 
#Matris Oluşturma----------------------------------------------------------------------------------------
for i in range(int(satir_sayisi)):
    a=1
    for x in range(int(sutun_sayisi)):
        while True:
            veri = input("{}. eleman için {}. gözlem değerini girin:\n". format(b,a))
            a=a+1
            q = list(veri)
            q1= ''.join(q[0:1])
            if q1 not in Rakam:
                print("Sayı girişi yapınız")
            else:
                break
    
        veri = str(veri.replace(',','.'))
        liste_top +=  float(veri)
    print("Liste toplamı =", liste_top)
  #Performans-------------------------------------------------------------------------------------------------------

    performans_beceri_puan=performans_caba_puan=performans_kosullar_puan=performans_tutarlilik_puan=0.00
    print ("\nPerformans Derecelendirme Skalasında")
  
    while True:
        performans_beceri = input("Becerisi; Üstün+ = 0\nÜstün- = 1,\nÇok İyi+ = 2,\nÇok İyi- = 3\nİyi+ = 4\nİyi- = 5\nOrta = 6\nZayıf+ = 7,\nZayıf- = 8\nÇok Zayıf+ = 9\nÇok Zayıf- = 10\n")
        if performans_beceri in Rakam or performans_beceri =="10" :
            if int(performans_beceri) == 0:
                performans_beceri_puan=0.15
            elif  int(performans_beceri) == 1:
                performans_beceri_puan=0.13
            elif int(performans_beceri)==2:
                performans_beceri_puan=0.11
            elif int(performans_beceri)==3:
                performans_beceri_puan=0.08
            elif int(performans_beceri)==4:
                performans_beceri_puan=0.06
            elif int(performans_beceri)==5:
                performans_beceri_puan=0.03
            elif int(performans_beceri)==6:
                performans_beceri_puan=0.00
            elif int(performans_beceri)==7:
                performans_beceri_puan=-0.05
            elif int(performans_beceri)==8:
                performans_beceri_puan=-0.10
            elif int(performans_beceri)==9:
                performans_beceri_puan=-0.16
            elif int(performans_beceri)==10:
                performans_beceri_puan=-0.22
            break
        else:
            print ("Yanlış giriş yapıldı.\n")
 
    while True:
        performans_caba = input("\nÇabası; \nMükemmel+ = 0\nMükemmel- = 1\nÇok İyi+ = 2\nÇok İyi- = 3\nİyi+ = 4\nİyi- = 5\nOrta = 6\nZayıf+ = 7\nZayıf- = 8\nÇok Zayıf+ = 9\nÇok Zayıf- = 10\n")
        if performans_caba in Rakam or performans_beceri =="10" :
            if int(performans_caba)==0:
                performans_caba_puan=0.13
            elif int(performans_caba)==1:
                performans_caba_puan=0.12
            elif int(performans_caba)==2:
                performans_caba_puan=0.10
            elif int(performans_caba)==3:
                performans_caba_puan=0.08
            elif int(performans_caba)==4:
                performans_caba_puan=0.05
            elif int(performans_caba)==5:
                performans_caba_puan=0.02
            elif int(performans_caba)==6:
                performans_caba_puan=0.00
            elif int(performans_caba)==7:
                performans_caba_puan=-0.04
            elif int(performans_caba)==8 :
                performans_caba_puan=-0.08
            elif int(performans_caba)==9:
                performans_caba_puan=-0.12
            elif int(performans_caba)==10:
                performans_caba_puan=-0.17
            break
        else:
            print ("Yanlış giriş yapıldı.")

    while True:
        performans_kosullar = input("\nKoşulları; \nİdeal = 0 \nÇok İyi = 1\nİyi = 2 \nOrta = 3 \nZayıf = 4  \nÇok Zayıf = 5 \n")
        if performans_kosullar in Rakam :
            if int(performans_kosullar)<6:
                if int(performans_kosullar)==1:
                    performans_kosullar_puan=0.06
                elif int(performans_kosullar)==2:
                    performans_kosullar_puan=0.04
                elif int(performans_kosullar)==3:
                    performans_kosullar_puan=0.02
                elif int(performans_kosullar)==4:
                    performans_kosullar_puan=0.00
                elif int(performans_kosullar)==5:
                    performans_kosullar_puan=-0.03
                elif int(performans_kosullar)==6:
                    performans_kosullar_puan=-0.07
                break
            else:
                print ("Yanlış giriş yapıldı.")
        else:
            print ("Yanlış giriş yapıldı.")

    while True:
        performans_tutarlilik = input("\nTutarlılığı; \nMükemmel = 0 \nÇok İyi = 1 \nİyi = 2 \nOrta = 3 \nZayıf = 4 \nÇok Zayıf = 5\n")
        if performans_tutarlilik in Rakam :
            if int(performans_tutarlilik)<6:
                if int(performans_tutarlilik)==0:
                    performans_tutarlilik_puan=0.04
                elif int(performans_tutarlilik)==1:
                    performans_tutarlilik_puan=0.03
                elif int(performans_tutarlilik)==2:
                    performans_tutarlilik_puan=0.01
                elif int(performans_tutarlilik)==3:
                    performans_tutarlilik_puan=0.00
                elif int(performans_tutarlilik)==4:
                    performans_tutarlilik_puan=-0.02
                elif int(performans_tutarlilik)==5:
                    performans_tutarlilik_puan=-0.04
                break
            else:
                print ("Yanlış giriş yapıldı.")
        else:
            print ("Yanlış giriş yapıldı.")

    performanslar_toplam = performans_beceri_puan + performans_caba_puan + performans_kosullar_puan + performans_tutarlilik_puan + 1.00

    print("\nPerformans Toplam = ",performanslar_toplam)

#Tolerans-------------------------------------------------------------------------------------------------------
  
    while True:
        secim = input("Pay (tolerans) değerleri toplamını kendiniz girecekseniz 1'e, değilse 0 girin.\n")
        if secim == "1" or secim =="0":
            break
        else:
            print ("0 veya 1 girin")

    if int(secim)==1:
    
        while True:
            pay=input("Pay toplam değerlerini ondalıksız girin.\n")
            q = list(pay)
            q1= ''.join(q[0:1])
            if q1 not in Rakam:
                print("Sayı girişi yapınız")
            else:
                break

        pay_puan = 1.00 + (int(pay) * 0.01)
        print(pay_puan)

    elif int(secim) == 0:

        lists=["Kişisel ihtiyaç yoksa 0 varsa 1","Temel Yorgunluk yoksa  0 varsa 1","Ayakta Durma Payı yoksa  0 varsa 1"]
        listc=["2.5 = 0, 5.0 = 1, 7.5 = 2, 10.0 = 3, 12.5 = 4, 15.0 = 5 17.5 = 6, 20.0 = 7, 22.5 = 8, 25.0 = 9, 30.0 = 10 40.0 = 11, 50.0 = 12"]
        listu=["Zora Yakın = 0, Zor(Eğilmiş durumda) = 1, Çok zor(Yere yatmış - Yukarı Uzanmış) = 2","Az Altında = 0, Çok Altında = 1, Tamamen Yetersiz = 2","İyi havalandırılmış - Açık hava = 0, Kötü havalandırılmış fakat zehirli gaz ortamı yok = 1, Fırın vb. yakın iş = 2","Dikkat Gerektiren İş = 0, İnce iş = 1, Çok İnce iş = 2","Sürekli = 0, Ani Yüksek = 1, Ani Çok Yüksek, Tiz Yüksek = 2 ","Oldukça karmaşık = 0, Karmaşık - Uzun sürekli dikkat gerektiren = 1, Çok karmaşık = 2","Düşük = 0, Orta = 1, Yülsek = 2","Oldukça Yorucu = 0, Yorucu = 1, Çok Yorucu = 2"]
        baslik=["ANORMAL POZİSYON PAYI","AYDINLATMA ŞARTLARI ÖNGÖRÜLEN DEĞER","HAVALANDIRMA ŞARTLARI(MEVSİMSEL FAKTÖRLER HARİÇ)","GÖRSEL ZORLAMA","GÜRÜLTÜ","ZİHİNSEL ZORLAMA","MONOTONLUK ZİHİNSEL","MONOTONLUK FİZKSEL"]
        listpk = []

  
        d = 0
        c = 1
        l = 0
        pk = 0

        while True:
            cinsiyet = input("\nErkek ise 0, kadın ise 1 giriniz: \n")
            if cinsiyet == "1" or cinsiyet =="0":
                break
            else:
                print ("0 veya 1 girin")

        if int(cinsiyet) == 1:
            print ("\nSABİT PAYLAR")
            for i in range(3):
                while True:                    
                    pk = input(f"{tuple(lists)[d:c]} uygun olan seçenek numarasını girin :\n")
                    c = c + 1
                    d = d +1
                    if pk == "1" or pk =="0":
                        break
                    else:print ("0 veya 1 girin")
                listpk.append(pk)
            
            c = 1
            d = 0
            for l in range(8):
                while True:
                    print(f"{tuple(baslik)[d:c]}")
                    pu = input(f"{tuple(listu)[d:c]} Varsa 1, yoksa 0 giriniz:\n")                   
                    
                    if pu in Rakam :
                        if int(pu)<3:
                            c = c + 1
                            d = d +1
                            listpk.append(pu)
                            break
                    else:
                        print ("Yanlış giriş yapıldı.")                                    
            while True:
                c = 1
                d = 0
                print ("\nKALDIRILAN AĞIRLIK - UYGULANAN KUVVET")
                pc = input(f"{tuple(listc)[d:c]} Varsa 1, yoksa 0 giriniz:\n")
                c = c + 1
                d = d +1
                if pc in Rakam or pc =="10" or pc =="11" or pc == "12" :
                   break
                else:
                    print ("Yanlış giriş yapıldı.")
            listpk.append(pc)


            p1 = ''.join(listpk[0:1])
            p2 = ''.join(listpk[1:2])
            p3 = ''.join(listpk[2:3])
            p4 = ''.join(listpk[3:4])
            p5 = ''.join(listpk[4:5])
            p6 = ''.join(listpk[5:6])
            p7 = ''.join(listpk[6:7])
            p8 = ''.join(listpk[7:8])
            p9 = ''.join(listpk[8:9])
            p10 = ''.join(listpk[9:10])
            p11 = ''.join(listpk[10:11])
            p12 = ''.join(listpk[11:12])

            pay_puan = float(p1)*0.07+float(p2)*0.04+float(p3)*0.04

            if p12 == "0":
                pay_puan+=0.01
            elif p12=="1":
                pay_puan+=0.02
            elif p12 == "2":
                pay_puan+=0.03
            elif p12 == "3":
                pay_puan+=0.04
            elif p12 == "4":
                pay_puan+=0.06
            elif p12 == "5":
                pay_puan+=0.09
            elif p12 == "6":
                pay_puan+=0.12
            elif p12 == "7":
                pay_puan+=0.15
            elif p12 == "8":
                pay_puan+=0.18
            elif p12 == "9":
                pay_puan+=0.14
            elif p12 == "10":
                pay_puan+=0.19
            elif p12 == "11":
                pay_puan+=0.33
            elif p12 == "12":
                pay_puan+=0.58

            if p4 == "0":
                pay_puan += 0.01
            elif p4 == "1":
                pay_puan+=0.03
            elif p4 == "2":
                pay_puan+=0.07

            if p5 == "0":
                pay_puan += 0.0
            elif p5 == "1":
                pay_puan+=0.02
            elif p5 == "2":
                pay_puan+=0.05

            if p6 == "0":
                pay_puan += 0.0
            elif p6 == "1":
                pay_puan+=0.05
            elif p6 == "2":
                pay_puan+=0.15

            if p7 == "0":
                pay_puan += 0.0
            elif p7 == "1":
                pay_puan+=0.02
            elif p7 == "2":
                pay_puan+=0.05

            if p8 == "0":
                pay_puan += 0.0
            elif p8 == "1":
                pay_puan+=0.02
            elif p8 == "2":
                pay_puan+=0.05

            if p9 == "0":
                pay_puan += 0.01
            elif p9 == "1":
                pay_puan+=0.04
            elif p9 == "2":
                pay_puan+=0.08

            if p10 == "0":
                pay_puan += 0.00
            elif p10 == "1":
                pay_puan+=0.01
            elif p10 == "2":
                pay_puan+=0.04

            if p11 == "0":
                pay_puan += 0.00
            elif p11 == "1":
                pay_puan+=0.01
            elif p11 == "2":
                pay_puan+=0.02                

       
        elif int(cinsiyet) == 0:
            print ("\nSABİT PAYLAR")
            for i in range(3):
                while True:                    
                    pk = input(f"{tuple(lists)[d:c]} uygun olan seçenek numarasını girin :\n")
                    c = c + 1
                    d = d +1
                    if pk == "1" or pk =="0":
                        break
                    else:print ("0 veya 1 girin")
                listpk.append(pk)
            
            c = 1
            d = 0
            for l in range(8):
                while True:
                    print(f"{tuple(baslik)[d:c]}")
                    pu = input(f"{tuple(listu)[d:c]} Varsa 1, yoksa 0 giriniz:\n")                   
                    
                    if pu in Rakam :
                        if int(pu)<3:
                            c = c + 1
                            d = d +1
                            listpk.append(pu)
                            break
                    else:
                        print ("Yanlış giriş yapıldı.")                                    
            while True:
                c = 1
                d = 0
                print ("\nKALDIRILAN AĞIRLIK - UYGULANAN KUVVET")
                pc = input(f"{tuple(listc)[d:c]} Varsa 1, yoksa 0 giriniz:\n")
                c = c + 1
                d = d +1
                if pc in Rakam or pc =="10" or pc =="11" or pc == "12" :
                   break
                else:
                    print ("Yanlış giriş yapıldı.")
            listpk.append(pc)


            p1 = ''.join(listpk[0:1])
            p2 = ''.join(listpk[1:2])
            p3 = ''.join(listpk[2:3])
            p4 = ''.join(listpk[3:4])
            p5 = ''.join(listpk[4:5])
            p6 = ''.join(listpk[5:6])
            p7 = ''.join(listpk[6:7])
            p8 = ''.join(listpk[7:8])
            p9 = ''.join(listpk[8:9])
            p10 = ''.join(listpk[9:10])
            p11 = ''.join(listpk[10:11])
            p12 = ''.join(listpk[11:12])

            pay_puan = float(p1)*0.05+float(p2)*0.04+float(p3)*0.02

            if p12 == "0":
                pay_puan+=0.0
            elif p12=="1":
                pay_puan+=0.01
            elif p12 == "2":
                pay_puan+=0.02
            elif p12 == "3":
                pay_puan+=0.03
            elif p12 == "4":
                pay_puan+=0.04
            elif p12 == "5":
                pay_puan+=0.06
            elif p12 == "6":
                pay_puan+=0.08
            elif p12 == "7":
                pay_puan+=0.10
            elif p12 == "8":
                pay_puan+=0.12
            elif p12 == "9":
                pay_puan+=0.14
            elif p12 == "10":
                pay_puan+=0.19
            elif p12 == "11":
                pay_puan+=0.33
            elif p12 == "12":
                pay_puan+=0.58

            if p4 == "0":
                pay_puan += 0.0
            elif p4 == "1":
                pay_puan+=0.02
            elif p4 == "2":
                pay_puan+=0.07

            if p5 == "0":
                pay_puan += 0.0
            elif p5 == "1":
                pay_puan+=0.02
            elif p5 == "2":
                pay_puan+=0.05

            if p6 == "0":
                pay_puan += 0.0
            elif p6 == "1":
                pay_puan+=0.05
            elif p6 == "2":
                pay_puan+=0.15

            if p7 == "0":
                pay_puan += 0.0
            elif p7 == "1":
                pay_puan+=0.02
            elif p7 == "2":
                pay_puan+=0.05

            if p8 == "0":
                pay_puan += 0.0
            elif p8 == "1":
                pay_puan+=0.02
            elif p8 == "2":
                pay_puan+=0.05

            if p9 == "0":
                pay_puan += 0.01
            elif p9 == "1":
                pay_puan+=0.04
            elif p9 == "2":
                pay_puan+=0.08

            if p10 == "0":
                pay_puan += 0.00
            elif p10 == "1":
                pay_puan+=0.01
            elif p10 == "2":
                pay_puan+=0.04

            if p11 == "0":
                pay_puan += 0.00
            elif p11 == "1":
                pay_puan+=0.02
            elif p11 == "2":
                pay_puan+=0.05

    print("Pay puanları = ",pay_puan)
            
    stdz= liste_top * performanslar_toplam * (1.00 + pay_puan)   

    standart_zaman=[]
    standart_zaman.append(stdz)
    print("Standart Zaman Değeri = ",standart_zaman)
  
    a=1    
    b=b+1