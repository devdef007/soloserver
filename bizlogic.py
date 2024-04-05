import subprocess

import mysql.connector

from conf_parser import DB_CONN
from conf_parser import TABLE_CONF

8
config = {
    'user': DB_CONN['USER'],
    'password': DB_CONN['PASSWORD'],
    'host': DB_CONN['HOST'],
    'port': DB_CONN['PORT'],
    'database': DB_CONN['DATABASE'],
    'raise_on_warnings': bool(DB_CONN['RAISE_ON_WARNINGS'])
}


def get_meta_data():
    cnx = mysql.connector.connect(**config)
    min_id, max_id, ctr = -1, -1, -1

    if cnx and cnx.is_connected():
        table_name = TABLE_CONF['NAME']
        table_id_col = TABLE_CONF['ID_COL']

        with cnx.cursor() as cursor:
            query = (
                f"select min({table_id_col}) as min_id, max({table_id_col}) as max_id, count({table_id_col}) as ctr from {table_name}")
            print(f"query -> {query}")
            cursor.execute(query)

            row = cursor.fetchone()

            print(f"{row}")
            min_id, max_id, ctr = row[0], row[1], row[2]

        cnx.close()

    else:
        print("Could not connect")

    return min_id, max_id, ctr


# def get_db_insert_ddl():
#     cnx = mysql.connector.connect(**config)
#     insert_data = ""
#
#     if cnx and cnx.is_connected():
#
#         with cnx.cursor() as cursor:
#             query = (
#                 f"mysqldump -t -c -u <user> -p<pass> <db_name> <table_name> --where=\"ID in (1, 2, 3, 4)\" > leads_dmp.sql")
#             print(f"query -> {query}")
#             cursor.execute(query)
#
#             insert_data = subprocess.check_output(['cat', 'leads_dmp.sql'])
#             print(f"{insert_data}")
#
#         cnx.close()
#
#     else:
#         print("Could not connect")
#
#     return insert_data


def get_db_insert_ddl():
    cnx = mysql.connector.connect(**config)
    insert_data = ""
    db_user = DB_CONN['DATABASE']
    db_pass = DB_CONN['PASSWORD']
    db_name = DB_CONN['DATABASE']
    table_name = TABLE_CONF['NAME']

    if cnx and cnx.is_connected():
        query = (
            f"mysqldump -t -c -u {db_user} -p{db_pass} {db_name} {table_name} --where=\"ID in (1, 2, 3, 4)\" > leads_dmp.sql"
        )

        print(f"query -> {query}")

        process = subprocess.Popen(query, shell=True, stdout=subprocess.PIPE)
        output, error = process.communicate()

        if error:
            print(f"Error: {error.decode('utf-8')}")
        else:
            with open("leads_dmp.sql", "r") as file:
                insert_data = file.read()
                print(f"{insert_data}")

        cnx.close()

    else:
        print("Could not connect")

    return insert_data


def insert_bulk_data(ins_stmt):
    cnx = mysql.connector.connect(**config)
    inserted_rows = -1

    if cnx and cnx.is_connected():

        with cnx.cursor() as cursor:
            cursor.execute(ins_stmt)

            # for sql_query in ins_stmt.strip().split(';'):
            #     if sql_query:
            #         cursor.execute(sql_query)

            inserted_rows = cursor.rowcount
            print(f"inserted rows: {inserted_rows}")

            cnx.commit()

        cnx.close()

    else:
        print("Could not connect")

    return str(inserted_rows)
