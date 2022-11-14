from .design import header,footer
from .database import database
from . import chek
from . import operasi


def saldo_ribuan(saldo):
    ribuan = f"{saldo:,}"
    return (f"{ribuan.replace(',','.')}")


def list_data_database():
    with open(database,'r') as file :
        list_data = file.readlines()
        return list_data

def list_data_database_index(index):
    with open(database,'r') as file :
        list_data = file.readlines()
        return list_data[index]

def transaksi_1(nama) :
    header()   
    list_data = list_data_database()    
    index_data = chek.cek_index(nama)
    data_break = list_data[index_data].split(',')

    print(f"Data nasabah sdr {nama}")
    print(f"\nNAMA BANK        : BANK ATM-QU")
    print(f"NOMOR REKENING   : {data_break[0]}")
    print(f"NAMA REKENING    : {data_break[2]:.20}")
    print(f"SALDO            : Rp. {saldo_ribuan(int(data_break[3]))}")
    footer()
        
    input("Enter untuk melanjutkan...")
        

def transaksi_2(nama):
    while True :
        header()
        print("""\nMENU PENARIKAN 
            1.Rp. 50.000
            2.RP. 100.000
            3.AMBIL BEBAS

            0.KEMBALI KE MENU
            """)
        tarik = input("MASUKAN KODE [1/2/3/0] : ")
        if tarik == "1" :
            saldo = 50000
            operasi.saldo_kurang(nama,saldo)

        elif tarik == "2" :
            saldo = 100000
            operasi.saldo_kurang(nama,saldo)

        elif tarik == "3" :
            saldo = int(input("\nMasukan Nominal Penarikan\nRp. "))
            if saldo < 50000 :
                print("\nTransaksi Gagal\nPenarikan Minimal Rp. 50.000")
                footer()
            else :
                operasi.saldo_kurang(nama,saldo)
        
        elif tarik == "0" :
            break

        input("Enter untuk melanjutkan...")


def transaksi_4(nama):
    header()
    setor = int(input("\nMASUKAN NOMINAL SETOR TUNAI : Rp. "))
    if setor < 50000 :
        print("\nTransaksi Gagal\nSetor Tunai Minimal Rp. 50.000")
        
        footer()

    else :
        operasi.saldo_tambah(nama,setor)
    
    input("Enter untuk melanjutkan...")

