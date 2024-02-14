"""
Calculo do primeiro dígito do CPF

"""
while True:
    while True:
        num_cpf = list(input('Informe os primeiros nove números do seu CPF: '))

        if len(num_cpf) != 9:
            if len(num_cpf) > 9:
                print('Voce informou mais que nove números')
            else:
                print('Voce informou menos que nove números')
        else:
            break

    i = 10
    j=0
    cont = 0

    while i >= 2:
        try:
            numeros = int(num_cpf[j])*i
            soma= numeros+cont
            cont = soma
        except Exception:
            print('Voce não informou valores válidos')
            break
        i-=1
        j+=1

    def primeiro_digito(soma): 
        digito = (soma * 10) % 11
        print(digito)
        if digito > 9:
            print('O primeiro digito do seu CPF é 0')
        elif digito < 9 and digito > 0 and digito != str:
            print(f'O primeiro digito do seu CPF é {digito}')
        nova_operacao = str(input('Deseja fazer uma nova consulta? [S]im ou [N]ão: '))
        nova_operacao.upper()
        if nova_operacao != 's':
            print('Operação encerrada')
            return False
        return True

    try: 
        final = primeiro_digito(soma)
        if not final:
            break
    except NameError:
        print('Informe os números corretamente')
    

    
