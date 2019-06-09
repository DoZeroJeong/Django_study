from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from datetime import date, time
import threading
import schedule

today = date.today()


def restaurant():
    req = Request("http://tusso.tu.ac.kr/jsp/manage/restaurant/restaurant_menu.jsp")
    res = urlopen(req)
    html = res.read().decode("UTF-8")
    bs = BeautifulSoup(html, 'html.parser')
    pic_date = bs.find('input', {'id': 'picdate'})
    student = bs.select('div > table')
    faculty = bs.select('div > table')

    if student == [] and faculty == []:
        s_f = open('static/student_menu.txt', 'a')
        s_f.write('식단메뉴가 없습니다.')
        s_f.write('\n')
        s_f.write(today.__str__())
        s_f.write('\n\n')
        f_f = open('static/faculty_menu.txt', 'a')
        f_f.write("식단메뉴가 없습니다.")
        f_f.write('\n')
        f_f.write(today.__str__())
        f_f.write('\n\n')
    else:
        for student_tag in student:
            student_menu = student_tag.tbody.text
            student_menu = student_menu.split()
            s_f = open('static/student_menu.txt', 'a')
            s_f.write(student_menu)
            s_f.write('\n')
            s_f.write(today.__str__())
            s_f.write('\n\n')

        for faculty_tag in faculty:
            faculty_menu = faculty_tag.tbody.text
            faculty_menu = faculty_menu.split()
            f_f = open('static/faculty_menu.txt', 'a')
            f_f.write(faculty_menu)
            f_f.write('\n')
            f_f.write(today.__str__())
            f_f.write('\n\n')

        print(today)


schedule.every().day.at("00:00").do(restaurant)

while True:
    schedule.run_pending()

