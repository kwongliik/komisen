# Atur cara mengira komisen

# Isytihar pemboleh ubah
jumlah = 0
jualan = 0
komisen = 0
ulang = "Y"

while ulang == "Y":
    # Input
    jualan = float(input("Masukkan jumlah jualan: RM"))
    # Proses
    if jualan > 80:
        kadar_komisen = 0.055
    elif jualan > 70:
        kadar_komisen = 0.05
    elif jualan > 60:
        kadar_komisen = 0.04
    elif jualan > 50:
        kadar_komisen = 0.03
    else:
        kadar_komisen = 0.02
    komisen = jualan * kadar_komisen
    # Output
    print("Komisen anda ialah RM", round(komisen, 2))
    # Proses
    jumlah = jumlah + komisen
    # Input
    ulang = input("Masukkan Y untuk teruskan pengiraan atau N untuk hentikan pengiraan:")
# Output
print("\n\tJumlah komisen ialah RM", round(jumlah, 2))
print("\t...Anda telah selesai membuat pengiraan...")
