import psycopg2
from equipamento import consulta_equip

connection = psycopg2.connect(
        dbname='academia',
        user='postgres',
        password='1234',
        host='localhost',
        port='5432'
    )

def consulta_exercicio():
    comando = """SELECT e.codexerc, e.nome, eq.nome FROM exercicio e
                join equipamento eq
                on e.cod_equip = eq.codequip
                ORDER BY codexerc ASC """

    cursor = connection.cursor()

    cursor.execute(comando)

    registros = cursor.fetchall()
    print("COD| EXERCICIO  -  EQUIPAMENTO  ")
    print('-------------------------------------')
    for registro in registros:
            print(f' {registro[0]} | {registro[1]} - {registro[2]}')

def consulta_simples_exercicio():
    comando = """SELECT e.codexerc, e.nome FROM exercicio e
                    ORDER BY codexerc ASC """

    cursor = connection.cursor()

    cursor.execute(comando)

    registros = cursor.fetchall()
    print("COD| EXERCICIO ")
    print('------------------------')
    for registro in registros:
            print(f' {registro[0]} | {registro[1]}')


def cadastra_exercicio():
    nome_exerc = input('Digite o nome do exercicio que deseja cadastrar: ')
    print()
    consulta_equip()
    print()
    cod_equip = int(input('Digite o codigo do equipamento usado no exercicio: '))
    print()

    comando = f"""INSERT INTO public.exercicio(
	nome, cod_equip)
	VALUES ('{nome_exerc}', {cod_equip});"""

    cursor = connection.cursor()
    cursor.execute(comando)
    
    print("Exercicio cadastrado com sucesso!")


def atualiza_exercicio():
      consulta_exercicio()
      print()
      exerc_atualiza = int(input('Digite o codigo do exercicio que deseja atualizar: '))
      print()
      novo_nome = input('Digite o nome atualizado do exercicio: ')
      print()
      consulta_equip()
      print()
      novo_equip = int(input('Digite o codigo atualizado do equipamento utilizado: '))
      print()

      comando = f"""UPDATE public.exercicio
	                SET nome='{novo_nome}', cod_equip={novo_equip}
	                WHERE codexerc = {exerc_atualiza};"""
      
      cursor = connection.cursor()
      cursor.execute(comando)
    
      print("Exercicio atualizado com sucesso!")

def remove_exercicio():
      consulta_simples_exercicio()
      exerc_remove = int(input('\nDigite o codigo do exercicio que deseja remover: '))

      comando1 = f"""DELETE FROM public.atividade
	                    WHERE cod_exerc={exerc_remove};"""
      
      comando2 = f"""DELETE FROM public.exercicio
	                    WHERE codexerc={exerc_remove};"""
      
      cursor = connection.cursor()
      cursor.execute(comando1)
      cursor.execute(comando2)
    
      print("\nExercicio removido com sucesso!\n")