# Self-Service Cashier System
Self-Service Cashier System sederhana dengan menggunakan bahasa pemrograman python
## Background Problem
Andi merupakan seorang pemiliki supermarket besar di salah satu kota di Indonesia. Andi berencana mengembangkan sistem kasir 
yang bersifat self-service, sehingga customer bisa langsung memasukkan nama item, jumlah item, dan harga item.
## Requirements/Objectives
- Membuat proses untuk menyelesaikan proses transaksi pada kasir yang bersifat self-service
- Membuat proses untuk `add_item()` dengan parameter `nama_item`, `jumlah_item`, `harga_item`
- Membuat proses untuk `update_item_name`, `update_item_quantity`, `update_item_price` berdasarkan parameter `nama_item`
- Membuat proses untuk `delete_item` untuk menghapus suatu item berdasarkan parameter `nama_item`
- Membuat proses untuk `reset_transaction` untuk menghapus semua data transaksi
- Membuat proses untuk `check_order` untuk mengecek kembali detail item yang telah diinputkan
- membuat proses untuk menghitung `total_price` untuk mengetahui detail pembayaran, dengan ketentuan diskon :
  - Jika total belanja di atas Rp.200.000 maka akan mendapatkan diskon 5%
  - Jika total belanja di atas Rp.300.000 maka akan mendapatkan diskon 8%
  - Jika total belanja di atas Rp.500.000 maka akan mendapatkan diskon 10%
## Alur Program / Flowchart
- Membuat objek dari `class Transaction`
```
class Transaction:
```
- Membuat attribute class berisi dataframe kosong
```
empty_dict = {"Item", "Quantity", "Price"}
data = pd.DataFrame(empty_dict)
```
- Menginisialisasi attribute mengenai nama toko
```
def ___init___:
    nama toko
```
- Mendefinisikan function `add_item()` dengan parameter `nama_item`, `jumlah_item`, `harga_item`
- Mendefinisikan function `update_item_name` untuk merubah nama item 
- Mendefinisikan function `update_item_quantity` untuk merubah jumlah item
- Mendefinisikan function `update_item_price` untuk merubah harga ite
- Mendefinisikan function `delete_item` untuk menghapus suatu item
- Mendefinisikan function `reset_transaction` untuk menghapus semua data transaksi
- Mendefinisikan function `check_order` untuk mengecek kembali detail item yang telah diinputkan
- Mendefinisikan function `total_price` untuk mengetahui detail pembayaran
## Cara Penggunaan Program
- Download semua file/module Python ke dalam satu direktori lokal.
- Buka terminal dan sesuaikan lokasi direktori lokal.
- Jalankan module python `Cashier_System.py` di terminal.
- Output akan ditampilkan sesuai Case yang telah diskenariokan
## Penjelasan Code
Script `Cashier_System.py` berfungsi untuk menjalankan program yang berisi function diatas, sekaligus melakukan test case
### Class Transaction
```
class Transaction:
    """Fungsi dasar sistem kasir """
```
Class Transaction akan menjadi class yang berisikan method/function untuk melakukan seluruh proses transaksi
### Attribute Class
```
    empty_dict = {"Item": [], "Quantity": [], "Price": []}
    data = pd.DataFrame(empty_dict)
```
Attribute class berisikan dataframe kosong untuk menampung input data yang diberikan
### Attribute
```
      def __init__(self):
        self.nama_toko = "Supermarket Andi"
```
Attribute berisikan informasi nama toko
### Method
#### Add_Item
```
      def add_item(
        self, nama_item: str, jumlah_item: int, harga_item: float or int
    ):
        """Fungsi untuk menambahkan nama_item, jumlah_item, harga_item
            ke dalam attribute class data

        Args:
            nama_item (str): nama item
            jumlah_item (int): jumlah item
            harga_item (float atau int): harga per item

        """

        # Check type of data parameter nama_item
        if type(nama_item) != str:
            raise TypeError(
                "Parameter 'nama_item' harus bertipe data 'str'"
            )
        # Check type of data parameter jumlah_item
        elif type(jumlah_item) != int:
            raise TypeError(
                "Parameter 'jumlah_item' harus bertipe data 'int'"
            )
        # Check type of data parameter harga_item
        elif type(harga_item) != float and type(harga_item) != int:
            raise TypeError(
                "Parameter 'harga_item' bertipe data 'float' atau 'int'"
            )
        else:
            # Assign parameter into attribute class data
            self.data.loc[len(self.data)] = [
                nama_item,
                jumlah_item,
                harga_item,
            ]
            print("Masukkan detail item yang dibeli")
            print(f"Nama Item     : {nama_item}")
            print(f"QTY           : {jumlah_item}")
            print(f"Harga per-Item: Rp. {harga_item}")
```
Method `Add Item` memerlukan beberapa parameter seperti `nama_item: str`, `jumlah_item: int`, dan `harga_item: float or int`. proses diawali 
dengan pengecekan tipe data parameter yang diinputkan, apabila tipe data yang diinputkan tidak sesuai maka akan memunculkan pesan `error`. 
Item yang berhasil diinputkan akan masuk ke dalam `Dataframe` dan juga ditampilkan untuk mengetahui detail item. 

