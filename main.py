from prettytable import PrettyTable
print("+=====================+")
print("| TOP UP GAME MAS BRO |")
print("+=====================+")

dompet = {
    "Dana": 100000,
    "Gems": 45,
}

def topUpDana():
    tabel = PrettyTable()
    tabel.clear_rows()
    tabel.title = "TOP UP DANA MAS BRO"
    tabel.field_names = ["NO", "PILIHAN"]
    tabel.add_row(["[1]", "Rp. 10.000"])
    tabel.add_row(["[2]", "Rp. 20.000"])
    tabel.add_row(["[3]", "Rp. 50.000"])
    tabel.add_row(["[4]", "Rp. 100.000"])
    tabel.add_row(["[5]", "Rp. 500.000"])
    tabel.add_row(["[6]", "Rp. 1.000.000"])
    tabel.add_row(["[7]", "Rp. 10.000.000"])
    print(tabel)
    pilihanDana = int(input("Masukkin angka pilihan: "))
    
    if pilihanDana == 1:
        dompet["Dana"] += 10000
    elif pilihanDana == 2:
        dompet["Dana"] += 20000
    elif pilihanDana == 3:
        dompet["Dana"] += 50000
    elif pilihanDana == 4:
        dompet["Dana"] += 100000
    elif pilihanDana == 5:
        dompet["Dana"] += 500000
    elif pilihanDana == 6:
        dompet["Dana"] += 1000000
    elif pilihanDana == 7:
        dompet["Dana"] += 10000000
    else:
        print("PILIHAN MAS BRO GA ADA NIH, MASUKKAN PILIHAN YANG TERSEDIA YA!!")
        return
    
    print(f"Dana masbro sekarang adalah: Rp. {dompet['Dana']}")

def beliGems():
    tabel = PrettyTable()
    tabel.clear_rows()
    tabel.title = "BELI GEMS MAS BRO"
    tabel.field_names = ["NO", "PILIHAN", "HARGA"]
    tabel.add_row(["[1]", 5,  "Rp. 10000"])
    tabel.add_row(["[2]", 15, "Rp. 20000"])
    tabel.add_row(["[3]", 45, "Rp. 50000"])
    tabel.add_row(["[4]", 95, "Rp. 100000"])
    tabel.add_row(["[5]", 495,"Rp. 500000"])
    tabel.add_row(["[6]", 995,"Rp. 1000000"])
    tabel.add_row(["[7]", 9995,"Rp. 10000000"])
    print(tabel)
    pilihanGems = int(input("Masukkin angka pilihan: "))

    if pilihanGems == 1:
        print("Masbro membeli 5 gems dengan harga Rp. 10000")
        choice = input("Apakah Benar? y/n: ").lower()
        if choice == "y":
            dompet["Dana"] -= 10000
            dompet["Gems"] += 5
            print(f"Terimakasih sudah top up di sini, Gems masbro sekarang adalah {dompet['Gems']}")
        elif choice == "n":
            milih()

    if pilihanGems == 2:
        print("Masbro membeli 15 gems dengan harga Rp. 20000")
        choice = input("Apakah Benar? y/n: ").lower()
        if choice == "y":
            dompet["Dana"] -= 20000
            dompet["Gems"] += 15
            print(f"Terimakasih sudah top up di sini, Gems masbro sekarang adalah {dompet['Gems']}")
        elif choice == "n":
            milih()

    if pilihanGems == 3:
        print("Masbro membeli 45 gems dengan harga Rp. 50000")
        choice = input("Apakah Benar? y/n: ").lower()
        if choice == "y":
            dompet["Dana"] -= 50000
            dompet["Gems"] += 45
            print(f"Terimakasih sudah top up di sini, Gems masbro sekarang adalah {dompet['Gems']}")
        elif choice == "n":
            milih()

    if pilihanGems == 4:
        print("Masbro membeli 95 gems dengan harga Rp. 100000")
        choice = input("Apakah Benar? y/n: ").lower()
        if choice == "y":
            dompet["Dana"] -= 100000
            dompet["Gems"] += 95
            print(f"Terimakasih sudah top up di sini, Gems masbro sekarang adalah {dompet['Gems']}")
        elif choice == "n":
            milih()

    if pilihanGems == 5:
        print("Masbro membeli 495 gems dengan harga Rp. 500000")
        choice = input("Apakah Benar? y/n: ").lower()
        if choice == "y":
            dompet["Dana"] -= 500000
            dompet["Gems"] += 495
            print(f"Terimakasih sudah top up di sini, Gems masbro sekarang adalah {dompet['Gems']}")
        elif choice == "n":
            milih()

    if pilihanGems == 6:
        print("Masbro membeli 995 gems dengan harga Rp. 1000000")
        choice = input("Apakah Benar? y/n: ").lower()
        if choice == "y":
            dompet["Dana"] -= 1000000
            dompet["Gems"] += 995
            print(f"Terimakasih sudah top up di sini, Gems masbro sekarang adalah {dompet['Gems']}")
        elif choice == "n":
            milih()

    if pilihanGems == 7:
        print("Masbro membeli 9995 gems dengan harga Rp. 10000000")
        choice = input("Apakah Benar? y/n: ").lower()
        if choice == "y":
            dompet["Dana"] -= 10000000
            dompet["Gems"] += 9995
            print(f"Terimakasih sudah top up di sini, Gems masbro sekarang adalah {dompet['Gems']}")
        elif choice == "n":
            milih()
    return

