from demoqa_tests.model.pages.student_registration_page import StudentRegistrationForm
from selene.core.entity import Element


class StudentRegistrationSteps:
    def __init__(self, element: Element):
        self.form = StudentRegistrationForm()
        self.element = element

    def fill_form(self, *values):
        self.form.first_name.type(values)
        self.form.last_name.type(values)
        self.form.subjects.autocomplete(values)
