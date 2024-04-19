# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 20:26:29 2024

@author: Fairuz Maulidya
"""

print('''====================
Nama: Fairuz Maulidya      ||
Nim: 064002300018          ||''')
class MasyarakatKampus:
    def __init__(self, golongan='LAINNYA', gaji=150000):
        self.golongan = golongan
        self.gaji = gaji

    def Gaji(self):
        return self.gaji

    def Penjelasan(self):
        print(f"Golongan {self.golongan} mendapatkan gaji: {self.Gaji()}")


class Dosen(MasyarakatKampus):
    def __init__(self):
        super().__init__('DOSEN', 450000)


class Staff(MasyarakatKampus):
    def __init__(self):
        super().__init__('STAFF', 300000)


# Contoh penggunaan
if __name__ == "__main__":
    dosen = Dosen()
    staff = Staff()
    lainnya = MasyarakatKampus()

    dosen.Penjelasan()
    staff.Penjelasan()
    lainnya.Penjelasan()
