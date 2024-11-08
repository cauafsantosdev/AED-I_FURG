def word_checker(word: str):
    if len(word) == 3:
        one = ["o", "n", "e"]
        for_one = 0

        for i in range(3):
            if word[i] == one[i]:
                for_one += 1

            if for_one == 2:
                return 1
        return 2
    return 3


cases = int(input(""))

for i in range(cases):
    word = input("")
    print(word_checker(word))