import numpy as np
import pandas as pd
from tabulate import tabulate


class Transaction:
    """Fungsi dasar sistem kasir """

    # Buat empty dict dan masukkan pada Dataframe
    empty_dict = {"Item": [], "Quantity": [], "Price": []}
    data = pd.DataFrame(empty_dict)

    def __init__(self):
        self.nama_toko = "Supermarket Andi"
        

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


user = Transaction()

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

# Test Case 2
# Delete pasta gigi from order table
print("\n")
print("Test Case 2")
print("--------------------------------------------------------------------------")
user.delete_item("Pasta Gigi")
print("Table Pemesanan:")
user.check_order()
user.total_price()

# Test Case 3
# Reset all transaction
print("\n")
print("Test Case 3")
print("--------------------------------------------------------------------------")
user.reset_transaction()

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

# Test Case 5
# Update Item, Quantity, dan Harga
print("\n")
print("Test Case 5")
print("--------------------------------------------------------------------------")
print("Tabel Pemesanan Sebelum Update:")
user.check_order()
user.total_price()
print("\n")
# Update Item pasta gigi
user.update_item_name("Pasta Gigi", "Sabun Mandi")
# Update Quantity ayam goreng
user.update_item_quantity("Ayam Goreng", 3)
# Update Harga mie instan
user.update_item_price("Mie Instan", 3_500)
print("\n")
print("Tabel Pemesanan Setelah Update:")
user.check_order()
user.total_price()

