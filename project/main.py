from CRU import main2,operasi,view,design,chek
#problem belum solved upddate data ...

while True :
    design.header()
    print(f"{'SELAMAT DATANG DI ATM-QU':^40}")
    print("""
    1.Registrasi
    2.Login
    3.keluar
        """) 
    design.footer()

    user_opsi = input("Silahkan pilih opsi [1/2/3] :  ")
    if user_opsi == "1" :
        operasi.registrasi()

    elif user_opsi == "2" :
        design.header()
        print(f"SILAHKAN LOGIN")
        nama = input("Nama \t: ")
        pin = input("Pin \t: ")
        operasi.login(nama,pin)

    elif user_opsi == "3" :
        design.header()
        print("\n")
        print(f"{'TERIMA KASIH TELAH MENGGUNAKAN':^40}")
        print(f"{'APLIKASI ATM-QU':^40}")
        print("\n")
        design.footer()

        break

