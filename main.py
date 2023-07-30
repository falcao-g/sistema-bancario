from typing import Final
import textwrap

def menu() -> str:
    menu: str = """
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo: float, valor: float, extrato: list[str], /) -> tuple[float, list[str]]:
    if valor > 0:
        saldo += valor
        extrato.append(f'Depósito:\tR$ {valor:.2f}')
        print('Depósito realizado com sucesso!')
    else:
        print('O valor precisa ser positivo!')

    return saldo, extrato

def sacar(*, saldo: float, valor: float, extrato: list[str], limite: float, numero_saques: int, limite_saques: int) -> tuple[float, list[str], int]:
    if valor > saldo:
        print('Saldo insuficiente!')
    
    elif valor > limite:
        print('Limite diário excedido!')

    elif numero_saques >= limite_saques:
        print('Limite de saques diários excedido!')

    elif valor <= 0:
        print('O valor precisa ser positivo!')

    else:
        saldo -= valor
        extrato.append(f'Saque:\t\tR$ {valor:.2f}')
        numero_saques += 1
        print('Saque realizado com sucesso!')
    
    return saldo, extrato, numero_saques

def exibir_extrato(saldo: float, /, *, extrato: list[str]) -> None:
    print('\n=========== EXTRATO ============')
    print('\n'.join(extrato) if extrato else 'Não foram realizadas movimentações!')
    print(f'\nSaldo:\t\tR$ {saldo:.2f}')
    print('================================')

def criar_conta(agencia: str, numero: int, usuarios: list[dict]) -> dict:
    cpf: str = input('Informe o CPF do usuário (somente os números): ')
    usuario: dict = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('Conta criada com sucesso!')
        return { 'agencia': agencia, 'numero_conta': numero, 'usuario': usuario }
    
    print('Usuário não encontrado, fluxo de criação de conta interrompido!')
    return {}

def listar_contas(contas: list) -> None:
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print('=' * 40)
        print(textwrap.dedent(linha))

def filtrar_usuario(cpf: str, usuarios: list[dict]) -> dict:
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return usuario

    return {}

def criar_usuario(usuarios: list[dict]) -> None:
    cpf: str = input('Informe o CPF (somente os números): ')
    usuario: dict = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('Usuário já cadastrado!')
        return
    
    nome: str = input('Informe o nome completo: ')
    data_nascimento: str = input('Informe a data de nascimento (dd/mm/aaaa): ')
    endereco: str = input('Informe o endereço (logradouro, num - bairro - cidade/sigla estado): ')

    usuarios.append({ 'cpf': cpf, 'nome': nome, 'data_nascimento': data_nascimento, 'endereco': endereco })

    print('Usuário cadastrado com sucesso!')

def main() -> None:
    LIMITE_SAQUES: Final = 5
    AGENCIA: Final = '1234'

    saldo: float = 0
    limite: float = 500
    extrato: list[str] = []
    numero_saques: int = 0
    usuarios: list[dict] = []
    contas: list = []
    

    while True:
        opcao: str = menu()

        match opcao:
            case 'd':
                valor: float = float(input('Digite o valor a ser depositado: '))
                saldo, extrato = depositar(saldo, valor, extrato)
                
            case 's':
                valor: float = float(input('Digite o valor a ser sacado: '))

                saldo, extrato, numero_saques = sacar(
                    saldo=saldo,
                    valor=valor,
                    extrato=extrato,
                    limite=limite,
                    numero_saques=numero_saques,
                    limite_saques=LIMITE_SAQUES
                )

            case 'e':
                exibir_extrato(saldo, extrato=extrato)

            case 'nc':
                numero_conta = len(contas) + 1
                conta = criar_conta(AGENCIA, numero_conta, usuarios)

                if conta:
                    contas.append(conta)

            case 'lc':
                listar_contas(contas)

            case 'nu':
                criar_usuario(usuarios)

            case 'q':
                print('Saindo do sistema...')
                break

            case default:
                print('Opção inválida!')

main()