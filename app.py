import os

restaurantes = [{'nome': 'Churrascaria ', 'categoria': 'churrascaria', 'ativo': True},
                {'nome': 'Saidera ','categoria': 'barzinho', 'ativo': False},
                {'nome': 'Comeu Morreu', 'categoria': 'comida do Samuel', 'ativo': True}]


def exibir_nome(): 
    '''Essa função se resume a mostrar o titúlo do meu programa'''
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
╚█████╗░███████║██████╦╝██║░░██║██████╔╝
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝

███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
█████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░ """)


def exibir_opcoes(): 
    '''Essa função serve para mostrar as opções que aparecerão no meu programa'''
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Alternar Estado do  Restaurante')
    print('4. Sair\n')


def finalizando_app(): 
    '''Esse função utiliza outra função para mostrar que o program está sendo encerrado'''
    exibir_subtitulo('Encerrando Programa')


def opcao_invalida(): 
    '''Essa função mostra que a opçao que o usuário digitou não é uma opção válida 
    
    Outputs: 
    - Voltar ao menu

    '''
    print('Opção inválida!\n')
    input("Digite uma tecla para voltar para o menu principal")
    main()


def voltar_ao_menu(): 
    '''Essa opção ajuda o usuário a voltar ao menu principal 
    
    Outputs: 
    - Voltar ao menu
    
    '''
    input('\nDigite uma tecla para voltar para o menu principal ')
    main()


def exibir_subtitulo(texto): 
    '''Essa função faz com que apareça subtitulos dependendo da opção escolhida 
    
    Inputs: 
    - texto str: o texto do subtítulo
    
    '''
    os.system('cls')
    linha = '*' * (len(texto)) 
    print(linha)
    print(texto) 
    print(linha)
    print()


def cadastrar_novo_restaurante(): 
    ''' Essa função é responsável por cadastrar um novo restaurante
    
    Inputs: 
    - Nome do restaurante 
    -Categoria 

    Outputs: 
    - Adiciona novos restaurantes a lista
    
    '''
    exibir_subtitulo('Cadastro de Novos Restaurantes')

    nome_do_restaurante = input(
        '\nDigite o nome do restaurante que deseja cadastrar: ')

    categoria = input(f'Digite o nome da categoria deste restaurante que  você cadastrou {nome_do_restaurante}: ')

    dados_do_restaurante = {'nome': nome_do_restaurante,'categoria': categoria, 'ativo': False}

    restaurantes.append(dados_do_restaurante)

    print(f'O resutaurante {nome_do_restaurante} foi cadastrado com sucesso\n')

    voltar_ao_menu()


def alternar_estado_restaurante(): 
    '''Essa função é responsável por Ativar e Desativar os restaurantes 
    
    Inputs: 
    - Nome do restaurante que deseja alternar o estado 

    Outputs: 
    -Ativar ou Desativar os restaurantes 
    
    '''
    exibir_subtitulo('Alterando estado do restaurante')

    nome_restaurante = input(
        'Digite o nome do restaurante que deseja alterar o estado: ')

    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {
                nome_restaurante} foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')

    voltar_ao_menu()


def listar_restaurantes():
    '''Essa função é responsável por listar os restaurantes já cadastrados
    
    Outputs: 
    - Listar os restaurantes com seu nomes, categorias e estado

    '''
    exibir_subtitulo('Listando novos Restaurantes\n') 

    print(f'{'Nome do Restaurante'.ljust(32)} | {'Categoria'.ljust(30)} | {'Status'}')
    print()
   
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ATIVADO' if restaurante['ativo'] else 'DESATIVADO'
        print(f'- {nome_restaurante.ljust(30)} | {categoria.ljust(30)} | {ativo}')  
       
       
    voltar_ao_menu()


def escolher_opcoes():
    '''Essa função faz com que, dependendo da opção que o usuário escolheu, aconteça outras coisas dentro da opção escolhida pelo usuário 
    
    Outputs: 
    -Dependendo da opção escolhida outras funções são chamadas para serem executadas

    '''
    try:

        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
            voltar_ao_menu()
        elif opcao_escolhida == 2:
            print('Listar Restaurante')
            listar_restaurantes()
            voltar_ao_menu()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
            voltar_ao_menu()
        elif opcao_escolhida == 4:
            finalizando_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main(): 
    '''Essa função faz com que apareca as funçoes primcipais dentro do terminal'''
    os.system('cls')
    exibir_nome()
    exibir_opcoes()
    escolher_opcoes()


if __name__ == '__main__':
    main()
