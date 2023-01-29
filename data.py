# Importing libraries
from faker import Faker
import random
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
import numpy as np

# Getting files
careers_excel = "List of Careers.xlsx"
courses_excel = "List of Classes.xlsx"
career_list = pd.read_excel(careers_excel)
class_list = pd.read_excel(courses_excel)

# Getting careers
possible_careers = []
for i in career_list["OCC_TITLE"]:
    possible_careers.append(i)

# Web Scraping - Getting courses
url = "http://student.mit.edu/catalog/m6a.html"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
a_tag = soup.find_all("a") # Finds me all the <a> </a> tags, which is the tag the course numbers are contained in
course = []
for i in a_tag:
    text = i.text
    if "6." in text and "/" not in text:
        course.append(text)
course = list(dict.fromkeys(course)) # remove duplicates
print(course) # 6.100B not in course

# Generating fake data
fake = Faker()
names = [] # List of fake names
majors = [] # List of fake majors
careers = [] # List of fake careers
classes = [] # List of fake courses
semester = [] # List of fake semesters

dp = 0 # How many datapoints to generate
for i in range(dp):
    names.append(fake.name())
    major_random = random.choice([1,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,18,20])
    majors.append(major_random)
    careers_random = random.choice(possible_careers)
    careers.append(careers_random)
    semester_random = random.choice(["Fall", "Spring"])
    semester.append(semester_random)

# Each person assumed to take 40 classes
for i in range(dp*40):
    course_random = random.choice(course)
    classes.append(course_random)
class Course(object):
    """
    Represents a Course

    course_num    <int>
    semester_offered   <string>
    rating     <int>
    hours     <int>
    units   <int>
    """
    def __init__(self, course_num, semester_offered, rating, hours):
        self.course_num = course_num
        self.semester_offered = semester_offered
        self.rating = rating
        self.hours = hours
    """ Field Accessors """
    def get_course_num(self):
        return self.course_num
    def get_semester_offered(self):
        return self.semester_offered
    def get_rating(self):
        return self.rating
    def get_hours(self):
        return self.hours

class Person(object):
    """
    Represents a Person

    name    <string>
    year   <string>
    major     <major>
    career     <major>
    courses   <list with each element of type Course>
    """
    def __init__(self, name, major, career, courses):
        self.name = name
        self.major = major
        self.career = career
        self.courses = courses
    """ Field Accessors """
    def get_name(self):
        return self.name

    def get_major(self):
        return self.major
    def get_career(self):
        return self.career
    def get_courses(self):
        return self.courses


