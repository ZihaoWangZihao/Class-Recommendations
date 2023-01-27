class dp(object):
    """
    Represents a datapoint(dp)

    course_num    <int>
    semester_offered   <string>
    rating     <int>
    hours     <int>
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
