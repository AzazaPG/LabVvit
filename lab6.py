import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit, QMessageBox


class Calculator(QWidget):
#
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Калькулятор')
        self.setGeometry(100, 100, 250, 250)
        self.setStyleSheet('font-size: 20px;')
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.create_display()
        self.create_buttons()
        self.show()

    def create_display(self):
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.grid.addWidget(self.display, 0, 0, 1, 4)

    def create_buttons(self):
        self.add_button('7', 1, 0)
        self.add_button('8', 1, 1)
        self.add_button('9', 1, 2)
        self.add_button('/', 1, 3)

        self.add_button('4', 2, 0)
        self.add_button('5', 2, 1)
        self.add_button('6', 2, 2)
        self.add_button('*', 2, 3)

        self.add_button('1', 3, 0)
        self.add_button('2', 3, 1)
        self.add_button('3', 3, 2)
        self.add_button('-', 3, 3)

        self.add_button('.', 4, 0)
        self.add_button('0', 4, 1)
        self.add_button('=', 4, 2)
        self.add_button('+', 4, 3)

        self.add_button('C', 5, 0, 1, 4)

    def add_button(self, label, row, col, rowspan=1, colspan=1):
        button = QPushButton(label)
        button.clicked.connect(lambda: self.button_click(label))
        self.grid.addWidget(button, row, col, rowspan, colspan)

    def button_click(self, label):
        if label == 'C':
            self.display.setText('')
        elif label == '=':
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except ZeroDivisionError:
                QMessageBox.warning(self, 'Ошибка', 'Деление на ноль невозможно')
                self.display.setText('')
            except Exception as e:
                QMessageBox.warning(self, 'Ошибка', str(e))
                self.display.setText('')
        else:
            self.display.setText(self.display.text() + label)

    def keyPressEvent(self, event):
        key = event.text()
        if key in '0123456789+-*/.':
            self.button_click(key)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    sys.exit(app.exec_())