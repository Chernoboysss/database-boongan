from CRU import chek,view


#dumy = (chek.cek_nama("agung"))
#kalo nama ada di database akan True
#kalo gaada akan false

# index = chek.cek_index("asep")
# print(index)

# saldo = int(chek.cek_saldo(index))
# print(saldo)
# saldo -= 2000
# print(saldo)

# index = chek.list_index_data()
# print(max(index))


saldo = 11000010

print(view.saldo_ribuan(saldo))

list_kosong = ["23000",50000]

saldo = (f"{list_kosong[0]:,}")
print(f"{saldo.replace(',', '.')}")

