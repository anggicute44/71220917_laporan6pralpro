def hitung_ips():
    # Bobot nilai berdasarkan soal
    bobot_nilai = {'A': 4, 'B': 3, 'C': 2, 'D': 1}
    sks_permatkul = 3  # SKS tiap mata kuliah selalu 3

    # Meminta jumlah mata kuliah
    jumlahmatkul = int(input("Masukkan jumlah mata kuliah: "))
    
    total_bobot = 0
    total_sks = jumlahmatkul * sks_permatkul # Total SKS
    
    for i in range(1, jumlahmatkul + 1):
        while True:
            nilai = input(f"Masukkan nilai untuk mata kuliah ke-{i} (A/B/C/D): ").upper()
            if nilai in bobot_nilai:
                total_bobot += bobot_nilai[nilai] * sks_permatkul
                break
            else:
                print("Nilai tidak valid! Masukkan A, B, C, atau D.")

    # Menghitung IPS
    ips = total_bobot / total_sks
    print(f"\nIndeks Prestasi Semester (IPS) Anda: {ips:.2f}")

# Pemanggilan fungsi
hitung_ips()






