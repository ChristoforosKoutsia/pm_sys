"""
This module will handle all the inputs of pm_sys app. Classes like incomes and expenses will be handled
in this module.
"""

#####################################
# Any needed from __future__ imports  #
# Create an "__all__" list to support #
#   "from module import member" use   #
#######################################


__all__ = [
    # Constants
    # Exceptions
    # Functions
    # ABC "interface" classes
    # ABC abstract classes
    # Concrete classes
]

#######################################
# Module metadata/dunder-names        #
#######################################

__author__ = 'Koutsianoudis Christoforos'
__copyright__ = 'Copyright 2022, all rights reserved'
__status__ = 'Development'

from abc import ABC
from datetime import datetime
from uuid import UUID
import sys
import os

# Get the root directory of the project
root_dir = os.path.dirname(os.path.abspath(__file__))

# Add the root directory to the Python search path
sys.path.insert(0, root_dir)

#######################################
# Standard library imports needed     #
#######################################

# Uncomment this if there are abstract classes or "interfaces"
#   defined in the module...
# import abc

#######################################
# Third-party imports needed          #
#######################################
from data_storage import JSONFileDataObject
from data_storage import AWSDatabaseObject
from data_storage import BaseDataObject

#######################################
# Local imports needed                #
#######################################

#######################################
# Initialization needed before member #
#   definition can take place         #
#######################################

#######################################
# Module-level Constants              #
#######################################
MONTHS = [
    "JANUARY",
    "FEBRUARY",
    "MARCH",
    "APRIL",
    "MAY",
    "JUNE",
    "JULY",
    "AUGUST",
]
VAT_RATE = 0.24

# dictionary that maps english terms to greek
eng_2_greek = {
    "created": "Δημιουργία",
    "modified": "Τροποποίηση",
    "month": "Μήνας",
    "income": "Ποσό",
    "taxable_income": "Φορολογητέο",
    'category': "Κατηγορία",
    'type_of_charge': "Τύπος Χρέωσης",
    'price': "Τιμή",
    'non_taxable_price': "Αποφορολογητέο",
    'vat': "ΦΠΑ",
    'is_active': "Ενεργό",
    'is_deleted': "Διεγραμένο",
}


#######################################
# Custom Exceptions                   #
#######################################

#######################################
# Module functions                    #
#######################################

#######################################
# ABC "interface" classes             #
#######################################

#######################################
# Abstract classes                    #
#######################################

