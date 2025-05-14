frn_dic = {
    "nama" : "Farhan Raditya Al Gazali",
    'jenis_kelamin' : False,
    'hobi' : "Eksplorasi",
    'no_telepon' : '082158527210',
    'status' : False,
    'nim' : 246661036,
    'kelas' : "TRK 2B",
    'pekerjaan' : "Mahasiswa",
    'kampus' : "Politeknik Negeri Samarinda",
    'jurusan' : "Teknologi Informasi",
}

print(f"Nama: {frn_dic['nama']}")

if frn_dic['jenis_kelamin']:
    print(f"Jenis kelamin: Perempuan")
else:
    print(f"Jenis kelamin: Laki-laki")

print(f"Hobi: {frn_dic['hobi']}")
print(f"no_telepon: {frn_dic['no_telepon']}")

if frn_dic['status']:
    print(f"Status: Menikah")
else:
    print(f"Status: Belum menikah")

print(f"NIM: {frn_dic['nim']}")
print(f"Kelas: {frn_dic['kelas']}")
print(f"Pekerjaan: {frn_dic['pekerjaan']}")
print(f"Jurusan: {frn_dic['jurusan']}")
print(f"Institut: {frn_dic['kampus']}")



