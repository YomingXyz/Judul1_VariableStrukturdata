A. PROGRAM MANAJEMEN TABUNGAN

B. Deskripsi Singkat
Program tersebut berfungsi sebagai sistem sederhana untuk manajemen keuangan atau tabungan. Pengguna dapat menyetor uang (menambah saldo), menarik uang (mengurangi saldo), serta melihat total saldo saat ini beserta riwayat transaksi yang telah dilakukan. Program berjalan dalam loop hingga pengguna memilih untuk keluar dari program. Selain itu, program juga dilengkapi dengan validasi input untuk memastikan data yang dimasukkan berupa angka yang valid, nominal tidak boleh nol atau minus, dan memastikan penarikan tidak melebihi jumlah saldo yang ada agar tidak menimbulkan error atau saldo negatif. Struktur data yang digunakan dalam program ini adalah variabel integer untuk menyimpan nilai saldo, dan list 1 dimensi, yaitu variabel riwayat_tabungan yang menyimpan kumpulan rekam jejak transaksi. Setiap elemen dalam list tersebut berupa tuple (jenis, nominal, saldo_akhir) yang menyimpan pasangan tipe transaksi (Setor/Tarik), jumlah uangnya, dan sisa saldo setelah transaksi terjadi. Operasi yang dilakukan meliputi penambahan data menggunakan append, penelusuran data menggunakan perulangan for dengan enumerate, serta pembaruan data secara matematis pada variabel saldo.

C. Source Code
Penjelasan kode per baris:
<img width="711" height="387" alt="Cuplikan layar 2026-04-28 215414" src="https://github.com/user-attachments/assets/93e821b0-21f4-475d-a7c0-5cd2f4b6921c" />
1. judul program
   
2. membuat fungsi menu()
   
3.mencetak judul menu sistem manajemen tabungan

4.mencetak menu pertama untuk setor uang (menabung)

5.mencetak menu kedua untuk tarik uang

6.mencetak menu ketiga untuk menampilkan saldo dan riwayat

7.mencetak menu keempat untuk keluar dari program

8.membuat fungsi main() sebagai program utama

9.membuat list variabel riwayat_tabungan = [ ] yang masih berupa list kosong

10.membuat variabel saldo = 0 untuk menyimpan jumlah uang

11.membuat variabel running yang bernilai boolean True agar program berjalan

<img width="1079" height="545" alt="Cuplikan layar 2026-04-28 215551" src="https://github.com/user-attachments/assets/1d859a6b-9d16-4249-a458-c6408a7beb2a" />
12.perulangan while yang membuat program terus berjalan selama kondisi True

13.menampilkan fungsi menu()

14.program akan mencoba

15.meminta user untuk input pilihan menu yang bernilai integer

16.pengecualian jika value yang diinputkan error (bukan angka)

17.program akan mencetak peringatan masukkan angka yang valid

18.continue berfungsi untuk membuat program kembali ke looping awal (menampilkan menu)

19.pengondisian jika user memilih menu 1

20.mencetak tulisan "-- Setor Uang --"

21.perulangan saat kondisi True

22.program akan mencoba

23.meminta user untuk input nominal uang yang disetor dan menyimpannya di variabel nominal dengan tipe data integer

24.pengondisian jika nominal yang diinputkan kurang dari atau sama dengan 0

25.program mencetak "Nominal harus lebih dari 0!"

26.continue untuk membuat program mengulang permintaan input nominal

27.break berfungsi untuk mengeluarkan dari perulangan input nominal jika input sudah benar

28.pengondisian jika value yang diinputkan error (bukan angka)

29.program akan mencetak input tidak valid dan meminta untuk memasukkan angka

<img width="1034" height="140" alt="Cuplikan layar 2026-04-28 215646" src="https://github.com/user-attachments/assets/77f1af97-5d10-4ed9-9398-eff14854b188" />

30.variabel saldo akan ditambahkan dengan nilai dari variabel nominal

31.jenis transaksi "Setor", nilai nominal, dan saldo akhir akan tersimpan di list riwayat_tabungan menggunakan operasi append

32.mencetak pesan berhasil menabung beserta jumlah nominal dan total saldo saat ini

<img width="1080" height="494" alt="Cuplikan layar 2026-04-28 215807" src="https://github.com/user-attachments/assets/9a3aa65b-ec6d-4e65-9e66-942eb23f31e3" />

33.pengondisian jika user memilih menu 2

34.mencetak tulisan "-- Tarik Uang --"

35.kondisi jika variabel saldo bernilai 0

36.program mencetak “Saldo Anda Rp 0. Belum ada uang yang bisa ditarik.”

37.else, kondisi jika variabel saldo lebih dari 0

38.perulangan saat kondisi True

39.program akan mencoba

40.meminta user untuk input nominal uang yang ditarik dan menyimpannya di variabel nominal dengan tipe integer

41.pengondisian jika nominal kurang dari atau sama dengan 0

