import mysql.connector

from conf_parser import DB_CONN
from conf_parser import TABLE_CONF

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