#### Update_Item_Name
```
def update_item_name(self, nama_item: str, update_nama_item: str):
        """Fungsi untuk memperbarui/mengganti nama_item 

        Args:
            nama_item (str): nama item lama
            update_nama_item (str): nama item baru

        """
        # Buat list seluruh item pd atribut class dari data
        list_nama_item = self.data["Item"].tolist()
        try:
            # Cek parameter nama_item pada list_nama_item 
            if nama_item not in list_nama_item:
                raise TypeError(
                        "nama_item tidak terdapat dalam list"
                    )
            else:
                # Cek tipe data parameter nama_item 
                if type(nama_item) != str:
                    raise TypeError(
                        "Parameter 'nama_item' harus bertipe data 'str'"
                    )
                # Cek tipe data parameter update_nama_item
                elif type(update_nama_item) != str:
                    raise TypeError(
                        "Parameter 'update_nama_item' harus bertipe data 'str'"
                    )
                else:
                    
                    self.data.loc[
                        self.data.Item == nama_item, "Item"
                    ] = update_nama_item
                    print(
                        f"Anda mengganti item {nama_item} menjadi {update_nama_item}"
                    )

        except ValueError:
            print(f"Item {nama_item} tidak ditemukan dalam riwayat transaksi")
```
Method `update_item_name` memerlukan beberapa parameter seperti `nama_item: str` dan `update_nama_item: str`. Proses diawali dengan pengecekan 
apakah `nama_item` yang akan diganti terdapat dalam `Dataframe`, apabila tidak ada akan ditampilkan `typeError`. Apabila ada, maka akan dicek kesesuaian
tipe data `nama_item` dan `update_nama_item`. Apabila tipe data tidak sesuai akan ditampilkan `typeError`. Apabila tipe data sudah sesuai, maka `nama_item` 
akan diubah menjadi `update_nama_item`.  
#### Update_Item_Quantity
```
def update_item_quantity(self, nama_item: str, update_jumlah_item: int):
        """Fungsi untuk memperbarui/mengganti jumlah_item 
        Args:
            nama_item (str)         :nama item sebagai keys untuk mengupdate jumlah_item
            update_jumlah_item (int):value jumlah_item baru yang akan di update

        """

        # Buat list seluruh item pd atribut class dari data
        list_nama_item = self.data["Item"].tolist()
        try:
            # Cek parameter nama_item pada list_nama_item 
            if nama_item not in list_nama_item:
                raise TypeError(
                        "nama_item tidak terdapat dalam list"
                    )
            else:
                # Cek tipe data parameter nama_item 
                if type(nama_item) != str:
                    raise TypeError(
                        "Parameter 'nama_item' bertipe data 'str'"
                    )
                # Cek tipe data parameter update_jumlah_item
                elif type(update_jumlah_item) != int:
                    raise TypeError(
                        "Parameter 'update_jumlah_item' berdata 'int'"
                    )
                else:
                   
                    self.data.loc[
                        self.data.Item == nama_item, "Quantity"
                    ] = update_jumlah_item
                    print(
                        f"Anda mengganti jumlah item {nama_item} menjadi {update_jumlah_item}"
                    )

        except ValueError:
            print(f"Item {nama_item} tidak ditemukan dalam riwayat transaksi")
```
Method `update_item_quantity` memerlukan beberapa parameter seperti `nama_item: str` dan `update_jumlah_item: int`. Proses diawali dengan pengecekan 
apakah `nama_item` yang akan diganti terdapat dalam `Dataframe`, apabila tidak ada akan ditampilkan `typeError`. Apabila ada, maka akan dicek kesesuaian
tipe data `nama_item` dan `update_jumlah_item`. Apabila tipe data tidak sesuai akan ditampilkan `typeError`. Apabila tipe data sudah sesuai, maka jumlah item `nama_item` 
akan diubah menjadi `update_jumlah_item`. 
#### Update_Item_Price
```
 def update_item_price(self, nama_item: str, update_harga: float or int):
        """Fungsi untuk menmperbarui/mengganti harga 

        Args:
            nama_item (str): nama item sebagai keys untuk mengupdate harga
            update_harga (float / int): value harga baru yang akan di update
        
        """
        # Buat list seluruh item pd atribut class dari data
        list_nama_item = self.data["Item"].tolist()
        try:
            # Cek parameter nama_item pada list_nama_item 
            if nama_item not in list_nama_item:
                raise TypeError(
                        "nama_item tidak terdapat dalam list"
                    )

            else:
                # Cek tipe data parameter nama_item 
                if type(nama_item) != str:
                    raise TypeError(
                        "Parameter 'nama_item' harus bertipe data 'str'"
                    )

                # Cek tipe data parameter nama_item  update_harga
                elif type(update_harga) != float and type(update_harga) != int:
                    raise TypeError(
                        "Parameter 'update_harga' bertipe data float/int"
                    )

                else:
                    
                    self.data.loc[
                        self.data.Item == nama_item, "Price"
                    ] = update_harga
                    print(
                        f"Anda mengganti harga item {nama_item} menjadi {update_harga}"
                    )

        except ValueError:
            print(f"Item {nama_item} tidak ditemukan dalam riwayat transaksi")
```
Method `update_item_price` memerlukan beberapa parameter seperti `nama_item: str` dan `update_harga: float or int`. Proses diawali dengan pengecekan 
apakah `nama_item` yang akan diganti terdapat dalam `Dataframe`, apabila tidak ada akan ditampilkan `typeError`. Apabila ada, maka akan dicek kesesuaian
tipe data `nama_item` dan `update_harga`. Apabila tipe data tidak sesuai akan ditampilkan `typeError`. Apabila tipe data sudah sesuai, maka harga item `nama_item` 
akan diubah menjadi `update_harga`.
#### Delete_Item
```
  def delete_item(self, nama_item: str):
        """Fungsi untuk menghapus item 

        Args:
            nama_item (str): nama_item yang ingin dihapus

        
        """

        # Buat list seluruh item pd atribut class dari data
        list_nama_item = self.data["Item"].tolist()
        try:
            # Cek parameter nama_item pada list_nama_item 
            if nama_item not in list_nama_item:
                raise TypeError(
                        "nama_item tidak terdapat dalam list"
                    )

            else:
                # Cek tipe data parameter nama_item 
                if type(nama_item) != str:
                    raise TypeError(
                        "Parameter 'nama_item' harus bertipe data 'str'"
                    )
                else:
                    # menampilkan data yang dihapus
                    print(
                        f"Anda telah menghapus item {nama_item} dari transaksi"
                    )

                    # Filter and drop by nama_item
                    data = self.data.drop(
                        self.data.index[self.data.Item == nama_item],
                        inplace=True,
                    )

                    # Assign and show table
                    table = tabulate(data, headers="keys", tablefmt="pretty")

                    return print(table)

        except ValueError:
            print(f"Item {nama_item} tidak ditemukan dalam riwayat transaksi")
```
Method `delete_item` memerlukan parameter `nama_item: str` . Proses diawali dengan pengecekan 
apakah `nama_item` yang akan dihapus terdapat dalam `Dataframe`, apabila tidak ada akan ditampilkan `typeError`. Apabila ada, maka akan dicek kesesuaian
tipe data `nama_item`. Apabila tipe data tidak sesuai akan ditampilkan `typeError`. Apabila tipe data sudah sesuai, maka kolom dimana `nama_item` tersebut ada
dalam dataframe akan dihapus kemudian ditampilkan tabel pemesanan yang tersisa.
#### Reset_Transaction
```
def reset_transaction(self):
        """Fungsi untuk menghapus semua item yang ada dalam attribute class data

        Returns:
            table: order tabel kosong
        """

        # Show blank table
        print("Semua item berhasil di delete!")

        # Drop index in attribute class data
        self.data.drop(self.data.index, inplace=True)

        # Create  and show table
        table = tabulate(self.data, headers="keys", tablefmt="pretty")

        return print(table)
```
Method `reset_transaction` tidak membutuhkan parameter apapun karena langsung menggunakan method `drop` untuk menghapus seluruh item yang ada dalam `Dataframe`. Kemudian akan
menampilkan pesan Semua item berhasil di delete! dan tabel kosong
#### Check_Order
```
 def check_order(self):
        """Fungsi untuk mengecek kembali item yang telah diinputkan

        Returns:
            table: Tabel order dengan total harga untuk tiap transaksinya
        """

        # Copy attribute class data
        output_data = self.data.copy()

        # Create new column
        output_data["Total_Price"] = (
            output_data.Quantity * output_data.Price
        )
        # Create and show table
        table = tabulate(output_data, headers="keys", tablefmt="pretty")

        return print(table)
 ```
