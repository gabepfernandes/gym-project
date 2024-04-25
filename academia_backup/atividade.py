import psycopg2
from treino import consulta_simples_treino
from exercicio import consulta_simples_exercicio

connection = psycopg2.connect(
        dbname='academia',
        user='postgres',
        password='1234',
        host='localhost',
        port='5432'
    )


def consulta_atividade():
    print()
    consulta_simples_treino()
    print()
    treino_consulta = int(input('Digite o codigo do treino que deseja consultar: '))
    print()
    comando = f"""SELECT a.cod_treino, e.codexerc, e.nome, a.nroseries FROM atividade a
                    join exercicio e 
                    on e.codexerc = a.cod_exerc
                    where a.cod_treino = {treino_consulta}
                    order by e.codexerc
                    """

    cursor = connection.cursor()

    cursor.execute(comando)

    registros = cursor.fetchall()

    print("|TREINO|SERIES|COD - EXERCICIO")
    print('-------------------------------------')
    for registro in registros:
            print(f'|   {registro[0]}   |  {registro[3]}  |  {registro[1]}  - {registro[2]}')
    
    print()

def consulta_especifica_atividade(x=int):
    print()
    comando = f"""SELECT a.cod_treino, e.codexerc, e.nome, a.nroseries FROM atividade a
                    join exercicio e 
                    on e.codexerc = a.cod_exerc
                    where a.cod_treino = {x}
                    order by e.codexerc
                    """

    cursor = connection.cursor()

    cursor.execute(comando)

    registros = cursor.fetchall()

    print("|TREINO|SERIES|COD - EXERCICIO")
    print('-------------------------------------')
    for registro in registros:
            print(f'|   {registro[0]}   |  {registro[3]}  |  {registro[1]}  - {registro[2]}')
    
    print()

def cadastra_atividade():
    print()
    consulta_simples_treino()
    print()
    cod_treino = int(input('Digite o codigo do treino que deseja adicionar exercicios: '))
    print()
    num = int(input('Quantos exercicios deseja adicionar: '))
      
    i = 0
    while i < num:
        consulta_simples_exercicio()
        print()
        cod_exerc = int(input("Digite o codigo do exercicio que deseja adicionar: "))
        print()
        nroSeries = int(input("Digite o numero de series do exercicio: "))
        print()
        comando = f"""INSERT INTO public.atividade(
	                    cod_treino, cod_exerc, nroseries)
	                    VALUES ({cod_treino}, {cod_exerc}, {nroSeries});"""

        cursor = connection.cursor()
        cursor.execute(comando)
        i += 1

    print('\nAtividade cadastrada com sucesso!\n')

def atualiza_atividade():
     consulta_simples_treino()
     print()
     atualiza_treino = int(input('Digite o codigo do treino que deseja atualizar: '))
     print()
     consulta_especifica_atividade(atualiza_treino)
     print()
     atualiza_exerc = int(input('Digite o codigo do exercicio que deseja atualizar: '))
     print()
     novo_nroseries = int(input('Digite o numero atualizado de series do exercicio:'))

     comando = f"""UPDATE public.atividade
	            SET nroseries={novo_nroseries}
            	WHERE cod_exerc={atualiza_exerc} and cod_treino={atualiza_treino};"""
     
     cursor = connection.cursor()
     cursor.execute(comando)
     print()
     print('Treino atualizado com sucesso!')

def remove_atividade():
     consulta_simples_treino()
     treino_remove = int(input('\nDigite o codigo do treino que deseja remover um exercicio: '))
     consulta_especifica_atividade(treino_remove)
     exerc_remove = int(input('\nDigite o codigo do exercicio que deseja remover do treino: '))
     
     comando = f"""DELETE FROM public.atividade
                	WHERE cod_treino={treino_remove}
                    and cod_exerc={exerc_remove};"""
     
     cursor = connection.cursor()
     cursor.execute(comando)
     
     print("\nExercicio removido do treino com sucesso!\n")

cursor = connection.cursor()