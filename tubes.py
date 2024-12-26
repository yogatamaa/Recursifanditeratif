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

# Data real untuk daftar opsi checkout
real_data = [
    "Shampo", "Sabun", "Pasta Gigi", "Handuk", "Sikat Gigi", "Sampo Bayi", "Sabun Mandi", "Minyak Rambut",
    "Kondisioner", "Deodoran", "Tisu", "Masker Wajah", "Hand Sanitizer", "Lotion Tubuh", "Krim Wajah", "Minyak Wangi",
    "Scrub Tubuh", "Sabun Cuci Muka", "Shower Gel", "Body Butter", "Face Wash", "Shaving Cream", "Hair Gel",
    "Body Mist", "Hand Cream", "Lip Balm", "Face Serum", "Face Toner", "Eye Cream", "Sunblock", "Aftershave",
    "Nail Polish Remover", "Foot Cream", "Hair Spray", "Hair Wax", "Body Oil", "Mouthwash", "Hair Mousse", "Hand Wash"
]

# Buat data CheckoutOption dari data real
options = [CheckoutOption(i + 1, real_data[i]) for i in range(len(real_data))]
options.sort(key=lambda option: option.description)  # Mengurutkan data berdasarkan deskripsi

# Fungsi untuk mengukur waktu eksekusi dengan presisi lebih tinggi
def measure_time(func, *args, repetitions=1000):
    start_time = time.perf_counter()
    for _ in range(repetitions):
        func(*args)
    return (time.perf_counter() - start_time) / repetitions

# Tabel untuk menyimpan hasil
results_table = PrettyTable()
results_table.field_names = ["n", "Linear Recursive Time (s)", "Linear Iterative Time (s)"]

# Kelipatan n untuk pengujian
n_values = list(range(5, 26, 5))  # Kelipatan 5 dari 5 hingga 25

# Melakukan pengujian dan perbandingan
recursive_times = []
iterative_times = []

for n in n_values:
    subset = options[:n]
    target = subset[-1].description  # Pilih opsi terakhir sebagai target pencarian

    # Waktu eksekusi untuk setiap metode pencarian
    linear_recursive_time = measure_time(linear_search_recursive, subset, target, repetitions=100)
    linear_iterative_time = measure_time(linear_search, subset, target, repetitions=100)

    # Menyimpan hasil ke tabel dan list
    results_table.add_row([n, linear_recursive_time, linear_iterative_time])
    recursive_times.append(linear_recursive_time)
    iterative_times.append(linear_iterative_time)

# Cetak tabel hasil
print(results_table)

# Membuat grafik perbandingan
plt.figure(figsize=(12, 8))
plt.plot(n_values, recursive_times, marker='o', label='Linear Recursive')
plt.plot(n_values, iterative_times, marker='o', label='Linear Iterative')

plt.title('Performance Comparison: Linear Search (Recursive vs Iterative)')
plt.xlabel('Input Size (n)')
plt.ylabel('Execution Time (seconds)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