#######################################
# Concrete classes                    #
#######################################
class Income(JSONFileDataObject):
    _file_store_dir = r'C:\Users\billk\OneDrive\Documents\GitHub\pm_sys\pm_sys_user\data'
    """
     Represents an income entity of the corresponding business.
     """

    # dictionary that maps english words with greek once so they can be represented in UI

    ###################################
    # Class attributes/constants      #
    ###################################

    ###################################
    # Property-getter methods         #
    ###################################

    def _get_month(self) -> str:
        return self._month

    def _get_income(self) -> float:
        return self._income

    def _get_taxable_income(self) -> float:
        return self._taxable_income

    ###################################
    # Property-setter methods         #
    ###################################

    def _set_month(self, value: str) -> None:
        # month should be a string and can only take values ["Jan-Dec"]
        # - Type-check: This is a required str value
        if type(value) != str:
            raise TypeError(
                '%s.month expects a single-line, '
                'non-empty str value, with no whitespace '
                'nor spaces and accepted strings are only %s, but was passed '
                '"%s" (%s)' %
                (
                    self.__class__.__name__, MONTHS, value,
                    type(value).__name__
                )
            )
        # value check
        if value not in MONTHS:
            raise ValueError(
                '%s.month expects a single-line, '
                'non-empty str value, with no whitespace '
                'nor spaces and accepted strings are only %s, but was passed '
                '"%s" (%s)' %
                (
                    self.__class__.__name__, MONTHS, value,
                    type(value).__name__
                )
            )
        self._month = value

    def _set_income(self, value: float) -> None:
        # month should be a string and can only take values ["Jan-Dec"]
        # - Type-check: This is a required str value
        if type(value) not in [float, int]:
            raise TypeError(
                '%s.income expects numeric values but instead was passed'
                '"%s" (%s)' %
                (
                    self.__class__.__name__, value,
                    type(value).__name__
                )
            )
        # value check (only non-negative values are accepted)
        if value < 0:
            raise ValueError(
                '%s.income expects non negative values but instead was passed'
                '"%s" (%s)' %
                (
                    self.__class__.__name__, value,
                    type(value).__name__
                )
            )
        self._income = value

    def _set_taxable_income(self, value: float) -> None:
        # month should be a string and can only take values ["Jan-Dec"]
        # - Type-check: This is a required str value
        if type(value) not in [float, int]:
            raise TypeError(
                '%s.taxable_income expects numeric values but instead was passed'
                '"%s" (%s)' %
                (
                    self.__class__.__name__, value,
                    type(value).__name__
                )
            )
        # value check (only non-negative values are accepted)
        if value < 0:
            raise ValueError(
                '%s.taxable_income expects non negative values but instead was passed'
                '"%s" (%s)' %
                (
                    self.__class__.__name__, value,
                    type(value).__name__
                )
            )
        self._taxable_income = value

    ###################################
    # Property-deleter methods        #
    ###################################

    def _del_month(self) -> None:
        self._month = None

    def _del_income(self) -> None:
        self._income = None

    def _del_taxable_income(self) -> None:
        self._taxable_income = None

    ###################################
    # Instance property definitions   #
    ###################################

    month = property(
        # TODO: Remove setter and deleter if access is not needed
        _get_month, _set_month, _del_month,
        'Gets, sets or deletes the month (str) of the instance'
    )
    income = property(
        # TODO: Remove setter and deleter if access is not needed
        _get_income, _set_income, _del_income,
        'Gets, sets or deletes the income (float) of the instance'
    )
    taxable_income = property(
        # TODO: Remove setter and deleter if access is not needed
        _get_taxable_income, _set_taxable_income, _del_taxable_income,
        'Gets, sets or deletes the taxable_income (float) of the instance'
    )

    ###################################
    # Object initialization           #
    ###################################

    # TODO: Add and document arguments if/as needed
    def __init__(self,
                 month,
                 income,
                 taxable_income,
                 oid: (UUID, str, None) = None,
                 created: (datetime, str, float, int, None) = None,
                 modified: (datetime, str, float, int, None) = None,
                 is_active: (bool, int, None) = None,
                 is_deleted: (bool, int, None) = None,
                 is_dirty: (bool, int, None) = None,
                 is_new: (bool, int, None) = None,
                 ):
        """
Object initialization.
self .............. (Income instance, required) The instance to
                    execute against
month.............. (str,required) The month that the income is referred to.
income............. (float,required)
taxable_income.......(float,requried)
"""
        self._set_month(month)
        self._set_income(income)
        self._set_taxable_income(taxable_income)

        JSONFileDataObject.__init__(
            self, oid, created, modified, is_active,
            is_deleted, is_dirty, is_new
        )

        self._set_is_dirty(False)

    def matches(self, **criteria) -> (bool,):
        return BaseDataObject.matches(self, **criteria)

    def to_data_dict(self) -> (dict,):
        return {
            # Properties from BaseArtisan:
            'month': self.month,
            'income': self.income,
            'taxable_income': self.taxable_income,
            # - Properties from BaseDataObject (through
            #   JSONFileDataObject)
            'created': datetime.strftime(
                self.created, self.__class__._data_time_string
            ),
            'is_active': self.is_active,
            'is_deleted': self.is_deleted,
            'modified': datetime.strftime(
                self.modified, self.__class__._data_time_string
            ),
            'oid': str(self.oid),
        }

    @classmethod
    def from_data_dict(cls, data_dict: (dict,)):
        return cls(**data_dict)

    @classmethod
    def sort(cls, objects: (list, tuple), sort_by: (str,)) -> (list,):
        """
Returns a list of the original objects supplied, sorted by the
criteria provided
"""
        raise NotImplementedError()


