import multiprocessing

def persegi(num):
    print("Persegi: {}\n".format(num * num))

def kubus(num):
    print("Kubus  : {}".format(num * num * num))
  
  
if __name__ == "__main__":
    # Membuat Process
    asek = int(input("Masukkan Angka Untuk Kalkukasi Luas Persegi dan Kubus : "))
    p1 = multiprocessing.Process(target=persegi, args=(asek, ))
    p2 = multiprocessing.Process(target=kubus, args=(asek, ))

    # Menjalankan Process
    p1.start()

    p2.start()
  
    # Menunggu Process Selesai
    p1.join()
    p2.join()
  
    # Process Selesai
    print("Process Selesai!")