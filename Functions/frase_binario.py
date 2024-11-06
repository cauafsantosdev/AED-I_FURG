def convert_bin(n: int):
    binary = []
    while n >= 1:
        binary.append(int(n % 2))
        n /= 2
    
    binary = "".join(map(str, reversed(binary)))
    return binary.zfill(8)

def phrase_to_bin(phrase: str):
    bin_phrase = []
    for letter in phrase:
        converted = convert_bin(ord(letter))
        bin_phrase.append(converted)

    return " ".join(bin_phrase)


print(f"\nEm binário: {phrase_to_bin(input('Insira uma frase: '))}")