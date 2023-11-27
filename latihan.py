# Menulis data ke file
file = open("data_mahasiswa_temp.txt", "a")
file.write("Andi 11119 1\n" +
           "Bima 11112 1\n" +
           "Rahma 11131 3\n" +
           "Zeno 11198 9\n" +
           "Rahma 11131 3\n" +
           "Andi 11119 1\n")
file.close()

# Fungsi untuk membersihkan data duplikat
def clean_data(lines):
    unique_lines = list(set(lines))
    return unique_lines

# Membaca data dari file sementara
file_name = 'data_mahasiswa_temp.txt'
with open(file_name, 'r') as file:
    lines = file.readlines()

# Membersihkan data dari duplikat
cleaned_data = clean_data(lines)

# Menulis data bersih ke file
with open('data_mahasiswa.txt', 'w') as file:
    for line in cleaned_data:
        file.write(line)

print("Data telah disimpan ke file 'data_mahasiswa.txt' setelah menghapus duplikat.")
