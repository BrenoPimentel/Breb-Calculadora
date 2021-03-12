from math import *
import sys
print('=' * 60)
print(f'{"CAlCULADORA":^60}')
print('=' * 60)
print('~~Eleve o número a 0.5 para a raiz quadrada.~~')
print('')


def matt():
    #  Checar se os valores digitados serão números
    contains_digit = False
    op = ' '
    while op != 'b' and op != 'a':
        op = str(input('Escolha entre operações Básica e Avançadas. [B/A] ')).lower().strip()
    num1 = input('Número: ')
    while True:
        #  Varrendo os valores de num1
        for character in num1:
            #  Assim que character for um digito, contains_digit passa a ser verdadeiro
            if character.isdigit():
                contains_digit = True
        #  Se existir digitos em num1
        if contains_digit is True:
            #  Checando se o valor digitado é um possível float
            if '.' in num1 and num1.count('.') == 1 and '.' != num1[0]:
                num1 = float(num1)
                break
            elif "-+!@#$%¨&*()/?^][´.,'•◘○♦♣♠☺☻♥☺☻♥" in num1:
                num1 = input('Digite somente números: ')
            else:
                if num1.isdecimal():
                    num1 = float(num1)
                    break
            num1 = input('OPÇÃO INVÁLIDA. Digite novamente: ')
        else:
            num1 = input('OPÇÃO INVÁLIDA. Número: ')
    add = num1
    #  Reseta contains_digit para falso, para poder checar os outros número digitado
    contains_digit = False
    if op == 'b':
        while True:
            print('[ +  ] Somar ')
            print('[ -  ] Subtrair ')
            print('[ x  ] Multiplicar ')
            print('[ /  ] Dividir ')
            print('[ ** ] Elevado')
            print('[ // ] Divisão total')
            print('[ %  ] Resto da divisão por')
            print('[ stop ] Parar')
            esc = input('Digite a operação: ').lower().strip()
            #  Se o usuário não digitar nada.
            while esc == '' or esc == ' ':
                esc = input('OPÇÃO INVÁLIDA. Digite a operação: ').lower().strip()
            #  Se o usuário digitar uma opção não catalogada
            while esc not in '+-xX///**stop%':
                print('OPÇÃO INVÁLIDA')
                print('[ +  ] Somar ')
                print('[ -  ] Subtrair ')
                print('[ x  ] Multiplicar ')
                print('[ /  ] Dividir ')
                print('[ ** ] Elevado')
                print('[ // ] Divisão total')
                print('[ %  ] Resto da divisão por')
                print('[ stop ] Parar')
                esc = input('Aqui: ').strip().lower()
            if esc == 'parar' or esc == 'stop':
                break
            num2 = input('Número: ')
            while True:
                #  Varrando os valores de num2
                for character in num2:
                    #  Se caracter for um digito. Contains_digit passa a ser verdadeiro
                    if character.isdigit():
                        contains_digit = True
                #  Se tiver digito no num2
                if contains_digit is True:
                    #  Para checar se o valor float é verdadeiro
                    if '.' in num2 and num2.count('.') == 1 and '.' != num2[0]:
                        num2 = float(num2)
                        break
                    elif "-+!@#$%¨&*()/?^][´.,'•◘○♦♣♠☺☻♥☺☻♥" in num2:
                        num2 = input('Digite somente números: ')
                    else:
                        if num2.isdecimal():
                            num2 = float(num2)
                            break
                    num2 = input('OPÇAÕ INVÁLIDA. Digite o número novamente: ')
                else:
                    num2 = input('Número: ')
            contains_digit = False
            if esc == 'soma' or esc == '+':
                add += num2
            elif esc == '-':
                add -= num2
            elif esc == 'x':
                add *= num2
            elif esc == '/':
                add /= num2
            elif esc == '//':
                add //= num2
            elif esc == '%':
                add %= num2
            elif esc == '**':
                add **= num2
            print('-' * 40)
            print(f'{"Resultado": >20}', end=' ')
            print(add)
            print('-' * 40)
    elif op == 'a':
        repet = 0
        num1 = int(num1)
        while True:
            # quando repet for maior que 1, entra em outro loop, pois se continuar no mesmo, não será possível escolher-
            # outro numero
            repet += 1
            if repet > 1:
                numrep = input('Digite um número: ')
                while True:
                    #  Varrendo os valores de num1
                    for character in numrep:
                        #  Assim que character for um digito, contains_digit passa a ser verdadeiro
                        if character.isdigit():
                            contains_digit = True
                    #  Se existir digitos em num1
                    if contains_digit is True:
                        #  Checando se o valor digitado é um possível float
                        if '.' in numrep and numrep.count('.') == 1 and '.' != numrep[0]:
                            numrep = float(numrep)
                            break
                        elif "-+!@#$%¨&*()/?^][´.,'•◘○♦♣♠☺☻♥☺☻♥" in numrep:
                            numrep = input('Digite somente números: ')
                        else:
                            if numrep.isdecimal():
                                numrep = float(numrep)
                                break
                        numrep = input('OPÇÃO INVÁLIDA. Digite novamente: ')
                    else:
                        numrep = input('OPÇÃO INVÁLIDA. Número: ')
                print('[ sen  ] Seno')
                print('[ cos  ] Cosseno')
                print('[ tg   ] Tangente')
                print('[  !   ] Fatorial')
                print('[ log  ] Logaritmo')
                print('[ raiz ] Raiz quadrada')
                esc1 = input('Digite a operação: ').strip()
                while esc1 not in 'sencostg!lograiz':
                    print('OPÇÃO INVÁLIDA')
                    print('[ sen  ] Seno')
                    print('[ cos  ] Cosseno')
                    print('[ tg   ] Tangente')
                    print('[  !   ] Fatorial')
                    print('[ log  ] Logaritmo')
                    print('[ raiz ] Raiz quadrada')
                    esc1 = input('Digite a operação: ').strip().lower()
                print('=' * 40)
                if esc1 == 'sen':
                    print(f'O seno de {numrep} é {sin(numrep):.2f}')
                elif esc1 == 'cos':
                    print(f'O cosseno de {numrep} é {cos(numrep)}')
                elif esc1 == 'tg':
                    print(f'A tangente de {numrep} é {tan(numrep):.2f}')
                elif esc1 == '!':
                    if numrep > 200:
                        print('Não foi possível calcular o fatorial. (NÚMERO GRANDE)')
                    else:
                        print(f'O fatorial de {numrep}! é {factorial(numrep)}')
                elif esc1 == 'log':
                    base = int(input('Digite a base para o log: '))
                    print(f'O log de {numrep} na base {base} é {log(numrep, base)}')
                elif esc1 == 'raiz':
                    print(f'A raiz quadrade de {numrep} é {sqrt(numrep):.2f}')
                print('=' * 40)
                cont = str(input('Quer continuar? [S/N]: ')).lower().strip()
                if cont == 's':
                    continue
                elif cont == 'n':
                    restart = ' '
                    while restart != 's' and restart != 'n':
                        restart = input('Deseja reiniciar o programa? [S/N]:').lower().strip()
                    if restart == 's':
                        matt()
                    elif restart == 'n':
                        input('ENTER PARA FINALIZAR')
                        # Exit program instantly
                        sys.exit()
            if repet == 1:
                print('[ sen  ] Seno')
                print('[ cos  ] Cosseno')
                print('[ tg   ] Tangente')
                print('[  !   ] Fatorial')
                print('[ log  ] Logaritmo')
                print('[ raiz ] Raiz quadrada')
                esc1 = input('Digite a operação: ').strip()
                while esc1 not in 'sencostg!lograiz':
                    print('OPÇÃO INVÁLIDA')
                    print('[ sen  ] Seno')
                    print('[ cos  ] Cosseno')
                    print('[ tg   ] Tangente')
                    print('[  !   ] Fatorial')
                    print('[ log  ] Logaritmo')
                    print('[ raiz ] Raiz quadrada')
                    esc1 = input('Digite a operação: ').strip()
                print('=' * 40)
                if esc1 == 'sen':
                    print(f'O seno de {num1} é {sin(num1):.2f}')
                elif esc1 == 'cos':
                    print(f'O cosseno de {num1} é {cos(num1)}')
                elif esc1 == 'tg':
                    print(f'A tangente de {num1} é {tan(num1):.2f}')
                elif esc1 == '!':
                    if num1 > 200:
                        print('Não foi possível calcular o fatorial. (NÚMERO GRANDE)')
                    else:
                        print(f'O fatorial de {num1}! é {factorial(num1)}')
                elif esc1 == 'log':
                    base = int(input('Digite a base para o log: '))
                    print(f'O log de {num1} na base {base} é {log(num1, base)}')
                elif esc1 == 'raiz':
                    print(f'A raiz quadrada de {num1} é {sqrt(num1)}')
                print('=' * 40)
                cont = ' '
                while cont != 's' and cont != 'n':
                    cont = str(input('Quer continuar? [S/N]: ')).lower().strip()
                if cont == 's':
                    continue
                elif cont == 'n':
                    restart = ' '
                    while restart != 's' and restart != 'n':
                        restart = input('Deseja reiniciar o programa? [S/N]: ').lower().strip()
                    if restart == 's':
                        #  Return the function matt(), then the program restart
                        matt()
                    elif restart == 'n':
                        #  Exit program instantly
                        sys.exit()
    print(f'O resultado é {add:.2f}')
    start = ' '
    while start != 's' and start != 'n':
        start = input('Deseja reiniciar o Programa? [S/N]').lower().strip()
    if start == 's':
        #  Return the function matt(), then the program restart
        matt()
    else:
        input('ENTER para finalizar: ')


if __name__ == '__main__':
    matt()