class Expense(JSONFileDataObject, ABC):
    """
     Represents an expense entity of the corresponding business.
     """
    _file_store_dir = r'C:\Users\billk\OneDrive\Documents\GitHub\pm_sys\pm_sys_user\data'
    ###################################
    # Class attributes/constants      #
    ###################################
    FIXED_EXPENSE_CATEGORIES = [
        "Λογιστική παρακολούθηση",
        "Διαχείριση site",
        "Καθαριότητα",
        "Συντηρήσεις",
        "Νερό",
        "Ασφάλεια επιχείρησης",
        "Πυρασφάλεια",
        "Αναλώσιμα γραφείου",
        "Email services",
        "Τηλέφωνο",
        "ΕΦΚΑ",
        "Ενοίκιο",
        "ERP",
        "CLOUD",
        "ANTIVIRUS",
        "ΣΥΝΔΡΟΜΕΣ ΕΠΙΜΕΛΗΤΗΡΙΩΝ",
        "Μισθοδοσίες",
        "Ηλεκτρικό ρεύμα",
        "Συμμετοχή σε εκθέσεις",
        "Υπεργολαβίες",
    ]

    TYPES_OF_CHARGE = [
        "Ετήσια",
        "Μηνιαία",
        "Εβδομαδιαία",
        "Ημερήσια",
        "Άπαξ",
    ]

    ###################################
    # Property-getter methods         #
    ###################################

    def _get_fixed_expense_category(self) -> str:
        return self._fixed_expense_category

    def _get_type_of_charge(self) -> str:
        return self._type_of_charge

    def _get_price(self) -> float:
        return self._price

    def _get_non_taxable_price(self) -> float:
        return self._non_taxable_price

    def _get_vat(self) -> float:
        return self._vat

    ###################################
    # Property-setter methods         #
    ###################################

    def _set_fixed_expense_category(self, value: str) -> None:
        # month should be a string and can only take values ["Jan-Dec"]
        # - Type-check: This is a required str value
        if type(value) != str:
            raise TypeError

        # value check
        if value not in self.FIXED_EXPENSE_CATEGORIES:
            raise ValueError

        self._fixed_expense_category = value

    def _set_type_of_charge(self, value: str) -> None:
        # month should be a string and can only take values ["Jan-Dec"]
        # - Type-check: This is a required str value
        if type(value) != str:
            raise TypeError

        # value check
        if value not in self.TYPES_OF_CHARGE:
            raise ValueError

        self._type_of_charge = value

    def _set_price(self, value: float) -> None:
        # month should be a string and can only take values ["Jan-Dec"]
        # - Type-check: This is a required str value
        print("My price is value")
        if type(value) not in [float, int]:
            raise TypeError(
                '%s.income expects numeric values but instead was passed'
                '"%s" (%s)' %
                (
                    self.__class__.__name__, value,
                    type(value).__name__
                )
            )
        # value check (only non-negative values are accepted)
        if value < 0:
            raise ValueError(
                '%s.income expects non negative values but instead was passed'
                '"%s" (%s)' %
                (
                    self.__class__.__name__, value,
                    type(value).__name__
                )
            )
        self._price = value

    def _set_non_taxable_price(self, value: float) -> None:
        if type(value) not in [float, int]:
            raise TypeError(
                '%s.taxable_income expects numeric values but instead was passed'
                '"%s" (%s)' %
                (
                    self.__class__.__name__, value,
                    type(value).__name__
                )
            )
        # value check (only non-negative values are accepted)
        if value < 0:
            raise ValueError(
                '%s.taxable_income expects non negative values but instead was passed'
                '"%s" (%s)' %
                (
                    self.__class__.__name__, value,
                    type(value).__name__
                )
            )
        # value check (non-taxable price should be lower than price)
        if self.price is not None and value > self.price:
            raise ValueError(
                "Το αποφορολογητέο ποσό πρέπει να είναι μικρότερο απο το ποσό εξόδου!"
            )

        self._non_taxable_price = value

    def _set_vat(self, value):
        if type(value) not in [float, int]:
            raise TypeError(
                '%s.taxable_income expects numeric values but instead was passed'
                '"%s" (%s)' %
                (
                    self.__class__.__name__, value,
                    type(value).__name__
                )
            )
        # value check (only non-negative values are accepted)
        if value < 0:
            raise ValueError(
                '%s.vat expects non negative values but instead was passed'
                '"%s" (%s)' %
                (
                    self.__class__.__name__, value,
                    type(value).__name__
                )
            )
        if value > 100:
            raise ValueError(
                '%s.vat expects to be <100 but instead was passed'
                '"%s" (%s)' %
                (
                    self.__class__.__name__, value,
                    type(value).__name__
                )
            )

        self._vat = value

    ###################################
    # Property-deleter methods        #
    ###################################
    # TODO -> add deleter methods

    ###################################
    # Instance property definitions   #
    ###################################

    category = property(
        # TODO: Remove setter and deleter if access is not needed
        _get_fixed_expense_category, _set_fixed_expense_category,
        'Gets, sets or deletes the month (str) of the instance'
    )
    type_of_charge = property(
        # TODO: Remove setter and deleter if access is not needed
        _get_type_of_charge, _set_type_of_charge,
        'Gets, sets or deletes the income (float) of the instance'
    )
    price = property(
        # TODO: Remove setter and deleter if access is not needed
        _get_price, _set_price,
        'Gets, sets or deletes the taxable_income (float) of the instance'
    )

    non_taxable_price = property(_get_non_taxable_price, _set_non_taxable_price)

    vat = property(_get_vat, _set_vat)

    ###################################
    # Object initialization           #
    ###################################

    # TODO: Add and document arguments if/as needed
    def __init__(self,
                 category,
                 type_of_charge,
                 price,
                 non_taxable_price,
                 vat,
                 oid: (UUID, str, None) = None,
                 created: (datetime, str, float, int, None) = None,
                 modified: (datetime, str, float, int, None) = None,
                 is_active: (bool, int, None) = None,
                 is_deleted: (bool, int, None) = None,
                 is_dirty: (bool, int, None) = None,
                 is_new: (bool, int, None) = None,
                 ):
        self.price = price
        self.non_taxable_price = non_taxable_price
        self.category = category
        self.type_of_charge = type_of_charge

        self.vat = vat
        JSONFileDataObject.__init__(
            self, oid, created, modified, is_active,
            is_deleted, is_dirty, is_new
        )

        self._set_is_dirty(False)

    def matches(self, **criteria) -> (bool,):
        return BaseDataObject.matches(self, **criteria)

    def to_data_dict(self) -> (dict,):
        return {
            # Properties from BaseArtisan:
            'category': self.category,
            'type_of_charge': self.type_of_charge,
            'price': self.price,
            'non_taxable_price': self.non_taxable_price,
            'vat': self.vat,

            # - Properties from BaseDataObject (through
            #   JSONFileDataObject)
            'created': datetime.strftime(
                self.created, self.__class__._data_time_string
            ),
            'is_active': self.is_active,
            'is_deleted': self.is_deleted,
            'modified': datetime.strftime(
                self.modified, self.__class__._data_time_string
            ),
            'oid': str(self.oid),
        }

    @classmethod
    def from_data_dict(cls, data_dict: (dict,)):
        return cls(**data_dict)

    @classmethod
    def sort(cls, objects: (list, tuple), sort_by: (str,)) -> (list,):
        """
Returns a list of the original objects supplied, sorted by the
criteria provided
"""
        raise NotImplementedError()


