from produk import Produk

def main():
    print("=== SISTEM PEMBELIAN PRODUK ===")
    
    # Meminta jumlah jenis produk yang dibeli
    jumlah_jenis = int(input("Masukkan jumlah produk yang akan dibeli: "))
    print("-" * 40)

    total_seluruh = 0

    # Perulangan untuk menginput setiap produk
    for i in range(jumlah_jenis):
        print(f"\nData Produk ke-{i + 1}:")
        
        nama = input("  Nama produk : ")
        harga = float(input("  Harga produk: Rp"))
        jumlah_beli = int(input("  Jumlah beli : "))

        # Membuat objek Produk baru
        p = Produk(nama, harga)
        
        # Menghitung total harga produk saat ini
        total_produk = p.hitung_total(jumlah_beli)
        
        # Menambahkan ke akumulasi total seluruh pembelian
        total_seluruh += total_produk
        
        print(f"  --> Total pembelian {p.nama}: Rp{total_produk:,.0f}")

    # Menggunakan method dari class Produk untuk menghitung diskon
    produk_helper = Produk("", 0)
    diskon = produk_helper.hitung_diskon(total_seluruh)
    total_bayar = total_seluruh - diskon
    
    print("\n" + "=" * 30)
    print("=== HASIL PEMBELIAN ===")
    print(f"Total Pembelian : Rp{total_seluruh:,.0f}")
    print(f"Diskon 5%       : Rp{diskon:,.0f}")
    print(f"Total Bayar     : Rp{total_bayar:,.0f}")
    print("=" * 30)

if __name__ == "__main__":
    main()