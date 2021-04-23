from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Проста програма")
        self.setGeometry(300, 250, 500, 200)

        self.new_text = QtWidgets.QLabel(self)


        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(70, 150)
        self.btn.setText("Нажми на мене")
        self.btn.setFixedWidth(200)
        
        self.btn.clicked.connect(self.add_label)

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("стандарт segzgshsthzdrg srsrs hsrhs rthtrh ")
        self.main_text.move(100, 100)
        self.main_text.adjustSize() # підлаштує ширину тексту до самого обєкта 


    def add_label(self):
        self.new_text.setText('Наступний текст') # при нажаті кнопки btn виводиться напис
        self.new_text.move(100, 50)
        self.new_text.adjustSize()

        print(sys.argv)

def application():
    app = QApplication(sys.argv)
    window = Window()

    
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()