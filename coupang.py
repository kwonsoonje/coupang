from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import time

class Thread(QThread):
    def run(self):
        while True:
            print('hi')
            time.sleep(1)

class MyWindow(QWidget):
    def __init__(self):
        self.id_value = ""
        self.pw_value = ""
        self.blog_url = ""
        self.blog_id = ""
        self.blog_pw = ""
        super().__init__()        
        self.setupUI()


    def setupUI(self):
        self.setGeometry(800, 200, 800, 600)

        #메인화면레이아웃
        main_layout = QVBoxLayout()
        


        #맨위레이아웃@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        top_layout = QGridLayout()

        #아이디인풋창###################
        id_input = QLineEdit()
        id_input.setPlaceholderText('아이디')
        id_input.textChanged[str].connect(self.id_input_action)
        ###############################

        #비밀번호입력창####################
        pw_input = QLineEdit()
        pw_input.setPlaceholderText('비밀번호')
        pw_input.textChanged[str].connect(self.pw_input_action)
        #################################

        #로그인버튼#######################
        login_button = QPushButton("로그인")
        login_button.released.connect(self.login_check)
        #################################

        #사용자등록버튼####################
        signup_button = QPushButton('사용자 등록')
        #################################

        #셋팅 관련 버튼들 ##########################
        setting_save_button = QPushButton('세팅 저장')
        setting_save_button.released.connect(self.save_setting)
        setting_load_button = QPushButton('세팅 로드')
        setting_load_button.released.connect(self.load_setting)
        #################################

        top_layout.addWidget(id_input, 0, 0)
        top_layout.addWidget(pw_input, 0, 1)
        top_layout.addWidget(login_button, 0, 2)
        top_layout.addWidget(signup_button, 0, 3)
        top_layout.addWidget(setting_save_button, 0, 4)
        top_layout.addWidget(setting_load_button, 0, 5)
        main_layout.addLayout(top_layout)
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


        #탭레이아웃@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        tabs = QTabWidget()
        tab1 = QWidget()
        tab2 = QWidget()
        tab3 = QWidget()
        tab1.layout_t = QVBoxLayout()
        tab2.layout_t = QVBoxLayout()
        tab3.layout_t = QVBoxLayout()
        #실행설정화면##############################################
        tab1_layout1 = QGridLayout() #맨위레이아웃

        blog_url_input = QLineEdit() #블로그주소입력
        blog_url_input.setPlaceholderText('블로그주소 입력')
        blog_url_input.textChanged[str].connect(self.blog_url_input_action)

        blog_id_input = QLineEdit()
        blog_id_input.setPlaceholderText('블로그 ID 입력')
        blog_id_input.textChanged[str].connect(self.blog_id_input_action)

        blog_pw_input = QLineEdit()
        blog_pw_input.setPlaceholderText('블로그 PW 입력')
        blog_pw_input.textChanged[str].connect(self.blog_pw_input_action)


        ##########################################################

        tabs.addTab(tab1, '실행설정')
        tabs.addTab(tab2, '홍보설정')
        tabs.addTab(tab3, '자동초대')
        main_layout.addWidget(tabs)
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        
        self.setLayout(main_layout)


    def id_input_action(self, text): #아이디 입력 받는 함수
        self.id_value = text

    def pw_input_action(self, text): #비번 입력받는 함수
        self.pw_value = text

    def login_check(self): #로그인버튼 실행함수
        print('로그인버튼실행')

    def save_setting(self): #셋팅저장 실행함수
        print('세팅 저장')

    def load_setting(self): #셋팅불러오기 실행함수
        print('셋팅 로드')

    def blog_url_input_action(self, text): #블로그 주소 입력 받는 함수
        self.blog_url = text

    def blog_id_input_action(self, text):
        self.blog_id = text

    def blog_pw_input_action(self, text):
        self.blog_pw = text


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()