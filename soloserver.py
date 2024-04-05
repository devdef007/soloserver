from _mysql_connector import MySQLError
from bottle import run, route, request
from mysql.connector import ProgrammingError

from bizlogic import get_meta_data, get_db_insert_ddl, insert_bulk_data
from conf_parser import API_CONF


@route('/soloserver')
def root():
    try:
        # Get DB meta information
        min_id, max_id, ctr = get_meta_data()
        data = {"min_id": min_id, "max_id": max_id, "count": ctr}

    except (MySQLError, ProgrammingError) as ex:
        print(f"Database error occurred {ex}")
        return {"status": 500, "message": "Something went wrong, please try again."}

    return {"status": 200, "message": "Success", "data": data}


@route('/soloserver/insertdump')
def insert_dump():
    try:
        # Get DB meta information
        data = get_db_insert_ddl()

    except (MySQLError, ProgrammingError) as ex:
        print(f"Database error occurred {ex}")
        return {"status": 500, "message": "----Something went wrong, please try again."}

    return data  # return string


@route('/soloserver/insertbulk', method='POST')
def insert_dump():
    try:
        input_string = request.body.read().decode('utf-8')

        # Insert in bulk
        data = insert_bulk_data(input_string)

    except (MySQLError, ProgrammingError) as ex:
        print(f"Database error occurred {ex}")
        return {"status": 500, "message": "----Something went wrong, please try again."}

    return {"status": 200, "message": "Success", "data": data}


run(host=API_CONF['HOST'], port=API_CONF['PORT'], debug=True)
