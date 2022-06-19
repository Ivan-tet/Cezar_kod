def szyfrowania(napis, przesunięcie):
    szyfer = ''     
    for x in range(len(napis)):
        if ord(napis[x]) < 1 or ord(napis[x]) > 122:
             szyfer += napis[x]
        elif ord(napis[x]) > 122:
             szyfer += chr(ord(napis[x]) + przesunięcie - 26)    
        else:    
             szyfer += chr(ord(napis[x])+ 5)
    return szyfer  


def deszyfrowania(napis,przesunięcie):
    szyfer = ''
    for x in range(len(napis)):
        if ord(napis[x]) < 1 or ord(napis[x]) > 122:
            szyfer += napis[x]
        elif ord(napis[x]) < 1:
            szyfer += chr(ord(napis[x]) - przesunięcie + 26)
        else:     
            szyfer += chr(ord(napis[x]) - 5)
    return  szyfer 

print(szyfrowania('sdasda', 5))
print(deszyfrowania('ufcufc',5))



     