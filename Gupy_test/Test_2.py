#Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e
#o próximo valor sempre será a soma dos 2 valores anteriores
#(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
#escreva um programa na linguagem que desejar onde, informado um número,
#ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número
#informado pertence ou não a sequência.

n= int(input("informe o numero: "))
num1 = 0
num2 = 1
next_number = num2


while next_number <= n:
    if n == next_number:
        print(next_number, end=" ")
        print("\nEsse número pertence a sequencia de Fibonacci.")
        break
    print(next_number, end=" ")
    num1, num2 = num2, next_number
    next_number = num1 + num2

else:
    print("\nEsse número não pertence a sequencia de Fibonacci.")