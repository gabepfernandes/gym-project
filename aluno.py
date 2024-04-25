import psycopg2
from plano import consulta_plano

connection = psycopg2.connect(
        dbname='academia',
        user='postgres',
        password='1234',
        host='localhost',
        port='5432'
    )

def cadastra_aluno():
    cpf_aluno = input('Digite o cpf do aluno: ')
    nome = input('Digite o nome do aluno: ')
    telefone = input('Digite o telefone do aluno: ')
    sexo = input('Digite o sexo do aluno(M/F): ')
    data_nascimento = input('Digite a data de nascimento do aluno(dd/mm/aaaa): ')
    email = input('Digite o email do aluno: ')
    peso = float(input('Digite o peso do aluno: '))
    altura = float(input('Digite a altura do aluno: '))
    consulta_plano()
    codigo_plano = int(input('\nQual o plano do aluno? '))

    cursor = connection.cursor()

    cursor.execute(f'''INSERT INTO public.aluno(
	nome, telefone, sexo, dtnascimento, email, peso, altura, cpf, cod_plano)
	VALUES ('{nome}', '{telefone}', '{sexo}', '({data_nascimento})', '{email}', {peso},{altura},'{cpf_aluno}', {codigo_plano});''')

    print('\nAluno cadastrado com sucesso!\n')

def consulta_dados_aluno():
    comando = 'SELECT * FROM aluno'

    cursor = connection.cursor()

    cursor.execute(comando)

    registros = cursor.fetchall()

    print('\n---------------------- A L U N O S ----------------------\n')

    print('|     EMAIL     |  TELEFONE |SEX|  DATA_NASC |  PESO | ALTURA |     CPF     |    NOME ')
    print('---------------------------------------------------------------------------------------')
    for registro in registros:
            print(f'| {registro[4]} | {registro[1]} | {registro[2]} | {registro[3]} | {registro[5]} |   {registro[6]}  | {registro[8]} | {registro[0]}')

def consulta_plano_aluno():
    comando = """SELECT a.cpf, a.nome, p.categoria from aluno a
                    join plano p 
                    on a.cod_plano = p.codplano"""
     
    cursor = connection.cursor()

    cursor.execute(comando)

    registros = cursor.fetchall()

    print('ALUNO | PLANO')
    print(('----------------'))
    for registro in registros:
            print(f'{registro[1]} | {registro[2]}')

def consulta_simples_aluno():
    comando = """SELECT a.cpf, a.nome from aluno a"""

    cursor = connection.cursor()

    cursor.execute(comando)

    registros = cursor.fetchall()

    print("|     CPF     |    NOME")
    print('---------------------------')
    for registro in registros:
            print(f'| {registro[0]} | {registro[1]}')

def remove_aluno():
      consulta_dados_aluno()

      nome_delete = (input('\nDigite o nome do aluno que deseja remover: '))
      
      comando = f"""DELETE FROM public.aluno
	                WHERE aluno.nome = '{nome_delete}'"""
      
      cursor = connection.cursor()

      cursor.execute(comando)

def atualiza_dados_aluno():
    consulta_simples_aluno()
    print()
    aluno_atualiza = input('Digite o nome do aluno que deseja atualizar: ')
    print()
    novo_nome = input("Digite o nome atualizado: ")
    novo_telefone = input("Digite o telefone atualizado: ")
    novo_sexo = input("Digite o sexo atualizado(M/F): ")
    novo_dtnascimento = input("Digite a data de nascimento atualizada: ")
    novo_email = input("Digite o email atualizado: ")
    novo_peso = float(input("Digite o peso atualizado: "))
    novo_altura = float(input("Digite a altura atualizado: "))

    comando = f"""UPDATE aluno SET cod_plano=NULL
                    WHERE aluno.nome = '{aluno_atualiza}'"""

    comando1 = f"""UPDATE public.aluno
	SET nome= '{novo_nome}', telefone='{novo_telefone}', sexo='{novo_sexo}', dtnascimento='({novo_dtnascimento})',
        email='{novo_email}', peso={novo_peso}, altura={novo_altura}
	    WHERE aluno.nome = '{aluno_atualiza}';"""
    
    cursor = connection.cursor()
    cursor.execute(comando)
    cursor.execute(comando1)
    
    cursor = connection.cursor()

    print('\nDados do aluno atualizados com sucesso!\n')

def atualiza_plano_aluno():
      consulta_plano_aluno()
      print()
      aluno_atualiza = input('Digite o nome do aluno que deseja atualizar o plano: ')
      print()
      consulta_plano()
      cod_plano = int(input('Digite o codigo do plano atualizado: '))

      comando = f"""UPDATE public.aluno
	                SET cod_plano={cod_plano}
	                WHERE aluno.nome = '{aluno_atualiza}';"""
      
      cursor = connection.cursor()
      cursor.execute(comando)
      print("\nPlano atualizado com sucesso!\n") 

def remove_aluno():
      consulta_simples_aluno()
      print()
      aluno_remove = input('Digite o cpf do aluno que deseja remover: ')
      
      comando1 = f"""UPDATE public.treino
	                    SET cpf_aluno=NULL
	                    WHERE cpf_aluno='{aluno_remove}';"""
                    
      comando2 = f"""DELETE FROM public.aluno
	                    WHERE cpf='{aluno_remove}'"""
      
      cursor = connection.cursor()
      cursor.execute(comando1)
      cursor.execute(comando2)

      print("\nAluno removido com sucesso\n") 

# atualiza_dados_aluno()

# atualiza_plano_aluno()


cursor = connection.cursor()



