from . import database

def list_index_data():
    list_index = []

    with open("data.txt","r") as file :
        data_list = file.readlines()

        for x,data in enumerate(data_list) :
            list_index.append(x)

    return (list_index)

def cek_nama_saldo(nama,pin):
    with open("data.txt","r") as file :
        list_data = file.readlines()

    for index,data in enumerate(list_data) :
        data_break = data.split(",")
        nama_panjang = nama + database.template["nama"][len(nama):]

        if nama_panjang == data_break[2] and pin == data_break[1] :
            return True
            break
    
    else :
        return False


def cek_nama(nama):    
    with open("data.txt","r") as file :
        list_data = file.readlines()
        
    for index,data in enumerate(list_data) :
        data_break = data.split(",")
        nama_panjang = nama + database.template["nama"][len(nama):]

        if nama_panjang == data_break[2] :
            return True
            break
    
    else :
        return False

              
def cek_pin(pin):    
    with open("data.txt","r") as file :
        list_data = file.readlines()
        
    for index,data in enumerate(list_data) :
        data_break = data.split(",")

        if pin == data_break[1] :
            return True
            break
    else :
        return False


def cek_index(nama):

    with open("data.txt","r") as file :
        list_data = file.readlines()
    
    for index,data in enumerate(list_data) :
        data_break = data.split(",")

        nama_panjang = nama + database.template["nama"][len(nama):]
        if nama_panjang == data_break[2] :
            return index 


def cek_saldo(index):
    with open("data.txt","r") as file :
        list_data = file.readlines()
    
    for x,data in enumerate(list_data) :
        data_break = data.split(",")
        if x == index :
            saldo = f"{(int(data_break[3]))}"
            return (f"{saldo}")
        



