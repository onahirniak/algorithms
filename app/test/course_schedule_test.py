import unittest
from app.main.graphs.course_schedule import CourseSchedule

class CourseSchedueTests(unittest.TestCase):

    def test_should_finish_courses(self):
        sut = CourseSchedule()

        result = sut.can_finish(2,[[1,0]])

        self.assertTrue(result)

    def test_should_not_finish_courses(self):
        sut = CourseSchedule()

        result = sut.can_finish(2,[[1,0],[0,1]])

        self.assertFalse(result)