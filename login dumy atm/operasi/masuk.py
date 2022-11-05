import os
from . import cek_data


def login():
    os.system("cls")
    print("SILAHKAN LOGIN")
    print("="*20)
    while True :
        nama = input("masukan Nama : ")
        pw   = input("masukan pin : ")

        cek = cek_data.data_in_database(nama, pw)
        if cek :
            os.system("cls")
            print("="*20)
            print("Login berhasil")
            break

        else :
            print("Nama atau PIN salah !!! ulangi lagi bwangg ")

        

