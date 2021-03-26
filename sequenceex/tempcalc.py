print("Programa de conversão de temperatura: Celsius e Fahrenheit\n")
print("1) Celsius para Fahrenheit")
print("2) Fahrenheit para Celsius")
print("3) Celsius para Kelvin")
print("4) Kelvin para Celsius")
print("5) Celsius para Rankine")
print("6) Rankine para Celsius")
print("7) Fahrenheit para Kelvin")
print("8) Kelvin para Fahrenheit")
print("9) Fahrenheit para Rankine")
print("10) Rankine para Fahrenheit")
print("11) Kelvin para Rankine")
print("12) Rankine para Kelvin\n")

option = input("> Digite uma opção: ")

# C = Celsius
# F = Fahrenheit
# K = Kelvin
# R = Rankine

if option == "1":  # Celsius > Fahrenheit
    try:
        c = float(input("\n> Digite a temperatura em Celsius que deseja converter: "))
        f = 9*c/5+32
        print(f'{c:.1f} graus Celsius correspondem a {f:.1f} graus Fahrenheit\n')
        print("Obrigado por utilizar o programa")
    except ValueError:
        print("\nO valor informado não corresponde a uma temperatura válida")
elif option == "2":  # Fahrenheit > Celsius
    try:
        f = float(input("\n> Digite a temperatura em Fahrenheit que deseja converter: "))
        c = 5/9*(f-32)
        print(f'{f:.1f} graus Fahrenheit correspondem a {c:.1f} graus Celsius\n')
        print("Obrigado por utilizar o programa")
    except ValueError:
        print("\nO valor informado não corresponde a uma temperatura válida")
elif option == "3":  # Celsius > Kelvin
    try:
        c = float(input("\n> Digite a temperatura em Celsius que deseja converter: "))
        k = c+275.15
        print(f'{c:.1f} graus Celsius correspondem a {k:.2f} graus Kelvin\n')
        print("Obrigado por utilizar o programa")
    except ValueError:
        print("\nO valor informado não corresponde a uma temperatura válida")
elif option == "4":  # Kelvin > Celsius
    try:
        k = float(input("\n> Digite a temperatura em Kelvin que deseja converter: "))
        c = k-275.15
        print(f'{k:.2f} graus Kelvin correspondem a {c:.1f} graus Celsius\n')
        print("Obrigado por utilizar o programa")
    except ValueError:
        print("\nO valor informado não corresponde a uma temperatura válida")
elif option == "5":  # Celsius > Rankine
    try:
        c = float(input("\n> Digite a temperatura em Celsius que deseja converter: "))
        r = (c+275.15)*1.8
        print(f'{c:.1f} graus Celsius correspondem a {r:.2f} graus Rankine\n')
        print("Obrigado por utilizar o programa")
    except ValueError:
        print("\nO valor informado não corresponde a uma temperatura válida")
elif option == "6":  # Rankine > Celsius
    try:
        r = float(input("\n> Digite a temperatura em Rankine que deseja converter: "))
        c = (r/1.8)-275.15
        print(f'{r:.2f} graus Rankine correspondem a {c:.1f} graus Celsius\n')
        print("Obrigado por utilizar o programa")
    except ValueError:
        print("\nO valor informado não corresponde a uma temperatura válida")
elif option == "7":  # Fahrenheit > Kelvin
    try:
        f = float(input("\n> Digite a temperatura em Fahrenheit que deseja converter: "))
        k = (f-32)*1.8+275.15
        print(f'{f:.2f} graus Fahrenheit correspondem a {k:.2f} graus Kelvin\n')
        print("Obrigado por utilizar o programa")
    except ValueError:
        print("\nO valor informado não corresponde a uma temperatura válida")
elif option == "8":  # Kelvin > Fahrenheit
    try:
        k = float(input("\n> Digite a temperatura em Kelvin que deseja converter: "))
        f = (k-275.15)*1.8+32
        print(f'{k:.2f} graus Kelvin correspondem a {f:.2f} graus Fahrenheit\n')
        print("Obrigado por utilizar o programa")
    except ValueError:
        print("\nO valor informado não corresponde a uma temperatura válida")
elif option == "9":  # Fahrenheit > Rankine
    try:
        f = float(input("\n> Digite a temperatura em Fahrenheit que deseja converter: "))
        c = 5/9*(f-32)
        r = (c + 275.15) * 1.8
        print(f'{f:.2f} graus Fahrenheit correspondem a {r:.2f} graus Rankine\n')
        print("Obrigado por utilizar o programa")
    except ValueError:
        print("\nO valor informado não corresponde a uma temperatura válida")
elif option == "10":  # Rankine > Fahrenheit
    try:
        r = float(input("\n> Digite a temperatura em Rankine que deseja converter: "))
        c = (r/1.8)-275.15
        f = 9 * c / 5 + 32
        print(f'{r:.2f} graus Rankine correspondem a {f:.2f} graus Fahrenheit\n')
        print("Obrigado por utilizar o programa")
    except ValueError:
        print("\nO valor informado não corresponde a uma temperatura válida")
elif option == "11":  # Kelvin > Rankine
    try:
        k = float(input("\n> Digite a temperatura em Kelvin que deseja converter: "))
        c = k-275.15
        r = (c + 275.15) * 1.8
        print(f'{k:.2f} graus Kelvin correspondem a {r:.2f} graus Rankine\n')
        print("Obrigado por utilizar o programa")
    except ValueError:
        print("\nO valor informado não corresponde a uma temperatura válida")
elif option == "12":  # Rankine > Kelvin
    try:
        r = float(input("\n> Digite a temperatura em Rankine que deseja converter: "))
        c = (r / 1.8) - 275.15
        k = c + 275.15
        print(f'{r:.2f} graus Rankine correspondem a {k:.2f} graus Kelvin\n')
        print("Obrigado por utilizar o programa")
    except ValueError:
        print("\nO valor informado não corresponde a uma temperatura válida")
else:
    print("\nO número ou letra escolhida não corresponde com nenhuma das opções.\n")
    print("Inicie o programa novamente para recomeçar.")
