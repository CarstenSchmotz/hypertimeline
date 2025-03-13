from typedb.driver import *
import os

PATH_TO_SCHEMA = os.path.join(os.path.dirname(os.path.abspath(__file__)) , "Queries/schema-hypertimelining.tql"  )
DB_NAME = "Hypertimelining_III"
username = "admin"
password = "password"
##driver = TypeDB.core_driver("127.0.0.1:1729")
#with TypeDB.core_driver("localhost:1729") as driver: #orginal
#with TypeDB.core_driver("localhost:1729", Credentials(username, password)) as driver: #only 1 missing error 
#with TypeDB.core_driver("localhost:1729", Credentials(username, password), DriverOptions(False,None)) as driver:
with TypeDB.core_driver("localhost:1729", Credentials(username, password), DriverOptions()) as driver: 
    print("Connecting to the server")

    # Delete Database if existent
    if driver.databases.contains(DB_NAME):
        driver.databases.get(DB_NAME).delete()

    # Create Database
    driver.databases.create(DB_NAME)
    
    #Initialize Schema
    data = open(PATH_TO_SCHEMA, 'r')
    define_query = data.read()
    data.close()
    with driver.session(DB_NAME, SessionType.SCHEMA) as schema_session:
        with schema_session.transaction(TransactionType.WRITE) as tx:
            print("Defining schema", end="...")
            tx.query.define(define_query)
            tx.commit()
    
print("Database {} was created".format(DB_NAME))



