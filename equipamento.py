import psycopg2

connection = psycopg2.connect(
        dbname='academia',
        user='postgres',
        password='1234',
        host='localhost',
        port='5432'
    )

def consulta_equip():
    comando = """SELECT * FROM public.equipamento
                    ORDER BY codequip"""

    cursor = connection.cursor()

    cursor.execute(comando)

    registros = cursor.fetchall()
    print("COD|QUANT|  NOME  ")
    print('--------------------')
    for registro in registros:
            print(f' {registro[0]} |  {registro[2]}  | {registro[1]}')

def cadastra_equip():
    nome_equip = input('Digite o nome do equipamento que deseja cadastrar: ')
    print()
    quant_equip = int(input('Digite a quantidade desse equipamento: '))
    print()

    comando = f"""INSERT INTO public.equipamento(
	nome, quantidade)
	VALUES ('{nome_equip}', {quant_equip});"""

    cursor = connection.cursor()

    cursor.execute(comando)
    
    print("Equipamento cadastrado com sucesso!")

def atualiza_equip():
     consulta_equip()
     print()
     equip_atualiza = int(input('Digite o codigo do equipamento que deseja atualizar: '))
     print()
     novo_nome = input('Digite o nome atualizado do equipamento: ')
     print()
     novo_quant = int(input('Digite a quantidade atualizada desse equipamento: '))
     comando = f"""UPDATE public.equipamento
	                SET nome='{novo_nome}', quantidade={novo_quant}
	                WHERE codequip = {equip_atualiza};"""
     
     cursor = connection.cursor()
     cursor.execute(comando)
    
     print("Equipamento atualizado com sucesso!")

def remove_equip():
     consulta_equip()
     equip_remove = int(input("\nDigite o codigo do equipamento que deseja remover: "))
     
     comando1 = f"""UPDATE public.exercicio
	                    SET cod_equip=NULL
	                    WHERE cod_equip={equip_remove};"""

     comando2 = f"""DELETE FROM public.equipamento
	                WHERE codequip={equip_remove};"""

     cursor = connection.cursor()
     cursor.execute(comando1)
     cursor.execute(comando2)
    
     print("\nEquipamento removido com sucesso!\n")




cursor = connection.cursor()
