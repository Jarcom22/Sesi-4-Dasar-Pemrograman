def cek_tahun_kabisat(tahun):
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        return f"{tahun} adalah tahun kabisat."
    else:
        return f"{tahun} bukan tahun kabisat."


def cek_angka(angka):
    if angka > 0:
        return "Positif"
    elif angka < 0:
        return "Negatif"
    else:
        return "Nol"


def hitung_total_bayar(total_belanja):
    if total_belanja > 100000:
        diskon = 0.10
    elif total_belanja > 50000:
        diskon = 0.05
    else:
        diskon = 0
    
    total_bayar = total_belanja - (total_belanja * diskon)
    return f"Total yang harus dibayar: Rp{total_bayar:.2f}"


tahun = int(input("Masukkan tahun: "))
print(cek_tahun_kabisat(tahun))

angka = int(input("Masukkan angka: "))
print(cek_angka(angka))

total_belanja = float(input("Masukkan total belanja: "))
print(hitung_total_bayar(total_belanja))

