import os 

"""
Sistema de gerenciamento de restaurantes via terminal.

Este programa permite:
- Cadastrar novos restaurantes
- Listar restaurantes cadastrados
- Alternar o status (ativo/inativo) de um restaurante

Observações importantes:
- O programa roda no terminal (CLI)
- Utiliza limpeza de tela com `os.system('clear')`
- Usa formatação de strings para exibição organizada
"""

restaurantes = [
    {'nome':'Praça', 'categoria':'Japonesa', 'ativo': False}, 
    {'nome':'Pizza Suprema', 'categoria':'Italiana', 'ativo': True},
    {'nome':'Cantina', 'categoria':'italiano', 'ativo': False}
]


def exibir_nome_do_programa():
    """
    Exibe o nome do sistema em formato ASCII art no terminal.
    """
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░ 
""")


def exibir_opcoes():
    """
    Exibe o menu principal com as opções disponíveis para o usuário.
    """
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')


def finalizar_app(): 
    """
    Finaliza o sistema exibindo uma mensagem de encerramento.
    """
    exibir_subtitulo('Finalizar app')


def voltar_ao_menu_principal():
    """
    Aguarda interação do usuário e retorna ao menu principal.
    """
    input('\nDigite uma tecla para voltar ao menu ')
    main()


def opcao_invalida():
    """
    Exibe mensagem de erro quando o usuário escolhe uma opção inválida.
    """
    print('Opção inválida!!\n')
    input('Digite uma tecla para voltar ao menu principal')
    main()


def exibir_subtitulo(texto):
    """
    Exibe um subtítulo formatado no terminal.

    Também limpa a tela antes de mostrar o conteúdo.

    Parâmetros:
    - texto (str): Texto que será exibido como título da seção

    Observação:
    - `os.system('clear')`:
        Executa um comando do sistema operacional.
        No caso, 'clear' limpa o terminal no Linux/Mac.
        No Windows, o equivalente seria 'cls'.
    """
    os.system('clear')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()


def cadastrar_novo_restaurante():
    """
    Cadastra um novo restaurante no sistema.

    Inputs:
    - Nome do restaurante
    - Categoria

    Funcionamento:
    - Cria um dicionário com os dados informados
    - Define o status inicial como inativo (False)
    - Adiciona o restaurante à lista global

    Output:
    - Restaurante adicionado na lista `restaurantes`
    """
    exibir_subtitulo('Cadastro de novos restaurantes')
    
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    
    dados_do_restaurante = {
        'nome': nome_do_restaurante,
        'categoria': categoria, 
        'ativo': False
    }

    restaurantes.append(dados_do_restaurante)

    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    input('Digite uma tecla para voltar ao menu principal ')
    main()


def listar_restaurantes():
    """
    Lista todos os restaurantes cadastrados no sistema.

    Exibe:
    - Nome do restaurante
    - Categoria
    - Status (ativado/desativado)

    Observação importante:
    - `ljust(n)`:
        Método de string que alinha o texto à esquerda,
        preenchendo com espaços até atingir o tamanho `n`.

        Exemplo:
        'Pizza'.ljust(10) → 'Pizza     '

        Isso é usado para manter a tabela visualmente organizada.
    """
    exibir_subtitulo('Listando restaurantes')
    
    print(f'{"Nome do restaurante".ljust(23)} | {"Categoria".ljust(20)} | Status')
    
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo  = 'ativado' if restaurante['ativo'] else 'desativado'

        print(f' - {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()


def alternar_estado_restaurante():
    """
    Alterna o estado (ativo/inativo) de um restaurante.

    Funcionamento:
    - Busca o restaurante pelo nome
    - Se encontrado, inverte o valor booleano usando `not`

    Explicação:
    - `not`:
        Operador lógico que inverte valores booleanos:
        True → False
        False → True

    Exemplo:
        restaurante['ativo'] = not restaurante['ativo']

    Output:
    - Atualiza o status do restaurante
    """
    exibir_subtitulo('Alternando estado do restaurante')
    
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True

            restaurante['ativo'] = not restaurante['ativo']

            mensagem = (
                f'O restaurante {nome_restaurante} foi ativado com sucesso'
                if restaurante['ativo']
                else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            )
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()


def escolher_opcao():
    """
    Captura a opção do usuário e direciona para a função correspondente.

    Tratamento de erro:
    - Usa `try/except` para evitar que o programa quebre caso o usuário
      digite algo que não seja número.
    """
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    """
    Função principal do sistema.

    Responsável por:
    - Limpar a tela
    - Exibir o menu
    - Iniciar o fluxo do programa

    Observação:
    - `if __name__ == '__main__'` garante que essa função só será executada
      quando o arquivo for rodado diretamente, e não quando for importado.
    """
    os.system('clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()