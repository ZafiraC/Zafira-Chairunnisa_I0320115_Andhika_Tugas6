#SOAL NO 2
#menghitung nilai rata-rata menggunakan perintah perulangan for
n = int(input("\nBanyaknya Data: "))

print()
data = []
jum = 0

for i in range(0,n):
    temp = int(input("Masukkan data ke-%d: "% (i+1)))
    data.append(temp)
    jum += data [i]
    ratarata = jum/n

print("\nNilai Rata-Rata= %0.2f" %ratarata)