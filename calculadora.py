##calculadora em python

while True:
    numero_1 = input('Digite um numero: ')
    numero_2 = input('Digite outro numero: ')
    Operador = input('Digite o operador(+-/*): ')

    numeros_validos = True
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
    
    if numeros_validos is None:
        print('Um ou ambos números digitados são invalidos.')

    operadores_permitidos = '+-/*'

    if Operador not in operadores_permitidos:
        print('Operador inválido.')
        continue
    if len(Operador) >1:
        print('Digite apenas um operador.')
        continue

    print(' Ralizando sua conta. Confira o resultado: ')
    if Operador == '+':
     print(f'{num_1_float}+{num_2_float}=', num_1_float + num_2_float)
    elif Operador == '-':
     print(f'{num_1_float}-{num_2_float}=', num_1_float - num_2_float)
    elif Operador == '/':
     print(f'{num_1_float}/{num_2_float}=', num_1_float / num_2_float)
    elif Operador == '*':
     print(f'{num_1_float}*{num_2_float}=', num_1_float * num_2_float)
     
    else:
       print('nunca deveria chegar aqui')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break