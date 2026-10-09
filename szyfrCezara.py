print(ord('a'),ord('z'))

def szyfrCezaraCzar(klucz,czar):
    wynik = ""
    index = ord(czar) + klucz
    while(index > ord('z')):
        index = index - ord('z') + ord('a')
        index = index - 1
    return chr(index)

def szyfrCezaraTekst(klucz,tekst):
    wynik = ""
    for i in tekst:
        wynik = wynik + szyfrCezaraCzar(klucz,i)
    return wynik

