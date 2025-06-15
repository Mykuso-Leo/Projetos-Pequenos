VALORES = {
    'PesoT' : '',
    'PesoM' : '',
    'Reps' : '',
    'Calculo' : ''
}

def Calculos(PesoT, PesoM, Reps, Calculo):
    if Calculo == 'M':
        print('Insira o Peso Total:')
        PesoT = float(input())
        return PesoT / 2
    elif Calculo == 'T':
        print('Insira quanto tem em cada lado:')
        PesoM = float(input())
        return PesoM * 2
    elif Calculo == 'V':
        print('Insira quanto tem de Peso Total:')
        PesoT = float(input())
        print('Insira quantas repetições você fez:')
        Reps = float(input())
        return PesoT * Reps
    else: 
        return "continue"

while True:
    print(
        "Escolha a função:\n"
        "Para calcular quanto você deve colocar de cada lado, insira - M\n"
        "Para calcular quanto de peso tem no total, insira - T\n"
        "Para calcular qual o volume da série, insira - V\n"
        "Para sair, insira - S"
        )
    Calculo = input().upper()
    if Calculo == 'S':
        break

    result = Calculos("PesoT", "PesoM", "Reps", Calculo)

    if result == 'continue':
        print('Inválido')
        continue
    elif Calculo == 'M':
        print(f'Você deve colocar {result} Kg em cada lado da barra') 
    elif Calculo == 'T':
        print(f'Tem {result} Kg na barra')
    elif Calculo == 'V':
        print(f'O volume da sua série foi de {result} Kg')
    
    print(
          "Para sair, aperte - S\n"
          "Para recomeçar, aperte qualquer outra letra\n"
          )
    escolha = input()
    if escolha.upper() == 'S':
        break
    else: continue
