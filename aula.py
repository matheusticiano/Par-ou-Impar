numero = input('Digite um inteiro: ')

if numero.isdigit() :
    numero = int(numero)
    if numero%2 == 0 :
        print(f"{numero} é par !")
    else :
        print(f"{numero} é impar !")
else:
    print("Insira um numero valido !")

