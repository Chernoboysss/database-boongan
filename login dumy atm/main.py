import os
import operasi
from operasi import cek_database
from operasi import registrasi 


while True :
    os.system("cls")
    print("""opsi :
    0.registrasi
    1.cek data
    2.login
    3.logout
            """)
    is_pilih = input("pilih opsi : ")
    if is_pilih == "0" :
        registrasi.regist()

    elif is_pilih == "1" :
        cek_database()

    elif is_pilih == "2" :
        print("fitur belum ada")

    elif is_pilih == "3" :
        print("fitur belum ada")

    is_selesai = input("\nkeluar program (y/n) ?\n")
    if is_selesai == "y" :
        os.system("cls")
        print("TERIMA KASIH KAKAKAAKAKAKKAKAKKA")
        break