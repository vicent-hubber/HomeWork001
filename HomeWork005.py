from time import sleep
import getpass

# Simulador de Caixa Electronico

tentativa = 3

while True:
    nome = input("nome do usuario: ").strip().upper()
    if nome == "":
        print("insira um nome de usuario")

    while tentativa >= 0:
        senha = getpass.getpass("password: ")
        if senha == '123456':
            print("PROCESSANDO...")
            sleep(2)
            print(f"Ola,{nome}. Seja bem-vindo ao nosso banco!")
            print('Desfrute da experiência na nossa Plataforma Online!!')
            break
        else:
            if senha != '123456':
                print(f"Senha incorreta! voce tem ainda {tentativa - 1} tentativas")
        tentativa -= 1

        if tentativa == 0:
            print("SUa senha foi bloqueada! por favor, dirija-se a um dos nossos caixas.")
            break

    break