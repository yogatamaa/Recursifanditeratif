import time
import matplotlib.pyplot as plt
from prettytable import PrettyTable

class CheckoutOption:
    def __init__(self, id, description):
        self.id = id
        self.description = description

# Implementasi Linear Search secara iteratif untuk menemukan opsi checkout

def linear_search(options, target):
    for option in options:
        if option.description == target:
            return option
    return None

# Implementasi Linear Search secara rekursif untuk menemukan opsi checkout

def linear_search_recursive(options, target, index=0):
    if index >= len(options):
        return None
    if options[index].description == target:
        return options[index]
    return linear_search_recursive(options, target, index + 1)

# Studi kasus dengan daftar opsi checkout
options = [CheckoutOption(i, f"Option {i}") for i in range(1, 1001)]
options.sort(key=lambda option: option.description)

# Fungsi untuk mengukur waktu eksekusi dengan presisi lebih tinggi
def measure_time(func, *args, repetitions=1000):
    start_time = time.perf_counter()
    for _ in range(repetitions):
        func(*args)
    return (time.perf_counter() - start_time) / repetitions

# Tabel untuk menyimpan hasil
results_table = PrettyTable()
results_table.field_names = ["n", "Linear Recursive Time (s)", "Linear Iterative Time (s)"]

# Menambahkan loop untuk pengujian dan perbandingan
while True:
    try:
        n = int(input("Masukkan nilai n (atau ketik -1 untuk keluar): "))
        if n == -1:
            break
        if n > len(options):
            print(f"Nilai n terlalu besar! Maksimal adalah {len(options)}.")
            continue

        subset = options[:n]
        target = subset[-1].description  # Pilih opsi terakhir sebagai target pencarian

        # Waktu eksekusi untuk setiap metode pencarian
        linear_recursive_time = measure_time(linear_search_recursive, subset, target, repetitions=100)
        linear_iterative_time = measure_time(linear_search, subset, target, repetitions=100)

        # Tambahkan hasil ke tabel
        results_table.add_row([n, linear_recursive_time, linear_iterative_time])

        # Cetak tabel hasil
        print(results_table)

        # Plot hasil untuk Linear Search
        sizes = [row[0] for row in results_table._rows]
        linear_recursive_times = [row[1] for row in results_table._rows]
        linear_iterative_times = [row[2] for row in results_table._rows]

        # Membuat grafik perbandingan
        plt.figure(figsize=(12, 8))

        plt.plot(sizes, linear_recursive_times, marker='o', label='Linear Recursive')
        plt.plot(sizes, linear_iterative_times, marker='o', label='Linear Iterative')

        plt.title('Performance Comparison: Checkout Optimization Search (Recursive & Iterative)')
        plt.xlabel('Input Size (n)')
        plt.ylabel('Execution Time (seconds)')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    except ValueError:
        print("Masukkan angka yang valid.")
