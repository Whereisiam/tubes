import os
import fileinput

def Menutampilan():
    print('============================')
    print('==== Inventaris Lab.Kom ====')
    print('============================')
    print('(1) Tambahkan Barang Baru')
    print('(2) Hapus Barang')
    print('(3) Update Barang')
    print('(4) Cari Barang di Inventaris')
    print('(5) Print Inventory Report')
    print('(6) Quit')
    CHOICE = int(input("Masukkan Pilihan: "))
    Menu(CHOICE)

def Menu(CHOICE):
    if CHOICE == 1:
        Tambahbarang()
    elif CHOICE ==2:
        hapusbarang()
    elif CHOICE ==3:
        Updatebarang()
    elif CHOICE == 5:
        liatbarang()
    elif CHOICE == 6:
        print("Terima kasih telah menggunakan program ini")
        exit()

#untuk open(r'C:\Users\zethm\Documents\Vscode\tubes\Gudang.txt', 'a') bisa diganti dengan open('gudang.txt', 'a')
#agar mempermudah pembacaan kode
def Tambahbarang():
    InventoryFile = open(r'C:\Users\zethm\Documents\Vscode\tubes\Gudang.txt', 'a')
    print("Menambahkan Inventory")
    print("================")
    item_description = input("Masukkan Nama Barang: ")
    item_quantity = input("Masukkan jumlah barang yang ingin dimasukkan: ")
    InventoryFile.write(item_description + '\n')
    InventoryFile.write(item_quantity + '\n')
    InventoryFile.close()

    lanjut=input('''
    tekan y jika ingin Melanjutkan program,
    tekan n untuk kembali ke menu : 
    ''').lower()
    if lanjut == "y":
        Tambahbarang()   
    elif lanjut == "n":
        Menutampilan()
    else:
        print("Inputan salah, Program kembali ke menu")
        Menutampilan()

def hapusbarang():
    print("Mengurangi Inventory")
    print("==================")
    item_description = input("Masukkan nama barang untuk di kurangi: ")

    file = fileinput.input('Gudang.txt', inplace=True)

    for line in file:
         if item_description in line:
             for i in range(1):
                 next(file, None)
         else:
             print(line.strip('\n'), end='\n')
    item_description
    lanjut=input('''
    tekan y jika ingin Melanjutkan program,
    tekan n untuk kembali ke menu : 
    ''').lower()
    if lanjut == "y":
        hapusbarang()   
    elif lanjut == "n":
        Menutampilan()
    else:
        print("Inputan salah, Program kembali ke menu")
        Menutampilan()

def Updatebarang():
    InventoryFile = open(r'C:\Users\zethm\Documents\Vscode\tubes\Gudang.txt', 'r')
    item_description = InventoryFile.readline()
    print('Inventory sekarang')
    print('-----------------')
    while item_description != '':
        item_quantity = InventoryFile.readline()
        item_description = item_description.rstrip('\n')
        item_quantity = item_quantity.rstrip('\n')
        print('Item:     ', item_description)
        print('Quantity: ', item_quantity)
        print('----------')
        item_description = InventoryFile.readline()
    print("Updating Inventory")
    print("==================")
    item_description = input('Masukkan nama barang untuk di update: ')
    item_quantity = int(input("Masukkan jumlah barang yang ingin di update. Ketik - untuk mengurangi: "))
    InventoryFile.close()
    
    with open(r'C:\Users\zethm\Documents\Vscode\tubes\Gudang.txt', 'r') as f:
        filedata = f.readlines()

    replace = ""
    line_number = 0
    count = 0
    f = open('Gudang.txt','r')
    file = f.read().split('\n')
    for i, line in enumerate(file):
        if item_description in line:
            for b in file[i+1:i+2]:
                value = int(b)
                change = value + (item_quantity)
                replace = b.replace(b, str(change))
                line_number = count
            count = i + 1      
    f.close()
    
    filedata[count] = replace + '\n'

    with open(r'C:\Users\zethm\Documents\Vscode\tubes\Gudang.txt', 'w') as f:
        for line in filedata:
            f.write(line)
                                             
    lanjut=input('''
    tekan y jika ingin Melanjutkan program,
    tekan n untuk kembali ke menu : 
    ''').lower()
    if lanjut == "y":
        Updatebarang()   
    elif lanjut == "n":
        Menutampilan()
    else:
        print("Inputan salah, Program kembali ke menu")
        Menutampilan()

def liatbarang():
    InventoryFile = open(r'C:\Users\zethm\Documents\Vscode\Tubes\Gudang.txt')
    item_description = InventoryFile.readline()
    print('Inventory sekarang')
    print('-----------------')
    while item_description != '':
        item_quantity = InventoryFile.readline()
        item_description = item_description.rstrip('\n')
        item_quantity = item_quantity.rstrip('\n')
        print('Item:     ', item_description)
        print('Quantity: ', item_quantity)
        print('----------')
        item_description = InventoryFile.readline()
    InventoryFile.close()

    lanjut=input('''
    tekan y jika ingin Melanjutkan program,
    tekan n untuk kembali ke menu : 
    ''').lower()
    if lanjut == "y":
        liatbarang()   
    elif lanjut == "n":
        Menutampilan()
    else:
        print("Inputan salah, Program kembali ke menu")
        Menutampilan()

Menutampilan()