import psycopg2

connection = psycopg2.connect(
        dbname='academia',
        user='postgres',
        password='1234',
        host='localhost',
        port='5432'
    )

def cadastra_instrutor():
    cpf_instrutor = input('digite o cpf do instrutor: ')
    nome = input('digite o nome do instrutor: ')
    telefone = input('digite o telefone do instrutor: ')
    sexo = input('digite o sexo do instrutor(M/F): ')
    data_nascimento = input('digite a data de nascimento do instrutor(dd/mm/aaaa): ')
    email = input('digite o email do instrutor: ')
    num_contrato = int(input('digite o numero do contrato do instrutor: '))
    salario = float(input('digite o salario do instrutor: '))
    cref = int(input('Planos:\n1 - Gold\n2 - Platinum\n3 - Silver\nQual o plano do instrutor?'))

    cursor = connection.cursor()

    cursor.execute(f'''INSERT INTO public.instrutor(
	nome, telefone, sexo, "dtNascimento", email, "nroContrato", salario, cref, cpf)
	VALUES ('{nome}', '{telefone}', '{sexo}', '({data_nascimento})', '{email}', {num_contrato},{salario}, {cref}, '{cpf_instrutor}');''')

    print('Instrutor cadastrado com sucesso!')

def consulta_dados_instrutor():
    comando = 'SELECT * FROM instrutor'

    cursor = connection.cursor()

    cursor.execute(comando)

    registros = cursor.fetchall()

    print('|     EMAIL     |  TELEFONE  |SEX|  DATA_NASC |Contrat|   salario  | CREF|     CPF     |    NOME ')
    print('--------------------------------------------------------------------------------------------------')
    for registro in registros:
            print(f'| {registro[4]} | {registro[1]} | {registro[2]} | {registro[3]} | {registro[5]} |   {registro[6]}  | {registro[7]} | {registro[8]} | {registro[0]}')

def consulta_simples_instrutor():
    comando = """SELECT i.cpf, i.nome from instrutor i"""

    cursor = connection.cursor()

    cursor.execute(comando)

    registros = cursor.fetchall()

    print("|     CPF     |    NOME")
    print('---------------------------')
    for registro in registros:
            print(f'| {registro[0]} | {registro[1]}')


cursor = connection.cursor()

def atualiza_dados_instrutor():
    consulta_simples_instrutor()
    print()
    instrutor_atualiza = input('Digite o nome do instrutor que deseja atualizar: ')
    print()
    novo_nome = input("Digite o nome atualizado: ")
    novo_telefone = input("Digite o telefone atualizado: ")
    novo_sexo = input("Digite o sexo atualizado(M/F): ")
    novo_dtnascimento = input("Digite a data de nascimento atualizada: ")
    novo_email = input("Digite o email atualizado: ")
    novo_nrocontrato = int(input("Digite o numero do contrato atualizado: "))
    novo_salario = float(input("Digite o salario atualizado: "))
    novo_cref = int(input('Digite o CREF atualizado: '))

    comando = f"""UPDATE public.instrutor
	SET nome= '{novo_nome}', telefone='{novo_telefone}', sexo='{novo_sexo}', dtnascimento='({novo_dtnascimento})',
        email='{novo_email}', nrocontrato={novo_nrocontrato}, salario={novo_salario}, cref={novo_cref}
	    WHERE instrutor.nome = '{instrutor_atualiza}';"""
    
    cursor = connection.cursor()
    cursor.execute(comando)

    cursor = connection.cursor()

    print()
    print('Dados do instrutor atualizados com sucesso!')

def remove_instrutor():
      consulta_simples_instrutor()
      instrutor_remove = input('\nDigite o cpf do instrutor que deseja remover: ')

      
      
      comando1 = f"""UPDATE public.treino
	                    SET cpf_instrutor=NULL
	                    WHERE cpf_instrutor='{instrutor_remove}';"""
                    
      comando2 = f"""DELETE FROM public.instrutor
	                    WHERE cpf='{instrutor_remove}'"""
      
      cursor = connection.cursor()
      cursor.execute(comando1)
      cursor.execute(comando2)

      print("\nInstrutor removido com sucesso!\n") 
