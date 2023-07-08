import sys
import os
# Get the absolute path of the parent directory of your script
script_dir = os.path.dirname(os.path.abspath(__file__))

dir = os.path.abspath(os.path.join(script_dir, '..', 'pm_sys_user'))
dir =os.path.join(dir,'src')
path = sys.path
# Append the directory containing pm_sys_user to sys.path
sys.path.append(dir)

path = sys.path

import pm_sys_user.src.data_storage as c




user = "dummy_id"
host= "pmsdatabase.cfyebvbrqzy6.eu-north-1.rds.amazonaws.com"
password = "12345678"
port = 5432
database_name = "postgres"

db = c.AWSDatabaseObject(host, port, database_name, user, password)

db.connect()
# Create a cursor object to execute SQL queries
cursor = db.connection.cursor()

# Define the CREATE TABLE statement
create_table_query = '''
CREATE TABLE IF NOT EXISTS Incomes (
    income_id UUID PRIMARY KEY,
    price NUMERIC,
    is_dirty BOOLEAN,
    is_new BOOLEAN
);
'''

# Insert data into the Incomes table
insert_query = '''
INSERT INTO incomes (income_id, price, is_dirty, is_new)
VALUES ('123e4567-e89b-12d3-a456-426655440001', 105.00, false, true);
'''

# Execute the CREATE TABLE statement
cursor.execute(create_table_query)

cursor.execute(insert_query)

db.connection.commit()
# Insert data into the Incomes table
# Check if the table exists in the database
table_name = 'incomes'
cursor.execute("SELECT EXISTS(SELECT 1 FROM information_schema.tables WHERE table_name = %s);", (table_name))
exists = cursor.fetchone()[0]

if exists:
    print(f"The table '{table_name}' exists in the database.")
else:
    print(f"The table '{table_name}' does not exist in the database.")

# Close the cursor and connection
cursor.close()


#db.execute_query(query)
db.disconnect()



