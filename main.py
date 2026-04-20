class Avtobus:
    def __init__(self, nom, o_rinlar_soni):
        self.nom = nom
        self.o_rinlar_soni = o_rinlar_soni
        self.band_qilish = 0
        self.bo_sh_o_rinlar = o_rinlar_soni

    def bron_qilish(self, son):
        if son > self.bo_sh_o_rinlar:
            print("Bo'sh o'rinlar mavjud emas.")
        elif son > self.o_rinlar_soni - self.band_qilish:
            print("Avtobus band qilingan.")
        else:
            self.band_qilish += son
            self.bo_sh_o_rinlar -= son
            print(f"{son} o'rin bron qilingan.")

    def band_qilishni_ko_rsatish(self):
        return self.band_qilish

    def bo_sh_o_rinlar_soni(self):
        return self.bo_sh_o_rinlar


class AvtobusReys:
    def __init__(self, nom, avtobuslar):
        self.nom = nom
        self.avtobuslar = avtobuslar

    def bron_qilish(self, avtobus_nom, son):
        for avtobus in self.avtobuslar:
            if avtobus.nom == avtobus_nom:
                avtobus.bron_qilish(son)
                return
        print("Avtobus mavjud emas.")

    def band_qilishni_ko_rsatish(self):
        band_qilish = 0
        for avtobus in self.avtobuslar:
            band_qilish += avtobus.band_qilish
        return band_qilish

    def bo_sh_o_rinlar_soni(self):
        bo_sh_o_rinlar = 0
        for avtobus in self.avtobuslar:
            bo_sh_o_rinlar += avtobus.bo_sh_o_rinlar
        return bo_sh_o_rinlar


avtobuslar = [
    Avtobus("Avtobus 1", 50),
    Avtobus("Avtobus 2", 60),
    Avtobus("Avtobus 3", 70)
]

avtobus_reys = AvtobusReys("Reys 1", avtobuslar)

avtobus_reys.bron_qilish("Avtobus 1", 20)
avtobus_reys.bron_qilish("Avtobus 2", 30)
avtobus_reys.bron_qilish("Avtobus 3", 40)

print(f"Band qilish: {avtobus_reys.band_qilishni_ko_rsatish()}")
print(f"Bo'sh o'rinlar: {avtobus_reys.bo_sh_o_rinlar_soni()}")
```

Kodda ikkita klass mavjud: `Avtobus` va `AvtobusReys`. `Avtobus` klassi avtobusning xususiyatlarini (nomi, o'rindar soni, band qilish soni, bo'sh o'rindar soni) ifodalaydi. `AvtobusReys` klassi avtobus reysining xususiyatlarini (nomi, avtobuslar ro'yxati) ifodalaydi.

`Avtobus` klassining `bron_qilish` metodi avtobusga bron qilishni amalga oshiradi. Agar bron qilish soni bo'sh o'rindar sonidan katta bo'lsa, "Bo'sh o'rinlar mavjud emas" xabari chiqadi. Agar bron qilish soni avtobus band qilish sonidan katta bo'lsa, "Avtobus band qilingan" xabari chiqadi. Boshqa holatlarda, bron qilish amalga oshiriladi.

`AvtobusReys` klassining `bron_qilish` metodi avtobus reysiga bron qilishni amalga oshiradi. Agar avtobus mavjud bo'lsa, bron qilish amalga oshiriladi. Boshqa holatlarda, "Avtobus mavjud emas" xabari chiqadi.

`AvtobusReys` klassining `band_qilishni_ko_rsatish` metodi avtobus reysining band qilish sonini qaytaradi. `bo_sh_o_rinlar_soni` metodi avtobus reysining bo'sh o'rindar sonini qaytaradi.
