from selene.support.shared import browser
from selene import have
from selene.support.shared.jquery_style import s
from demoqa_tests.resourse import resourse
from demoqa_tests.model.pages.student_registration_page import StudentRegistrationForm
from demoqa_tests.model.utils.data import name, cities, results, years, months, subjects, states, surname, mail

firstname = 'Anna'
lastname = 'Hanna'
email = '1@test.ru'
gender = 'Other'
phonenumber = '1111111111'
year = '2000'
month_str = 'April'
# переменная month_int должна иметь значение (число месяца из переменной month_str минус 1)
month_int = 3
# переменная day всегда должна быть обозначена двумя знаками: 01, 02, 15, 31
day = '20'
days = StudentRegistrationForm(s(f'.react-datepicker__day--0{day}'))
subject = 'English'
subject2 = 'Maths'
hobby = 'Sports'
picture = '1.jpg'
address = 'my room'
state = 'NCR'
city = 'Delhi'



def test_setting_data_manual(browser_config):
    browser.open('/automation-practice-form').driver.maximize_window()

    name.set_value(firstname)
    surname.set_value(lastname)
    mail.set_value(email)
    s('[for="gender-radio-3"]').click()
    s('#userNumber').type(phonenumber)
    s('#dateOfBirthInput').click()
    years.set_year(option=year)
    months.set_month(option=month_str)
    days.set_day(option=day)
    subjects.input_subject_by_tab(to_type=subject).input_subject_by_tab(to_type=subject2)
    s('[for="hobbies-checkbox-1"]').click()
    s('#uploadPicture').send_keys(resourse(picture))
    s('#currentAddress').type(address)
    states.set_dropdown(option=state)
    cities.set_dropdown(option=city)
    s('#submit').click()

    # Проверка с использованием Page Object
    results.row(0).should(have.exact_texts('Student Name', f'{firstname} {lastname}'))
    results.row(1).should(have.exact_texts('Student Email', f'{email}'))
    results.row(2).should(have.exact_texts('Gender', f'{gender}'))
    results.row(3).should(have.exact_texts('Mobile', f'{phonenumber}'))
    results.row(4).should(have.exact_texts('Date of Birth', f'{day} {month_str},{year}'))
    results.row(5).should(have.exact_texts('Subjects', f'{subject}, {subject2}'))
    results.row(6).should(have.exact_texts('Hobbies', f'{hobby}'))
    results.row(7).should(have.exact_texts('Picture', f'{picture}'))
    results.row(8).should(have.exact_texts('Address', f'{address}'))
    results.row(9).should(have.exact_texts('State and City', f'{state} {city}'))



