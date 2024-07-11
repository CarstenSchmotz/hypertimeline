from typedb.driver import *
import os

PATH_TO_QUERY = os.path.join(os.path.dirname(os.path.abspath(__file__)) , "Queries/inconsistency_graph.tql" )
DB_NAME = "Hypertimelining_III"



print("This script determines whether there are temporal inconsistencies in the data. This may even take a few minutes.")

with TypeDB.core_driver("localhost:1729") as driver:
    #print("Connecting to the server")
    
    data = open(PATH_TO_QUERY, 'r')
    inconsistency_query = data.read()
    data.close()
    
    options = TypeDBOptions(infer=True)
    with driver.session(DB_NAME, SessionType.DATA) as data_session:
        with data_session.transaction(TransactionType.READ, options) as tx:
            #print("Querying for inconsistencies, please wait", end="...")
            resp = list(tx.query.get(inconsistency_query))
            #print(resp)
            if len(resp) == 0:
                print("Result: No inconsistencies found.")
            else:
                print("Result: One or more inconsistencies found.")
