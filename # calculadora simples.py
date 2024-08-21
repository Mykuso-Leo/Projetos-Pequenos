# calculadora simples

numero1 = 0
numero2 = 0
resultado = 0
operacao = ''


numero1 = int(input('Digite o número 1:'))
operacao = input('Digite a Operação:')
numero2 = int(input('Digite o número 2:'))

if operacao == '+':
    resultado = numero1 + numero2

elif operacao == '-':
    resultado = numero1 - numero2

elif operacao == '/':
    resultado = numero1 / numero2

elif operacao == '*':
    resultado = numero1 * numero2

else:
    resultado = 'Operação Inválida'

print(str(numero1) + '' + str(operacao) + '' + str(numero2) + ' = ' + str(resultado))