import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
from random import randint

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Кубы")
        self.setGeometry(600, 300, 450, 400)

        self.label = QLabel(self)
        self.label.setText("Введите количество кубов:")
        self.label.setGeometry(20, 20, 200, 30)

        self.input_cnt_dice = QLineEdit(self)
        self.input_cnt_dice.move(230, 20)

        self.label = QLabel(self)
        self.label.setText("Введите количество бросков:")
        self.label.setGeometry(20, 80, 200, 30)

        self.input_cnt_toss = QLineEdit(self)
        self.input_cnt_toss.move(230, 80)

        self.button = QPushButton("Проверить", self)
        self.button.move(150, 150)
        self.button.clicked.connect(self.check_cnt)

        self.answer_label = QLabel(self)
        self.answer_label.move(150, 200)

    def check_cnt(self):
        cnt_dice = int(self.input_cnt_dice.text())
        self.input_cnt_dice.clear()
        cnt_toss = int(self.input_cnt_toss.text())
        self.input_cnt_toss.clear()
        result = []
        for i in range(cnt_toss):
            cnt = 0
            for j in range(cnt_dice):
                num = randint(1, 6)
                cnt += num
            result.append(cnt)
        probability_text = ""
        for i in range(cnt_dice, (cnt_dice * 6) + 1):
            cnt_result = result.count(i)
            ver = (cnt_result / cnt_toss) * 100
            probability_text += f"Вероятность выпадения {i}: {ver}%\n"
            self.answer_label.setText(probability_text)
            self.answer_label.adjustSize()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = MyWindow()
    game.show()
    sys.exit(app.exec())
    game.show


    # def on_clicked(self):
    #     cube = int(self.lineEdit_1.text())
    #     self.lineEdit_1.clear()
    #     throw = int(self.lineEdit_2.text())
    #     self.lineEdit_2.clear()
    #     sum = []
    #     for i in range(throw):
    #         count = 0
    #         for j in range(cube):
    #             num = randint(1, 6)
    #             count += num
    #         sum.append(count)
    #     for i in range(cube, (cube * 6) + 1):
    #         kol_sum = sum.count(i)
    #         ver = (kol_sum / throw) * 100
    #         self.textEdit.append(f"Вероятность выпадения {i}: {ver}%")