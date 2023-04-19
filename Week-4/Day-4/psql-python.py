"""Данный код импортирует библиотеку, позволяющую подключиться к некоторой библиотеке SQL,
 после чего обратиться к каким-либо её таблицам и колонкам (напечатать их)."""

from datetime import date
import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = '111111'
DATABASE = 'dvdrental'


connection = psycopg2.connect(host = HOSTNAME, user = USERNAME, password = PASSWORD, dbname = DATABASE)


def select(table_name: str, *args) -> str:
    if args:
        column_name = ','.join(args)
    else:
        column_name = '*'
    query = f'select {column_name} from {table_name}'
    return query 

def insert_query(table, *args, **kwargs) -> str:

    """
    Inserts data into a table.

    Args:
        table (str): The name of the table to insert data into.
        *args (str): The names of the columns to insert data into.
        **kwargs (Any): The values to insert into the columns specified in *args.

    Example:
        To insert a row into the "actor" table with the values "Brad", "Pitt", "1970-01-01", and 2 in the "first_name",
        "last_name", "birthday", and "number_oscars" columns, respectively, use:

        insert_query("actor", "first_name", "last_name", "birthday", "number_oscars",
                     first_name="Brad", last_name="Pitt", birthday=date(1970, 1, 1), number_oscars=2)

    Output:
        insert into actor (first_name,last_name,birthday,number_oscars) values ('Brad','Pitt','1970-01-01',2)

    Returns:
        str: SQL insert query string.
    """

    columns = ','.join(args)

    # Функция в "values = ..." проверяет, является ли переданное значение датой с помощью isinstance(x, datetime.date), 
    # и если это так, то оно преобразуется в строку с использованием strftime('%Y-%m-%d'). 
    # В противном случае значение просто добавляется в строку с помощью f"'{x}'".
    values = ','.join(map(lambda x: date(x).strftime('%Y-%m-%d') if isinstance(x, date) else f"'{x}'", kwargs.values()))
    return f'insert into {table} ({columns}) values ({values})'

# print(insert_query("table", "c1", "c2", v1="v1", v2="v2", v3='v3'))
print(insert_query.__doc__)


def run_select_query(query: str):
    with connection.cursor() as cursor:
        # cursor - query runner 
        cursor.execute(query)
        # cursor.fetchall - returns all data from cursor 
        result = cursor.fetchall()
    return result

def run_change_query(query: str): 
    
    with connection.cursor() as cursor:
        cursor.execute(query)
        connection.commit()


newactor = insert_query('actor', 'first_name', 'last_name', 'birthday', 'number_oscars', fn='Brad', ln='Pitt', bd='date(1970,1,1)', no='2')
# run_change_query(newactor)
print((newactor))
# print(run_select_query(select("actor", "first_name")))


