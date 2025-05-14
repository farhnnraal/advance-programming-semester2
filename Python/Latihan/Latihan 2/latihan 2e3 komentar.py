class Pagar:
    """kelas pagar untuk membuat objek pagar. Dibuat oleh Petani Kode sebagai contoh saja."""
    def __init__(self, warna, tinggi, bahan):
        self.warna = warna
        self.tinggi = tinggi
        self.bahan = bahan

# Mengakses dokumentasi kelas
print Pagar.__doc__
input('\ntekan [enter] untuk melihat bantuan (dokumentasi) kelas: ')
help(Pagar) # untuk melihat dokumentasi kelas
