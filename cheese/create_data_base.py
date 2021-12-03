import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import urllib.parse as urlparse

DATABASEURL = 'postgres://bqnpnvwtxembdw:82b17ca0229e736ca066caf5c791a7b760dcec6c530756135c9a5ecbd4632f91@ec2-34-251-245-108.eu-west-1.compute.amazonaws.com:5432/d1s0ev7kr29le1'

url = urlparse.urlparse(DATABASEURL)
dbname = url.path[1:]
user = url.username
password = url.password
host = url.hostname
port = url.port

# Создает базу данных
def create_db():
    try:
        # Подключение к существующей базе данных
        connection = psycopg2.connect(user=user,
                                           # пароль, который указали при установке PostgreSQL
                                           password=password,
                                           host=host,
                                           port=port,
                                           database=dbname)
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        # Курсор для выполнения операций с базой данных
        cursor = connection.cursor()
        sql_create_database = 'create database cheese'
        cursor.execute(sql_create_database)
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")


def create_table():
    try:
        connection = psycopg2.connect(user="postgres",
                                      # пароль, который указали при установке PostgreSQL
                                      password="ryecbfgps",
                                      host="127.0.0.1",
                                      port="5432",
                                      database='cheese')
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        # SQL-запрос для создания новой таблицы
        create_table_query = '''CREATE TABLE cheese
                              (ID SERIAL,
                              NAME VARCHAR (150) NOT NULL,
                              PRICE INT,
                              DESCRIPTION TEXT,
                              IMG TEXT); '''
        # Выполнение команды: это создает новую таблицу
        cursor = connection.cursor()
        cursor.execute(create_table_query)
        connection.commit()
        print("Таблица успешно создана в PostgreSQL")

        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)

# create_db()
create_table()
