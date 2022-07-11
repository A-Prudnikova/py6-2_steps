from dataclasses import dataclass
from demoqa_tests.model.pages.student_registration_page import StudentRegistrationForm
from selene.support.shared.jquery_style import s, ss

@dataclass
class User:
    first_name: str
    last_name: str

name = StudentRegistrationForm(s('#firstName'))
surname = StudentRegistrationForm(s('#lastName'))
mail = StudentRegistrationForm(s('#userEmail'))
cities = StudentRegistrationForm(s('#city'))
results = StudentRegistrationForm(s('.modal-content .table'))
years = StudentRegistrationForm(s('.react-datepicker__year-select'))
months = StudentRegistrationForm(s('.react-datepicker__month-select'))
subjects = StudentRegistrationForm(s('#subjectsInput'))
states = StudentRegistrationForm(s('#state'))