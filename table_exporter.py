import csv

import mysql.connector

from conf_parser import DB_CONN, TABLE_CONF

config = {
    'user': DB_CONN['USER'],
    'password': DB_CONN['PASSWORD'],
    'host': DB_CONN['HOST'],
    'port': DB_CONN['PORT'],
    'database': DB_CONN['DATABASE'],
    'raise_on_warnings': bool(DB_CONN['RAISE_ON_WARNINGS'])
}

table_name = TABLE_CONF['NAME']
output_file = "leads_data.csv"


def main():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    query = f"select * from {table_name} limit 100"

    cursor.execute(query)

    # column headers
    column_names = [desc[0] for desc in cursor.description]

    # write to file
    with open(output_file, "w", newline="") as csvfile:
        # headers
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(column_names)

        for row in cursor:
            csv_writer.writerow(row)

    cnx.close()

    print(f"Data from table '{table_name}' exported to '{output_file}'")


if __name__ == "__main__":
    main()
