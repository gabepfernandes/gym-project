import psycopg2
from aluno import consulta_simples_aluno
from instrutor import consulta_dados_instrutor, consulta_simples_instrutor

connection = psycopg2.connect(
        dbname='academia',
        user='postgres',
        password='1234',
        host='localhost',
        port='5432'
    )

def cadastra_treino():
    consulta_dados_instrutor()
    print()
    cpf_instrutor = input('Digite o cpf do instrutor responsavel pelo treino: ')
    print()
    consulta_simples_aluno()
    print()
    cpf_aluno = input('Digite o cpf do aluno: ')
    print()
    foco = input('Digite o foco do treino: ')
    print()
    duracao = int(input("Digite a duracao do treino em minutos: "))

    comando = f"""INSERT INTO public.treino(
	duracao, cpf_aluno, cpf_instrutor, foco)
	VALUES ({duracao}, '{cpf_aluno}', '{cpf_instrutor}', '{foco}');"""

    cursor = connection.cursor()
    cursor.execute(comando)

    print('\nTreino cadastrado com sucesso!\n')

def consulta_treino():
    comando = """SELECT t.codtreino, t.duracao, a.nome, i.nome, t.foco FROM treino t
                join aluno a on a.cpf = t.cpf_aluno
                join instrutor i on i.cpf = t.cpf_instrutor
                order by t.codtreino"""

    cursor = connection.cursor()

    cursor.execute(comando)

    registros = cursor.fetchall()
    print("COD| MIN|    FOCO    |  ALUNO  - INSTRUTOR")
    print('----------------------------------------------')
    for registro in registros:
            print(f' {registro[0]} | {registro[1]} | {registro[4]} | {registro[2]} - {registro[3]} ')

def consulta_simples_treino():
    comando = """SELECT t.codtreino, a.nome, t.foco FROM treino t
                join aluno a on a.cpf = t.cpf_aluno
                order by t.codtreino asc"""

    cursor = connection.cursor()
    cursor.execute(comando)

    registros = cursor.fetchall()
    print("COD|    FOCO    | ALUNO ")
    print('---------------------------')
    for registro in registros:
            print(f' {registro[0]} | {registro[2]} | {registro[1]}')

def atualiza_treino():
      print()
      consulta_treino()
      atualiza_treino = int(input('\nDigite o codigo do treino que deseja atualizar: '))
      novo_duracao = int(input('\nDigite a duracao atualizada do treino: '))
      novo_foco = input('\nDigite o foco atualizado do treino: ')
      print()
      consulta_simples_aluno()
      novo_aluno = input('\nDigite o cpf atualizado do aluno: ')
      print()
      consulta_simples_instrutor()
      novo_instrutor = input('\nDigite o cpf atualizado do instrutor: ')

      comando = f"""UPDATE public.treino
	                SET duracao={novo_duracao}, cpf_aluno='{novo_aluno}', cpf_instrutor='{novo_instrutor}', foco='{novo_foco}'
	                WHERE codtreino={atualiza_treino};"""
      
      cursor = connection.cursor()
      cursor.execute(comando)

      print('\nTreino atualizado com sucesso!\n')

def remove_treino():
      consulta_simples_treino()
      treino_remove = int(input('\nDigite o codigo do treino que deseja remover: '))

      comando1 = f"""DELETE FROM public.atividade
	                    WHERE cod_treino={treino_remove};"""
      
      comando2 = f"""DELETE FROM public.treino
	                    WHERE codtreino={treino_remove};"""
      
      cursor = connection.cursor()
      cursor.execute(comando1)
      cursor.execute(comando2)
    
      print("\nTreino removido com sucesso!\n")
