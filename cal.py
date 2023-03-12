import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import *
from cal_ui import Ui_Dialog

import time
import re

class Thread1(QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        p = re.compile("([0-9]+)([+-/*])([0-9]+)")
        m = p.match(self.parent.lineEdit.text())

        self.token = True
        self.num1 = m.group(1)
        self.num2 = m.group(3)
        self.operator = m.group(2)
        self.total = self.num1

    def run(self):

        while self.token == True:
            if self.operator == "+":
                while self.token:           
                    self.total = str(eval(self.total+'+'+self.num2)) # 이 결과 값을 다시 +num2해서 eval 해야됨.
                    #total += num2
                    self.parent.lineEdit.setText(str(self.total))
                    time.sleep(0.5)
            elif self.operator == "-":
                while self.token:
                    self.total = str(eval(self.total+'-'+self.num2))
                    self.parent.lineEdit.setText(str(self.total))
                    time.sleep(0.5)
            elif self.operator == "/":
                while self.token:
                    self.total = str(eval(self.total+'/'+self.num2)) 
                    self.parent.lineEdit.setText(str(self.total))
                    time.sleep(0.5)       
            elif self.operator == "*":
                while self.token:
                    self.total = str(eval(self.total+'*'+self.num2))
                    self.parent.lineEdit.setText(str(self.total))
                    time.sleep(0.5)

    def stop(self):
        self.token = False
        self.parent.lineEdit.setText(str(self.total))
        self.quit()

        

class Cal(QWidget,Ui_Dialog):
    def __init__(self):
        super().__init__()

        # use the Ui_login_form
        self.initUI()  
        self.show()
    
    def initUI(self):
        self.setupUi(self)
        self.btn_1.clicked.connect(self.button_1)  # 버튼 클릭시 연결되는 함수
        self.btn_2.clicked.connect(self.button_2)
        self.btn_3.clicked.connect(self.button_3)
        self.btn_4.clicked.connect(self.button_4)
        self.btn_5.clicked.connect(self.button_5)
        self.btn_6.clicked.connect(self.button_6)
        self.btn_7.clicked.connect(self.button_7)
        self.btn_8.clicked.connect(self.button_8)
        self.btn_9.clicked.connect(self.button_9)
        self.btn_0.clicked.connect(self.button_0)
        self.btn_plus.clicked.connect(self.button_plus)
        self.btn_minus.clicked.connect(self.button_minus)
        self.btn_mul.clicked.connect(self.button_mul)
        self.btn_div.clicked.connect(self.button_div)
        self.btn_del.clicked.connect(self.del_num)
        self.btn_equal.clicked.connect(self.result)
        self.btn_clear.clicked.connect(self.clear)
        self.btn_rp.clicked.connect(self.repeat_press)
        self.pushButton_2.clicked.connect(self.StopPress)

    def button_1(self):
        self.number("1")

    def button_2(self):
        self.number("2")

    def button_3(self):
        self.number("3")

    def button_4(self):
        self.number("4")

    def button_5(self):
        self.number("5")

    def button_6(self):
        self.number("6")

    def button_7(self):
        self.number("7")

    def button_8(self):
        self.number("8")

    def button_9(self):
        self.number("9")

    def button_0(self):
        self.number("0")


    def number(self,num):
        exist_text = self.lineEdit.text() #lineEdit값을 가져와서 exist_text에 저장
        self.lineEdit.setText(exist_text+num) #기존값 + 새로입력된값
        

    def del_num(self):
        exist_text = self.lineEdit.text()
        self.lineEdit.setText(exist_text[:-1])

    def button_plus(self):
        exist_text = self.lineEdit.text()
        try:
            if((exist_text[-1] == "+")| (exist_text[-1] == "-")|(exist_text[-1] == "*")|(exist_text[-1] == "/")):
                self.lineEdit.setText(exist_text[:-1])
            self.number("+")
        except:
            pass

    def button_minus(self):
        exist_text = self.lineEdit.text()
        try:
            if((exist_text[-1] == "+")| (exist_text[-1] == "-")|(exist_text[-1] == "*")|(exist_text[-1] == "/")):
                self.lineEdit.setText(exist_text[:-1])
            self.number("-")
        except:
            pass

    def button_mul(self):
        exist_text = self.lineEdit.text()

        try:
            if((exist_text[-1] == "+")| (exist_text[-1] == "-")|(exist_text[-1] == "*")|(exist_text[-1] == "/")):
                self.lineEdit.setText(exist_text[:-1])
            self.number("*")
        except:
            pass

    def button_div(self):
        exist_text = self.lineEdit.text()
        try:
            if((exist_text[-1] == "+")| (exist_text[-1] == "-")|(exist_text[-1] == "*")|(exist_text[-1] == "/")):
                self.lineEdit.setText(exist_text[:-1])
            self.number("/")
        except:
            pass
             
        
    def result(self):
        exist_text = self.lineEdit.text()
        self.number("=")
        try:
            ans = eval(exist_text)
            self.lineEdit.setText(str(ans))
        except Exception as e:
            print(e)

    def clear(self):
        self.lineEdit.setText("")

    def repeat_press(self):
        self.h1 = Thread1(self)
        self.h1.start()

    def StopPress(self):
        self.h1.stop()
        


    
 
    
    
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Cal()
    sys.exit(app.exec())