while True:
    print("Olá, escolha a opção que você deseja:\n"
          "1 - Ordenar números de forma crescente\n"
          "2 - Encerrar atividades")
    choice = int(input("Qual opção você deseja? "))



    if choice == 1:
        n1 = int(input("Digite um valor: "))
        n2 = int(input("Digite o segundo valor: "))
        n3 = int(input("Digite o terceiro valor: "))
    
        if n1 <= n2 and n1 <= n3:
            valorp1 = n1

            if n2 <= n3:
                valorp2 = n2
                valorp3 = n3

            else:
                valorp2 = n3
                valorp3 = n2
            
        elif n2 <= n1 and n2 <= n3:
            valorp1 = n2

            if n1 <= n3:
                valorp2 = n1
                valorp3 = n3

            else:
                valorp2 = n3
                valorp3 = n1

        else:
            valorp1 = n3

            if n1 <= n2:
                valorp2 = n1
                valorp3 = n2

            else:
                valorp2 = n2
                valorp3 = n1


        print("Os valores em ordem crescente são: ",valorp1, valorp2, valorp3)


    if choice == 2:
        print ("Obrigado por testar esse grandioso sistema desenvolvido por aluno de Eng.Soft.")
        break