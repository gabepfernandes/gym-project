import psycopg2
from plano import *
from aluno import *
from instrutor import *
from treino import *
from equipamento import *
from exercicio import *
from atividade import *
from relatorio import *

def painel_geral():
    print("1 - Realizar um Cadastro")
    print("2 - Realizar uma Consulta")
    print("3 - Realizar uma Atualizacao")
    print("4 - Realizar uma Remocao")
    print("5 - Relatorios")
    print("6 - Sair")

def painel_consulta():
    print("1 - Consultar Alunos")
    print("2 - Consultar Instrutores")
    print("3 - Consultar Planos")
    print("4 - Consultar Treinos")
    print("5 - Consultar Exercicios")
    print("6 - Consultar Equipamentos")

def painel_consulta_aluno():
    print("1 - Consultar Dados dos Alunos")
    print("2 - Consultar Planos dos Alunos")

def painel_consulta_treino():
    print("1 - Consultar Dados dos Treinos")
    print("2 - Consultar Atividades de Treino Especifico")

def painel_cadastro():
    print("1 - Cadastrar Aluno")
    print("2 - Cadastrar Instrutor")
    print("3 - Cadastrar Plano")
    print("4 - Cadastrar Treino")
    print("5 - Cadastrar Exercicio")
    print("6 - Cadastrar Equipamento")

def painel_cadastro_treino():
    print("1 - Cadastrar Treino")
    print("2 - Cadastrar Atividades em Treino")

def painel_atualiza():
    print("1 - Atualizar Aluno")
    print("2 - Atualizar Instrutor")
    print("3 - Atualizar Plano")
    print("4 - Atualizar Treino")
    print("5 - Atualizar Exercicio")
    print("6 - Atualizar Equipamento")

def painel_atualiza_aluno():
    print("1 - Atualizar Dados do Aluno")
    print("2 - Atualizar Plano do Aluno")

def painel_remove():
    print("1 - Remover Aluno")
    print("2 - Remover Instrutor")
    print("3 - Remover Plano")
    print("4 - Remover Treino")
    print("5 - Remover Exercicio")
    print("6 - Remover Equipamento")

def painel_remove_treino():
    print('1 - Remover Treino')
    print('2 - Remover Atividades de Treino')

def painel_relatorio():
    print('1 - Relatorio de Alunos nascidos antes de 2000 com Plano Diamond')
    print('2 - Relatorio de Instrutores homens que montaram Treinos com foco em Superiores')
    print('3 - Relatorio de Exercicios que podem ser feito na polia')

try:
    connection = psycopg2.connect(
        dbname='academia',
        user='postgres',
        password='1234',
        host='localhost',
        port='5432'
    )
    cursor = connection.cursor()

    while True:
        print('\n------- PAINEL -------\n')
        painel_geral()
        opcao = int(input('\nVoce deseja: '))

        match opcao:
            case 1:
                print()
                painel_cadastro()
                opcao_cadastro = int(input('\nSelecione uma opcao: '))
                print()

                match opcao_cadastro:
                    case 1:
                        print()
                        cadastra_aluno()
                        print()

                    case 2:
                        print()
                        cadastra_instrutor()
                        print()

                    case 3:
                        print()
                        cadastra_plano()
                        print()

                    case 4:
                        print()
                        painel_cadastro_treino()
                        opcao_cadastro_treino = int(input('\nSelecione uma opcao: '))

                        match opcao_cadastro_treino:
                            case 1:
                                print()
                                cadastra_treino()
                                print()

                            case 2:
                                print()
                                cadastra_atividade()
                                print()

                    case 5:
                        print()
                        cadastra_exercicio()
                        print()

                    case 6:
                        print()
                        cadastra_equip()
                        print()

            case 2:
                print()
                painel_consulta()
                opcao_consulta = int(input('\nSelecione uma opcao: '))
                print()

                match opcao_consulta:
                    case 1:
                        painel_consulta_aluno()
                        opcao_consulta_aluno = int(input('\nSelecione uma opcao: '))
                        print()

                        match opcao_consulta_aluno:
                            case 1:
                                consulta_dados_aluno()
                                print()
                            
                            case 2:
                                consulta_plano_aluno()
                                print()

                    case 2:
                        print()
                        consulta_dados_instrutor()
                        print()

                    case 3:
                        print()
                        consulta_plano()
                        print()

                    case 4:
                        print()
                        painel_consulta_treino()
                        opcao_consulta_treino = int(input('\nSelecione uma opcao: '))

                        match opcao_consulta_treino:
                            case 1:
                                print()
                                consulta_treino()
                                print()

                            case 2:
                                print()
                                consulta_atividade()
                                print()

                    case 5:
                        print()
                        consulta_exercicio()
                        print()

                    case 6:
                        print()
                        consulta_equip()
                        print()


            case 3:
                print()
                painel_atualiza()
                opcao_atualiza = int(input('\nSelecione uma opcao: '))
                print()

                match opcao_atualiza:
                    case 1:
                        print()
                        painel_atualiza_aluno()

                        opcao_atualiza_aluno = int(input('\nSelecione uma opcao: '))
                        
                        match opcao_atualiza_aluno:
                    
                            case 1:
                                print()
                                atualiza_dados_aluno()
                                print()

                            case 2:
                                print()
                                atualiza_plano_aluno()
                                print()

                    case 2:
                        print()
                        atualiza_dados_instrutor()
                        print()

                    case 3:
                        print()
                        atualiza_plano()
                        print()

                    case 4:
                        print()
                        atualiza_atividade()
                        print()

                    case 5:
                        print()
                        atualiza_exercicio()
                        print()


                    case 6:
                        print()
                        atualiza_equip()
                        print()
    
            case 4:
                print()
                painel_remove()
                opcao_remove = int(input('\nSelecione uma opcao: '))
                print()

                match opcao_remove:
                    case 1:
                        print()
                        remove_aluno()
                        print()
                        
                    case 2:
                        print()
                        remove_instrutor()
                        print()

                    case 3:
                        print()
                        remove_plano()
                        print()

                    case 4:
                        print()
                        painel_remove_treino()
                        print()
                        opcao_remove_treino = int(input('\nSelecione uma opcao: '))

                        match opcao_remove_treino:
                            case 1:
                                print()
                                remove_treino()
                                print()

                            case 2:
                                print()
                                remove_atividade()
                                print()

                    case 5:
                        print()
                        remove_exercicio()
                        print()


                    case 6:
                        print()
                        remove_equip()
                        print()

            case 5:
                print()
                painel_relatorio()
                opcao_relatorio = int(input("\nQual relatorio deseja gerar: "))

                match opcao_relatorio:
                    case 1:
                        print()
                        relatorio_1()
                        print()

                    case 2:
                        print()
                        relatorio_2()
                        print()

                    case 3:
                        print()
                        relatorio_3()
                        print()

            case 6:
                print('Saindo dos sistema...')
                break



except Exception as error:
    print(error)
finally:
    if cursor is not None:
        cursor.close()
    if connection is not None:
        connection.close()