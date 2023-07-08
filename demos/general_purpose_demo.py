"""
just demo to try out things
"""
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

import pm_sys_user.src.user_objects as user
print(user.Income.__name__)


user_income = user.Income.get()[0]
print(user_income.to_data_dict())
print(vars(user_income))


