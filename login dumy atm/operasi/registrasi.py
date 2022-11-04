def regist() :
    list_nama = []

    while True :
        print("REGISTRASI")
        nama = input("nama : ")
        pin = input("pin : ")
        data_database = f"{nama},{pin},\n"
             
        with open("data.txt","r") as file :
            data_baru = file.readlines()

            for index,data in enumerate (data_baru) :
                data_break = data.split(",")
                list_nama.append(data_break[0])

            if nama in list_nama :
                print("\nnama tidak bisa dipakai")                                          
                is_done = input("\nlanjut registrasi (y/n) ?\n")
                if is_done == "n" :
                    break            

            else:
                with open("data.txt","a",encoding="utf-8") as file :
                    file.write(data_database)
                
                break
                
