import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit

class SimpleCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Calculadora Simple")
        self.setGeometry(100, 100, 300, 400)

        # Crear el layout principal
        layout = QVBoxLayout()

        # Crear la pantalla de entrada
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setStyleSheet("font-size: 20px; padding: 10px;")
        layout.addWidget(self.display)

        # Crear los botones
        button_layout = QGridLayout()
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        row, col = 0, 0
        for button in buttons:
            btn = QPushButton(button)
            btn.setStyleSheet("font-size: 18px;")
            btn.clicked.connect(self.on_button_click)
            button_layout.addWidget(btn, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        layout.addLayout(button_layout)
        self.setLayout(layout)

    def on_button_click(self):
        sender = self.sender()
        text = sender.text()

        if text == "C":
            self.display.clear()
        elif text == "=":
            try:
                expression = self.display.text()
                result = eval(expression)  # Evalúa la expresión ingresada
                self.display.setText(str(result))
            except Exception as e:
                self.display.setText("Error")
        else:
            self.display.setText(self.display.text() + text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = SimpleCalculator()
    calculator.show()
    sys.exit(app.exec_())
