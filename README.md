# python-project-pacmann
Cashier Project – Naufal Muhamad Adzkia | Project sangat sederhana ini memiliki tujuan utama yakni membuat sistem kasir self-service. Project ini juga ditujukkan untuk tugas Pacmann – Python. Disclaimer: saya sadar sebagai sosok yang masih belajar, tentu masih jauh dari kesempurnaan. Jadi, mohon masukan dan sarannya :D.

# Cara Menggunakan
    1. Jalankan Program
    2. Definisikan class awal dengan menggunakan atribut (misalkan: transaksi_1 = Transaction())
    3. Jalankan beberapa metode sebagai berikut:
        a.  Gunakan metode add_item([<nama_item>, <jumlah_item>, <harga_item>]) untuk menambahkan item ke dalam list transaksi item
        b.	Gunakan metode berikut untuk mengupdate beberapa hal:
            i.	metode update_item_name(<nama_item>, <new_nama_item>) untuk mengganti nama item di dalam list transaksi item
            ii.	metode update_item_qty(<nama_item>, <new_jumlah_item>) untuk mengganti jumlah/kuantitas item di dalam list transaksi item
            iii.metode update_item_price(<nama_item>, <new_harga_item>) untuk mengganti harga per item di dalam list transaksi item
        c.	Gunakan metode delete_item(<nama item>) untuk menghapus item beserta keterangannya dari list transaksi item
        d.	Gunakan metode reset_transaction() untuk mereset seluruh item beserta keterangannya dari list transaksi item
        e.	Gunakan metode check_order() untuk mengecek keseluruhan transaksi di dalam list transaksi item, beserta input data yang sudah diisi sudah benar atau belum.
        g.	Gunakan metode total_price() untuk mengecek total harga beserta diskon yang telah didapatkan berdasarkan belanjaan
# Latar Belakang
    Masalah yang terjadi adalah sistem kasir yang masih manual, dimana masih perlu adanya bantuan penjaga kasir untuk menghitung harga akhir yang akan dibayarkan.

# Objectives
    Tujuan utama dari program ini adalah untuk membuat sistem kasir self-service. Kemudian, berikut adalah rincian dari objectives yang harus dicapai:
        a.	Membuat transaksi masing-masing per customer
        b.	Memasukkan nama item, jumlah item, dan harga item ke dalam list transaksi item
        c.	Mengganti nama item, jumlah item, dan harga item ke dalam list transaksi item
        d.	Menghapus salah satu item di dalam list transaksi item
        e.	Menghapus seluruh item dalam list transaksi item
        f.	Mengecek orderan yang sudah ditambahkan ke dalam list transaksi item
        g.	Menghitung harga total serta harga total setelah diskon

# Fitur
    Programming dalam python dilakukan untuk menjawab tujuan di atas. Adapula beberapa fitur yang dapat digunakan dalam program ini untuk membantu pengoperasian sistem kasir self-service ini.
        a.	Membuat class Transaction() yang kemudian dapat diakses dengan memasukkan transaksi_n = Transaction(). Kemudian, diberikan metode untuk inisialisasi list               awal dengan atribut data_transaksi.
        b.	Membuat metode add_item([<nama_item>, <jumlah_item>, <harga_item>]). Fungsi yang digunakan berupa .append ke dalam list data_transaksi.
        c.	Membuat metode update dengan rincian sebagai berikut dengan mengganti data di index sekian dengan menggunakan nilai baru.
            i.	Membuat metode update_item_name(<nama_item>, <new_nama_item>)
            ii.	Membuat metode update_item_qty(<nama_item>, <new_jumlah_item>)
            iii.	Membuat metode update_item_price(<nama_item>, <new_harga_item>)
        d.	Membuat metode delete_item(<nama item>). Fungsi yang digunakan adalah while yang kemudian menggunakan .remove berdasarkan ketentuan nama_item.
        e.	Membuat metode reset_transaction(). Fungsi yang digunakan adalah membuat atribut data_transaksi menjadi kosong kembali.
        f.	Membuat metode check_order(). Fungsi yang digunakan adalah fungsi conditional sebagai syarat untuk checking kondisi awal, yang dilanjutkan dengan fungsi looping for, dan juga dibantu dengan pembentukan data frame menggunakan Pandas.
        g.	Membuat metode total_price(). Fungsi yang digunakan adalah fungsi conditional sebagai syarat untuk checking kondisi awal, dilanjutkan dengan fungsi looping for, dibantu dengan pembentukan data frame menggunakan Pandas, dan juga fungsi .sum untuk menjumlahkan harga akhir, kemudian diteruskan ke dalam fungsi conditional untuk melihat harga diskon.

            Adapula fitur tambahan untuk menunjang pengerjaan:
        h.	Membuat metode index_transaksi. Fungsi yang digunakan adalah looping for untuk determinasi index yang tersimpan ke dalam list transaksi item.
        i.	Membuat metode check_data_transaksi. Metode ini digunakan untuk mengecek data apa saja yang sudah masuk ke dalam list transaksi item.

# Test Case
Tentunya, program ini telah harus diujicoba dan dievaluasi untuk bisa dioperasikan dengan baik oleh customernya. Dokumentasi ini dibuat sebagai petunjuk               pengoperasian dari sistem kasir self-service ini. Berikut adalah dokumentasi dari pengerjaan:
    
 Test Case 1:
 ![Test 1](https://user-images.githubusercontent.com/112636018/205481356-db789a10-7167-487c-b489-d4a52405e3f5.jpg)
 
 Test Case 2:
 ![Test 2](https://user-images.githubusercontent.com/112636018/205481400-43d1049e-b814-452b-9084-8a8fd0047a87.jpg)

 Test Case 3:
 ![Test 3](https://user-images.githubusercontent.com/112636018/205481404-8b080aa7-0e56-4a11-a1bc-ea2da1c7b9e5.jpg)

 Test Case 4:
 ![Test 4](https://user-images.githubusercontent.com/112636018/205481405-28cc111b-cc15-4035-83c0-0c92022f3a76.jpg)

 Test Case 5:
 ![Test 5](https://user-images.githubusercontent.com/112636018/205481406-f0cf0094-a25c-43bb-b5fe-4662e3e27428.jpg)

 Test Case 6:
 ![Test 6](https://user-images.githubusercontent.com/112636018/205481410-536430c1-713f-4f32-b0b2-d7c822f4b348.jpg)

        
        

