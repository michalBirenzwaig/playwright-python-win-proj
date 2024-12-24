from playwright.sync_api import sync_playwright,Page, expect
from time import sleep
from faker import Faker

fake = Faker()

def test_homework():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        place="Sea"
        transportation="Train"
        timeToTravel="Next week"
        page.goto('https://www.qa-practice.com/elements/select/mult_select')
        page.locator('[id="id_choose_the_place_you_want_to_go"]').select_option(place)
        page.locator('[id="id_choose_how_you_want_to_get_there"]').select_option(transportation)
        page.locator('[id="id_choose_when_you_want_to_go"]').select_option(timeToTravel)
        page.locator('[id="submit-id-submit"]').click()
        result_text= page.locator('[id="result-text"]').text_content()
        print(f"to go by {transportation.lower()} to the {place.lower()} {timeToTravel.lower()}")
        assert result_text==f"to go by {transportation.lower()} to the {place.lower()} {timeToTravel.lower()}"
        print(result_text)
        sleep(3)


def test_class_work():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        page.goto('https://canvusapps.com/signup')
        page.locator('#user_name').fill("Michal")
        page.locator('#user_email').fill(fake.email())
        user_password=fake.password(length=8)
        page.locator('#user_password').fill(user_password)
        page.locator('#user_password_confirmation').fill(user_password)
        page.locator('#company_name').fill(fake.company())
        page.get_by_role('button',name='Sign up').click()


