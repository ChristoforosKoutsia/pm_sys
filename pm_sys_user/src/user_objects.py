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

from datetime import datetime
from uuid import UUID

#######################################
# Standard library imports needed     #
#######################################

# Uncomment this if there are abstract classes or "interfaces"
#   defined in the module...
# import abc

#######################################
# Third-party imports needed          #
#######################################
from data_storage  import JSONFileDataObject
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
    'non_taxable_price': "Αποφορολογητέο" ,
    'vat': "ΦΠΑ",
    'is_active': "Ενεργό" ,
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
class Income:
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
                 taxable_income
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


class Expense(JSONFileDataObject):
    """
     Represents an expense entity of the corresponding business.
     """
    _file_store_dir = r'..\data'
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
        self._non_taxable_price = value

    def _set_vat(self, value):
        # TODO -> improve it
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
        self._set_non_taxable_price(non_taxable_price)
        self._set_fixed_expense_category(category)
        self._set_type_of_charge(type_of_charge)
        self._set_price(price)
        self._set_vat(vat)
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


class User(JSONFileDataObject, object):
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


if __name__ == '__main__':
    pass
