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

db.disconnect()



