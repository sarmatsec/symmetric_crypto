import random

char_to_code = {
    'A': '00000', 'Ą': '00001', 'B': '00010', 'C': '00011', 'Ć': '00100',
    'D': '00101', 'E': '00110', 'Ę': '00111', 'F': '01000', 'G': '01001',
    'H': '01010', 'I': '01011', 'J': '01100', 'K': '01101', 'L': '01110',
    'Ł': '01111', 'M': '10000', 'N': '10001', 'Ń': '10010', 'O': '10011',
    'Ó': '10100', 'P': '10101', 'R': '10110', 'S': '10111', 'Ś': '11000',
    'T': '11001', 'U': '11010', 'W': '11011', 'Y': '11100', 'Z': '11101',
    'Ż': '11110', ' ': '11111'
}

tekstJawny = input("Proszę podać tekst jawny: ").upper()

# Wykrywanie nieznanych znaków
nieznane_symbole = [symbol for symbol in tekstJawny if symbol not in char_to_code]

if nieznane_symbole:
    print("Tekst zawiera nieznane symbole:", set(nieznane_symbole))
else:
    print("\nTekst w systemie binarnym:")
    tekstBinarnie = [char_to_code[symbol] for symbol in tekstJawny]
    print(tekstBinarnie)

    # Wylosowanie klucza z listy kluczy słownika
    klucze_lista = list(char_to_code.values())
    klucz = [random.choice(klucze_lista) for _ in range(len(tekstJawny))]

    print("\nWygenerowany klucz:")
    print(klucz)

    szyfrogram = []
    for i in range(len(tekstBinarnie)):
        # Konwersja ciągów binarnych na liczby, XOR i powrót do formatu 5-bitowego
        bit_tekst = int(tekstBinarnie[i], 2)
        bit_klucz = int(klucz[i], 2)
        wynik_xor = bit_tekst ^ bit_klucz
        szyfrogram.append(f"{wynik_xor:05b}")

    print("\nSzyfrogram Vernama:")
    print(szyfrogram)
