pakai = "y"
tabungan = 0
umum= 0


def tsaldo():
    global umum, tabungan
    print("[1] Umum")
    print("[2] Tabungan")
    print("-----------------------------------------")
    a = int(input("Pilih Menu :"))
    if (a==1):
        b = int(input("Masukan Saldo Yang mau diisi :"))
        umum = umum + b

        print("Penambahan saldo sebesar Rp.",b,",- Berhasil")
        print("Total saldo anda Sekarang Rp.",umum,",-")
        pakai == "n"
        
    elif(a==2):
        c = int(input("Masukan saldo Yang Mau diisi :"))
        tabungan = tabungan + c
        print("Penambahan saldo sebesar Rp.",c,",- Berhasil")
        print("Total saldo anda Sekarang Rp.",tabungan,",-")
        pakai =="n"
        
def isaldo():
    print("Saldo Umum Anda saat ini adalah Rp.",umum,",-")
    print("Saldo tabungan Anda saat ini adalah Rp.",tabungan,",-")
    print("")

def asaldo():
    global umum, tabungan
    print ("Saldo mana Yang akan di ambil : ")
    print("[1] Umum")
    print("[2] Tabungan")
    print("-----------------------------------------")
    a = int(input("Pilih Menu :"))
    if (a==1):
        b = int(input("Masukan Saldo Yang mau diambil :"))
        umum = umum - b

        print("Pengambilan saldo sebesar Rp.",b,",- Berhasil")
        print("Total saldo anda Sekarang Rp.",umum,",-")
        pakai == "n"
    
    elif (a==2):
        c = int(input("Masukan Saldo Yang mau diambil :"))
        tabungan = tabungan - c

        print("Pengambilan saldo sebesar Rp.",c,",- Berhasil")
        print("Total saldo anda Sekarang Rp.",tabungan,",-")
        pakai == "n"    

while pakai == "y":
        print("\n")
        print("=== APLIKASI PENCATATAN UANG DIGITAL ===")
        print("[1] Informasi Saldo")
        print("[2] Tambah Saldo")
        print("[3] Ambil Saldo")
        print("[0] Keluar")
        print("-----------------------------------------")

        menu  = int(input("Pilihan menu : "))
        print("-----------------")
        if (menu==1):
         isaldo()
        elif (menu==2):
         tsaldo()
        elif (menu==3):
         asaldo()
        elif (menu==0):
         exit()
        else:
         print("")