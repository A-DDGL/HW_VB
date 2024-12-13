# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 13:50:13 2024

@author: tester02
"""

class City:
    def __init__(self, sehir, sicaklik):
        self.city= sehir
        self.a= [self.city]
        self.temperature= sicaklik
        self.b= [self.temperature]
        self.tempandcity= dict(zip(self.a,self.b))
    
class HavaDurumu(City):
    def __init__(self, sehir, sicaklik):
        City.__init__(self, sehir, sicaklik)
        
    def sehirEkle(self, yenisehir):
        self.yenisehir=str(input("Bir şehir ismi giriniz: ").upper())
        self.a.append(yenisehir)
        
    def sicaklikGuncelle(self, yenisicaklik,c):
        self.c=str(input("Bir şehir ismi giriniz: ").upper())
        def sehirBul():
            if self.c in self.tempandcity.keys():
                self.yenisicaklik=float(input("Şehrin sıcaklığını Celcius cinsinden giriniz: "))
            else:
                print("Mevcut şehir adı listede ekli değil.")
    
    def tavsiyeVer(self,d):
        self.d=str(input("Bir şehir ismi giriniz: ").upper())
        if self.d in self.tempandcity.keys():
            self.mevcutsicaklik= self.tempandcity[self.d]
            if self.mevcutsicaklik <0:
                print("""Hava çok soğuk. 
                         Kar yağışı ihtimali de var. 
                         Buzlanma riski yüksek""")
            elif self.mevcutsicaklik <10:
                print("""Hava serin. 
                         Yağmur yağabilir. 
                         Mont ya da yağmurluk giymeniz gerekebilir.""")
            elif self.mevcutsicaklik <20:
                print("""Hava hafif yağışlı olabilir. 
                         Hafif bir kaban ya da yağmurluk giymeniz gerekebilir.""")
            elif self.mevcutsicaklik <25:
                print("""Bahar Havası. 
                         Hafif yağış ihtimali var. Aam düşük bir ihtimal. 
                         İsterseniz hafif bir yağmurluk taşıyabilirsiniz""")
            elif self.mevcutsicaklik <30:
                print("""Yaz havası hakim. 
                         Rahat giysiler giyin""")
            elif self.mevcutsicaklik <40:
                print("""Hava gerçekten çok sıcak 
                         Başınzı güneş ışınlarından koruyacak bir örtücü kullanmanız gerekebilir.
                         Bol sıvı tüketin.
                         Açık renkli ve rahat kumaşlı elbiseler tercih ediniz""")
            elif self.mevcutsicaklik >40:
                print("""Dikkat güneş çarpması riski. 
                         Çok önemli değil ise evden ayrılmayın. 
                         Özellikle hamile olanlar ve kronik hastalar dikkatli olmalı.
                         Bol sıvı tüketimi gerekli.""")
            else
                print("Seçtiğiniz şehir için bir sıcaklık değeri girilmemiş.")

        else:
            print("Mevcut şehir adı listede ekli değil.")
        
        
            
        
    