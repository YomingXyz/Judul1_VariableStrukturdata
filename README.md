<img width="1252" height="261" alt="Cuplikan layar 2026-04-28 213204" src="https://github.com/user-attachments/assets/26c3a53c-b90a-4fef-9aa8-a095b877e2d8" /><img width="1252" height="261" alt="Cuplikan layar 2026-04-28 213204" src="https://github.com/user-attachments/assets/aab3b783-14b8-4d38-915c-0ae9136f4803" />A. Judul Program
PROGRAM MANAJEMEN TABUNGAN

B. Deskripsi Singkat
Program tersebut berfungsi sebagai sistem sederhana untuk manajemen keuangan atau tabungan. Pengguna dapat menyetor uang (menambah saldo), menarik uang (mengurangi saldo), serta melihat total saldo saat ini beserta riwayat transaksi yang telah dilakukan. Program berjalan dalam loop hingga pengguna memilih untuk keluar dari program. Selain itu, program juga dilengkapi dengan validasi input untuk memastikan data yang dimasukkan berupa angka yang valid, nominal tidak boleh nol atau minus, dan memastikan penarikan tidak melebihi jumlah saldo yang ada agar tidak menimbulkan error atau saldo negatif. Struktur data yang digunakan dalam program ini adalah variabel integer untuk menyimpan nilai saldo, dan list 1 dimensi, yaitu variabel riwayat_tabungan yang menyimpan kumpulan rekam jejak transaksi. Setiap elemen dalam list tersebut berupa tuple (jenis, nominal, saldo_akhir) yang menyimpan pasangan tipe transaksi (Setor/Tarik), jumlah uangnya, dan sisa saldo setelah transaksi terjadi. Operasi yang dilakukan meliputi penambahan data menggunakan append, penelusuran data menggunakan perulangan for dengan enumerate, serta pembaruan data secara matematis pada variabel saldo.

