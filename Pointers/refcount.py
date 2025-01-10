import sys

text = ['python']

print(f"Pointers ----> {sys.getrefcount(text)}")

outro = text

print(text, id(text))
print(outro, id(outro))

print("-" * 30)
print(f"Pointers ----> {sys.getrefcount(text)}")