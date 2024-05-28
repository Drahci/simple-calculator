def calculadora():
    num1 = float(input("Informe um núemro : "))
    num2 = float(input("Informe outro núemro : "))
    op = input("Digite a operação (+, -, *, /): ")

    if (op == '+'):
        resultado = num1 + num2
    elif (op == '-'):
          resultado = num1 - num2
    elif (op == '*'):
          resultado = num1 * num2
    elif (op == '/'):
          resultado = num1 / num2
    else:
         print("A operção não encontrado !!!")
    print(f"O resultado da operção {num1} {op} {num2} = {resultado}")
    

#Programa principal
#Chamado suprograma calculdora() para executar
calculadora()
         