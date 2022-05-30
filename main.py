#This software was written by Ahmet Disci.
#Matrisleri yazdırdıgım fonksiyon
def yazdır():
    for i in range(12):
            print(sehirler[i][1], end="\t")
            print(matris[i])

#Konumları yazdırdıgım fonksiyon
def konum(kod):
    if sehirler[kod-1][0]==12:
        print("Konya'ya varmış bulunmaktayız.")
        exit()
    print("KONUM=", end="")
    print(sehirler[kod-1][1])
    komsuSehirler(kod-1)

#Bulundugu sehirlerin komsu sehirlerini yazdırdıgı fonksiyon
def komsuSehirler(komsukod):
    enyakın="-1"
    print("KOMŞU ŞEHİRLER:")
    for i in range(12):
        if matris[komsukod][i]==1:
            print("->"+sehirler[i][1]+"\t\t"+"Kuş Bakışı Uzaklık=",end="\t")
            print(sehirler[i][2], end="km\n")
            if enyakın=="-1":
                enyakın=sehirler[i]
            if enyakın!="-1" and enyakın[2]>sehirler[i][2]:
                enyakın=sehirler[i]
    print("\n")
    konum(enyakın[0])

#Matrisleri olusturdugum  yer  ulaşıyorsa "1"  ulaşılmıyorsa "0"
matris = ([0,1,1,1,0,0,0,0,1,0,1,1],[1,0,1,0,1,0,0,0,0,0,0,0],[1,1,0,1,1,0,0,0,0,0,0,0],[1,0,1,0,1,0,1,1,0,0,1,0],[0,1,1,1,0,1,1,0,0,0,0,0],[0,0,0,0,1,0,1,0,0,0,0,0]
,[0,0,0,1,1,1,0,1,0,0,0,0],[0,0,0,1,0,0,1,0,0,1,0,0],[1,0,0,0,0,0,0,0,0,1,1,1],[0,0,0,0,0,0,0,0,1,0,1,1],[1,0,0,1,0,0,0,0,1,1,0,0],[1,0,0,0,0,0,0,0,1,1,0,0])

#Menu
print("Program Başlatıldı.Konya'ya Greedy Search Example İle Geleceğiz.")
print("Şehirler ve Komsuluk Matrisi")
#Sehirler ve hakkında verileri girdigim yer
sehirler=[1,"Afyonk.",195],[2,"Kütahya",280],[3,"Uşak   ",285],[4,"Denizli",300],[5,"Manisa ",450],[6,"İzmir  ",472],[7,"Aydın  ",408],[8,"Muğla  ",371],[9, "Isparta",170],[10, "Antalya",190],[11, "Burdur ",194],[12, "Konya  ",0]


yazdır()
print("")
print("1-Afyonkarahisar"+ "\n" +
      "2-Kütahya"+ "\n" +
      "3-Uşak"+ "\n" +
      "4-Denizli"+ "\n" +
      "5-Manisa"+ "\n" +
      "6-İzmir"+ "\n" +
      "7-Aydın"+ "\n" +
      "8-Muğla"+ "\n" +
      "9-Isparta"+ "\n" +
      "10-Antalya" + "\n" +
      "11-Burdur" + "\n" +
      "12-Konya"+ "\n" )

baslangicSehir=input("Başlangıç şehrinizin  kodunu giriniz:")
baslangicSehir=int(baslangicSehir)

print("\n")
konum(baslangicSehir)