class Employee(JSONFileDataObject, ABC):
    _file_store_dir = r'C:\Users\billk\OneDrive\Documents\GitHub\pm_sys\pm_sys_user\data'
    """
     Represents an income entity of the corresponding business.
     """

    TYPE_OF_EMPLOYMENT = ["ΠΛΗΡΗΣ"
                          "ΗΜΙΑΠΑΣΧΟΛΗΣΗ"
                          "ΠΕΡΙΟΔΙΚΗ"]

    ###################################
    # Class attributes/constants      #
    ###################################

    ###################################
    # Property-setter methods         #
    ###################################

    def _set_name(self, value: str) -> None:
        # name should be a string consists at least of 3 characters
        # - Type-check: This is a required str value
        if type(value) != str:
            raise TypeError(
                '%s.name expects a single-line, '
                'non-empty str value, with no whitespace '
                'nor spaces and accepted strings are only %s, but was passed '
                '"%s" (%s)' %
                (
                    self.__class__.__name__, value,
                    type(value).__name__
                )
            )
        # value check
        if len(value) < 4:
            raise ValueError(
                f"Name of employee should be at least 4 characters given name {value} is below this threshold ")
        self._name = value

    def _set_surname(self, value: str) -> None:
        # name should be a string consists at least of 3 characters
        # - Type-check: This is a required str value
        if type(value) != str:
            raise TypeError(
                '%s.name expects a single-line, '
                'non-empty str value, with no whitespace '
                'nor spaces and accepted strings are only %s, but was passed '
                '"%s" (%s)' %
                (
                    self.__class__.__name__, value,
                    type(value).__name__
                )
            )
        # value check
        if len(value) < 4:
            raise ValueError(
                f"Name of employee should be at least 4 characters given name {value} is below this threshold ")
        self._surname = value

    def _set_gross_salary(self, value: float) -> None:
        # employees salar should be either float or integer value > 0
        # - Type-check: This is a required str value
        if type(value) not in [float, int]:
            raise TypeError(f"Salary should be either float or integer value")
        # value check (only non-negative values are accepted)
        if value < 0:
            raise ValueError(f"Salary of employee should be either float or integer")
        self._gross_salary = value

    def _set_net_salary(self, value: float) -> None:
        # employees salar should be either float or integer value > 0
        # - Type-check: This is a required str value
        if type(value) not in [float, int]:
            raise TypeError(f"Salary should be either float or integer value")
        # value check (only non-negative values are accepted)
        if value < 0:
            raise ValueError(f"Salary of employee should be either float or integer")
        self._net_salary = value

    def _set_type_of_employment(self, value: str) -> None:
        # employees salar should be either float or integer value > 0
        # - Type-check: This is a required str value
        if type(value) not in self.TYPE_OF_EMPLOYMENT:
            raise TypeError(f"Type of employment should be in {self.TYPE_OF_EMPLOYMENT}")
        self._type_of_employment = value

    ###################################
    # Instance property definitions   #
    ###################################

    name = property(
        # TODO: Remove setter and deleter if access is not needed
        _set_name
    )
    surname = property(
        # TODO: Remove setter and deleter if access is not needed
        _set_surname
    )
    gross_salary = property(
        # TODO: Remove setter and deleter if access is not needed
        _set_gross_salary)

    net_salary = property(
        # TODO: Remove setter and deleter if access is not needed
        _set_net_salary
    )

    type_of_employment = property(
        # TODO: Remove setter and deleter if access is not needed
        _set_type_of_employment
    )

    ###################################
    # Object initialization           #
    ###################################

    # TODO: Add and document arguments if/as needed
    def __init__(self,
                 name,
                 surname,
                 net_salary,
                 gross_salary,
                 type_of_employment,
                 oid: (UUID, str, None) = None,
                 created: (datetime, str, float, int, None) = None,
                 modified: (datetime, str, float, int, None) = None,
                 is_active: (bool, int, None) = None,
                 is_deleted: (bool, int, None) = None,
                 is_dirty: (bool, int, None) = None,
                 is_new: (bool, int, None) = None,
                 ):

        self._set_name(name)
        self._set_surname(surname)
        self._set_net_salary(net_salary)
        self._set_gross_salary(gross_salary)
        self._type_of_employment(type_of_employment)

        JSONFileDataObject.__init__(
            self, oid, created, modified, is_active,
            is_deleted, is_dirty, is_new
        )

        self._set_is_dirty(False)

    def matches(self, **criteria) -> (bool,):
        return BaseDataObject.matches(self, **criteria)

    def to_data_dict(self) -> (dict,):
        return {
            # Properties from BaseArtisan:
            'name': self.name,
            'surname': self.surname,
            'net_salary': self.net_salary,
            'gross_salary': self.gross_salary,
            'type_of_employment': self.type_of_employment,
            # - Properties from BaseDataObject (through
            #   JSONFileDataObject)
            'created': datetime.strftime(
                self.created, self.__class__._data_time_string
            ),
            'is_active': self.is_active,
            'is_deleted': self.is_deleted,
            'modified': datetime.strftime(
                self.modified, self.__class__._data_time_string
            ),
            'oid': str(self.oid),
        }

    @classmethod
    def from_data_dict(cls, data_dict: (dict,)):
        return cls(**data_dict)

    @classmethod
    def sort(cls, objects: (list, tuple), sort_by: (str,)) -> (list,):
        """
Returns a list of the original objects supplied, sorted by the
criteria provided
"""
        raise NotImplementedError()


