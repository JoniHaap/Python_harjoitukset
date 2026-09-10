num = int(input("anna luku: "))

if num > 0: #jos merkataan != katsoo vain että numero ei ole nolla 
    if num % 2 == 0: # jakojäännös (jaettuna 2 kahdella niin saadaan parillinen tai pariton)
        print("numero on parillinen")
    else:
        print("numero on pariton")
else:
    print("numero oli nolla tai negatiivinen")

