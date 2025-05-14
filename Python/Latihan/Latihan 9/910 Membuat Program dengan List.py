# Membuat list kosong untuk menampung hobi
hobi = []
stop = False
i = 0

# Mengisi hobi
while(not stop):
    hobi_baru = input(f"Inputkan hobi yang ke-{i}: ")
    hobi.append(hobi_baru)

    # Increment i
    i += 1
    
    tanya = input("Mau isi lagi? (y/t): ")
    if(tanya == "t"): 
        stop = True


# Cetak Semua Hobi
print("=" * 10) 
print(f"Kamu memiliki {len(hobi)} hobi")
for hb in hobi:
    print("- {hb}")