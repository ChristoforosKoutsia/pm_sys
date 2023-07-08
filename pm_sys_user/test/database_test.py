import sys
import os
import random

# Get the absolute path of the parent directory of your script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Append the directory containing 'pm_sys_user' to sys.path
directory = os.path.abspath(os.path.join(script_dir, '..', 'src'))
sys.path.append(directory)

import unittest
import pm_sys_user.src.data_storage as f
import pm_sys_user.src.user_objects as user_objects

price = round(random.uniform(33.33, 10000.66), 2)
tax = round(random.uniform(33.33, 5000.66), 2)
month = random.choice(user_objects.MONTHS)
income_object = user_objects.Income_AWS(month=month,income=price,taxable_income=tax)
#income_object.save()



cat = random.choice(user_objects.Expense_AWS.FIXED_EXPENSE_CATEGORIES)
type_of_charge = random.choice(user_objects.Expense_AWS.TYPES_OF_CHARGE)
price = round(random.uniform(33.33, 10000.66), 2)
tax = round(random.uniform(33.33, 5000.66), 2)
vat = round(random.uniform(3, 70), 2)
expense_object = user_objects.Expense_AWS(category=cat,type_of_charge=type_of_charge,price=price,non_taxable_price=tax,vat=vat)
expense_object.save()
if __name__ == '__main__':
    unittest.main()
