class Produk:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def tampilkan_info(self):
        print(f"Nama Produk : {self.nama}")
        print(f"Harga Produk: Rp{self.harga:,.0f}")

    def hitung_total(self, jumlah_beli):
        return self.harga * jumlah_beli

    def hitung_diskon(self, total_seluruh):
        if total_seluruh > 5000:
            return total_seluruh * 0.05
        return 0