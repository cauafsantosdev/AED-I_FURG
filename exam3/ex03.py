def get_emails(filename: str):
    emails = []

    with open(filename, "r") as file:
        emails = []

        for line in file.readlines():
            emails.append(line.strip())

    return emails

def update_emails(filename: str, emails: list):
    with open(filename, "w") as file:
        for email in emails:
            file.write(f"{email}\n")

def check_email(email: str):
    at = email.count("@") # Quantidade de @

    if at != 1: # Se tiver nenhum ou mais de 1 @
        return False
    
    at_idx = email.index("@") # Indice do @

    if at_idx == 0: # Se começa com @
        return False
    
    if "," in email: # Se tem vírgula
        return False
    
    domain = email[at_idx+1:] # Fatiando string, deixando dominio e .com
    
    if domain == ".com": # Se possui dominio
        return False
    
    for character in domain: # Se o dominio não é numérico
        if character.isdigit():
            return False
        
    point_idx = domain.index(".") # Indice do primeiro ponto

    if point_idx == 0: # Se não tem ponto
        return False
    else:
        point_ridx = domain.rindex(".") # Indice do ultimo ponto

        if point_ridx - point_idx == 1:
            return False

    return True

def check_list(emails: list):
    emails = [i for i in emails if check_email(i)]
    return emails


emails = get_emails("emails.txt")
emails = check_list(emails)
update_emails("emails.txt", emails)