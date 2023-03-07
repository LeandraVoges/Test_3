schluessel = int(input("Geben Sie eine Zahl ein, die als Schlüssel dient (1 - 18): "))
eingabe = input("Geben Sie ein Wort/einen Satz ein, der verschlüsselt werden soll: ")

def verschluesselung(schluessel, eingabe):
    ASCII = []
    x = []
    for character in eingabe:
        ASCII.append(ord(character))
#    print(ASCII)   
    i = 0
    while i <= len(ASCII) - 1:
        ASCII[i] = ASCII[i] + schluessel
        i += 1
    print(ASCII)
    for inhalt in ASCII:
        x.append(chr(inhalt))
    verschluesselt = "".join(x)
    print(x)
    print(f"Verschlüsselung: {verschluesselt}")

verschluesselung(schluessel, eingabe)

        