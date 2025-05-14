print("Pilih keterangan kondisi berikut yang sesuai dengan keadaan mu")
print("A. Cuaca hujan.")
print("B. Kamu terlambat.")
print("C. Tanggal merah.")
print("D. Kondisi lainnya... 'Masukan kondisi sendiri'")

user_condition = str(input("Beritahu kondisi mu disini -> A/B/C/D -> "))

if user_condition != "D":

    if user_condition == "A" or user_condition == "a":
        print("Kamu boleh terlambat")
    elif user_condition == "B" or user_condition == "b":
        print("Waktu perkuliahan ditambah")
    elif user_condition == "C" or user_condition == "c":
        print("Perkuliahan di liburkan")
    else:
        print("Enggak jelas banget kamu")

else:
    print("Jelaskan kondisi mu...")

    user_story = str(input("-> "))

    if user_story != "":
        print("Ya udah deh tidur saja")
    else:
        print("Wow keren...")
