nilai_mahasiswa = int(input("Berapa nilaimu?"))

# A range grade
if nilai_mahasiswa > 96 and nilai_mahasiswa <= 100:
    print("Kamu mendapat nilai A+")

elif nilai_mahasiswa > 93 and nilai_mahasiswa <= 96:
    print("Kamu mendapat nilai A")

elif nilai_mahasiswa >= 90 and nilai_mahasiswa <= 93:
    print("Kamu mendapat nilai A-")

# B range grade
elif nilai_mahasiswa > 86 and nilai_mahasiswa < 90:
    print("Kamu mendapat nilai B+")

elif nilai_mahasiswa > 83 and nilai_mahasiswa <= 86:
    print("Kamu mendapat nilai B")

elif nilai_mahasiswa >= 80 and nilai_mahasiswa <= 83:
    print("Kamu mendapat nilai B-")

# C range grade
elif nilai_mahasiswa > 76 and nilai_mahasiswa < 80:
    print("Kamu mendapat nilai C+")

elif nilai_mahasiswa > 73 and nilai_mahasiswa <= 76:
    print("Kamu mendapat nilai C")

elif nilai_mahasiswa >= 70 and nilai_mahasiswa <= 73:
    print("Kamu mendapat nilai C-")

# D range grade
elif nilai_mahasiswa > 66 and nilai_mahasiswa < 70:
    print("Kamu mendapat nilai D+")

elif nilai_mahasiswa > 63 and nilai_mahasiswa <= 66:
    print("Kamu mendapat nilai D")

elif nilai_mahasiswa >= 60 and nilai_mahasiswa <= 63:
    print("Kamu mendapat nilai D-")

# E range grade
else:
    print("Kamu mendapat nilai E")
