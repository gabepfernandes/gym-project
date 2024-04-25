import psycopg2

connection = psycopg2.connect(
        dbname='academia',
        user='postgres',
        password='1234',
        host='localhost',
        port='5432'
    )

def cadastra_plano():
    categoria = input('digite a categoria do plano: ')
    preco = float(input('digite o preco do plano: '))

    cursor = connection.cursor()

    cursor.execute(f'''INSERT INTO public.plano(
	categoria, preco)
	VALUES ('{categoria}', {preco});''')

    print('Plano cadastrado com sucesso!')

def consulta_plano():
    comando = 'SELECT * FROM plano'

    cursor = connection.cursor()
    cursor.execute(comando)

    registros = cursor.fetchall()

    print('\n----- P L A N O S -----\n')
    for registro in registros:
            print(f'| {registro[0]} | {registro[1]} - R${registro[2]}')
            print()

def atualiza_plano():
    consulta_plano()
    cod = int(input('Digite o codigo do plano que deseja atualizar: '))
    categoria_nova = input('Digite o novo nome da categoria: ')
    preco_novo = float(input('Digite o novo preco do plano: '))

    comando = f"""UPDATE public.plano
	SET categoria='{categoria_nova}', preco={preco_novo}
	WHERE plano.codplano = {cod};"""

    cursor = connection.cursor()
    cursor.execute(comando)

def remove_plano():
    consulta_plano()
    plano_remove = int(input('\nDigite o codigo do plano que deseja deletar: '))

    comando1 = f"""UPDATE aluno
	                SET cod_plano=NULL
	                WHERE cod_plano ={plano_remove};"""

    comando2 = f"""DELETE FROM public.plano
	                WHERE plano.codplano = {plano_remove};"""

    cursor = connection.cursor()
    cursor.execute(comando1)
    cursor.execute(comando2)

    print('Plano removido com sucesso!')


cursor = connection.cursor()