C. Source Code
Penjelasan kode per baris:
<img width="711" height="387" alt="Cuplikan layar 2026-04-28 215414" src="https://github.com/user-attachments/assets/93e821b0-21f4-475d-a7c0-5cd2f4b6921c" />
judul program
membuat fungsi menu()
mencetak judul menu sistem manajemen tabungan
mencetak menu pertama untuk setor uang (menabung)
mencetak menu kedua untuk tarik uang
mencetak menu ketiga untuk menampilkan saldo dan riwayat
mencetak menu keempat untuk keluar dari program
membuat fungsi main() sebagai program utama
membuat list variabel riwayat_tabungan = [ ] yang masih berupa list kosong
membuat variabel saldo = 0 untuk menyimpan jumlah uang
membuat variabel running yang bernilai boolean True agar program berjalan
<img width="1079" height="545" alt="Cuplikan layar 2026-04-28 215551" src="https://github.com/user-attachments/assets/1d859a6b-9d16-4249-a458-c6408a7beb2a" />
perulangan while yang membuat program terus berjalan selama kondisi True
menampilkan fungsi menu()
program akan mencoba
meminta user untuk input pilihan menu yang bernilai integer
pengecualian jika value yang diinputkan error (bukan angka)
program akan mencetak peringatan masukkan angka yang valid
continue berfungsi untuk membuat program kembali ke looping awal (menampilkan menu)
pengondisian jika user memilih menu 1
mencetak tulisan "-- Setor Uang --"
perulangan saat kondisi True
program akan mencoba
meminta user untuk input nominal uang yang disetor dan menyimpannya di variabel nominal dengan tipe data integer
pengondisian jika nominal yang diinputkan kurang dari atau sama dengan 0
program mencetak "Nominal harus lebih dari 0!"
continue untuk membuat program mengulang permintaan input nominal
break berfungsi untuk mengeluarkan dari perulangan input nominal jika input sudah benar
pengondisian jika value yang diinputkan error (bukan angka)
program akan mencetak input tidak valid dan meminta untuk memasukkan angka
<img width="1034" height="140" alt="Cuplikan layar 2026-04-28 215646" src="https://github.com/user-attachments/assets/77f1af97-5d10-4ed9-9398-eff14854b188" />
variabel saldo akan ditambahkan dengan nilai dari variabel nominal
jenis transaksi "Setor", nilai nominal, dan saldo akhir akan tersimpan di list riwayat_tabungan menggunakan operasi append
mencetak pesan berhasil menabung beserta jumlah nominal dan total saldo saat ini
<img width="1080" height="494" alt="Cuplikan layar 2026-04-28 215807" src="https://github.com/user-attachments/assets/9a3aa65b-ec6d-4e65-9e66-942eb23f31e3" />
pengondisian jika user memilih menu 2
mencetak tulisan "-- Tarik Uang --"
kondisi jika variabel saldo bernilai 0
program mencetak “Saldo Anda Rp 0. Belum ada uang yang bisa ditarik.”
else, kondisi jika variabel saldo lebih dari 0
perulangan saat kondisi True
program akan mencoba
meminta user untuk input nominal uang yang ditarik dan menyimpannya di variabel nominal dengan tipe integer
pengondisian jika nominal kurang dari atau sama dengan 0
program mencetak "Nominal harus lebih dari 0!" dan continue untuk mengulang input
pengondisian jika nominal yang ditarik lebih besar dari variabel saldo
program mencetak "Saldo tidak mencukupi!" beserta info saldo saat ini dan continue untuk mengulang input
break berfungsi untuk mengeluarkan dari perulangan input nominal jika input valid
pengondisian jika value yang diinputkan error
program akan mencetak input tidak valid dan meminta untuk memasukkan angka
<img width="1060" height="151" alt="Cuplikan layar 2026-04-28 215833" src="https://github.com/user-attachments/assets/42e86bdd-cd08-4bcc-ae44-906cf45417db" />
variabel saldo akan dikurangi dengan nilai dari variabel nominal
jenis transaksi "Tarik", nilai nominal, dan saldo akhir akan tersimpan di list riwayat_tabungan menggunakan operasi append
mencetak pesan berhasil menarik uang beserta jumlah ditarik dan sisa saldo saat ini
<img width="1150" height="431" alt="Cuplikan layar 2026-04-28 215954" src="https://github.com/user-attachments/assets/6a62003f-45cd-4c12-b205-f7606c2a2bc3" />
pengondisian jika user memilih menu 3
mencetak judul "=== INFORMASI TABUNGAN ==="
mencetak total saldo saat ini dari variabel saldo
mencetak garis pembatas
kondisi jika variabel riwayat_tabungan adalah list kosong
program mencetak “Belum ada riwayat transaksi.”
else, kondisi jika list riwayat_tabungan sudah terisi
program mencetak tulisan "Riwayat Transaksi:"
perulangan for untuk melakukan iterasi dengan operasi enumerate, mengambil jenis, nominal, dan saldo_akhir yang ada pada list riwayat_tabungan
pengondisian jika jenis == "Setor"
mencetak nomor urut (index ditambah satu), jenis transaksi setor, nominal uang dengan tanda tambah (+), dan jumlah saldo menjadi
pengondisian jika jenis == "Tarik"
mencetak nomor urut (index ditambah satu), jenis transaksi tarik, nominal uang dengan tanda kurang (-), dan jumlah sisa saldo
mencetak garis pembatas
<img width="938" height="269" alt="Cuplikan layar 2026-04-28 220006" src="https://github.com/user-attachments/assets/124efe71-7a23-490b-bbda-d96db7a99930" />
pengondisian jika user input menu 4
variabel running akan diubah menjadi False sehingga program berhenti
mencetak “Program selesai. Terima kasih telah rajin menabung!”
kondisi jika user menginputkan selain angka 1, 2, 3 dan 4
program mencetak pilihan tidak valid! Silakan pilih angka 1-4.
entry point, agar program hanya berjalan saat dijalankan langsung dan jika diimport ke file lain program tidak otomatis berjalan

D. Output Program
Penjelasan Output:
Program akan langsung menampilkan menu saat dijalankan dan meminta user untuk menginputkan pilihan menu yang diinginkan. Saat user memilih menu 1, program meminta user untuk menginputkan jumlah uang yang disetor. User menginputkan nominal 100000. Program akan mencetak pesan bahwa berhasil menabung dan saldo menjadi Rp 100000. Selanjutnya, program akan melakukan perulangan dengan menampilkan menu utama. User memilih menu 1 lagi dan menginputkan nominal 50000. Program menampilkan pesan berhasil menabung dan saldo terupdate menjadi Rp 150000. Program akan mengulang dan menampilkan menu kembali. Tahap selanjutnya, user memilih menu 2 (Tarik Uang). Program meminta input nominal uang yang ditarik, lalu user menginputkan angka 30000. Program menampilkan pesan berhasil menarik uang dan menampilkan sisa saldo yang telah berkurang menjadi Rp 120000. Lalu, program kembali ke menu dan user menginputkan menu 3. Program akan menampilkan Informasi Tabungan yang berisi Total Saldo Saat Ini yaitu Rp 120000, beserta Riwayat Transaksi di bawahnya secara berurutan (Setor Rp 100000, Setor Rp 50000, dan Tarik Rp 30000 lengkap dengan jumlah saldo akhir di setiap barisnya). Selanjutnya, user menginputkan menu 4 untuk keluar, program mencetak pesan terima kasih, dan program pun telah selesai dijalankan.