class Supplier(JSONFileDataObject, ABC):
    _file_store_dir = r'C:\Users\billk\OneDrive\Documents\GitHub\pm_sys\pm_sys_user\data'
    """
     Represents an income entity of the corresponding business.
     """

    ###################################
    # Class attributes/constants      #
    ###################################

    ###################################
    # Property-setter methods         #
    ###################################

    def _set_name(self, value: str) -> None:
        # name should be a string consists at least of 3 characters
        # - Type-check: This is a required str value
        if type(value) != str:
            raise TypeError(
                '%s.name expects a single-line, '
                'non-empty str value, with no whitespace '
                'nor spaces and accepted strings are only %s, but was passed '
                '"%s" (%s)' %
                (
                    self.__class__.__name__, value,
                    type(value).__name__
                )
            )
        # value check
        if len(value) < 4:
            raise ValueError(
                f"Name of supplier should be at least 4 characters given name {value} is below this threshold ")
        self._name = value

    def _set_surname(self, value: str) -> None:
        # name should be a string consists at least of 3 characters
        # - Type-check: This is a required str value
        if type(value) != str:
            raise TypeError(
                '%s.name expects a single-line, '
                'non-empty str value, with no whitespace '
                'nor spaces and accepted strings are only %s, but was passed '
                '"%s" (%s)' %
                (
                    self.__class__.__name__, value,
                    type(value).__name__
                )
            )
        # value check
        if len(value) < 4:
            raise ValueError(
                f"Name of supplier should be at least 4 characters given name {value} is below this threshold ")
        self._surname = value

    def _set_price(self, value: float) -> None:
        # employees salar should be either float or integer value > 0
        # - Type-check: This is a required str value
        if type(value) not in [float, int]:
            raise TypeError(f"Price should be either float or integer value")
        # value check (only non-negative values are accepted)
        if value < 0:
            raise ValueError(f"Price should be either float or integer")
        self._price = value

    def _set_non_taxable_price(self, value: float) -> None:
        # employees salar should be either float or integer value > 0
        # - Type-check: This is a required str value
        if type(value) not in [float, int]:
            raise TypeError(f"Salary should be either float or integer value")
        # value check (only non-negative values are accepted)
        if value < 0:
            raise ValueError(f"Salary of employee should be either float or integer")
        self._non_taxable_price = value

    ###################################
    # Instance property definitions   #
    ###################################

    name = property(
        # TODO: Remove setter and deleter if access is not needed
        _set_name
    )
    surname = property(
        # TODO: Remove setter and deleter if access is not needed
        _set_surname
    )
    price = property(
        # TODO: Remove setter and deleter if access is not needed
        _set_price)

    non_taxable_price = property(
        # TODO: Remove setter and deleter if access is not needed
        _set_non_taxable_price
    )

    ###################################
    # Object initialization           #
    ###################################

    # TODO: Add and document arguments if/as needed
    def __init__(self,
                 name,
                 surname,
                 price,
                 non_taxable_price,
                 oid: (UUID, str, None) = None,
                 created: (datetime, str, float, int, None) = None,
                 modified: (datetime, str, float, int, None) = None,
                 is_active: (bool, int, None) = None,
                 is_deleted: (bool, int, None) = None,
                 is_dirty: (bool, int, None) = None,
                 is_new: (bool, int, None) = None,
                 ):

        self._set_name(name)
        self._set_surname(surname)
        self._set_price(price)
        self._set_non_taxable_price(non_taxable_price)

        JSONFileDataObject.__init__(
            self, oid, created, modified, is_active,
            is_deleted, is_dirty, is_new
        )

        self._set_is_dirty(False)

    def matches(self, **criteria) -> (bool,):
        return BaseDataObject.matches(self, **criteria)

    def to_data_dict(self) -> (dict,):
        return {
            # Properties from BaseArtisan:
            'name': self.name,
            'surname': self.surname,
            'net_salary': self.net_salary,
            'gross_salary': self.gross_salary,
            'type_of_employment': self.type_of_employment,
            # - Properties from BaseDataObject (through
            #   JSONFileDataObject)
            'created': datetime.strftime(
                self.created, self.__class__._data_time_string
            ),
            'is_active': self.is_active,
            'is_deleted': self.is_deleted,
            'modified': datetime.strftime(
                self.modified, self.__class__._data_time_string
            ),
            'oid': str(self.oid),
        }

    @classmethod
    def from_data_dict(cls, data_dict: (dict,)):
        return cls(**data_dict)

    @classmethod
    def sort(cls, objects: (list, tuple), sort_by: (str,)) -> (list,):
        """
Returns a list of the original objects supplied, sorted by the
criteria provided
"""
        raise NotImplementedError()


