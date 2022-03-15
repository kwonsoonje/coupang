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
        self.category_value = ""
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

        category_input = QLineEdit()
        category_input.setPlaceholderText('카테고리 입력(생략)')
        category_input.textChanged[str].connect(self.category_input_action)

        blog_add_button = QPushButton('블로그 추가')
        blog_add_button.released.connect(self.blog_add_action)

        blog_load_button = QPushButton('블로그 불러오기')
        blog_load_button.released.connect(self.blog_load_action)

        tab1_layout1.addWidget(blog_url_input, 0, 1)
        tab1_layout1.addWidget(blog_id_input, 0, 2)
        tab1_layout1.addWidget(blog_pw_input, 0, 3)
        tab1_layout1.addWidget(category_input, 0, 4)
        tab1_layout1.addWidget(blog_add_button, 0, 5)
        tab1_layout1.addWidget(blog_load_button, 0, 6)

        tab1.layout_t.addLayout(tab1_layout1)#탭1 맨위레이아웃 끝

        #탭1 중간 레이아웃시작##################################
        table1 = QTableWidget(self)
        table1.setRowCount(0)
        table1.setColumnCount(5)
        table1.setHorizontalHeaderLabels(["블로그 리스트", "아이디", "패스워드", "카테고리", "작업현황"])
        table1.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        tab1.layout_t.addWidget(table1)
        ###########################################################


        #탭1 맨및 버튼들 #######################################
        tab1_layout3 = QGridLayout()
        tedering_check = QCheckBox(' 테더링 사용')
        proxy_check = QCheckBox(' 프록시 사용')
        ip_load_button = QPushButton('IP 불러오기')
        label1 = QLabel('포스팅 딜레이')
        posting_delay_input = QLineEdit()
        posting_delay_input.setPlaceholderText('분')
        label2 = QLabel('포스팅 수량')
        posting_counter_input = QLineEdit()
        posting_counter_input.setPlaceholderText('00')
        start_button = QPushButton('자동 홍보 시작')
        stop_button = QPushButton('자동 홍보 정지')

        tab1_layout3.addWidget(tedering_check, 0, 1)
        tab1_layout3.addWidget(proxy_check, 0, 2)
        tab1_layout3.addWidget(ip_load_button, 0, 3)
        tab1_layout3.addWidget(label1, 0, 4)
        tab1_layout3.addWidget(posting_delay_input, 0, 5)
        tab1_layout3.addWidget(label2, 0, 6)
        tab1_layout3.addWidget(posting_counter_input, 0, 7)
        tab1_layout3.addWidget(start_button, 0, 8)
        tab1_layout3.addWidget(stop_button, 0, 9)

        tab1.layout_t.addLayout(tab1_layout3)
        #탭1 끝##################################################



        #탭2 끝##################################################


        #탭3 시작###################################################
        tab3_layout1 = QGridLayout()        #제목에 설정
        tab3_label1 = QLabel("★ 제목에 설정")
        tab3_layout1.addWidget(tab3_label1, 0, 1)
        subject_load_button = QPushButton("제목 파일 불러오기")
        tab3_layout1.addWidget(subject_load_button, 0, 2)
        keyword_check = QCheckBox(' 사용한 키워드 넣기')
        tab3_layout1.addWidget(keyword_check, 0, 3)
        product_check = QCheckBox(' 사용한 상품명 넣기')
        tab3_layout1.addWidget(product_check, 0, 4)
        change_text_button = QCheckBox(' 치환(변경)단어 적용')
        tab3_layout1.addWidget(change_text_button, 1, 1)
        change_text_button2 = QPushButton(' 치환 파일 불러오기')
        tab3_layout1.addWidget(change_text_button2, 1, 2)

        tab3_oo = QLabel(" ")
        tab3_layout1.addWidget(tab3_oo, 2, 1)

        tab3_label2 = QLabel("★ 내용 상단 설정")
        tab3_layout1.addWidget(tab3_label2, 3, 1)
        file_load_button = QPushButton("내용 파일 불러오기")
        tab3_layout1.addWidget(file_load_button, 3, 2)
        tab3_cc1 = QCheckBox(' 치환(변경)단어 적용')
        tab3_layout1.addWidget(tab3_cc1, 3, 3)

        tab3_cc2 = QPushButton('치환 파일 불러오기')
        tab3_layout1.addWidget(tab3_cc2, 3, 4)

        tab3_cc3 = QCheckBox(' 특정단어에 사용한 키워드로 변경')
        tab3_layout1.addWidget(tab3_cc3, 4, 1)
        tab3_cc4 = QLineEdit()
        tab3_layout1.addWidget(tab3_cc4, 4, 2)
        tab3_cc5 = QCheckBox(' 특정단어에 사용한 상품명으로 변경')
        tab3_layout1.addWidget(tab3_cc5, 4, 3)
        tab3_cc6 = QLineEdit()
        tab3_layout1.addWidget(tab3_cc6, 4, 4)

        tab3_oo = QLabel(" ")
        tab3_layout1.addWidget(tab3_oo, 5, 1)


        tab3_dd1 = QLabel("★ 내용 중앙 쿠팡 광고 삽입 부분")
        tab3_layout1.addWidget(tab3_dd1, 6, 1)

        tab3_dd2 = QCheckBox(' 쿠팡파트너스 링크우회/단축도메인 사용')
        tab3_layout1.addWidget(tab3_dd2, 6, 2)

        tab3_oo = QLabel(" ")
        tab3_layout1.addWidget(tab3_oo, 7, 1)

        tab3_ff1 = QLabel("★ 내용 하단 설정")
        tab3_layout1.addWidget(tab3_ff1, 8, 1)

        tab3_ff2 = QPushButton("내용 파일 불러오기")
        tab3_layout1.addWidget(tab3_ff2, 8, 2)

        tab3_ff3 = QCheckBox(" 치환(변경)단어 적용")
        tab3_layout1.addWidget(tab3_ff3, 8, 3)

        tab3_ff4 = QPushButton("치환 파일 불러오기")
        tab3_layout1.addWidget(tab3_ff4, 8, 4)

        tab3_ff5 = QCheckBox("특정단어에 사용한 키워드로 변경")
        tab3_layout1.addWidget(tab3_ff5, 9, 1)

        tab3_ff6 = QLineEdit()
        tab3_layout1.addWidget(tab3_ff6, 9, 2)

        tab3_ff7 = QCheckBox("특정단어에 사용한 상품명으로 변경")
        tab3_layout1.addWidget(tab3_ff7, 9, 3)

        tab3_ff8 = QLineEdit()
        tab3_layout1.addWidget(tab3_ff8, 9, 4)

        tab3_oo = QLabel(" ")
        tab3_layout1.addWidget(tab3_oo, 10, 1)


        tab3_ee1 = QLabel("★내용 하단 추가 설정")
        tab3_layout1.addWidget(tab3_ee1, 11, 1)

        tab3_ee2 = QCheckBox("자동 원고 덧붙임")
        tab3_layout1.addWidget(tab3_ee2, 11, 2)

        tab3_ee3 = QRadioButton("자동원고 안보이게 히든 적용")
        tab3_layout1.addWidget(tab3_ee3, 11, 3)

        tab3_oo = QLabel(" ")
        tab3_layout1.addWidget(tab3_oo, 12, 1)


        tab3_gg1 = QLabel("★마무리 설정")
        tab3_layout1.addWidget(tab3_gg1, 13, 1)

        tab3_gg2 = QCheckBox("태그 자동 입력")
        tab3_layout1.addWidget(tab3_gg2, 13, 2) 

        tab3_gg3 = QCheckBox("태그 파일 사용 입력")
        tab3_layout1.addWidget(tab3_gg3, 13, 3)

        tab3_gg4 = QPushButton("태그 파일 불러오기")
        tab3_layout1.addWidget(tab3_gg4, 13, 4)

        tab3_gg5 = QRadioButton(" 전체공개")
        tab3_layout1.addWidget(tab3_gg5, 14, 1)

        tab3_gg6 = QRadioButton(" 이웃공개")
        tab3_layout1.addWidget(tab3_gg6, 14, 2)

        tab3_gg7 = QRadioButton(" 서로이웃공개")
        tab3_layout1.addWidget(tab3_gg7, 14, 3)

        tab3_gg8 = QRadioButton(" 비공개")
        tab3_layout1.addWidget(tab3_gg8, 14, 4)


        
        tab3.layout_t.addLayout(tab3_layout1)   #제목설정 끝


        ##탭3 끝#######################################################
        tab1.setLayout(tab1.layout_t) 
        tab3.setLayout(tab3.layout_t)
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

    def category_input_action(self, text):
        self.category_value = text

    def blog_add_action(self):
        print('블로그추가')

    def blog_load_action(self):
        print('블로그불러오기')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()