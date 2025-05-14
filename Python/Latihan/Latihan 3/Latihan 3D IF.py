# program untuk mengecek bonus dan diskon
# file: bonus.py

total_belanja = input("Total belanja: Rp ")

# jumlah yang harus dibayar adalah berapa total belanjaannya
# tapi kalau dapat diskon akan berkurang
bayar = total_belanja

# jika dia belanja di atas 100rb maka berikan bonus dan diskon
if total_belanja > 100000:
    print("Kamu mendapatkan bonus minuman dingin")
    print("dan diskon 5%")

    # hitung diskonnya
    diskon = total_belanja * 5/100 #5%
    bayar = total_belanja - diskon


# cetak struk
print("Total yang harus dibayar: Rp %s" % bayar)
print("Terima kasih sudah berbelanja")
print("Datang lagi yaa...")