class User(JSONFileDataObject):
    _file_store_dir = r'..\data'

    def __init__(self, company_name, legal_form,

                 oid: (UUID, str, None) = None,
                 created: (datetime, str, float, int, None) = None,
                 modified: (datetime, str, float, int, None) = None,
                 is_active: (bool, int, None) = None,
                 is_deleted: (bool, int, None) = None,
                 is_dirty: (bool, int, None) = None,
                 is_new: (bool, int, None) = None,
                 ):
        self.company_name = company_name
        self.legal_form = legal_form

        JSONFileDataObject.__init__(
            self, oid, created, modified, is_active,
            is_deleted, is_dirty, is_new
        )

        self._set_is_dirty(False)

    def matches(self, **criteria) -> (bool,):
        return BaseDataObject.matches(self, **criteria)

    def to_data_dict(self) -> (dict,):
        return {
            # Properties from BaseArtisan:
            'legal_form': self.legal_form,
            'company_name': self.company_name,

            # - Properties from BaseDataObject (through
            #   JSONFileDataObject)
            'created': datetime.strftime(
                self.created, self.__class__._data_time_string
            ),
            'is_active': self.is_active,
            'is_deleted': self.is_deleted,
            'modified': datetime.strftime(
                self.modified, self.__class__._data_time_string
            ),
            'oid': str(self.oid),
        }

    @classmethod
    def from_data_dict(cls, data_dict: (dict,)):
        return cls(**data_dict)

    @classmethod
    def sort(cls, objects: (list, tuple), sort_by: (str,)) -> (list,):
        """
Returns a list of the original objects supplied, sorted by the
criteria provided
"""
        raise NotImplementedError()


class IncomesDataProcessing:
    """
    This class will manipulate attributes of incomes objects in a manner that we have useful data to work with.
    At the end we will have values for
    -
    """

    def __init__(self):
        self.income_objects = Income.get()

    def get_annual_income(self):
        """
        Returns: sum of all incomes for each month
        """
        # Use a list comprehension to extract the 'income' attribute from each object
        # and pass the resulting list to the sum function
        return sum(obj.income for obj in self.income_objects)

    def get_monthly_contribution_rate(self):
        return {obj.month: obj.income / 12 for obj in self.income_objects}

    def get_distribution_of_representatives(self):
        # Α)Άθροισμα μηνιαίων φορολογητέων / ετήσιος κύκλος εργασιών
        # Β)(Ετήσιος κύκλος εργασιών  - Άθροισμα φορολογητέων)/ ετήσιος κύκλος εργασιών
        annual_income = self.get_annual_income()
        dist_a = sum(obj.taxable_income for obj in self.income_objects) / annual_income
        dist_b = (annual_income - sum(obj.taxable_income for obj in self.income_objects)) / annual_income
        return dist_a, dist_b

    def get_taxable_incomes(self):
        return sum(obj.taxable_income for obj in self.income_objects)

    def get_annual_vat(self):
        return self.get_taxable_incomes() * VAT_RATE


class ExpensesDataProcessing:
    pass


