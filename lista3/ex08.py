import random


alphanum = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789"

senha = "".join(random.choice(alphanum) for _ in range(6))

while True:
    chute = "".join(random.choice(alphanum) for _ in range(6))
    if chute == senha:
        print(f"A senha gerada foi {chute}")
        break