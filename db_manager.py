import sqlite3

# Manages the database located at cse2050_students_db.db
class DBManager:
    # Initializes variables in order to connect with the database
    def __init__(self, db_path=""):
        # Set up any necessary instance variables
        # By default the db_path is empty, but we may send one during instantiation like so: db_manager = DBManager("../data/")

        self._db = "cse2050_students_db.db"
        self._conn = None # no connection is made upon instantiation
        pass

    # Establishes connection with database using sqlite3
    def open_connection(self):
        self._conn = sqlite3.connect(self._db)

    # Closes connection with database
    def close_connection(self):
        self._conn.close()

    # Initializes the database with values
    def init_tables(self):
        # Remove old tables each time your app loads 
        # (just for demonstration purposes and for this assignment; not applicable in the real world)
        self.open_connection()
        sql_command = """
        DROP TABLE IF EXISTS Students
        """
        cursor = self._conn.cursor()
        cursor.execute(sql_command)
        self._conn.commit()
        sql_command = """CREATE TABLE Students(student_id INTEGER, first_name  TEXT, last_name TEXT,
            email_address TEXT, admittance_year INTEGER, photo TEXT);"""
        cursor.execute(sql_command)
        self._conn.commit()
        self.close_connection()

    # Adds a single student record to the database
    def add_record(self, record):
        # prepare the record for insertion into the DB
        self.open_connection()
        sql_command = """INSERT INTO Students(student_id, first_name, last_name, email_address, 
                    admittance_year, photo) VALUES (?,?,?,?,?,?);"""
        cursor = self._conn.cursor()
        cursor.execute(sql_command, record)
        self._conn.commit()
        self.close_connection()

    # Searches the database for a student with specific id (sid)
    def search_by_id(self, sid):
        # return a single record based on the given student id
        self.open_connection()
        cursor = self._conn.cursor()
        cursor.execute("""SELECT * FROM Students WHERE student_id LIKE \'%""" + str(sid) + "%\' LIMIT 1")
        student = cursor.fetchall()
        self.close_connection()
        if len(student) == 0:
            return
        return student[0]

    # Searches the database for students with a specific string (student_name) in their first or last name
    def search_by_name(self, student_name):
        # return one or more records that match the criteria given on the assignment
        self.open_connection()
        cursor = self._conn.cursor()
        cursor.execute("""SELECT * FROM Students WHERE first_name LIKE \'%""" + student_name + """%\' OR last_name
        LIKE \'%""" + student_name + """%\' OR first_name || " " || last_name
                LIKE \'%""" + student_name + """%\'""")
        # cursor.execute("""SELECT * FROM Students WHERE first_name || " " || last_name
        # LIKE \'%""" + student_name + """%\'""")
        rows = cursor.fetchall()
        self.close_connection()
        return rows

    # Retrieves the last student's ID number
    def get_last_student_id(self):
        # You may need this in order to determine the id to use when 
        # adding a new record outside of the predefined list using the add student dialog
        self.open_connection()
        cursor = self._conn.cursor()
        cursor.execute("""SELECT student_id FROM Students ORDER BY  student_id DESC LIMIT 1""")
        sid = cursor.fetchall()
        self.close_connection()
        return sid