42.program mencetak "Nominal harus lebih dari 0!" dan continue untuk mengulang input

43.pengondisian jika nominal yang ditarik lebih besar dari variabel saldo

44.program mencetak "Saldo tidak mencukupi!" beserta info saldo saat ini dan continue untuk mengulang input

45.break berfungsi untuk mengeluarkan dari perulangan input nominal jika input valid

46.pengondisian jika value yang diinputkan error

47.program akan mencetak input tidak valid dan meminta untuk memasukkan angka

<img width="1060" height="151" alt="Cuplikan layar 2026-04-28 215833" src="https://github.com/user-attachments/assets/42e86bdd-cd08-4bcc-ae44-906cf45417db" />

48.variabel saldo akan dikurangi dengan nilai dari variabel nominal

49.jenis transaksi "Tarik", nilai nominal, dan saldo akhir akan tersimpan di list riwayat_tabungan menggunakan operasi append

50.mencetak pesan berhasil menarik uang beserta jumlah ditarik dan sisa saldo saat ini

<img width="1150" height="431" alt="Cuplikan layar 2026-04-28 215954" src="https://github.com/user-attachments/assets/6a62003f-45cd-4c12-b205-f7606c2a2bc3" />

51.pengondisian jika user memilih menu 3

52.mencetak judul "=== INFORMASI TABUNGAN ==="

53.mencetak total saldo saat ini dari variabel saldo

54.mencetak garis pembatas

55.kondisi jika variabel riwayat_tabungan adalah list kosong

56.program mencetak “Belum ada riwayat transaksi.”

57.else, kondisi jika list riwayat_tabungan sudah terisi

58.program mencetak tulisan "Riwayat Transaksi:"

59.perulangan for untuk melakukan iterasi dengan operasi enumerate, mengambil jenis, nominal, dan saldo_akhir yang ada pada list riwayat_tabungan

60.pengondisian jika jenis == "Setor"

61.mencetak nomor urut (index ditambah satu), jenis transaksi setor, nominal uang dengan tanda tambah (+), dan jumlah saldo menjadi

62.pengondisian jika jenis == "Tarik"

63.mencetak nomor urut (index ditambah satu), jenis transaksi tarik, nominal uang dengan tanda kurang (-), dan jumlah sisa saldo

64.mencetak garis pembatas

<img width="938" height="269" alt="Cuplikan layar 2026-04-28 220006" src="https://github.com/user-attachments/assets/124efe71-7a23-490b-bbda-d96db7a99930" />

65.pengondisian jika user input menu 4

66.variabel running akan diubah menjadi False sehingga program berhenti

67.mencetak “Program selesai. Terima kasih telah rajin menabung!”

68.kondisi jika user menginputkan selain angka 1, 2, 3 dan 4

69.program mencetak pilihan tidak valid! Silakan pilih angka 1-4.

70.entry point, agar program hanya berjalan saat dijalankan langsung dan jika diimport ke file lain program tidak otomatis berjalan.

D. Output Program
<img width="839" height="970" alt="Cuplikan layar 2026-04-28 223749" src="https://github.com/user-attachments/assets/101e4584-b392-4ab4-b5e1-90a3ea813cc2" />
<img width="702" height="523" alt="Cuplikan layar 2026-04-28 223801" src="https://github.com/user-attachments/assets/b36691e0-0cfd-408f-8f52-ae1c09e30d0f" />

Penjelasan Output:
Program akan langsung menampilkan menu saat dijalankan dan meminta user untuk menginputkan pilihan menu yang diinginkan. Saat user memilih menu 1, program meminta user untuk menginputkan jumlah uang yang disetor. User menginputkan nominal 100000. Program akan mencetak pesan bahwa berhasil menabung dan saldo menjadi Rp 100000. Selanjutnya, program akan melakukan perulangan dengan menampilkan menu utama. User memilih menu 1 lagi dan menginputkan nominal 50000. Program menampilkan pesan berhasil menabung dan saldo terupdate menjadi Rp 150000. Program akan mengulang dan menampilkan menu kembali. Tahap selanjutnya, user memilih menu 2 (Tarik Uang). Program meminta input nominal uang yang ditarik, lalu user menginputkan angka 30000. Program menampilkan pesan berhasil menarik uang dan menampilkan sisa saldo yang telah berkurang menjadi Rp 120000. Lalu, program kembali ke menu dan user menginputkan menu 3. Program akan menampilkan Informasi Tabungan yang berisi Total Saldo Saat Ini yaitu Rp 120000, beserta Riwayat Transaksi di bawahnya secara berurutan (Setor Rp 100000, Setor Rp 50000, dan Tarik Rp 30000 lengkap dengan jumlah saldo akhir di setiap barisnya). Selanjutnya, user menginputkan menu 4 untuk keluar, program mencetak pesan terima kasih, dan program pun telah selesai dijalankan.

E. LINK VIDIO
https://www.youtube.com/watch?v=MN51E3Tg6Bg
