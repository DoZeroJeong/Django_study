from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from datetime import date
import schedule

today = date.today()

def restaurant():
    req = Request("http://tusso.tu.ac.kr/jsp/manage/restaurant/restaurant_menu.jsp")
    res = urlopen(req)
    html = res.read().decode("UTF-8")
    bs = BeautifulSoup(html, 'html.parser')
    pic_date = bs.find('input', {'id': 'picdate'})
    student_th_tag = bs.select('body > div.center > div:nth-child(4) > table > tbody > tr > th')
    student_td_tag = bs.select('body > div.center > div:nth-child(4) > table > tbody > tr > td')
    faculty_th_tag = bs.select('body > div.center > div:nth-child(6) > table > tbody > tr > th')
    faculty_td_tag = bs.select('body > div.center > div:nth-child(6) > table > tbody > tr > td')

    students_th = []
    students_td = []
    faculties_th = []
    faculties_td = []

    if student_th_tag == [] and faculty_th_tag == []:
        s_f = open('static/student_menu.json', 'a')
        s_f.write('{')
        s_f.write('\n')
        s_f.write("result : 식단메뉴가 없습니다.")
        s_f.write('\n')
        s_f.write('}')
        f_f = open('static/faculty_menu.json', 'a')
        f_f.write('{')
        f_f.write('\n')
        f_f.write("result : 식단메뉴가 없습니다.")
        f_f.write('\n')
        f_f.write('}')
    else:
        for students in student_th_tag:
            students_th.append(students.text)

        for students in student_td_tag:
            student_menu = students.text.split()
            student_menu = " ".join(student_menu)
            students_td.append(student_menu)

        for faculties in faculty_th_tag:
            faculties_th.append(faculties.text)

        for faculties in faculty_td_tag:
            faculty_menu = faculties.text.split()
            faculty_menu = " ".join(faculty_menu)
            faculties_td.append(faculty_menu)

        s_f = open('static/student_menu.json', 'a')
        s_f.write('{')
        for i in range(0, len(students_th)):
            s_f.write('\n\t')
            s_f.write('"{}" : "{}"'.format(students_th[i], students_td[i]))
            s_f.write(',')
        s_f.write('\n},')
        s_f.write('\n')

        f_f = open('static/faculty_menu.json', 'a')
        f_f.write('{')
        for i in range(0, len(faculties_th)):
            f_f.write('\n\t')
            f_f.write('"{}" : "{}"'.format(faculties_th[i], faculties_td[i]))
        f_f.write('\n},')
        f_f.write('\n')



restaurant()
# schedule.every().day.at("00:00").do(restaurant)
#
# while True:
#     schedule.run_pending()
