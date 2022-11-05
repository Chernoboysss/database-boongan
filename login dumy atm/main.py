import os
from operasi import cek_data,registrasi,masuk


while True :
    os.system("cls")
    print("SELAMAT DATANG")
    print("="*20)
    print("""opsi :
    1.registrasi
    2.login
    3.keluar
            """)
    is_pilih = input("pilih opsi : ")
    if is_pilih == "1" :
        registrasi.regist()

    elif is_pilih == "2" :
        masuk.login()
        while True :
            os.system("cls")
            print("selamat datang")
            print("""pilih opsi bang
            1.cek data
            2.logout
            """)
            
            opsi_user = input("masukan opsi bwang : ")
            if opsi_user == "1" :
                cek_data.cek_database()
                input("")
            
            elif opsi_user == "2" :
                os.system("cls")
                print("Logout berhasil bwanggg")
                input("")
                break


    elif is_pilih == "3" :
        os.system("cls")
        print("TERIMA KASIH KAKAKAAKAKAKKAKAKKA")
        break
