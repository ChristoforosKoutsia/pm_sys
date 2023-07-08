#!/usr/bin/env python
"""
TODO: Document the module.
Provides classes and functionality for SOME_PURPOSE
"""
import abc
import json
import os
from abc import ABC
import datetime
import psycopg2

from datetime import datetime
from uuid import UUID, uuid4
from data_objects import BaseDataObject


#######################################

class JSONFileDataObject(BaseDataObject, metaclass=abc.ABCMeta):
    """
Provides baseline functionality, interface requirements, and
type-identity for objects that can persist their state-data as
JSON files in a local file-system file-cache
"""
    ###################################
    # Class attributes/constants      #
    ###################################

    _file_store_dir = None
    _file_store_ready = False
    _loaded_objects = None

    ###################################
    # Object initialization           #
    ###################################

    def __init__(self,
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
self .............. (JSONFileDataObject instance, required) The
                    instance to execute against
oid ............... (UUID|str, optional, defaults to None)
created ........... (datetime|str|float|int, optional, defaults to None)
modified .......... (datetime|str|float|int, optional, defaults to None)
is_active ......... (bool|int, optional, defaults to None)
is_deleted ........ (bool|int, optional, defaults to None)
is_dirty .......... (bool|int, optional, defaults to None)
is_new ............ (bool|int, optional, defaults to None)
"""
        # - When used by a subclass, require that subclass to
        #   define a valid file-system path in its _file_store_dir
        #   class-attribute - that's where the JSON files will live
        if self.__class__._file_store_dir is None:
            raise AttributeError(
                '%s has not defined a file-system location to '
                'store JSON data of its instances\' data. Please '
                'set %s._file_store_dir to a valid file-system '
                'path' %
                (self.__class__.__name__, self.__class__.__name__)
            )
        if not self.__class__._file_store_ready:
            # - The first time the class is used, check the file-
            #   storage directory, and if everything checks out,
            #   then re-set the flag that controls the checks.
            if not os.path.exists(self.__class__._file_store_dir):
                # - If the path-specification exists, try to
                #   assure that the *path* exists, and create it
                #   if it doesn't. If the path can't be created,
                #   then that'll be an issue later too, so it'll
                #   need to be dealt with.
                try:
                    os.makedirs(self.__class__._file_store_dir)
                except PermissionError:
                    raise PermissionError(
                        '%s cannot create the JSON data-store '
                        'directory (%s) because permission was '
                        'denied. Please check permissions on '
                        'that directory (or its parents, if it '
                        'hasn\'t been created yet) and try '
                        'again.' %
                        (
                            self.__class__.__name__,
                            self.__class__._file_store_dir
                        )
                    )
                # - Check to make sure that files can be
                #   created there...
                try:
                    test_file = open(
                        '%s%stest-file.txt' %
                        (self.__class__._file_store_dir, os.sep),
                        'w'
                    )
                    test_file.write('test-file.txt')
                    test_file.close()
                except PermissionError:
                    raise PermissionError(
                        '%s cannot write files to the JSON data-'
                        'store directory (%s) because permission was '
                        'denied. Please check permissions on that '
                        'directory and try again.' %
                        (
                            self.__class__.__name__,
                            self.__class__._file_store_dir
                        )
                    )
                # - ... that files can be read from there...
                try:
                    test_file = open(
                        '%s%stest-file.txt' %
                        (self.__class__._file_store_dir, os.sep),
                        'r'
                    )
                    test_file.read()
                    test_file.close()
                except PermissionError:
                    raise PermissionError(
                        '%s cannot read files in the JSON data-'
                        'store directory (%s) because permission was '
                        'denied. Please check permissions on that '
                        'directory and try again.' %
                        (
                            self.__class__.__name__,
                            self.__class__._file_store_dir
                        )
                    )
                # - ... and deleted from there...
                try:
                    os.unlink(
                        '%s%stest-file.txt' %
                        (self.__class__._file_store_dir, os.sep)
                    )
                except PermissionError:
                    raise PermissionError(
                        '%s cannot delete files in the JSON data-'
                        'store directory (%s) because permission was '
                        'denied. Please check permissions on that '
                        'directory and try again.' %
                        (
                            self.__class__.__name__,
                            self.__class__._file_store_dir
                        )
                    )
                # - If no errors were raised, then re-set the flag:
                self._file_store_ready = True
        # - Call parent initializers if needed
        BaseDataObject.__init__(
            self, oid, created, modified, is_active, is_deleted,
            is_dirty, is_new
        )
        # - Set default instance property-values using _del_... methods
        # - Set instance property-values from arguments using
        #   _set_... methods
        # - Perform any other initialization needed

    ###################################
    # Object deletion                 #
    ###################################

    ###################################
    # Abstract methods                #
    ###################################

    ###################################
    # Instance methods                #
    ###################################

    def _create(self) -> None:
        """
Creates a new state-data record for the instance in the back-end
data-store
"""
        # - Since all data-transactions for these objects involve
        #   a file-write, we're just going to define this method
        #   in order to meet the requirements of BaseDataObject,
        #   make it raise an error, and override the save method
        #   to perform the actual file-write.
        raise NotImplementedError(
            '%s._create is not implemented, because the save '
            'method handles all the data-writing needed for '
            'the class. Use save() instead.' %
            self.__class__.__name__
        )

    def _update(self) -> None:
        """
Updates an existing state-data record for the instance in the
back-end data-store
"""
        # - Since all data-transactions for these objects involve
        #   a file-write, we're just going to define this method
        #   in order to meet the requirements of BaseDataObject,
        #   make it raise an error, and override the save method
        #   to perform the actual file-write.
        raise NotImplementedError(
            '%s._update is not implemented, because the save '
            'method handles all the data-writing needed for '
            'the class. Use save() instead.' %
            self.__class__.__name__
        )

    # NOTE: This can be used to illustrate unittest.skip
    def save(self):
        """
Saves the instance's state-data to the back-end data-store by
creating it if the instance is new, or updating it if the
instance is dirty
"""
        if self.is_new or self.is_dirty:
            # - Make sure objects are loaded:
            self.__class__._load_objects(self.__class__)
            # - Try to save the data:
            try:
                # - Open the file
                fp = open(
                    '%s%s%s-data%s%s.json' %
                    (
                        self.__class__._file_store_dir, os.sep,
                        self.__class__.__name__, os.sep,
                        self.oid
                    ), 'w'
                )

                # - Write the instance's data-dict to the file as JSON
                json.dump(self.to_data_dict(), fp, indent=4)

                # - re-set the new and dirty state-flags
                self._set_is_dirty(False)
                self._set_is_new(False)
                # - Update it in the loaded objects
                self.__class__._loaded_objects[self.oid] = self
            except PermissionError:
                # - Raise a more informative error
                raise PermissionError(
                    '%s could not save an object to the JSON data-'
                    'store directory (%s) because permission was '
                    'denied. Please check permissions on that '
                    'directory and try again.' %
                    (
                        self.__class__.__name__,
                        self.__class__._file_store_dir
                    )
                )
            # - Any other errors will just surface for the time being

    ###################################
    # Overrides of built-in methods   #
    ###################################

    ###################################
    # Class methods                   #
    ###################################

    def _load_objects(cls, force_load=False):
        """
Class-level helper-method that loads all the objects in the
local file-system data-store into memory so that they can be
used more quickly afterwards.
Expected to be called by the get class-method to load objects
for local retrieval, and other places as needed.
cls .......... (class, required) The class that the method is
               bound to
force_load ... (bool, optional, defaults to False) If True,
               forces the process to re-load data from scratch,
               otherwise skips the load process if data already
               exists.
"""
        if cls._loaded_objects is None or force_load:
            if not os.path.exists(cls._file_store_dir):
                # - If the path-specification exists, try to
                #   assure that the *path* exists, and create it
                #   if it doesn't. If the path can't be created,
                #   then that'll be an issue later too, so it'll
                #   need to be dealt with.
                try:
                    os.makedirs(cls._file_store_dir)
                except PermissionError:
                    raise PermissionError(
                        '%s cannot create the JSON data-store '
                        'directory (%s) because permission was '
                        'denied. Please check permissions on '
                        'that directory (or its parents, if it '
                        'hasn\'t been created yet) and try '
                        'again.' %
                        (cls.__name__, cls._file_store_dir)
                    )
            class_files_path = '%s%s%s-data' % (
                cls._file_store_dir, os.sep,
                cls.__name__
            )
            if not os.path.exists(class_files_path):
                try:
                    os.makedirs(class_files_path)
                except PermissionError:
                    raise PermissionError(
                        '%s cannot create the JSON data-store '
                        'directory (%s) because permission was '
                        'denied. Please check permissions on '
                        'that directory (or its parents, if it '
                        'hasn\'t been created yet) and try '
                        'again.' %
                        (cls.__name__, class_files_path)
                    )
            # - Get a list of all the JSON files in the data-store
            #   path
            files = [
                fname for fname in os.listdir(
                    '%s%s%s-data' % (
                        cls._file_store_dir, os.sep,
                        cls.__name__
                    )
                ) if fname.endswith('.json')
            ]
            cls._loaded_objects = {}
            if files:
                for fname in files:
                    item_file = '%s%s%s-data%s%s' % (
                        cls._file_store_dir, os.sep,
                        cls.__name__, os.sep, fname
                    )

                    try:
                        # - Read the JSON data
                        fp = open(item_file, 'r')
                        data_dict = json.load(fp)
                        fp.close()
                        # - Create an instance from that data
                        instance = cls.from_data_dict(data_dict)
                        # - Keep track of it by oid in the class
                        cls._loaded_objects[instance.oid] = instance
                    # - If permissions are a problem, raise an
                    #   error with helpful information
                    except PermissionError as error:
                        raise PermissionError(
                            '%s could not load object-data from '
                            'the data-store file at %s because '
                            'permission was denied. Please check '
                            '(and, if needed, correct) the file- '
                            'and directory-permissions and try '
                            'again' %
                            (cls.__name__, item_file)
                        )
                    # - If data-structure or -content is a problem,
                    #   raise an error with helpful information
                    except (TypeError, ValueError) as error:
                        raise error.__class__(
                            '%s could not load object-data from '
                            'the data-store file at %s because '
                            'the data was corrupt or not what '
                            'was expected (%s: %s)' %
                            (
                                cls.__name__, item_file,
                                error.__class__.__name__, error
                            )
                        )
                    # - Other errors will simply surface, at
                    #   least for now

    @classmethod
    def delete(cls, *oids):
        """
Performs an ACTUAL record deletion from the back-end data-store
of all records whose unique identifiers have been provided
"""
        # - First, ensure that objects are loaded
        cls._load_objects(cls)
        # - For each oid specified, try to remove the file, handling
        #   any errors raised in the process.
        failed_deletions = []
        for oid in oids:
            try:
                # - Try to delete the file first, so that deletion
                #   failures won't leave the files but remove the
                #   in-memory copies
                file_path = '%s%s%s-data%s%s.json' % (
                    cls._file_store_dir, os.sep,
                    cls.__name__, os.sep, oid
                )
                # - Delete the file at file_path
                os.unlink(file_path)
                # - Remove the in-memory object-instance:
                del cls._loaded_objects[oid]
            except PermissionError:
                failed_deletions.append(file_path)
        if failed_deletions:
            # - Though we *are* raising an error here, *some* deletions
            #   may have succeeded. If this error-message is displayed,
            #   the user seeing it need only be concerned with the
            #   items that failed, though...
            raise PermissionError(
                '%s.delete could not delete %d object-data %s '
                'because permission was denied. Please check the '
                'permissions on %s and try again' %
                (
                    cls.__name__, len(failed_deletions),
                    ('files' if len(failed_deletions) > 1 else 'file'),
                    ', '.join(failed_deletions)
                )
            )

    @classmethod
    def get(cls, *oids, **criteria):
        """
Finds and returns all instances of the class from the back-end
data-store whose oids are provided and/or that match the supplied
criteria
"""
        # - First, ensure that objects are loaded
        cls._load_objects(cls)
        # - If oids have been specified, then the initial results are all
        #   items in the in-memory store whose oids are in the supplied
        #   oids-list
        if oids:
            oids = tuple(
                [str(o) for o in oids]
            )
            # - If no criteria were supplied, then oids are all we need
            #   to match against:
            if not criteria:
                results = [
                    o for o in cls._loaded_objects.values()
                    if str(o.oid) in oids
                ]
            # - Otherwise, we *also* need to use matches to find items
            #   that match the criteria
            else:
                results = [
                    o for o in cls._loaded_objects.values()
                    if str(o.oid) in oids
                       and o.matches(**criteria)
                ]
            # - In either case, we have a list of matching items, which
            #   may be empty, so return it:
            return results
        # - If oids were NOT specified, then the results are all objects
        #   in memory that match the criteria
        elif criteria:
            results = [
                o for o in cls._loaded_objects
                if o.matches(**criteria)
            ]
            return results
        # - If neither were specified, return all items available:
        else:
            return list(cls._loaded_objects.values())

    ###################################
    # Static methods                  #
    ###################################


class AWSDatabaseObject(BaseDataObject, metaclass=abc.ABCMeta):
    """
    Provides baseline functionality, interface requirements and type-identity for objects that can persist their
    state-data to a RDBS(relational database SQL like) back-end data store.
    Since SQL, for the various CRUD operations, or at least for specific starting points for those CRUD operations,
    would need to be stored and accessible to the classes, a viable option would be to attach them as class-attributes
    """

    _user = "dummy_id"
    _host = "pmsdatabase.cfyebvbrqzy6.eu-north-1.rds.amazonaws.com"
    _password = "12345678"
    _port = 5432
    _database_name = "postgres"
    """
    Since the SQL for the various CRUD operations would include the tables that the data
    is stored in, and the process of connecting to the database in most RDBMS' handles
    the equivalents to the connection and database in our MongoDB approach, only
    the connection itself needs to be tracked and available as a property:
    """
    _sql_delete = "DELETE FROM {} WHERE oid IN ('{}');"
    _sql_read_oids = "SELECT * FROM {} WHERE oid IN ('{}')"
    _sql_read_all = "SELECT * FROM {}"
    _sql_read_criteria = "SELECT * FROM {} WHERE {}"

    ###################################
    # Property-getter methods #
    ###################################
    def _get_connection(self):
        try:
            return self.__class__._connection
        except AttributeError:
            # - Most RDBMS libraries provide a "connect" function, or
            # allow the creation of a "connection" object, using the
            # parameters we've named in DatastoreConfig, or simple
            # variations of them, so all we need to do is connect:
            try:
                self.__class__._connection = psycopg2.connect(
                    host=self.__class__.host,
                    port=self.__class__.port,
                    user=self.__class__.username,
                    password=self.__class__.password,
                    database=self.__class__.database_name
                )
                print("Connected to the database!")
            except Exception as e:
                print("Connection to the database failed:", str(e))

            return self.__class__._connection

    """
    Connection is lazily instantiated and performs an actual deletion, rather than resetting to default values,
    as follows:
    """

    ###################################
    # Property-deleter methods #
    ###################################
    def _del_connection(self) -> None:
        try:
            del self.__class__._connection

        except AttributeError:
            # - It may already not exist
            pass

    connection = property(_get_connection, None, _del_connection,
                          'Gets or deletes the database-connection that the instance '
                          'will use to manage its persistent state-data'
                          )

    python_to_sql_type_mapping = {
        str: 'VARCHAR',
        int: 'INTEGER',
        float: 'FLOAT',
        bool: 'BOOLEAN',
        datetime: 'TIMESTAMP',
        UUID: 'UUID'
        # Add more mappings for other Python types and SQL data types as needed
    }

    def __init__(self,
                 oid: (UUID, str, None) = None,
                 created: (datetime, str, float, int, None) = None,
                 modified: (datetime, str, float, int, None) = None,
                 is_active: (bool, int, None) = None,
                 is_deleted: (bool, int, None) = None,
                 is_dirty: (bool, int, None) = None,
                 is_new: (bool, int, None) = None, ):
        self.table_name = self.__class__.__name__

        # - Call parent initializers if needed
        BaseDataObject.__init__(
            self, oid, created, modified, is_active, is_deleted,
            is_dirty, is_new
        )
        self.column_names = self.to_data_dict().keys()
        self.column_values = self.to_data_dict().values()
        # check if table name exists otherwise create a new table.
        # all the tables will have as primary key the uiid
        sql_type = [type(column) for column in self.column_values]

        column_definitions = ', '.join(
            f"{column} {(self.__class__.python_to_sql_type_mapping[data])}" for column, data in
            zip(self.column_names, sql_type))
        create_table_query = f'''
        CREATE TABLE IF NOT EXISTS {self.table_name} ({column_definitions} , PRIMARY KEY (oid))
        '''
        # initialize class instance
        self.__class__.execute_query(create_table_query)

    def _create(self) -> None:
        # - Write the instance's data-dict to the database
        # we need to define first the sql string
        placeholders = ', '.join('%s' for _ in self.to_data_dict().values())
        column_definitions = ', '.join(f"{column}" for column in self.column_names)
        values = tuple(val for val in self.column_values)
        values_definition = ', '.join(f"'{val}'" for val in values)
        insert_query = f"INSERT INTO {self.table_name} ({column_definitions}) VALUES ({values_definition});"
        print(insert_query)
        self.__class__.execute_query(insert_query)

    def _update(self) -> None:
        """
Updates an existing state-data record for the instance in the
back-end data-store
"""
        set_clause = ', '.join(f"{column_name} = %s" for column_name in self.column_names)
        values = tuple(val for val in self.column_names)
        update_query = f"UPDATE {self.table_name} SET {set_clause} WHERE oid = {self.oid}"

    def save(self):
        """
        Saves the instance's state-data to the back-end data-store by
        creating it if the instance is new, or updating it if the
        instance is dirty
        """
        if self.is_new:
            self._create()
        elif self.is_dirty:
            self._update()

    ###################################
    # Class methods #
    ###################################
    @classmethod
    def get_connection(cls):
        try:
            return cls._connection
        except AttributeError:
            # - Most RDBMS libraries provide a "connect" function, or
            # allow the creation of a "connection" object, using the
            # parameters we've named in DatastoreConfig, or simple
            # variations of them, so all we need to do is connect:
            try:
                cls._connection = psycopg2.connect(
                    host=cls._host,
                    port=cls._port,
                    user=cls._user,
                    password=cls._password,
                    database=cls._database_name
                )
                print("Connected to the database!")
            except Exception as e:
                print("Connection to the database failed:", str(e))

            return cls._connection



    @classmethod
    def execute_query(cls, query,command =""):
        connection = cls.get_connection()
        result = None
        try:
            cursor = connection.cursor()
            result = cursor.execute(query)
            if command == 'read':
                result = cursor.fetchall()
                columns = [column[0] for column in cursor.description]  # Get the column names
                results = []
                for row in result:
                    row_dict = dict(zip(columns, row))
                    results.append(row_dict)
                return results
            connection.commit()
            return result
        except Exception as e:
            print("Query execution failed:", str(e))
            return result

    @classmethod
    def delete(cls, *oids):
        # - First, we need the database-connection that we're
        # working with:
        SQL = cls._sql_delete.format(cls.__name__, oids)
        # - Don't forget to sanitize it before executing it!
        result_set = cls.execute_query(SQL)

    """
    Most of the pattern and approach behind the get method should look familiar; again,
    it's got the same signature (and is intended to perform the same activities) as the
    methods that have been created so far, which implement the required functionality of
    the BaseDataObject:
    """

    @classmethod
    def get(cls, *oids, **criteria) -> list:
        result_set = []
        # - The first pass of the process retrieves documents based
        # on oids or criteria.
        # - We also need to keep track of whether or not to do a
        # matches call on the results after the initial data-
        # retrieval:
        post_filter = False

        # - Records are often returned as a tuple (result_set)
        # of tuples (rows) of tuples (field-name, field-value):
        # ( ..., ( ('field-name', 'value' ), (...), ... ), …)
        # The branch that handles oid requests is as follows:
        if oids:
            # - Need to replace any placeholder values in the raw SQL
            # with actual values, AND sanitize the SQL string, but
            # it starts with the SQL in cls._sql_read_oids
            SQL = cls._sql_read_oids.format(cls.__name__)
            result_set = cls.execute_query(SQL)
            if criteria:
                post_filter = True
        # The criteria branch is as follows:
        elif criteria:
            # - The same sort of replacement would need to happen here
            # as happens for oids, above. If the query uses just
            # single criteria key/value pair initially, we can use the
            # match-based filtering later to filter further as needed
            conditions = ' AND '.join(["{} = '{}'".format(key, value) for key, value in criteria.items()])
            read_query = "SELECT * FROM {} WHERE {}".format(cls.__name__, conditions)
            SQL = cls._sql_read_criteria
            result_set = cls.execute_query(SQL)
            if len(criteria) > 1:
                post_filter = True

        # The default branch that simply gets everything else is as follows:
        else:
            SQL = cls._sql_read_all.format(cls.__name__)
            result_set = cls.execute_query(SQL)

        result_set = cls.execute_query(SQL,'read')
        #data_dicts = [dict([field_tuple for field_tuple in row]) for row in result_set]

        """From this point on, the process is pretty much the same as in the previous
        implementations, in JSONFileDataObject and HMSMongoDataObject:
        # - With those, we can create the initial list of instances:"""
        try:
            results = [cls.from_data_dict(data_dict) for data_dict in result_set]
        except TypeError:
            print("There are not yet objects")
            results={}
        # - If post_filter has been set to True, then the request
        # was for items by oid *and* that have certain criteria
        # if post_filter:
        #     results = [
        #         obj for obj in results if obj.matches(**criteria)
        #     ]

        return results







class DatastoreConfig:
    """
    Represents a set of credentials for connecting to a back-end database engine that requires host,port,database,user and
    password values.
    """
    # todo:this class should be implemented to read configuration from external file
    pass


if __name__ == '__main__':
    pass
