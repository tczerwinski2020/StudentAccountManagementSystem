# Student Account (first name, last name, admittance year, email address, student id, photo)
class StudentAccount:
    # The constructor that initializes the instance variables
    _last_assigned_student_id = 90188000
    # Constructs an object of StudentAccount
    def __init__(self, first_name, last_name, admittance_year):
        self._first_name = first_name
        self._last_name = last_name
        self._admittance_year = admittance_year
        self._email_address = (first_name[0:1] + last_name + str(admittance_year) + "@my.fit.edu").lower()
        self._student_id = StudentAccount._last_assigned_student_id + 1
        StudentAccount._last_assigned_student_id = StudentAccount._last_assigned_student_id + 1
        self._photo = "male_silhouette.png"

    # Returns a student record (example, as a tuple)
    def get_record(self):
        record = (self._student_id, self._first_name, self._last_name, self._email_address,
                  self._admittance_year,self._photo)
        return record

    # Sets student ID as student_id
    def set_student_id(self, student_id):
        self._student_id = student_id
        _last_assigned_student_id = student_id

    # Returns a student's student ID
    def get_student_id(self):
        return self._student_id

    # Sets a student's photo to photo
    def set_photo(self, photo):
        self._photo = photo