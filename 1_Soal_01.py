arr = []


# Input nilai dari mahasiswa
print("Masukan Nilai Mahasiswa:")
for i in range(10):
    n = int(input(f"Nilai Mahasiswa {i+1}: "))
    arr.append(n)

# Tampilkan nilai yang dimasukan
print("\nNilai Mahasiswa:", arr)

# Nilai tertingi dan terkecil
nilai_Terbesar = max(arr)
nilai_Terkecil = min(arr)

print(f"Nilai Tertinggi: {nilai_Terbesar}")
print(f"Nilai Terendah: {nilai_Terkecil}")

# Rata-rata nilai
rata_rata = sum(arr) / len(arr)
print(f"Rata-rata Nilai: {rata_rata:.2f}")

# menghitung jumlah mahasiswa yang lulus
jumlah_lulus = sum(1 for n in arr if n >= 60)

tidak_lulus = len(arr) - jumlah_lulus

print(f"Jumlah Mahasiswa Lulus: {jumlah_lulus}")
print(f"Jumlah Mahasiswa Tidak Lulus: {tidak_lulus}")

# Grafik tertinggi dan terendah
import matplotlib.pyplot as plt

labels = ['Tertinggi', 'Terendah']
values = [nilai_Terbesar, nilai_Terkecil]
plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Perbandingan Nilai Tertinggi dan Terendah')
plt.axis('equal')
plt.show()

# Grafik kelulusan
labels = ['Lulus', 'Tidak Lulus']
values = [jumlah_lulus, tidak_lulus]        
plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Persentase Kelulusan Mahasiswa')
plt.axis('equal')
plt.show()
