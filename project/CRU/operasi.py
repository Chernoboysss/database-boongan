from .design import header,footer
from .database import database,template
from . import generator
from . import chek
from . import view
from . import main2

def creat(nama,pin,saldo = "2500000"):
    data = template.copy()

    data["rekening"] = generator.generate_rek()
    data["pin"]      = pin
    data["nama"]     = nama + template["nama"][len(nama):]
    data["saldo"]    = saldo + template["saldo"][len(saldo):]

    data_in_database = f'{data["rekening"]},{data["pin"]},{data["nama"]},{data["saldo"]}\n'

    try : 
        with open(database,'a',encoding="utf-8") as file:
            file.write(data_in_database)
    except :
        with open(database,'w+',encoding="utf-8") as file:
            file.write(data_in_database)

def registrasi(): 
    while True :
        header()
        print(f"SILAHKAN REGISTRASI")
        nama = input("Nama \t: ")
        pin = input("Pin \t: ")

        nama_sama = chek.cek_nama(nama)
        
        if len(pin) != 6 :
            print(f"\nPIN HARUS 6 DIGIT !!!")
            
        if nama_sama == True :
            print(f"\nNAMA TIDAK BISA DIGUNAKAN!!\nsudah ada yang pakai")


        elif len(pin) == 6 :
            print(f"\n\nREGISTRASI BERHASIL")
            creat(nama,pin)
            

        is_lanjut = input("lanjutkan Registrasi [y/n] ? \n")
        if is_lanjut == "n" :
            break



def login(nama,pin) :
    if chek.cek_nama_saldo(nama, pin) :
        print(f"\nLOGIN BERHASIL")
        input("\nEnter untuk melanjutkan...") 

        main2.menu_login(nama,pin)

    else :
        print(f"\nNAMA ATAU PIN SALAH")
        input("\nEnter untuk kembali ke menu...")


def update_data(nama,saldo):
    data = template.copy()
    banyak_data = chek.list_index_data()
    index = chek.cek_index(nama)
    
    list_data = view.list_data_database_index(index)
    data_break = list_data.split(",")

    data["rekening"]  = data_break[0]
    data["pin"]       = data_break[1]
    data["nama"]      = nama + data["nama"][len(nama):]
    data["saldo"]     = saldo + data["saldo"][len(saldo):]
    

    if index == min(banyak_data)   :
        data_update = f'{data["rekening"]},{data["pin"]},{data["nama"]},{data["saldo"]}'
        panjang_data = len(data_update)
        with open(database,"r+",encoding="utf-8") as file :
            file.seek(panjang_data * index)
            file.write(data_update)

    elif index >= 2 and index <= max(banyak_data) :
        data_update = f'\n{data["rekening"]},{data["pin"]},{data["nama"]},{data["saldo"]}'
        panjang_data = len(data_update)
        with open(database,'r+',encoding="utf-8") as file:
            file.seek (panjang_data * index)
            file.write(data_update)

    else:
        data_update = f'{data["rekening"]},{data["pin"]},{data["nama"]},{data["saldo"]}'
        panjang_data = len(data_update)
        with open(database,'r+',encoding="utf-8") as file:
            file.seek ((panjang_data * index)+1)
            file.write(data_update)




def saldo_kurang(nama,nominal):
    index = chek.cek_index(nama)
    saldo = int(chek.cek_saldo(index))
  
    if saldo < 50000 :
        header()
        print("\nTRANSAKSI GAGAL")
        print("SALDO ANDA TIDAK CUKUP")            
        footer()

    else :
        saldo -= nominal
        if saldo < 0 :
            header()
            print("\nTRANSAKSI GAGAL")
            print("SALDO ANDA TIDAK CUKUP") 
            footer()

        else :
            header()
            print("\nPENARIKAN BERHASIL\n")
            print(f"SALDO      : Rp. {view.saldo_ribuan(saldo)}\n")
            print(f"PENARIKAN  : Rp. {view.saldo_ribuan(nominal)}")
            saldo = str(saldo)
            update_data(nama,saldo)
            footer()
        
def saldo_tambah(nama,setor):
    index = chek.cek_index(nama)
    saldo = int(chek.cek_saldo(index))

    saldo += setor
    header()
    print("\nSETOR TUNAI BERHASIL\n")
    print(f"SALDO        : Rp. {view.saldo_ribuan(saldo)}\n")
    print(f"SETOR TUNAI  : Rp. {view.saldo_ribuan(setor)}")
    saldo = str(saldo)
    update_data(nama,saldo)
    footer()



    


      
