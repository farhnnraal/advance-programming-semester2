# Membuat Dictionary
pak_tani = {
    "nama": "Petani Kode",
    "umur": 22,
    "hobi": ["coding", "membaca", "cocok tanam"],
    "menikah": False,
    "sosmed": {
        "facebook": "petanikode",
        "twitter": "@petanikode"
    } 
}

# Mengakses isi dictionary
print("Nama saya adalah %s" % pak_tani["nama"])
print("Twitter: %s" % pak_tani["sosmed"]["twitter"])