class Income_AWS(AWSDatabaseObject):

    # dictionary that maps english words with greek once so they can be represented in UI

    ###################################
    # Class attributes/constants      #
    ###################################

    ###################################
    # Property-getter methods         #
    ###################################

    def _get_month(self) -> str:
        return self._month

    def _get_income(self) -> float:
        return self._income

    def _get_taxable_income(self) -> float:
        return self._taxable_income

    ###################################
    # Property-setter methods         #
    ###################################

    def _set_month(self, value: str) -> None:
        # month should be a string and can only take values ["Jan-Dec"]
        # - Type-check: This is a required str value
        if type(value) != str:
            raise TypeError(
                '%s.month expects a single-line, '
                'non-empty str value, with no whitespace '
                'nor spaces and accepted strings are only %s, but was passed '
                '"%s" (%s)' %
                (
                    self.__class__.__name__, MONTHS, value,
                    type(value).__name__
                )
            )
        # value check
        if value not in MONTHS:
            raise ValueError(
                '%s.month expects a single-line, '
                'non-empty str value, with no whitespace '
                'nor spaces and accepted strings are only %s, but was passed '
                '"%s" (%s)' %
                (
                    self.__class__.__name__, MONTHS, value,
                    type(value).__name__
                )
            )
        self._month = value

    def _set_income(self, value: float) -> None:
        # month should be a string and can only take values ["Jan-Dec"]
        # - Type-check: This is a required str value
        if type(value) not in [float, int]:
            raise TypeError(
                '%s.income expects numeric values but instead was passed'
                '"%s" (%s)' %
                (
                    self.__class__.__name__, value,
                    type(value).__name__
                )
            )
        # value check (only non-negative values are accepted)
        if value < 0:
            raise ValueError(
                '%s.income expects non negative values but instead was passed'
                '"%s" (%s)' %
                (
                    self.__class__.__name__, value,
                    type(value).__name__
                )
            )
        self._income = value

    def _set_taxable_income(self, value: float) -> None:
        # month should be a string and can only take values ["Jan-Dec"]
        # - Type-check: This is a required str value
        if type(value) not in [float, int]:
            raise TypeError(
                '%s.taxable_income expects numeric values but instead was passed'
                '"%s" (%s)' %
                (
                    self.__class__.__name__, value,
                    type(value).__name__
                )
            )
        # value check (only non-negative values are accepted)
        if value < 0:
            raise ValueError(
                '%s.taxable_income expects non negative values but instead was passed'
                '"%s" (%s)' %
                (
                    self.__class__.__name__, value,
                    type(value).__name__
                )
            )
        self._taxable_income = value

    ###################################
    # Property-deleter methods        #
    ###################################

    def _del_month(self) -> None:
        self._month = None

    def _del_income(self) -> None:
        self._income = None

    def _del_taxable_income(self) -> None:
        self._taxable_income = None

    ###################################
    # Instance property definitions   #
    ###################################

    month = property(
        # TODO: Remove setter and deleter if access is not needed
        _get_month, _set_month, _del_month,
        'Gets, sets or deletes the month (str) of the instance'
    )
    income = property(
        # TODO: Remove setter and deleter if access is not needed
        _get_income, _set_income, _del_income,
        'Gets, sets or deletes the income (float) of the instance'
    )
    taxable_income = property(
        # TODO: Remove setter and deleter if access is not needed
        _get_taxable_income, _set_taxable_income, _del_taxable_income,
        'Gets, sets or deletes the taxable_income (float) of the instance'
    )

    ###################################
    # Object initialization           #
    ###################################

    # TODO: Add and document arguments if/as needed
    def __init__(self,
                 month,
                 income,
                 taxable_income,
                 oid: (UUID, str, None) = None,
                 created: (datetime, str, float, int, None) = None,
                 modified: (datetime, str, float, int, None) = None,
                 is_active: (bool, int, None) = None,
                 is_deleted: (bool, int, None) = None,
                 is_dirty: (bool, int, None) = None,
                 is_new: (bool, int, None) = None,
                 ):
        """
Object initialization.
self .............. (Income instance, required) The instance to
                    execute against
month.............. (str,required) The month that the income is referred to.
income............. (float,required)
taxable_income.......(float,requried)
"""
        self._set_month(month)
        self._set_income(income)
        self._set_taxable_income(taxable_income)

        AWSDatabaseObject.__init__(
            self,
            oid, created, modified, is_active,
            is_deleted, is_dirty, is_new
        )

    def matches(self, **criteria) -> (bool,):
        return BaseDataObject.matches(self, **criteria)

    def to_data_dict(self) -> (dict,):
        return {
            # Properties from BaseArtisan:
            'month': self.month,
            'income': self.income,
            'taxable_income': self.taxable_income,
            # - Properties from BaseDataObject

            'created': datetime.strftime(
                self.created, self.__class__._data_time_string
            ),
            'is_active': self.is_active,
            'is_deleted': self.is_deleted,
            'modified': datetime.strftime(
                self.modified, self.__class__._data_time_string
            ),
            'oid': str(self.oid),
        }

    @classmethod
    def from_data_dict(cls, data_dict: (dict,)):
        return cls(**data_dict)

    @classmethod
    def sort(cls, objects: (list, tuple), sort_by: (str,)) -> (list,):
        """
Returns a list of the original objects supplied, sorted by the
criteria provided
"""
        raise NotImplementedError()






