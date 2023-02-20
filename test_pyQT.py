from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Простая програма")
        self.setGeometry(int(250), int(250), 350, 200)
        
        self.new_text = QtWidgets.QLabel(self)

        self.main_text = QtWidgets.QLabel(self) # Создание объекта и вывод его на окно Window
        self.main_text.setText("Это базовая надпись") # Задание надписи для объекта
        self.main_text.move(100, 100) # изменить положение текста относительно окна
        self.main_text.adjustSize() # Динамически миняет размер объекта под размер текста

        self.btn = QtWidgets.QPushButton(self) # Добавить кнопку в окно Window
        self.btn.move(70, 150) # Изменить ее положение относительно окна
        self.btn.setText("Нажми на меня!") # Надпись на кнопке
        self.btn.setFixedWidth(200) # Установить фиксированную: weight - ширина, height - высота.
        self.btn.clicked.connect(self.get_click)

    def     get_click(self):
        self.new_text.setText("Вторая надпись")
        self.new_text.move(100, 50)
        self.new_text.adjustSize()

def     app(): # функция, которая запускает окно
    app = QApplication(sys.argv)  
    window = Window() # открытие окна
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    app()