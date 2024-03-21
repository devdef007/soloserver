# soloserver

Lightweight utility to be created with bottle framework to create an api to access some quick information from the server
running it.

## Pre-requisites

python and pip ($ python -m pip install --upgrade pip)



## Clone the project repo on the server

- cd into the project root
- add a config.ini file into the project root
```
[db_conn]
user = <db_user>
password = <db_pass>
host = localhost
port = 3306
database = <db>
raise_on_warnings = True

[api_conf]
host = localhost
port = <api_port>

[table_conf]
name = <db_table_name>
id_col = <db_table_id_column>
```
- create the virtual environment 
 ```$ python -m venv venv```
- activate the virtual environment
  ```$ source venv/Scripts/activate``` in Windows systems or ```$ source venv/bin/activate``` in Unix systems
- install all the dependencies related to functionalities
  ```$ pip install -r requirements.txt```
- run the main launcher 
  ```$ python soloserver.py```
- want to run it in background as long-running process, run with nohup instead (can use screen as well)
    ```$ nohup python soloserver.py > soloserver.log &```