from math import *
import sys


print('=' * 60)
print(f'{"CAlCULADORA":^60}')
print('=' * 60)
print('~~Eleve o número a 0.5 para a raiz quadrada.~~')
print('')


def matt():
    op = ' '
    while op != 'b' and op != 'a':
        op = str(input('Operações Básica ou Avançadas? [B/A] ')).lower().strip()
    num1 = float(input('Número: '))
    add = num1
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
            num2 = float(input('Número: '))
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
                numrep = int(input('Digite um número: '))
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
                        matt()
                    elif restart == 'n':
                        sys.exit()
    print(f'O resultado é {add:.2f}')
    start = ' '
    while start != 's' and start != 'n':
        start = input('Deseja reiniciar o Programa? [S/N]').lower().strip()
    if start == 's':
        matt()
    else:
        input('ENTER para finalizar: ')


if __name__ == '__main__':
    matt()
