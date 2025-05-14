count = 0

while(True):
    answer = input("Lanjut atau berhenti? ").lower()
    if answer == 'lanjut':
        count += 1
        continue
    elif answer == 'berhenti':
        count += 1
        break
    else:
        print(f"Pilihan tidak valid. Silakan coba lagi. Perhitungan saat ini -> {count}")

print(f"Total perulangan: {count}")