Method `check_order` diawali dengan menyalin `Dataframe` dari atribute class data untuk membuat `Dataframe` baru yang ditambahkan satu kolom baru berisi `Total_Price`
dari item yang merupakan perkalian dari `Quantity` dan `Price`. Hasil perhitungan ini kemudian ditampilkan dalam bentuk tabel pesanan
#### Total_Price
```
 def total_price(self):
        """Fungsi untuk menghitung total transaksi dari item yang diinputkan, termasuk diskon yang diperoleh

        Returns:
            int : total transaksi
        """
        # Copy attribute class data
        output_data = self.data.copy()
        # buat kolom baru
        output_data["Total_Price"] = (
            output_data.Quantity * output_data.Price
        )
        # Assign variable total payment
        total = np.sum(output_data.Total_Price)

        # If total payment les than 200.000 get normal price
        if total >= 0 and total <= 200_000:
            return print(f"Total pembayaran sebesar Rp.{int(total)}")

        # if total paymen more than 200.000 and less than 300.000
        # Get 5 percent discount
        elif total > 200_000 and total <= 300_000:
            total_belanja = total * 0.95
            return print(
                f"Total Harga item sebesar Rp.{int(total)} \nAnda mendapatkan diskon sebesar 5% \nTotal pembayaran sebesar Rp.{int(total_belanja)}"
            )

        # if total paymen more than 300.000 and less than 500.000
        # Get 8 percent discount
        elif total > 300_000 and total <= 500_000:
            total_belanja = total * 0.92
            return print(
                f"Total Harga item sebesar Rp.{int(total)} \nAnda mendapatkan diskon sebesar 8% \nTotal pembayaran sebesar Rp.{int(total_belanja)}"
            )

        # if total paymen more than 500.000, get 10 percent discount
        elif total > 500_000:
            total_belanja = total * 0.90
            return print(
                f"Total Harga item sebesar Rp.{int(total)} \nAnda mendapatkan diskon sebesar 10% \nTotal pembayaran sebesar Rp.{int(total_belanja)}"
            )

        else:
            return "Total Belanja Tidak Boleh kurang dari nol"
```
Method `total_price` diawali dengan menyalin `Dataframe` dari atribute class data untuk membuat `Dataframe` baru yang ditambahkan satu kolom baru berisi `Total_Price`
dari item yang merupakan perkalian dari `Quantity` dan `Price`. Kemudian dilakukan penjumlahan `Total_Price` dari setiap item yang disimpan dalam
variabel `total` untuk memperoleh total pembayaran dari keseluruhan item,dengan ketentuan diskon :
  - Jika total belanja di atas Rp.200.000 maka akan mendapatkan diskon 5%
  - Jika total belanja di atas Rp.300.000 maka akan mendapatkan diskon 8%
  - Jika total belanja di atas Rp.500.000 maka akan mendapatkan diskon 10%
