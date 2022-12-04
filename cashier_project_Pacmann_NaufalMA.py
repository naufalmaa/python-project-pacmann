{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 441,
   "id": "bae7a3e1",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from tabulate import tabulate"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 636,
   "id": "a38b1f71",
   "metadata": {},
   "outputs": [],
   "source": [
    "#main\n",
    "#buat class\n",
    "class Transaction:\n",
    "    #metode untuk inisialisasi awal list item transaksi\n",
    "    def __init__(self):\n",
    "        \"\"\"\n",
    "        fungsi untuk inisialisasi list\n",
    "        \"\"\"\n",
    "        self.data_transaksi = list()\n",
    "\n",
    "    #metode untuk mengganti nama, kuantitas, atau harga di dalam list item transaksi   \n",
    "    def add_item(self, nama_item, jumlah_item, harga_item):\n",
    "        \"\"\"\n",
    "        fungsi untuk menambahkan data transaksi\n",
    "        \n",
    "        parameters\n",
    "        nama_item      :str - nama item yang akan ditambahkan\n",
    "        jumlah_item    :int - jumlah item yang akan dibeli\n",
    "        harga_item     :int - harga per item yang akan dibeli\n",
    "        \"\"\"\n",
    "        self.data_transaksi.append([nama_item, jumlah_item, harga_item])\n",
    "        print(\"Item berhasil ditambahkan!\")\n",
    "    \n",
    "    #metode untuk mengganti nama, kuantitas, atau harga di dalam list item transaksi\n",
    "    def update_item_name(self, nama_item, new_nama_item):\n",
    "        \"\"\"\n",
    "        fungsi untuk mengupdate nama item\n",
    "        \"\"\"\n",
    "        self.data_transaksi[self.index_transaksi(nama_item)][0] = new_nama_item\n",
    "        print(\"Nama item berhasil diganti!\")\n",
    "        \n",
    "    def update_item_qty(self, nama_item, new_jumlah_item):\n",
    "        \"\"\"\n",
    "        fungsi untuk mengupdate jumlah item\n",
    "        \"\"\"\n",
    "        self.data_transaksi[self.index_transaksi(nama_item)][1] = new_jumlah_item\n",
    "        print(\"Jumlah item berhasil diganti!\")\n",
    "    \n",
    "    def update_item_price(self, nama_item, new_harga_item):\n",
    "        \"\"\"\n",
    "        fungsi untuk mengupdate harga per item\n",
    "        \"\"\"\n",
    "        self.data_transaksi[self.index_transaksi(nama_item)][2] = new_harga_item\n",
    "        print(\"Harga item berhasil diganti!\")\n",
    "    \n",
    "    #metode untuk memberi index di dalam list item transaksi\n",
    "    def index_transaksi(self, nama_item):\n",
    "        \"\"\"\n",
    "        fungsi mengembalikan nilai index dari baris yang mengandung value 'nama_item'\n",
    "\n",
    "        parameters\n",
    "        nama_item   : str   nama item yang akan ditambahkan\n",
    "\n",
    "        return\n",
    "        i       : int   index dari baris yang mengandung judul\n",
    "        \"\"\"\n",
    "        for i in range(len(self.data_transaksi)):\n",
    "            if nama_item == self.data_transaksi[i][0]:\n",
    "                return i\n",
    "    \n",
    "    #metode untuk menghapus salah satu item yang tidak jadi dibeli di dalam list item transaksi\n",
    "    def delete_item(self, nama_item):\n",
    "        \"\"\"\n",
    "        fungsi untuk menghapus baris pada suatu item yang tidak jadi dibeli\n",
    "        \"\"\"\n",
    "        \n",
    "        del_list = [nama_item, self.data_transaksi[self.index_transaksi(nama_item)][1], self.data_transaksi[self.index_transaksi(nama_item)][2]]\n",
    "\n",
    "        while(del_list in self.data_transaksi):\n",
    "            self.data_transaksi.remove(del_list)\n",
    "        \n",
    "        print(\"Item berhasil di delete!\")\n",
    "        \n",
    "    #metode untuk reset semua transaksi\n",
    "    def reset_transaction(self):\n",
    "        \"\"\"\n",
    "        fungsi untuk reset semua transaksi\n",
    "        \"\"\"\n",
    "        self.data_transaksi = list()\n",
    "        print(\"Semua item berhasil di delete!\")\n",
    "        \n",
    "    #metode untuk mengecek kembali pesanan di dalam list item transaksi\n",
    "    def check_order(self):\n",
    "        \"\"\"\n",
    "        fungsi untuk menampilkan seluruh order dari transaksi,\n",
    "        \"\"\"\n",
    "        if self.data_transaksi == []:\n",
    "            \"\"\"\n",
    "            Jika list kosong, akan menampilkan strip pada setiap kolom\n",
    "            \"\"\"\n",
    "            data = {'Nama Item': ['-'],\n",
    "                    'Jumlah Item': [0],\n",
    "                    'Harga/Item': [0],\n",
    "                    'Harga Total': [0]}\n",
    "            df = pd.DataFrame(data)  \n",
    "            print(df.to_markdown())\n",
    "        \n",
    "        else:\n",
    "            \"\"\"\n",
    "            menambahkan list pada tabel\n",
    "            \"\"\"\n",
    "            for i in range(len(self.data_transaksi)):\n",
    "                if isinstance(self.data_transaksi[i][0], str) and isinstance(self.data_transaksi[i][1], int) and isinstance(self.data_transaksi[i][2], int):              \n",
    "                    data = pd.DataFrame(self.data_transaksi)\n",
    "                    data.columns = ['Nama Item', 'Jumlah Item', 'Harga/Item']\n",
    "\n",
    "                    \"\"\"\n",
    "                    memanggil harga total\n",
    "                    \"\"\"\n",
    "                    data['Harga Total'] = data['Jumlah Item'] * data['Harga/Item']\n",
    "\n",
    "                    print(\"Pemesanan Berhasil!\\n\\n\")\n",
    "                    print(data.to_markdown())\n",
    "\n",
    "                    return\n",
    "\n",
    "                else:\n",
    "                    print(\"Terdapat input yang belum sesuai!\")\n",
    "                    return\n",
    "    \n",
    "    #metode untuk mencari total harga yang harus dibayarkan beserta diskon yang didapatkan\n",
    "    def total_price(self):\n",
    "        \"\"\"\n",
    "        fungsi untuk mencari total harga yang harus dibayarkan\n",
    "        \"\"\"\n",
    "        if self.data_transaksi == []:\n",
    "            \"\"\"\n",
    "            Jika list kosong, akan menampilkan strip pada setiap kolom\n",
    "            \"\"\"\n",
    "            data = {'Nama Item': ['-'],\n",
    "                    'Jumlah Item': [0],\n",
    "                    'Harga/Item': [0],\n",
    "                    'Harga Total': [0]}\n",
    "            df = pd.DataFrame(data)  \n",
    "            print(df.to_markdown())\n",
    "        \n",
    "        else:\n",
    "            \"\"\"\n",
    "            menambahkan list pada tabel\n",
    "            \"\"\"\n",
    "            for i in range(len(self.data_transaksi)):\n",
    "                if isinstance(self.data_transaksi[i][0], str) and isinstance(self.data_transaksi[i][1], int) and isinstance(self.data_transaksi[i][2], int):              \n",
    "                    data = pd.DataFrame(self.data_transaksi)\n",
    "                    data.columns = ['Nama Item', 'Jumlah Item', 'Harga/Item']\n",
    "\n",
    "                    \"\"\"\n",
    "                    memanggil harga total\n",
    "                    \"\"\"\n",
    "                    data['Harga Total'] = data['Jumlah Item'] * data['Harga/Item']\n",
    "\n",
    "                    print(data.to_markdown())\n",
    "                    print(f\"\\n\\nHarga Total = Rp.{data['Harga Total'].sum()}\")\n",
    "        \n",
    "                    \"\"\"\n",
    "                    menggunakan conditioning untuk diskon 5%, 8%, dan 10%\n",
    "                    \"\"\"\n",
    "                    if data['Harga Total'].sum() < 200_000:\n",
    "                        pass\n",
    "\n",
    "                    elif (data['Harga Total'].sum() > 200_000) and (data['Harga Total'].sum() <= 300_000):\n",
    "                        harga_diskon = data['Harga Total'].sum() * 0.95\n",
    "                        print(f\"\\n\\nAnda mendapatkan diskon 5%! \\n\\nSetelah diskon, harga total menjadi Rp.{harga_diskon}\")\n",
    "\n",
    "                    elif (data['Harga Total'].sum() > 300_000) and (data['Harga Total'].sum() <= 500_000):\n",
    "                        harga_diskon = data['Harga Total'].sum() * 0.92\n",
    "                        print(f\"\\n\\nAnda mendapatkan diskon 8%! \\n\\nSetelah diskon, harga total menjadi Rp.{harga_diskon}\")\n",
    "\n",
    "                    elif (data['Harga Total'].sum() > 500_000):\n",
    "                        harga_diskon = data['Harga Total'].sum() * 0.90\n",
    "                        print(f\"\\n\\nAnda mendapatkan diskon 10%! \\n\\nSetelah diskon, harga total menjadi Rp.{harga_diskon}\")\n",
    "\n",
    "                    else:\n",
    "                        pass\n",
    "\n",
    "                    return\n",
    "\n",
    "    #metode untuk check data di dalam list item transaksi\n",
    "    def check_data_transaksi(self):\n",
    "        print(f\"Item yang dibeli adalah: {self.data_transaksi}\")\n",
    "    \n",
    "    \n",
    "        \n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 637,
   "id": "f36c55a6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Item yang dibeli adalah: []\n"
     ]
    }
   ],
   "source": [
    "#running metode untuk pertama kali\n",
    "transaksi_1 = Transaction()\n",
    "#check awal list item transaksi\n",
    "transaksi_1.check_data_transaksi()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 638,
   "id": "1e1e9f97",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Item berhasil ditambahkan!\n",
      "Item berhasil ditambahkan!\n",
      "Item berhasil ditambahkan!\n",
      "Item berhasil ditambahkan!\n",
      "Item berhasil ditambahkan!\n",
      "Item yang dibeli adalah: [['Ayam Goreng', 3, 20000], ['Bumbu Dapur', 4, 15000], ['Minyak Goreng', 2, 20000], ['Panci', 1, 250000], ['Tabung Gas', 1, 150000]]\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "Test 1:\n",
    "Menambahkan item berikut:\n",
    "Nama Item: Ayam Goreng, Qty: 3, Harga: 20_000\n",
    "Nama Item: Bumbu Dapur, Qty: 4, Harga: 15_000\n",
    "Nama Item: Minyak Goreng, Qty: 2, Harga: 20_000\n",
    "Nama Item: Panci, Qty: 1, Harga: 250_000\n",
    "Nama Item: Tabung Gas, Qty: 1, Harga: 150_000\n",
    "\"\"\"\n",
    "transaksi_1.add_item(\"Ayam Goreng\", 3, 20_000)\n",
    "transaksi_1.add_item(\"Bumbu Dapur\", 4, 15_000)\n",
    "transaksi_1.add_item(\"Minyak Goreng\", 2, 20_000)\n",
    "transaksi_1.add_item(\"Panci\", 1, 250_000)\n",
    "transaksi_1.add_item(\"Tabung Gas\", 1, 150_000)\n",
    "#check kembali list\n",
    "transaksi_1.check_data_transaksi()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 639,
   "id": "2f95d44e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Pemesanan Berhasil!\n",
      "\n",
      "\n",
      "|    | Nama Item     |   Jumlah Item |   Harga/Item |   Harga Total |\n",
      "|---:|:--------------|--------------:|-------------:|--------------:|\n",
      "|  0 | Ayam Goreng   |             3 |        20000 |         60000 |\n",
      "|  1 | Bumbu Dapur   |             4 |        15000 |         60000 |\n",
      "|  2 | Minyak Goreng |             2 |        20000 |         40000 |\n",
      "|  3 | Panci         |             1 |       250000 |        250000 |\n",
      "|  4 | Tabung Gas    |             1 |       150000 |        150000 |\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "Test 2:\n",
    "Melihat item yang sudah masuk ke dalam list item transaksi\n",
    "\"\"\"\n",
    "#dapat digunakan metode check_order untuk melihat list item transaksi\n",
    "transaksi_1.check_order()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 640,
   "id": "1ab06264",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "|    | Nama Item     |   Jumlah Item |   Harga/Item |   Harga Total |\n",
      "|---:|:--------------|--------------:|-------------:|--------------:|\n",
      "|  0 | Ayam Goreng   |             3 |        20000 |         60000 |\n",
      "|  1 | Bumbu Dapur   |             4 |        15000 |         60000 |\n",
      "|  2 | Minyak Goreng |             2 |        20000 |         40000 |\n",
      "|  3 | Panci         |             1 |       250000 |        250000 |\n",
      "|  4 | Tabung Gas    |             1 |       150000 |        150000 |\n",
      "\n",
      "\n",
      "Harga Total = Rp.560000\n",
      "\n",
      "\n",
      "Anda mendapatkan diskon 10%! \n",
      "\n",
      "Setelah diskon, harga total menjadi Rp.504000.0\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "Test 3:\n",
    "Melihat total harga dan diskon berdasarkan item yang akan dibeli\n",
    "\"\"\"\n",
    "transaksi_1.total_price()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 641,
   "id": "6b7efaf0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Jumlah item berhasil diganti!\n",
      "Item yang dibeli adalah: [['Ayam Goreng', 3, 20000], ['Bumbu Dapur', 3, 15000], ['Minyak Goreng', 2, 20000], ['Panci', 1, 250000], ['Tabung Gas', 1, 150000]]\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "Test 4:\n",
    "Mengganti kuantitas Bumbu Dapur dari 4 menjadi 3\n",
    "\"\"\"\n",
    "transaksi_1.update_item_qty(\"Bumbu Dapur\", 3)\n",
    "#check kembali list\n",
    "transaksi_1.check_data_transaksi()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 642,
   "id": "30070812",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Pemesanan Berhasil!\n",
      "\n",
      "\n",
      "|    | Nama Item     |   Jumlah Item |   Harga/Item |   Harga Total |\n",
      "|---:|:--------------|--------------:|-------------:|--------------:|\n",
      "|  0 | Ayam Goreng   |             3 |        20000 |         60000 |\n",
      "|  1 | Bumbu Dapur   |             3 |        15000 |         45000 |\n",
      "|  2 | Minyak Goreng |             2 |        20000 |         40000 |\n",
      "|  3 | Panci         |             1 |       250000 |        250000 |\n",
      "|  4 | Tabung Gas    |             1 |       150000 |        150000 |\n"
     ]
    }
   ],
   "source": [
    "#dapat digunakan kembali metode check_order untuk melihat list item transaksi\n",
    "transaksi_1.check_order()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 643,
   "id": "c5991391",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Item berhasil di delete!\n",
      "Item yang dibeli adalah: [['Ayam Goreng', 3, 20000], ['Bumbu Dapur', 3, 15000], ['Panci', 1, 250000], ['Tabung Gas', 1, 150000]]\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "Test 5:\n",
    "Menghapus item Minyak Goreng dari list\n",
    "\"\"\"\n",
    "transaksi_1.delete_item(\"Minyak Goreng\")\n",
    "#check kembali list\n",
    "transaksi_1.check_data_transaksi()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 644,
   "id": "ba3dca3b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Pemesanan Berhasil!\n",
      "\n",
      "\n",
      "|    | Nama Item   |   Jumlah Item |   Harga/Item |   Harga Total |\n",
      "|---:|:------------|--------------:|-------------:|--------------:|\n",
      "|  0 | Ayam Goreng |             3 |        20000 |         60000 |\n",
      "|  1 | Bumbu Dapur |             3 |        15000 |         45000 |\n",
      "|  2 | Panci       |             1 |       250000 |        250000 |\n",
      "|  3 | Tabung Gas  |             1 |       150000 |        150000 |\n"
     ]
    }
   ],
   "source": [
    "#dapat digunakan kembali metode check_order untuk melihat list item transaksi\n",
    "transaksi_1.check_order()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 645,
   "id": "1ef050d4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Semua item berhasil di delete!\n",
      "Item yang dibeli adalah: []\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "Test 6:\n",
    "Reset semua item dari list\n",
    "\"\"\"\n",
    "transaksi_1.reset_transaction()\n",
    "#check kembali list\n",
    "transaksi_1.check_data_transaksi()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 646,
   "id": "7123100c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "|    | Nama Item   |   Jumlah Item |   Harga/Item |   Harga Total |\n",
      "|---:|:------------|--------------:|-------------:|--------------:|\n",
      "|  0 | -           |             0 |            0 |             0 |\n"
     ]
    }
   ],
   "source": [
    "#dapat digunakan kembali metode check_order untuk melihat list item transaksi\n",
    "transaksi_1.check_order()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