class Expense_AWS(AWSDatabaseObject, ABC):
    """
     Represents an expense entity of the corresponding business.
     """
    _file_store_dir = r'C:\Users\billk\OneDrive\Documents\GitHub\pm_sys\pm_sys_user\data'
    ###################################
    # Class attributes/constants      #
    ###################################
    FIXED_EXPENSE_CATEGORIES = [
        "Λογιστική παρακολούθηση",
        "Διαχείριση site",
        "Καθαριότητα",
        "Συντηρήσεις",
        "Νερό",
        "Ασφάλεια επιχείρησης",
        "Πυρασφάλεια",
        "Αναλώσιμα γραφείου",
        "Email services",
        "Τηλέφωνο",
        "ΕΦΚΑ",
        "Ενοίκιο",
        "ERP",
        "CLOUD",
        "ANTIVIRUS",
        "ΣΥΝΔΡΟΜΕΣ ΕΠΙΜΕΛΗΤΗΡΙΩΝ",
        "Μισθοδοσίες",
        "Ηλεκτρικό ρεύμα",
        "Συμμετοχή σε εκθέσεις",
        "Υπεργολαβίες",
    ]

    TYPES_OF_CHARGE = [
        "Ετήσια",
        "Μηνιαία",
        "Εβδομαδιαία",
        "Ημερήσια",
        "Άπαξ",
    ]

    ###################################
    # Property-getter methods         #
    ###################################

    def _get_fixed_expense_category(self) -> str:
        return self._fixed_expense_category

    def _get_type_of_charge(self) -> str:
        return self._type_of_charge

    def _get_price(self) -> float:
        return self._price

    def _get_non_taxable_price(self) -> float:
        return self._non_taxable_price

    def _get_vat(self) -> float:
        return self._vat

    ###################################
    # Property-setter methods         #
    ###################################

    def _set_fixed_expense_category(self, value: str) -> None:
        # month should be a string and can only take values ["Jan-Dec"]
        # - Type-check: This is a required str value
        if type(value) != str:
            raise TypeError

        # value check
        if value not in self.FIXED_EXPENSE_CATEGORIES:
            raise ValueError

        self._fixed_expense_category = value

    def _set_type_of_charge(self, value: str) -> None:
        # month should be a string and can only take values ["Jan-Dec"]
        # - Type-check: This is a required str value
        if type(value) != str:
            raise TypeError

        # value check
        if value not in self.TYPES_OF_CHARGE:
            raise ValueError

        self._type_of_charge = value

    def _set_price(self, value: float) -> None:
        # month should be a string and can only take values ["Jan-Dec"]
        # - Type-check: This is a required str value
        print("My price is value")
        if type(value) not in [float, int]:
            raise TypeError(
                '%s.income expects numeric values but instead was passed'
                '"%s" (%s)' %
                (
                    self.__class__.__name__, value,
                    type(value).__name__
                )
            )
        # value check (only non-negative values are accepted)
        if value < 0:
            raise ValueError(
                '%s.income expects non negative values but instead was passed'
                '"%s" (%s)' %
                (
                    self.__class__.__name__, value,
                    type(value).__name__
                )
            )
        self._price = value

    def _set_non_taxable_price(self, value: float) -> None:
        if type(value) not in [float, int]:
            raise TypeError(
                '%s.taxable_income expects numeric values but instead was passed'
                '"%s" (%s)' %
                (
                    self.__class__.__name__, value,
                    type(value).__name__
                )
            )
        # value check (only non-negative values are accepted)
        if value < 0:
            raise ValueError(
                '%s.taxable_income expects non negative values but instead was passed'
                '"%s" (%s)' %
                (
                    self.__class__.__name__, value,
                    type(value).__name__
                )
            )
        # value check (non-taxable price should be lower than price)
        if self.price is not None and value > self.price:
            raise ValueError(
                "Το αποφορολογητέο ποσό πρέπει να είναι μικρότερο απο το ποσό εξόδου!"
            )

        self._non_taxable_price = value

    def _set_vat(self, value):
        if type(value) not in [float, int]:
            raise TypeError(
                '%s.taxable_income expects numeric values but instead was passed'
                '"%s" (%s)' %
                (
                    self.__class__.__name__, value,
                    type(value).__name__
                )
            )
        # value check (only non-negative values are accepted)
        if value < 0:
            raise ValueError(
                '%s.vat expects non negative values but instead was passed'
                '"%s" (%s)' %
                (
                    self.__class__.__name__, value,
                    type(value).__name__
                )
            )
        if value > 100:
            raise ValueError(
                '%s.vat expects to be <100 but instead was passed'
                '"%s" (%s)' %
                (
                    self.__class__.__name__, value,
                    type(value).__name__
                )
            )

        self._vat = value

    ###################################
    # Property-deleter methods        #
    ###################################
    # TODO -> add deleter methods

    ###################################
    # Instance property definitions   #
    ###################################

    category = property(
        # TODO: Remove setter and deleter if access is not needed
        _get_fixed_expense_category, _set_fixed_expense_category,
        'Gets, sets or deletes the month (str) of the instance'
    )
    type_of_charge = property(
        # TODO: Remove setter and deleter if access is not needed
        _get_type_of_charge, _set_type_of_charge,
        'Gets, sets or deletes the income (float) of the instance'
    )
    price = property(
        # TODO: Remove setter and deleter if access is not needed
        _get_price, _set_price,
        'Gets, sets or deletes the taxable_income (float) of the instance'
    )

    non_taxable_price = property(_get_non_taxable_price, _set_non_taxable_price)

    vat = property(_get_vat, _set_vat)

    ###################################
    # Object initialization           #
    ###################################

    # TODO: Add and document arguments if/as needed
    def __init__(self,
                 category,
                 type_of_charge,
                 price,
                 non_taxable_price,
                 vat,
                 oid: (UUID, str, None) = None,
                 created: (datetime, str, float, int, None) = None,
                 modified: (datetime, str, float, int, None) = None,
                 is_active: (bool, int, None) = None,
                 is_deleted: (bool, int, None) = None,
                 is_dirty: (bool, int, None) = None,
                 is_new: (bool, int, None) = None,
                 ):
        self.price = price
        self.non_taxable_price = non_taxable_price
        self.category = category
        self.type_of_charge = type_of_charge

        self.vat = vat
        AWSDatabaseObject.__init__(
            self, oid, created, modified, is_active,
            is_deleted, is_dirty, is_new
        )

        self._set_is_dirty(False)

    def matches(self, **criteria) -> (bool,):
        return BaseDataObject.matches(self, **criteria)

    def to_data_dict(self) -> (dict,):
        return {
            # Properties from BaseArtisan:
            'category': self.category,
            'type_of_charge': self.type_of_charge,
            'price': self.price,
            'non_taxable_price': self.non_taxable_price,
            'vat': self.vat,

            # - Properties from BaseDataObject (through
            #   JSONFileDataObject)
            'created': datetime.strftime(
                self.created, self.__class__._data_time_string
            ),
            'is_active': self.is_active,
            'is_deleted': self.is_deleted,
            'modified': datetime.strftime(
                self.modified, self.__class__._data_time_string
            ),
            'oid': str(self.oid),
        }

    @classmethod
    def from_data_dict(cls, data_dict: (dict,)):
        return cls(**data_dict)

    @classmethod
    def sort(cls, objects: (list, tuple), sort_by: (str,)) -> (list,):
        """
Returns a list of the original objects supplied, sorted by the
criteria provided
"""
        raise NotImplementedError()

if __name__ == '__main__':
    pass
