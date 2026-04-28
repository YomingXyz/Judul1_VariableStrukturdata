# PROGRAM MANAJEMEN TABUNGAN

def menu():
    print("\n=== SISTEM MANAJEMEN TABUNGAN ===")
    print("1. Setor Uang (Menabung)")
    print("2. Tarik Uang")
    print("3. Tampilkan Saldo dan Riwayat")
    print("4. Keluar")

def main():
    riwayat_tabungan = []
    saldo = 0
    running = True
    
    while running:
        menu()
        try:
            choice = int(input("Pilihan (1-4): "))
        except ValueError:
            print("Masukkan angka yang valid.")
            continue
            
        if choice == 1:
            print("\n-- Setor Uang --")
            while True:
                try:
                    nominal = int(input("Masukkan jumlah uang yang disetor: Rp "))
                    if nominal <= 0:
                        print("Nominal harus lebih dari 0!")
                        continue
                    break
                except ValueError:
                    print("Input tidak valid, silakan masukkan angka!")
            
            saldo += nominal
            # Simpan juga saldo setelah transaksi ke dalam riwayat
            riwayat_tabungan.append(("Setor", nominal, saldo))
            print(f"Berhasil menabung sebesar Rp {nominal}. Saldo Anda sekarang: Rp {saldo}")
            
        elif choice == 2:
            print("\n-- Tarik Uang --")
            if saldo == 0:
                print("Saldo Anda Rp 0. Belum ada uang yang bisa ditarik.")
            else:
                while True:
                    try:
                        nominal = int(input("Masukkan jumlah uang yang ditarik: Rp "))
                        if nominal <= 0:
                            print("Nominal harus lebih dari 0!")
                            continue
                        if nominal > saldo:
                            print(f"Saldo tidak mencukupi! Saldo Anda saat ini: Rp {saldo}")
                            continue
                        break
                    except ValueError:
                        print("Input tidak valid, silakan masukkan angka!")
                
                saldo -= nominal
                # Simpan juga saldo setelah penarikan ke dalam riwayat
                riwayat_tabungan.append(("Tarik", nominal, saldo))
                print(f"Berhasil menarik uang sebesar Rp {nominal}. Saldo Anda sekarang: Rp {saldo}")
                
        elif choice == 3:
            print("\n=== INFORMASI TABUNGAN ===")
            print(f"Total Saldo Saat Ini: Rp {saldo}")
            print("--------------------------------------------------")
            if not riwayat_tabungan:
                print("Belum ada riwayat transaksi.")
            else:
                print("Riwayat Transaksi:")
                # Ambil jenis, nominal, dan saldo_akhir dari riwayat
                for i, (jenis, nominal, saldo_akhir) in enumerate(riwayat_tabungan):
                    if jenis == "Setor":
                        print(f"{i + 1}. Setor : + Rp {nominal} \t| Saldo menjadi : Rp {saldo_akhir}")
                    elif jenis == "Tarik":
                        print(f"{i + 1}. Tarik : - Rp {nominal} \t| Sisa Saldo    : Rp {saldo_akhir}")
            print("--------------------------------------------------")
            
        elif choice == 4:
            running = False
            print("\nProgram selesai. Terima kasih telah rajin menabung!")
            
        else:
            print("Pilihan tidak valid! Silakan pilih angka 1-4.")

if __name__ == "__main__":
    main()