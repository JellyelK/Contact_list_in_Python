#Funções
def listar_contatos():
    with open("lista_contatos.txt", "r") as contatos:
        print(contatos.read())

def criar_contato():
    with open("lista_contatos.txt", "a+") as contatos:
            nome = str(input("Digite o Nome desse contato: "))
            try:
                numero = int(input("Digite o Número desse contato: "))
            except ValueError:
                print("Por favor digite apenas números")
                print(" ")
                return False
            email = str(input("Digite o Email desse contato: "))

            contatos.write(f"Nome: {nome} \n")
            contatos.write(f"Numero: {numero} \n")
            contatos.write(f"Email: {email} \n")
            contatos.write(f"\n")
            print("Contato registrado com sucesso\n")    

#Programa
while True:
    try:
        comando = int(input("Digite o numero da operação que deseja realizar: \n 1. Listar contatos \n 2. Criar Contato \n 0. Sair \n > "))
    except ValueError:
        print("Por favor digite um dos número acima \n")
        continue

    if comando == 1:
        listar_contatos()
        continue
    elif comando == 2:
        criar_contato()
    elif comando == 0:
        break
    else:
        print("Por favor digite um dos número acima")
        continue
