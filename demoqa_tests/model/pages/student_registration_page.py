from selene import command, have
from selene.support.shared.jquery_style import s, ss

from selene.core.entity import Element


class StudentRegistrationForm:

    def __init__(self, element: Element):
        self.element = element
        self.first_name = s('#firstName')
        self.last_name = s('#lastName')
        self.email = s('#userEmail')
        self.subjects = s('#subjectsInput')

    def set_value(self, value: str):
        self.element.type(value)

    def select_subject_from_list(self, to_type: str):
        self.element.type(to_type)
        ss(
            '.subjects-auto-complete__option'
        ).element_by(have.text(to_type)).click()
        return self

    def input_subject_by_tab(self, to_type: str):
        self.element.type(to_type).press_tab()
        return self

    def select_dropdown(self, /, *, option: str):
        self.element.perform(command.js.scroll_into_view).click()
        ss('[id^=react-select-][id*=-option]').element_by(have.exact_text(option)).click()

    def set_dropdown(self, /, *, option: str):
        self.element.element(
            '[id^=react-select-][id*=-input]'
        ).type(option).press_enter()

    def select_year(self, option: str):
        self.element.click()
        s('.react-datepicker__year-select').s(f'[value="{option}"]').click()

    def select_month(self, option: int):
        s('.react-datepicker__month-select').s(f'[value="{option}"]').click()

    def select_day(self, option: str):
        s(f'.react-datepicker__day--0{option}').click()

    def set_year(self, option: str):
        self.element.click()
        s('.react-datepicker__year-select').type(option)

    def set_month(self, option: str):
        s('.react-datepicker__month-select').type(option)

    def set_day(self, option: str):
        s(f'.react-datepicker__day--0{option}').type(option).click()

    def row(self, index):
        return self.element.all('tbody tr')[index].all('td')



