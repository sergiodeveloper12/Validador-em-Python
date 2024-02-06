nome= str(input("Digite seu nome:..."))
print(nome ,"Bem vindo(a)")

print("Digite sua credencial")
id = int(input())

if id <=6:
    print("ID inválida, redigite credencial")
else:
    print("ID ok")
    
print("Insira seu email")
email=str(input())

def validar_email(email):
    if '@' in email and '.' in email:
        return True
    else:
        return False

if validar_email(email):
    print(f'O e-mail "{email}" é válido.')
else:
    print(f'O e-mail "{email}" não é válido.')
    
print("Insira seu telefone de contato")
tel= str(input("Telefone:"))
