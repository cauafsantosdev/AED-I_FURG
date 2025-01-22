string = input("Insira uma string: ")

whitespace_sequences = []
sequence = 0
for i in range(len(string)):
    if string[i] == " ":
        sequence += 1
        if i == len(string) -1:
            whitespace_sequences.append(sequence)
    elif sequence > 0:
        whitespace_sequences.append(sequence)
        sequence = 0

print(f"Maior sequencia de espaços: {max(whitespace_sequences)} espaços")