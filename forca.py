#Luiz Eduardo Treméa e Pablo Bortoluzzi
from os import system
import time
system("cls")

while True:
    print("----------------------------------")
    print("---Bem vindo ao jogo da Forca!---")
    print("-------do Luiz e Pablo----------")

    jogador = str(input("Nome do Jogador? "))
    carrasco = str(input("Nome do Carrasco? "))

    system("cls")

    palavra_secreta = str(input("Escolha a palavra secreta: ")).upper()
    system("cls")
    letras_acertadas= [ '_' for letra in palavra_secreta ]
    enforcou = False
    acertou  = False
    erros = 0
    faltas = 6    
    print(letras_acertadas)
    
    while True:
        print("O", carrasco, "devera digitar a dica 1 ")
        dica1 = input("Dica: ")
        if dica1.isalpha():
            break
        else:
            print("A dica deve conter apenas letras, tente novamente.")
            time.sleep(3)
            system("cls")
            print(letras_acertadas)

    while True:
        print("O", carrasco, "devera digitar a dica 2 ")
        dica2 = input("Dica: ")
        if dica2.isalpha():
            break
        else:
            print("A dica deve conter apenas letras, tente novamente.")
            time.sleep(3)
            system("cls")
            print(letras_acertadas)

    while True:
        print("O", carrasco, "devera digitar a dica 3 ")
        dica3 = input("Dica: ")
        if dica3.isalpha():
            break
        else:
            print("A dica deve conter apenas letras, tente novamente.")
            time.sleep(3)
            system("cls")
            print(letras_acertadas)

    while(not enforcou and not acertou):
        print("Você possui {} tentativas".format(faltas))
        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            faltas -= 1

        enforcou = erros == 6
        acertou = '_' not in (letras_acertadas)     
        if enforcou:
            file = open('log.txt', "w")
            file.write("Jogador:")
            file.write(jogador)
            file.write(",Carrasco:")
            file.write(carrasco)
            file.write(",o vencedor foi o(a):")
            file.write( carrasco)
            file.write(",a palavra era:")
            file.write(palavra_secreta)
            file.close()  

        elif acertou:
            file = open('log.txt', "w")
            file.write("jogador:")
            file.write(jogador)
            file.write(",Carrasco:")
            file.write(carrasco)
            file.write(",o vencedor foi o(a):")
            file.write(jogador)
            file.write(",a palavra era:")
            file.write(palavra_secreta)
            file.close()
        
        system("cls")
        print(letras_acertadas)

    if(acertou):
        print(jogador," Você venceu, Parabéns!")    
        print(" ░██░░░██░░░▄▄░░░░░░░██░░░▄▄░░░░░ ")
        print(" ██▀░▄██▀░▄███░░░░░░░▀██▄░▀█▄░██░ ")
        print(" ██░▄██░▄██▀░░░░░░░░░░░███░██░▀█▄ ")
        print(" ██▄██████░░░░░░░░░░░░░░██▄░██░██ ")
        print(" ███████▀░░▄▄░░░░░░░░░░░░████████ ")
        print(" ███████▄▄████▄▄░░░▄▄███▄▄███████ ")
        print(" ███████████▀▀███░███▀▀██████████ ")
        print(" ████████▀░░░░░▀▀▀▀▀░░░░░░███████ ")
        print(" ███████▀░░░░░░░░░░░░░░░░░░██████ ")
        print(" ███████▄░░░░░░░░░░░░░░░░░░██████ ")
        print(" ████████▄░░░░░░░░░░░░░░░░▄██████ ")
        print(" ██████████▄▄▄░░░░░░░▄▄▄▄████████ ")
        print(" ████████████████▄▄██████████████ ")
        print(" ▀▀▀▀▀░░░░░░░▀▀▀████▀▀▀░░░░░░░▀▀▀ ")
        print(" ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ ")
        print(" ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ ")

    else:
        system("cls")
        print("Que pena, você foi enforcado!")
        print("A palavra era {}".format(palavra_secreta))
        print("    ████▀░░░░░░░░░░░░░░░░░▀████")
        print("    ███│░░░░░░░░░░░░░░░░░░░│███")
        print("    ██▌│░░░░░░░░░░░░░░░░░░░│▐██")
        print("    ██░└┐░░░░░░░░░░░░░░░░░┌┘░██")
        print("    ██░░└┐░░░░░░░░░░░░░░░┌┘░░██")
        print("    ██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██")
        print("    ██▌░│██████▌░░░▐██████│░▐██")
        print("    ███░│▐███▀▀░░▄░░▀▀███▌│░███")
        print("    ██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██")
        print("    ██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██")
        print("    ████▄─┘██▌░░░░░░░▐██└─▄████")
        print("    █████░░▐█─┬┬┬┬┬┬┬─█▌░░█████")
        print("    ████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████")
        print("    █████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████")
        print("    ███████▄░░░░░░░░░░░▄███████")
        print("              Game Over        ")
        
        time.sleep(5)
        system("cls")

    print("Para Jogar novamente digite 1" )
    print("Para sair digite 0")
    opcao = input()
    if opcao == 1:
        continue
    else:
        break
        