def beliItem():
    tabel = PrettyTable()
    tabel.clear_rows()
    tabel.title = "BELI ITEM MAS BRO"
    tabel.field_names = ["NO", "PILIHAN", "HARGA"]
    tabel.add_row(["[1]", "SKIN EPEP SHOTGUN API GOKIL", 15])
    tabel.add_row(["[2]", "ELITE PASS EPEP GOKIL BUANGET", 70])
    tabel.add_row(["[3]", "BLESSING GENSHIN WANGY BANGET", 75])
    tabel.add_row(["[4]", "CHARA ALOK EPEP GANTENG MAKSIMAL", 495])
    tabel.add_row(["[5]", "SKIN KEQING GENSHIN WANGY BANGET", 995])
    tabel.add_row(["[6]", "SKIN KELLY EPEP KUNING CANTIK", 9995])
    tabel.add_row(["[7]", "CHARA BURNICE ZZZ PUANAS BANGET", 9995])
    print(tabel)
    pilihanItem = int(input("Masukkin angka pilihan: "))

    if pilihanItem == 1:
        print("Masbro membeli SKIN EPEP SHOTGUN API GOKIL dengan harga 15 gems?")
        choice =  input("Apakah Benar? y/n: ").lower()
        if choice == "y":
            if dompet["Gems"] >= 15:
                print("PEMBAYARAN BERHASIL, TERIMAKASIH TELAH MEMBELI ITEM DI TOP UP GAME MAS BRO!!")
            elif dompet["Gems"] < 15:
                print("MAAF MAS BRO, GEMS NYA KURANG NIH")
            else:
                None
        elif choice == "n":
            milih()

    if pilihanItem == 2:
        print("Masbro membeli ELITE PASS EPEP GOKIL BUANGET dengan harga 70 gems?")
        choice =  input("Apakah Benar? y/n: ").lower()
        if choice == "y":
            if dompet["Gems"] >= 70:
                print("PEMBAYARAN BERHASIL, TERIMAKASIH TELAH MEMBELI ITEM DI TOP UP GAME MAS BRO!!")
            elif dompet["Gems"] < 70:
                print("MAAF MAS BRO, GEMS NYA KURANG NIH")
            else:
                None
        elif choice == "n":
            milih()
        
    if pilihanItem == 3:
        print("Masbro membeli BLESSING GENSHIN WANGY BANGET dengan harga 75 gems?")
        choice =  input("Apakah Benar? y/n: ").lower()
        if choice == "y":
            if dompet["Gems"] >=75:
                print("PEMBAYARAN BERHASIL, TERIMAKASIH TELAH MEMBELI ITEM DI TOP UP GAME MAS BRO!!")
            elif dompet["Gems"] < 75:
                print("MAAF MAS BRO, GEMS NYA KURANG NIH")
            else:
                None
        elif choice == "n":
            milih()

    if pilihanItem == 4:
        print("Masbro membeli CHARA ALOK EPEP GANTENG MAKSIMAL dengan harga 495 gems?")
        choice =  input("Apakah Benar? y/n: ").lower()
        if choice == "y":
            if dompet["Gems"] >= 495:
                print("PEMBAYARAN BERHASIL, TERIMAKASIH TELAH MEMBELI ITEM DI TOP UP GAME MAS BRO!!")
            elif dompet["Gems"] < 495:
                print("MAAF MAS BRO, GEMS NYA KURANG NIH")
            else:
                None
        elif choice == "n":
            milih()

    if pilihanItem == 5:
        print("Masbro membeli SKIN KEQING GENSHIN WANGY BANGET dengan harga 995 gems?")
        choice =  input("Apakah Benar? y/n: ").lower()
        if choice == "y":
            if dompet["Gems"] >= 995:
                print("PEMBAYARAN BERHASIL, TERIMAKASIH TELAH MEMBELI ITEM DI TOP UP GAME MAS BRO!!")
            elif dompet["Gems"] < 995:
                print("MAAF MAS BRO, GEMS NYA KURANG NIH")
            else:
                None
        elif choice == "n":
            milih()

    if pilihanItem == 6:
        print("Masbro membeli SKIN KELLY EPEP KUNING CANTIK dengan harga 9995 gems?")
        choice =  input("Apakah Benar? y/n: ").lower()
        if choice == "y":
            if dompet["Gems"] >= 9995:
                print("PEMBAYARAN BERHASIL, TERIMAKASIH TELAH MEMBELI ITEM DI TOP UP GAME MAS BRO!!")
            elif dompet["Gems"] < 9995:
                print("MAAF MAS BRO, GEMS NYA KURANG NIH")
            else:
                None
        elif choice == "n":
            milih()

    if pilihanItem == 7:
        print("Masbro membeli CHARA BURNICE ZZZ PUANAS BANGET dengan harga 9995 gems?")
        choice =  input("Apakah Benar? y/n: ").lower()
        if choice == "y":
            if dompet["Gems"] >= 9995:
                print("PEMBAYARAN BERHASIL, TERIMAKASIH TELAH MEMBELI ITEM DI TOP UP GAME MAS BRO!!")
            elif dompet["Gems"] < 9995:
                print("MAAF MAS BRO, GEMS NYA KURANG NIH")
            else:
                None
        elif choice == "n":
            milih()
            
    return

