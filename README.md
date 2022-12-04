# python-project-pacmann
Cashier Project – Naufal Muhamad Adzkia
Project sangat sederhana ini memiliki tujuan utama yakni membuat sistem kasir self-service. Project ini juga ditujukkan untuk tugas Pacmann – Python. 
Disclaimer: saya sadar sebagai sosok yang masih belajar, tentu masih jauh dari kesempurnaan. Jadi, mohon masukan dan sarannya :D. 
    1.	Latar Belakang
    Masalah yang terjadi adalah sistem kasir yang masih manual, dimana masih perlu adanya bantuan penjaga kasir untuk menghitung harga akhir yang akan dibayarkan.

    2.	Objectives
    Tujuan utama dari program ini adalah untuk membuat sistem kasir self-service. Kemudian, berikut adalah rincian dari objectives yang harus dicapai:
        a.	Membuat transaksi masing-masing per customer
        b.	Memasukkan nama item, jumlah item, dan harga item ke dalam list transaksi item
        c.	Mengganti nama item, jumlah item, dan harga item ke dalam list transaksi item
        d.	Menghapus salah satu item di dalam list transaksi item
        e.	Menghapus seluruh item dalam list transaksi item
        f.	Mengecek orderan yang sudah ditambahkan ke dalam list transaksi item
        g.	Menghitung harga total serta harga total setelah diskon

    3.	Fitur
    Programming dalam python dilakukan untuk menjawab tujuan di atas. Adapula beberapa fitur yang dapat digunakan dalam program ini untuk membantu pengoperasian sistem     kasir self-service ini.
        a.	Membuat class Transaction() yang kemudian dapat diakses dengan memasukkan transaksi_n = Transaction(). Kemudian, diberikan metode untuk inisialisasi list               awal dengan atribut data_transaksi.
        b.	Membuat metode add_item([<nama_item>, <jumlah_item>, <harga_item>]). Fungsi yang digunakan berupa .append ke dalam list data_transaksi.
        c.	Membuat metode update dengan rincian sebagai berikut dengan mengganti data di index sekian dengan menggunakan nilai baru.
            i.	Membuat metode update_item_name(<nama_item>, <new_nama_item>)
            ii.	Membuat metode update_item_qty(<nama_item>, <new_jumlah_item>)
            iii.	Membuat metode update_item_price(<nama_item>, <new_harga_item>)
        d.	Membuat metode delete_item(<nama item>). Fungsi yang digunakan adalah while yang kemudian menggunakan .remove berdasarkan ketentuan nama_item.
        e.	Membuat metode reset_transaction(). Fungsi yang digunakan adalah membuat atribut data_transaksi menjadi kosong kembali.
        f.	Membuat metode check_order(). Fungsi yang digunakan adalah fungsi conditional sebagai syarat untuk checking kondisi awal, yang dilanjutkan dengan fungsi               looping for, dan juga dibantu dengan pembentukan data frame menggunakan Pandas.
        g.	Membuat metode total_price(). Fungsi yang digunakan adalah fungsi conditional sebagai syarat untuk checking kondisi awal, dilanjutkan dengan fungsi looping             for, dibantu dengan pembentukan data frame menggunakan Pandas, dan juga fungsi .sum untuk menjumlahkan harga akhir, kemudian diteruskan ke dalam fungsi                 conditional untuk melihat harga diskon.
        
              Adapula fitur tambahan untuk menunjang pengerjaan:
        h.	Membuat metode index_transaksi. Fungsi yang digunakan adalah looping for untuk determinasi index yang tersimpan ke dalam list transaksi item.
        i.	Membuat metode check_data_transaksi. Metode ini digunakan untuk mengecek data apa saja yang sudah masuk ke dalam list transaksi item.

    4.	Test Case
    Tentunya, program ini telah harus diujicoba dan dievaluasi untuk bisa dioperasikan dengan baik oleh customernya. Dokumentasi ini dibuat sebagai petunjuk               pengoperasian dari sistem kasir self-service ini. Berikut adalah dokumentasi dari pengerjaan:
