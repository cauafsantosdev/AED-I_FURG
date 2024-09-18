pontuacoes = ['.', ',', '!', '?', ';', ':']

texto = input("Digite um texto: ")
palavra = input("\nEscolha uma palavra do texto: ")

texto_minusc = texto.lower()
palavra_minusc = palavra.lower()

if palavra_minusc not in texto_minusc:
    print(f"{palavra} não faz parte do texto")
else:
    troca = input(f"Informe a palavra que substituirá {palavra}: ")
    palavras = texto.split()

    for i in range(len(palavras)):
        palavra_atual = palavras[i]
        ultima_letra = palavra_atual[-1]

        if ultima_letra in pontuacoes:
            base = palavra_atual[:-1]
            pontuacao = ultima_letra
        else:
            base = palavra_atual
            pontuacao = ''

        if base.lower() == palavra_minusc:
            if base.istitle():
                nova_palavra = troca.capitalize()
            elif base.isupper():
                nova_palavra = troca.upper()  
            else:
                nova_palavra = troca 

            palavras[i] = nova_palavra + pontuacao
    
    print(f"\n{" ".join(palavras)}")