import sys
import matplotlib
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QPushButton, QMessageBox, QLineEdit
from PyQt5.QtGui import QIcon

def dialog():
  print(btn1.text)


if __name__ == "__main__":
  app = QApplication(sys.argv)
  calc = QMainWindow()
  calc.resize(1000,800)
  calc.setWindowTitle("Xalculator")
  calc.setWindowIcon(QIcon("keys.png"))

  ID = QLineEdit(calc)
  ID.move(180,10)
  ID.resize(800, 80)
  ID.show

  btnclr = QPushButton(calc)
  btnclr.setText('clr')
  btnclr.show()
  btnclr.resize(80,80)
  btnclr.move(20,120)
  btnclr.clicked.connect(dialog)

  btndel = QPushButton(calc)
  btndel.setText('del')
  btndel.show()
  btndel.resize(80,80)
  btndel.move(120,120)
  btndel.clicked.connect(dialog)

  btn0 = QPushButton(calc)
  btn0.setText('0')
  btn0.show()
  btn0.resize(80,80)
  btn0.move(20,220)
  btn0.clicked.connect(dialog)

  btn1 = QPushButton(calc)
  btn1.setText('1')
  btn1.show()
  btn1.resize(30,30)
  btn1.move(110,150)
  btn1.clicked.connect(dialog)

  btn2 = QPushButton(calc)
  btn2.setText('2')
  btn2.show()
  btn2.resize(30,30)
  btn2.move(110,150)
  btn2.clicked.connect(dialog)

  btn3 = QPushButton(calc)
  btn3.setText('3')
  btn3.show()
  btn3.resize(30,30)
  btn3.move(110,150)
  btn3.clicked.connect(dialog)

  btn4 = QPushButton(calc)
  btn4.setText('4')
  btn4.resize(30,30)
  btn4.move(110,150)
  btn4.show()
  btn4.clicked.connect(dialog)

  btn5 = QPushButton(calc)
  btn5.setText('5')
  btn5.show()
  btn5.resize(30,30)
  btn5.move(110,150)
  btn5.clicked.connect(dialog)

  btn6 = QPushButton(calc)
  btn6.setText('6')
  btn6.show()
  btn6.resize(30,30)
  btn6.move(110,150)
  btn6.clicked.connect(dialog)

  btn7 = QPushButton(calc)
  btn7.setText('7')
  btn7.show()
  btn7.resize(30,30)
  btn1.move(110,150)
  btn1.clicked.connect(dialog)

  btn8 = QPushButton(calc)
  btn8.setText('8')
  btn8.show()
  btn8.resize(30,30)
  btn8.move(110,150)
  btn8.clicked.connect(dialog)

  btn9 = QPushButton(calc)
  btn9.setText('9')
  btn9.show()
  btn9.resize(30,30)
  btn9.move(110,150)
  btn9.clicked.connect(dialog)

  btn_plus = QPushButton(calc)
  btn_plus.setText('+')
  btn_plus.show()
  btn_plus.resize(30,30)
  btn_plus.move(110,150)
  btn_plus.clicked.connect(dialog)

  btn_minus = QPushButton(calc)
  btn_minus.setText('-')
  btn_minus.show()
  btn_minus.resize(30,30)
  btn_minus.move(110,150)
  btn_minus.clicked.connect(dialog)

  btn_mult = QPushButton(calc)
  btn_mult.setText('×')
  btn_mult.show()
  btn_mult.resize(30,30)
  btn_mult.move(110,150)
  btn_mult.clicked.connect(dialog)

  btn_div = QPushButton(calc)
  btn_div.setText('/')
  btn_div.show()
  btn_div.resize(30,30)
  btn_div.move(110,150)
  btn_div.clicked.connect(dialog)

  calc.show()
  sys.exit(app.exec_())