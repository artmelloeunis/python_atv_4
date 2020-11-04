def verifica_numero_primo(num):
    if num < 0 or num > 100:
        print("O número precisa ser maior ou igual a 0 e menor ou igual a 100!")
    else:
        iterador = 1
        contador = 0
        while iterador <= num:
            if num % iterador == 0:
                contador += 1
            iterador += 1
        if contador != 2:
            print(num, "não é um número primo!")
        else:
            print(num, "é um número primo!")

numero = int(input("Digite um numero: "))
verifica_numero_primo(numero)