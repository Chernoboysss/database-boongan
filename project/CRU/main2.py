from .design import header,footer
from .database import database
from . import chek
from . import view

def menu_login(nama,pin):
    while True :
        header()
        print(f"{'JENIS TRANSAKSI':^40}")
        print("""
        1.INFORMASI REKENING
        2.PENARIKAN
        3.TRANSFER
        4.SETOR TUNAI

        0.LOGOUT
        """)

        user_input = input("JENIS TRANSAKSI 1/2/3/4/0 : ")

        if user_input == "1" :
            view.transaksi_1(nama)

        elif user_input == "2" :
            view.transaksi_2(nama)

        elif user_input == "4" :
            view.transaksi_4(nama)
        
        elif user_input == "0" :
            break