## Hasil Test Case
### Test Case 1
Customer ingin menambahkan dua item menggunakan method add_item(). Item yang ditambahkan adalah :
- Nama Item: Ayam Goreng, Qty: 2, Harga: 20.000
- Nama Item: Pasta Gigi, Qty: 3, Harga: 15.000
```
# Test Case 1
# Add Item 1
print("Test Case 1")
print("--------------------------------------------------------------------------")
user.add_item("Ayam Goreng", 2, 20_000)
print("\n")
# Add Item 2
user.add_item("Pasta Gigi", 3, 15_000)
print("\n")
print("Tabel pemesanan :")
user.check_order()
user.total_price()
```
Output :
<br /> 
![This is an image](https://github.com/achmadfanany/cashier-system-project/blob/main/Test_Case1.PNG)
<br /> 
### Test Case 2
Ternyata Customer salah membeli salah satu item yang sudah ditambahkan, maka Customer menggunakan method `delete_item()` untuk menghapus item. Item yang ingin dihapus adalah Pasta Gigi
```
# Test Case 2
# Delete pasta gigi from order table
print("\n")
print("Test Case 2")
print("--------------------------------------------------------------------------")
user.delete_item("Pasta Gigi")
print("Table Pemesanan:")
user.check_order()
user.total_price()

```
Output:
<br /> 
![This is an image](https://github.com/achmadfanany/cashier-system-project/blob/main/Test_Case2.PNG)
<br /> 
### Test Case 3
Ternyata Customer salah memasukkan item yang ingin dibelanjakan dan ingin menhapus semua item. Customer cukup menggunakan method 'reset_transaction()' untuk menghapus semua item yang sudah ditambahkan.
```
# Test Case 3
# Reset all transaction
print("\n")
print("Test Case 3")
print("--------------------------------------------------------------------------")
user.reset_transaction()
```
Output:
<br /> 
![This is an image](https://github.com/achmadfanany/cashier-system-project/blob/main/Test_Case3.PNG)
<br /> 
### Test Case 4
Setelah Customer selesai berbelanja, dilakukan perhitungan total belanja dengan menggunakan method `total_price()`. Detail item yang dibeli akan ditampilkan sebelum mengeluarkan output total belanja.
```
# Test Case 4
print("\n")
print("Test Case 4")
print("--------------------------------------------------------------------------")
# Add Item 1
user.add_item("Ayam Goreng", 2, 20_000)
print("\n")
# Add Item 2
user.add_item("Pasta Gigi", 3, 15_000)
print("\n")
# Add Item 3
user.add_item("Mainan Mobil", 1, 200_000)
print("\n")
# Add Item 4
user.add_item("Mie Instan", 5, 3_000)
print("\n")
print("Tabel Pemesanan :")
user.check_order()
user.total_price()
```
Output:
<br /> 
![This is an image](https://github.com/achmadfanany/cashier-system-project/blob/main/Test_Case4.PNG)
<br /> 
## Conclusion/ Future Work
Sistem Kasir self-service yang dikembangkan sudah bekerja dengan baik, namun dapat ditingkatkan agar lebih efisien, dengan membuat modular code dan input parameter yang bisa dimasukkan secara otomatis.