def cekDana():
    print(f"Dana Anda: Rp. {dompet['Dana']}")
    print(f"Gems Anda: {dompet['Gems']}")

def milih():
    while True:
        tabel = PrettyTable()
        tabel.clear_rows()
        tabel.title = "MAS BRO MAU BELI APA NIH"
        tabel.field_names = ["NO", "PILIHAN"]
        tabel.add_row(["[1]", "MAU TOP UP DANA, MAS BRO"])
        tabel.add_row(["[2]", "MAU TOP UP GEMS, MAS BRO"])
        tabel.add_row(["[3]", "MAU BELI ITEM, MAS BRO"])
        tabel.add_row(["[4]", "MAU CEK DANA dan GEMS, MAS BRO"])
        tabel.add_row(["[5]", "KELUAR AJA DEH, MAS BRO"])
        print(tabel)
        try:
            pilihan = int(input("Masukkan pilihan 1/2/3/4/5: "))
            return pilihan
        except ValueError:
            print("Input harus angka masbro")

while True:
    pilihan = milih()
    if pilihan == 1:
        topUpDana()
    elif pilihan == 2:
        beliGems()
    elif pilihan == 3:
        beliItem()
    elif pilihan == 4:
        cekDana()
    elif pilihan == 5:
        print("TERIMAKASIH UDAH MAMPIR MAS BRO")
        break
    else:
        print("PILIHAN MAS BRO GA ADA NIH, MASUKKAN PILIHAN YANG VALID MAS BRO")