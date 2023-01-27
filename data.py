class Course(object):
    """
    Represents a Course

    course_num    <int>
    semester_offered   <string>
    rating     <int>
    hours     <int>
    units   <int>
    """
    def __init__(self, course_num, semester_offered, units, rating, hours):
        self.course_num = course_num
        self.semester_offered = semester_offered
        self.rating = rating
        self.hours = hours
        self.units = units
    """ Field Accessors """
    def get_course_num(self):
        return self.course_num
    def get_semester_offered(self):
        return self.semester_offered
    def get_rating(self):
        return self.rating
    def get_hours(self):
        return self.hours
    def get_units(self):
        return self.units

class Person(object):
    """
    Represents a Person

    name    <string>
    year   <string>
    major     <major>
    career     <major>
    courses   <list with each element of type Course>
    """
    def __init__(self, name, year, major, career, courses):
        self.name = name
        self.year = year
        self.major = major
        self.career = career
        self.courses = courses
    """ Field Accessors """
    def get_name(self):
        return self.name
    def get_year(self):
        return self.year
    def get_major(self):
        return self.major
    def get_career(self):
        return self.career
    def get_courses(self):
        return self.courses


