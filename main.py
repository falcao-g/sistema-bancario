from typing import Iterable, Final

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo: float = 0
limites: float = 500
extrato: Iterable[str] = []
numero_saques: int = 0
LIMITE_SAQUES: Final = 5

while True:
    opcao: str = input(menu)

    if opcao == 'd':
        valor: float = float(input('Digite o valor a ser depositado: '))

        if valor > 0:
            saldo += valor
            extrato.append(f"Depósito: R$ {valor:.2f}")
        
        else:
            print('O valor precisa ser positivo!')

    elif opcao == 's':
        valor: float = float(input('Digite o valor a ser sacado: '))

        if valor > 0:
            if numero_saques < LIMITE_SAQUES:
                if saldo >= valor:
                    saldo -= valor
                    extrato.append(f"Saque: R$ {valor:.2f}")
                    numero_saques += 1
                
                else:
                    print('Saldo insuficiente!')
            
            else:
                print('Limite de saques atingido!')

        else:
            print('O valor precisa ser positivo!')

    elif opcao == 'e':
        print('\n ========== EXTRATO ==========')
        print('\n'.join(extrato) if extrato else 'Não foram realizadas movimentações!')
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('================================')

    elif opcao == 'q':
        print('Encerrando o programa...')
        break

    else:
        print('Opção inválida!')