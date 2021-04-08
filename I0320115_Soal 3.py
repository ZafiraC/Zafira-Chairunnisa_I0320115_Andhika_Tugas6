#SOAL NO 3
#Menentukan bilangan prima
for num in range(10, 25):
    if num % 2 == 0 or num % 3 == 0:
        print("%d bukan prima" % num)
    else:
        print("%d adalah bilangan prima" % num)