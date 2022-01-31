#buka file
file_puisi = open(r"file-io\puisi.txt")

#baca isi file
puisi = file_puisi.read()

#cetak baris pertama
#print(puisi[0])
#cetak baris kedua
#print(puisi[1])

#for text in puisi:
#    print(text)

print(puisi)

#tutup file
file_puisi.close()