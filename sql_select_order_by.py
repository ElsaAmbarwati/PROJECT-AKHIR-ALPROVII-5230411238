#urutan nama hewan berdasarkan dari alphabetic
import sqlite3

koneksi = sqlite3.connect('database_hewan.db')

kursor = koneksi.cursor()

kursor.execute("SELECT * FROM HEWAN ORDER BY nama_hewan ASC")

baris_tabel = kursor.fetchall()

print('Data Hewan berdasarkan dari alphabetic')
print('-' * 105)
print('{:<10} {:<20} {:<12} {:<16} {:<18} {:<20}'.format('ID HEWAN',
                                                 'NAMA HEWAN',
                                                 'JENIS',
                                                 'ASAL',
                                                 'JUMLAH SAAT INI',
                                                 'TAHUN TERAKHIR DITEMUKAN'
                                                 ))
print('-' * 105)

for baris in baris_tabel:
    print('{:<10} {:<20} {:<12} {:<20} {:<23} {:<19}'.format(baris[0], baris[1], baris[2], baris[3], baris[4], baris[5]))

koneksi.close()
print()
print()
print('=' * 105)
print()
print()


#urutan jumlah hewan saat ini berdasarkan dari yang tebanyak ke paling sedikit
import sqlite3

koneksi = sqlite3.connect('database_hewan.db')

kursor = koneksi.cursor()

kursor.execute("SELECT * FROM HEWAN ORDER BY jml_skrng DESC")

baris_tabel = kursor.fetchall()

print('Data Hewan saat ini berdasarkan dari yang tebanyak ke paling sedikit')
print('-' * 105)
print('{:<10} {:<20} {:<12} {:<16} {:<18} {:<20}'.format('ID HEWAN',
                                                 'NAMA HEWAN',
                                                 'JENIS',
                                                 'ASAL',
                                                 'JUMLAH SAAT INI',
                                                 'TAHUN TERAKHIR DITEMUKAN'
                                                 ))
print('-' * 105)

for baris in baris_tabel:
    print('{:<10} {:<20} {:<12} {:<20} {:<23} {:<19}'.format(baris[0], baris[1], baris[2], baris[3], baris[4], baris[5]))

koneksi.close()

print()
print()
print('=' * 105)
print()
print()



#urutan tahun ditemukan hewan berdasarkan dari tahun terlama ke terbaru
import sqlite3

koneksi = sqlite3.connect('database_hewan.db')

kursor = koneksi.cursor()

kursor.execute("SELECT * FROM HEWAN ORDER BY thn_ditemukan ASC")

baris_tabel = kursor.fetchall()

print('Data Hewan berdasarkan dari tahun terlama ke terbaru')
print('-' * 105)
print('{:<10} {:<20} {:<12} {:<16} {:<18} {:<20}'.format('ID HEWAN',
                                                 'NAMA HEWAN',
                                                 'JENIS',
                                                 'ASAL',
                                                 'JUMLAH SAAT INI',
                                                 'TAHUN TERAKHIR DITEMUKAN'
                                                 ))
print('-' * 105)

for baris in baris_tabel:
    print('{:<10} {:<20} {:<12} {:<20} {:<23} {:<19}'.format(baris[0], baris[1], baris[2], baris[3], baris[4], baris[5]))

koneksi.close()

