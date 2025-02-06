while True:
    #Primeiro passo é definir as operações que a calculadora vai realizar.
    print("\nSelecione a operação:")
    print ("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")
    #verificar qual alternativa o usuário deseja.
    escolha = input("Digite sua escolha (1/2/3/4/5): ")
    
    if escolha == '5':
        print("Calculadora encerrada. Até mais!")
        break
    
    if escolha not in ['1', '2', '3', '4']:
        print("Opção inválida! Por favor, tente novamente.")
        continue
       #Capturar os números que o usuário solicitou
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Erro: Por favor, insira apenas números válidos.")
        continue
    #Verificar a operação escolhida pelo usuário.    
    if escolha == '1':
        resultado = num1 + num2
        print(f"Resultado: {num1} + {num2} = {resultado:.2f}")
    elif escolha == '2':
        resultado = num1 - num2
        print(f"Resultado: {num1} - {num2} = {resultado:.2f}")
    elif escolha == '3':
        resultado = num1 * num2
        print(f"Resultado: {num1} × {num2} = {resultado:.2f}")
    elif escolha == '4':
        if num2 == 0: 
            print("Erro: Não é possível dividir por zero!")
            #Não é permitido dividir por 0
        else:
            resultado = num1 / num2
            print(f"Resultado: {num1} ÷ {num2} = {resultado:.2f}")
