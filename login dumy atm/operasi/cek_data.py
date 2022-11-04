def cek_database() :
    nama_kosong = []
    pin_kosong = []

    with open("data.txt","r") as file :
        data_baru = file.readlines()

    nama_baru = input("\ncek nama yang mau dicek di database : ")
    for index,data in enumerate (data_baru) :
        data_break = data.split(",")
        nama_kosong.append(data_break)

    jumlah = 0
    while True :
        if jumlah >= len(nama_kosong) :
            print(f"sorry nama {nama} gaada di database")
            break
        
        elif nama_baru in nama_kosong[jumlah] :
            new_data = nama_kosong[jumlah]
            nama = new_data[0]
            print(f"nama {nama} ada di database ") 
            break

        else :
            jumlah += 1

        
        
    
