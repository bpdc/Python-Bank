# INTEGRANTE:

# BEATRIZ PIMENTA DE CAMARGO - 42339561

# DIFERENCIAS NO PROGRAMA:

# VALIDAÇÃO DO EMAIL (@ .COM)
# VALIDAÇÃO DO TELEFONE (9 CARACTÉRES)
# CORES PADRONIZADAS NO PROGAMA
# LETRAS  MAIÚSCULAS NO NOME
# lETRAS MIÍSCULAS NO EMAIL

from random import randint
import os
import string

# DECLARANDO CORES
RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[1;32m"
RESET = "\033[0;0m"
BOLD  = "\033[;1m"
REVERSE = "\033[;7m"
YELLOW = "\033[1;33m"

# FUNÇÃO 14 17 20 23 26 29 E 30 ESTÉTICA 
def printred(msg):
    print( f'{RED}{msg}{RESET}')

def printblue(msg):
    print( f'{BLUE}{msg}{RESET}')

def printcyan(msg):
    print( f'{CYAN}{msg}{RESET}')

def printgreen(msg):
    print( f'{GREEN}{msg}{RESET}')

def printyellow(msg):
    print( f'{YELLOW}{msg}{RESET}')

def linhas():
    print('-=-=-=' * 15)

# FUNÇÃO SOLICITA A DIGITACAO DE UM CAMPO TEXTO,
#CASO O CAMPO TENHA UM VALOR EXIGIDO, INCLUIR O PARAMETRO EXIGIDO COM A QTDE DE CARACTERES NECESSÁRIOS
def digitatexto(msg,exigido=0):
    result = ''
    while True:
        result = input(msg)
        
        # VALIDAÇÃO DE ESPAÇO EM BRANCO
        if len(result) == 0:
            printred('[ERROR] ESTE CAMPO DEVE SER PREENCHIDO! TENTE NOVAMENTE')
            continue

        if (exigido > 0):
            if( len(result) != exigido ):
                printred(f'[ERROR] ESTE CAMPO DEVE POSSUIR {exigido} CARÁCTERES !')
                continue
        break
    return result

# FUNÇÃO SOLICITA A DIGITACAO DE UM CAMPO NUMÉRICO,
#CASO O CAMPO TENHA UM VALOR EXIGIDO, INCLUIR O PARAMETRO EXIGIDO COM A QTDE DE CARACTERES NECESSÁRIOS
def digitanum(msg,exigido=0):
    result = ''
    while True:
        result = input(msg)
        
        # VALIDAÇÃO DE ESPAÇO EM BRANCO
        if len(result) == 0:
            printred('[ERROR] ESTE CAMPO DEVE SER PREENCHIDO! TENTE NOVAMENTE')
            continue

        if not result.isdigit():
            printred('[ERROR] ESTE CAMPO DEVE SER PREENCHIDO SOMENTE COM NÚMEROS! TENTE NOVAMENTE')
            continue

        if (exigido > 0):
            if( len(result) != exigido ):
                printred(f'[ERROR] ESTE CAMPO DEVE POSSUIR {exigido} CARÁCTERES !')
                continue
        break
    return int(result)

# FUNÇÃO SOLICITA A DIGITAÇÃO DO EMAIL
def digitaemail(msg):
    result = ''
    while True:
        result = input(msg).lower()

        # VALIDAÇÃO DE ESPAÇO EM BRANCO
        if result == '':
            printred('[ERROR] ESTE CAMPO DEVE SER PREENCHIDO! TENTE NOVAMENTE')
            continue
        
        if '@' and '.com' not in result or len(result) == 0:
            printred('[ERROR] EMAIL INVÁLIDO! TENTE NOVAMENTE')
        else: 
            break
    return result

# FUNÇÃO  QUE SOLICITA A DIGITAÇÃO DE UM VALOR
def digitavalor(msg,minimo,msgerro):
    result = ''
    while True:
        result = input(msg)

        # VALIDAÇÃO DE ESPAÇO EM BRANCO
        if result == '':
            printred('[ERROR] ESTE CAMPO DEVE SER PREENCHIDO! TENTE NOVAMENTE')
            continue

        result = float(result)

        if(result <= minimo ):
            printred(msgerro)
            continue
        break
    return result

# FUNÇÃO DE VERIFICAÇÃO DE SENHA
def digitasenha(texto):
    senha = ''
    maxdigitos = 6
    while ( len(senha) != maxdigitos ):
        senha = input(texto)
        if len(senha) == 0:
            printred('[ERROR] ESTE CAMPO DEVE SER PREENCHIDO! TENTE NOVAMENTE')
            continue

        if len(senha) != 6:
            printred('[ERROR] A SENHA DEVE CONTER 6 DIGÍTOS!')

    return senha

# FUNÇÃO MENU PRINCIPAL
def menu():
    global listaconta
    global bloqueada
    
    # LIMPA O TERMINAL AO INICIAR O MEU PRINCIPAL
    os.system('cls')
    
    linhas()
    printred('SEJA BEM-VINDO(A) Python Bank')    
    linhas()
    printblue('MENU PRINCIPAL:')
    
    if not bloqueada:
        printcyan('''
        [1] CADASTRAR A CONTA CORRENTE
        [2] DEPOSITAR
        [3] SACAR
        [4] CONSULTAR SALDO
        [5] CONSULTAR EXTRATO
        [6] FINALIZAR \n''')
    else:
        printcyan('''
        [1] CADASTRAR A CONTA CORRENTE
        [2] DEPOSITAR
        [6] FINALIZAR \n''')

    # print('(DEBUG) ====> INFORMAÇÃO ARMAZENADA NA LISTA', listaconta)

# FUNÇÃO OPÇÃO 1
def opcao1():
    global listaconta

    #SOMENTE PARA TESTE
    # listaconta = [ 2120, "Beatriz Pimenta de Camargo", "998727103", "beatriz@gmail.com", 1000, 500, '123456' ]
    # return

    # VALIDAÇÃO DE APENAS UM CLIENTE 
    if len( listaconta ) != 0:
        printred('VOCÊ JÁ EFETUOU O CADASTRO! É PERMITIDO APENAS 1 CLIENTE')
        return

    # SORTEIO DO NÚMERO DE CONTA
    printyellow('\nMACK BANCO DIGITAL - CADASTRO INICIAL\n')
    numcont = int("%04d" % randint(1000, 9999))
    print(f'NÚMERO DA CONTA: {numcont}')

    nome = digitatexto('DIGITE O NOME DO CLIENTE: ').upper()
    tel = digitanum('DIGITE O TELEFONE (APENAS 9 NÚMERO): ',exigido=9)
    email = digitaemail('DIGITE O EMAIL: ')
    saldo = digitavalor('DIGITE O SALDO INICIAL: R$ ', 999, '[ERROR] O SALDO DEVE SER MAIOR QUE R$ 1000')
    lim = digitavalor('DIGITE O VALOR DO LIMITE: R$ ', -1,  '[ERROR] O LIMITE DEVE SER MAIOR QUE R$ 0')
    
    # VALIDAÇÃO DE SENHA
    senha = ''
    repeticao = None
    while senha != repeticao:
        senha = digitasenha('DIGITE A SENHA: ')
        repeticao = digitasenha('REPITA A SENHA: ')
        if senha != repeticao:
            printred('[ERROR] SENHAS NÃO CONFEREM! TENTE NOVAMENTE')
    
    # SALVA OS DADOS DIGITADOS EM UMA LISTA 
    listaconta = [ numcont, nome, tel, email, saldo, lim, senha ]
    
    tecla = input('PRESSIONE ENTER PARA VOLTAR AO MENU...')    

# FUNÇÃO OPÇÃO 2
def opcao2():
    global listaconta

    printyellow('\nMACK BANCO DIGITAL - DEPÓSITO \n')

    # VALIDAÇÃO DE APENAS UM CLIENTE 
    if len( listaconta ) == 0:
        printred('[ERROR] NÃO ENCONTRAMOS NENHUM CLIENTE CADASTRADO! USE A OPÇÃO 1')
        return

    # LENDO OS DADOS DOS CLIENTES
    numconta = listaconta[0]
    nome     = listaconta[1]
    telefone = listaconta[2]
    email    = listaconta[3]
    saldo    = listaconta[4]
    lim      = listaconta[5]
    senha    = listaconta[6]

    while True:
        numcontadigitado = int(digitatexto('NÚMERO DA CONTA PARA DEPÓSITO: ',exigido=4))
        
        if numcontadigitado != numconta:
            printred('[ERROR] NÚMERO DA CONTA INVÁLIDO! TENTE NOVAMENTE')
        else:
            printgreen(f'NOME DO CLIENTE: {nome}')
            break
       
    valdeposito = digitavalor('DIGITE O VALOR DO DEPÓSITO: R$ ', 0, '[ERROR] VALOR DO DEPÓSITO DEVE SER MAIOR QUE ZERO')

    # ATUALIZANDO O SALDO DA CONTA
    saldo = (saldo + valdeposito)

    # ATUALIZANDO A LISTA
    listaconta = [ numconta, nome, telefone, email, saldo, lim, senha ]
    historico.append( ['(+) DEPÓSITO', valdeposito ])
    
    tecla = input('PRESSIONE ENTER PARA VOLTAR AO MENU...')
   
# FUNÇÃO OPÇÃO 3
def opcao3():
    global listaconta
    global bloqueada
    global bloqueada

    printyellow('\nMACK BANCO DIGITAL - SAQUE \n')

    #  VALIDAÇÃO DE APENAS UM CLIENTE
    if len( listaconta ) == 0:
        printred('[ERROR] NÃO ENCONTRAMOS NENHUM CLIENTE CADASTRADO! USE A OPÇÃO 1')
        return

    # LENDO OS DADOS DO CLIENTE 
    numconta = listaconta[0]
    nome     = listaconta[1]
    telefone = listaconta[2]
    email    = listaconta[3]
    saldo    = listaconta[4]
    lim      = listaconta[5]
    senha    = listaconta[6]

    while True:
        numcontadigitado = int(digitatexto('NÚMERO DA CONTA PARA SAQUE: ',exigido=4))
        if numcontadigitado != numconta:
            printred('[ERROR] NÚMERO DA CONTA INVÁLIDO! TENTE NOVAMENTE')
        else:
            break        
    
    printgreen(f'NOME DO CLIENTE: {nome}')
    
    # VALIDAÇÃO DO NÚMERO DE TENTATIVAS E BLOQUEAR FUNÇÕES
    tentativas = 0
    while True:
        if tentativas >= 3:
            printred('[ERROR] FUNÇÃO CANCELADA...VOCÊ EXCEDEU O NÚMERO DE TENTATIVAS DE DIGITAÇÃO DE SENHA')
            bloqueada = True
            return
        
        senhadigitada = digitasenha('DIGITE A SENHA: ')
        if senhadigitada != senha:
            tentativas += 1
            printred('[ERROR] SENHAS NÃO CONFEREM! TENTE NOVAMENTE')
        else:
            break
    
    # VALIDAÇÃO DE SALDO
    while True:
        valorsaque = digitavalor('DIGITE O VALOR DO SAQUE: R$ ', -1, '[ERROR] O VALOR DO SAQUE DEVE SER MAIOR QUE ZERO')
        
        # CASO O VALOR DO SALDO SEJA 0 ELE VOLTA PARA O MENU PRINCIPAL
        if valorsaque == 0:
            return

        if ( valorsaque > saldo + lim ):
            printred('[ERROR] SAQUE IRA EXCEDER O SALDO + LIMITE')
        else:
            saldo = saldo - valorsaque
            break

    if saldo < 0:
        printyellow(f'VOCÊ ESTÁ USANDO O SEU LIMITE! ')

    printgreen(f'SALDO ATUAL: R$ {saldo}')
    printgreen(f'LIMITE ATUAL: R$ {lim}')


    # ATUALIZAÇÃO DA LISTA
    listaconta = [ numconta, nome, telefone, email, saldo, lim, senha ]
    historico.append( ['(-) SAQUE', valorsaque ])

    tecla = input('PRESSIONE ENTER PARA VOLTAR AO MENU...')

# FUNÇÃO OPÇÃO 4
def opcao4():
    global listaconta
    global historico
    global bloqueada

    printyellow('\nMACK BANCO DIGITAL - CONSULTA SALDO \n')

    # VALIDAÇÃO DE APENAS UM CLIENTE 
    if len( listaconta ) == 0:
        printred('[ERROR] NÃO ENCONTRAMOS NENHUM CLIENTE CADASTRADO! USE A OPÇÃO 1')
        return

    # LENDO OS DADOS DO CLIENTE 
    numconta = listaconta[0]
    nome     = listaconta[1]
    telefone = listaconta[2]
    email    = listaconta[3]
    saldo    = listaconta[4]
    lim      = listaconta[5]
    senha    = listaconta[6]

    # VALIDAÇÃO DO NÚMERO DA CONTA DE CONSULTA DE SALDO
    while True:
        numcontadigitado = input('DIGITE O NÚMERO DA CONTA: ')
        
        if numcontadigitado == '':
            printred('[ERROR] ESTE CAMPO DEVE SER PREENCHIDO! TENTE NOVAMENTE ')
        else:
            numcontadigitado = int(numcontadigitado)

        if numcontadigitado != numconta:
            printred('NÚMERO DA CONTA INVÁLIDO! TENTE NOVAMENTE')
        else:
            printgreen(f'NOME DO CLIENTE: {nome}')
            break

    # VALIDAÇÃO DO NÚMERO DE TENTATIVAS E BLOQUEAR FUNÇÃO
    tentativas = 0
    while True:
        if tentativas >= 3:
            printred('[ERROR] FUNÇÃO CANCELADA...VOCÊ EXECEDEU O NÚMERO DE TENTATIVAS DE DIGITAÇÃO DE SENHA')
            bloqueada = True
            return
        
        senhadigitada = digitasenha('DIGITE A SENHA: ')
        if senhadigitada != senha:
            tentativas += 1
            printred('[ERROR] SENHAS NÃO CONFEREM! TENTE NOVAMENTE')
        else:
            break        

    printgreen(f'NOME DO CLIENTE : {nome}')
    printgreen(f'SALDO DO CLIENTE : R$ {saldo}')
    printgreen(f'LIMITE DO CLIENTE: R$ {lim}')
    
    tecla = input('PRESSIONE ENTER PARA VOLTAR AO MENU...')

# FUNÇÃO OPÇÃO 5
def opcao5():
    global listaconta
    global historico
    global bloqueada

    printyellow('\nMACK BANCO DIGITAL - CONSULTA DE EXTRATO \n')

    #  VALIDAÇÃO DE APENAS UM CLIENTE
    if len( listaconta ) == 0:
        printred('[ERROR] NÃO ENCONTRAMOS NENHUM CLIENTE CADASTRADO! USE A OPÇÃO 1')
        return    

    # LENDO OS DADOS DO CLIENTE 
    numconta = listaconta[0]
    nome     = listaconta[1]
    telefone = listaconta[2]
    email    = listaconta[3]
    saldo    = listaconta[4]
    lim      = listaconta[5]
    senha    = listaconta[6]

    # VALIDAÇÃO DO NÚMERO DA CONTA DE CONSULTA DE SALDO
    while True:
        numcontadigitado = input('DIGITE O NÚMERO DA CONTA: ')
        
        if numcontadigitado == '':
            printred('[ERROR] ESTE CAMPO DEVE SER PREENCHIDO! TENTE NOVAMENTE')
        else:
            numcontadigitado = int(numcontadigitado)

        if numcontadigitado != numconta:
            printred('NÚMERO DA CONTA INVÁLIDO! TENTE NOVAMENTE')
        else:
            break

    # VALIDAÇÃO DO NÚMERO DE TENTATIVAS E BLOQUEAR FUNÇÕES
    tentativas = 0
    while True:
        if tentativas >= 3:
            printred('[ERROR] FUNÇÃO CANCELADA...VOCÊ EXECEDEU O NÚMERO DE TENTATIVAS DE DIGITAÇÃO DE SENHA')
            bloqueada = True
            return
        
        senhadigitada = digitasenha('DIGITE A SENHA: ')
        if senhadigitada != senha:
            tentativas += 1
            printred('[ERROR] SENHAS NÃO CONFEREM! TENTE NOVAMENTE')
        else:
            break  
    
    printgreen(f'NUMERO DA CONTA: {numconta}')
    printgreen(f'NOME DO CLIENTE: {nome}')
    printgreen(f'LIMITE DO CLIENTE: R$ {lim}')

    # VALIDAÇÃO DO HISTÓRICO DE OPERAÇÕES
    printcyan(f'HISTÓRICO DE OPERAÇÕES RECENTES')
    for operacoes in historico:
        printgreen( f'{operacoes[0]} --> {operacoes[1]}')

    printgreen(f'SALDO DO CLIENTE: R$ {saldo}')
    if ( saldo < 0 ):
        printyellow(f'ATENÇÃO AO SEU SALDO!')

    tecla = input('PRESSIONE ENTER PARA VOLTAR AO MENU...')

# FUNÇÃO OPÇÃO 6
def opcao6():
    printyellow('INTEGRANTE:')
    printgreen('Beatriz Pimenta de Camargo - 42339561')
    linhas()
    printred('FIM DO PROGRAMA! ATÉ BREVE')
    linhas()
    tecla = input('PRESSIONE ENTER PARA VOLTAR AO MENU...')


# COMEÇO DO PROGRAMA PRINCIPAL
listaconta = []
historico = []
bloqueada = False

while True:
    menu()

    opcao = None
    while opcao not in (1, 2, 3, 4, 5, 6):
        opcao = input('Digite sua opção: ')
        if len(opcao) == 0:
            printred('[ERROR] OPÇÃO DEVE SER PREENCHIDA! TENTE NOVAMENTE')
        else:
            opcao = int(opcao)

        linhas()

    # CADASTRO DE CONTA
    if opcao == 1:
        opcao1()

    # DEPOSITAR
    if opcao == 2:
        opcao2()

    # SACAR
    if opcao == 3:
        if bloqueada:
            printred('FUNÇÃO BLOQUEADA')
        else:
            opcao3()

    # CONSULTA DE SALDO
    if opcao == 4:
        if bloqueada:
            printred('FUNÇÃO BLOQUEADA')
        else:
            opcao4()

    # CONSULTA DE EXTRATO
    if opcao == 5:
        if bloqueada:
            printred('FUNÇÃO BLOQUEADA')
        else:
            opcao5()

    # FINALIZAR O PROGRAMA
    if opcao == 6:
        opcao6()
        break

