import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
from random import randint

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Угадай число")
        self.setGeometry(700, 400, 450, 200)

        self.label = QLabel(self)
        self.label.setText("Введите число от 1 до 100:")
        self.label.setGeometry(20, 20, 200, 30)

        self.input_line = QLineEdit(self)
        self.input_line.move(200, 20)

        self.button = QPushButton("Проверить", self)
        self.button.move(300, 20)
        self.button.clicked.connect(self.check_number)

        self.answer_label = QLabel(self)
        self.answer_label.move(130, 80)

        self.attempts_label = QLabel(self)
        self.attempts_label.move(30, 150)
        self.remaining_attempts = 5
        self.update_attempts_label()
        self.random_number = randint(1,100)

    def check_number(self):
        number = self.input_line.text()
        self.input_line.clear()
        if number == "":
            self.answer_label.setText("Введите число!")
            self.answer_label.adjustSize()
        elif 0 > int(number) or 100 < int(number):
            self.answer_label.setText("Число должно быть в пределах от 1 до 100!")
            self.answer_label.adjustSize()
        elif int(number) == self.random_number:
            self.answer_label.setText("Вы угадали!!!")
            self.answer_label.adjustSize()
            self.button.setEnabled(False)
        elif int(number) < self.random_number:
            self.answer_label.setText("Загаданное число больше этого.")
            self.answer_label.adjustSize()
            self.remaining_attempts -= 1
            self.update_attempts_label()
            if self.remaining_attempts == 0:
                self.answer_label.setText(f"Вы проиграли:( Загаданное число: {self.random_number}")
                self.answer_label.adjustSize()
                self.button.setEnabled(False)
        elif int(number) > self.random_number:
            self.answer_label.setText("Загаданное число меньше этого.")
            self.answer_label.adjustSize()
            self.remaining_attempts -= 1
            self.update_attempts_label()
            if self.remaining_attempts == 0:
                self.answer_label.setText(f"Вы проиграли:( Загаданное число: {self.random_number}")
                self.answer_label.adjustSize()
                self.button.setEnabled(False)


    def update_attempts_label(self):
        self.attempts_label.setText(f"Осталось попыток: {self.remaining_attempts}")
        self.attempts_label.adjustSize()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = MyWindow()
    game.show()
    sys.exit(app.exec())
    game.show
