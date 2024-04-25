import psycopg2

connection = psycopg2.connect(
        dbname='academia',
        user='postgres',
        password='1234',
        host='localhost',
        port='5432'
    )

def relatorio_1():
    comando = """select a.cpf, a.dtnascimento, a.nome, p.categoria from aluno a
                        join plano p on a.cod_plano = p.codplano
                        where p.categoria = 'Diamond'
                        and extract(year from a.dtnascimento) < 2000"""
    
    cursor = connection.cursor()
    cursor.execute(comando)

    registros = cursor.fetchall()
    print('\n---------------- RELATORIO ----------------\n')
    print("|     CPF     | DTNASCIMENTO | CATEGORIA |   NOME")
    print('-------------------------------------------------')
    for registro in registros:
            print(f'| {registro[0]} |  {registro[1]}  |  {registro[3]}  | {registro[2]} ')


def relatorio_2():
    comando = """select i.cpf, i.nome, t.codtreino, a.nome, t.foco from instrutor i
                    join treino t on i.cpf = t.cpf_instrutor
                    join aluno a on a.cpf = t.cpf_aluno
                    where i.sexo = 'M' and t.foco = 'Superiores'"""
    
    cursor = connection.cursor()
    cursor.execute(comando)

    registros = cursor.fetchall()
    print('\n---------------- RELATORIO ----------------\n')
    print("| CPF INSTRUTOR | NOME INSTRUTOR | COD |     FOCO   | ALUNO")
    print('-------------------------------------------------------------')
    for registro in registros:
            print(f'|  {registro[0]}  |     {registro[1]}    |  {registro[2]}  | {registro[4]} | {registro[3]} ')


def relatorio_3():
    comando = """select ex.codexerc, ex.nome, eq.nome from exercicio ex
                    join equipamento eq on eq.codequip = ex.cod_equip
                    where eq.nome = 'Polia'"""
    
    cursor = connection.cursor()
    cursor.execute(comando)

    registros = cursor.fetchall()
    print('\n---------------- RELATORIO ----------------\n')
    print("| COD | NOME | EQUIPAMENTO ")
    print('-------------------------------')
    for registro in registros:
            print(f'|  {registro[0]}  | {registro[1]} |  {registro[2]}')


cursor = connection.cursor()