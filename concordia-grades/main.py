from env import ACADEMIC_TERM, MYCONCORDIA_USERNAME, MYCONCORDIA_PASSWORD
from chromedriver import chromedriver_path, download_chromedriver, options
from text_message import text_myself
from gpa import gpa

import argparse
from time import sleep
from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


parser = argparse.ArgumentParser(description="Configure MyConcordia crawler.")
parser.add_argument("-hide", "--hide-grade", action="store_true", help="do not reveal grade in text message", default=False)
args = parser.parse_args()

courses_and_grades = {}
done = False
errors = 0

download_chromedriver()
sleep(1)

# Keep running until all courses have a grade
while not done:

    try:

        browser = webdriver.Chrome(executable_path=chromedriver_path, options=options)

        browser.get("https://my.concordia.ca")

        browser.find_element_by_id("userid").send_keys(MYCONCORDIA_USERNAME)
        browser.find_element_by_id("pwd").send_keys(MYCONCORDIA_PASSWORD)
        browser.find_element_by_class_name("form_button_submit").submit()

        sleep(3)

        browser.find_elements_by_class_name("ptnav2toggle")[1].click()
        sleep(1)
        browser.find_element_by_link_text("View My Grades").click()

        sleep(5)

        """
        When you wanna manipulate elements in an <iframe> tag, you have to switch to it first.
        """
        frame = browser.find_element_by_css_selector("iframe#ptifrmtgtframe")
        browser.switch_to.frame(frame)

        """
        Find semester and the row it's in.
        Check the radio button in that row.
        """
        term = browser.find_element_by_xpath('//span[text()="{}"]'.format(ACADEMIC_TERM))
        term_row = term.find_element_by_xpath("../../..")
        term_row.find_element_by_tag_name("input").click()

        """
        Click on 'Continue'.
        Headless Chrome can't click on the element for some reason, so we send the ENTER key to it.
        """
        browser.find_element_by_id("DERIVED_SSS_SCT_SSR_PB_GO").send_keys(Keys.ENTER)

        sleep(1)

        grades_table = browser.find_element_by_id("TERM_CLASSES$scroll$0")
        rows = grades_table.find_elements_by_tag_name("tr")
        rows = [row for row in rows if row.get_attribute("id").startswith("trTERM_CLASSES$0_row")]

        for row in rows:

            data = row.find_elements_by_tag_name("td")
            course = data[0].text
            grade = data[4].text.strip()

            if course not in courses_and_grades:
                courses_and_grades[course] = grade
            elif grade != courses_and_grades[course]:
                courses_and_grades[course] = grade
                if args.hide_grade:
                    text_myself("Your grade for {} is out.".format(course))
                else:
                    text_myself("You got {} ({} GPA) in {}.".format(grade, gpa[grade], course))

        browser.quit()

        print(courses_and_grades)

        # Check if all keys have a non-empty value, i.e. if not all grades are out, then keep the script running.
        done = all(grade for grade in courses_and_grades.values())

        if not done:
            sleep(randint(180, 360))

    except Exception as e:

        errors += 1
        print("{}, {} error(s) so far".format(e.__class__.__name__, errors))
        sleep(1)
        pass
