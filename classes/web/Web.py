from classes.web.Connection import *
from classes.web.pages.SigninWeb import SigninWeb
from classes.web.pages.Evaluationweb import Evaluationweb
from classes.web.pages.StudentListWeb import StudentListWeb
from classes.web.pages.StudentGradesWeb import StudentGradesWeb

class Web:
    def take_grades_from_student_page(self,secrets):
        saga_url = secrets['SAGA_URL'] or ''
        if secrets == '': raise Exception('URL not provided')
        driver = Connection(Browser.Chrome).driver
        # ACCESS SAGA #
        driver.get(saga_url)
        # SIGN IN PAGE #
        signin_page = SigninWeb(driver,secrets)
        signin_page.do_login()
        print(driver.title)
        # ENTER EVALUATION PAGE #
        evaluation_page = Evaluationweb(driver)
        evaluation_page.go_to_teacher_menu()
        evaluation_page.go_to_groups_menu()
        evaluation_page.go_to_group(secrets['GROUP_NAME'])
        # ENTER STUDENT LIST #
        student_list_page = StudentListWeb(driver)
        students_list = student_list_page.get_student_list()
        class_grades = []
        for i in range(len(students_list)):
            student_list_page.click_into_student(students_list[i])
            # ENTER STUDENT'S GRADES #
            student_grades_web = StudentGradesWeb(driver)
            class_grades.append(student_grades_web.get_grades_matrix())
            student_grades_web.click_go_back()
        driver.quit()
        return [students_list,class_grades]
