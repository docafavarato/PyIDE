from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
import sys
import contextlib
from io import StringIO
import os

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('main.ui', self)
        self.UiStyleSheet()
        self.show()

        self.runButton.clicked.connect(self.execute)
        self.clearButton.clicked.connect(self.clear)
        self.saveButton.clicked.connect(self.save)
        
    def execute(self):
        commandText = self.commandEdit.toPlainText()
        output = StringIO()

        with contextlib.redirect_stdout(output):
            try:
                exec(commandText)
            except Exception as e:
                print(e)

        final = output.getvalue()
        self.resultText.setText(final)

    def clear(self):
        self.commandEdit.clear()
        self.resultText.clear()

    def save(self):
        folder = str(QFileDialog.getExistingDirectory(self, "Select a folder"))
        output = self.commandEdit.toPlainText()

        if not folder:
            folder = os.getcwd()
        else:
            os.chdir(folder)

        with open(f"{folder}/output.py", "w") as f:
            f.write(output)

    def UiStyleSheet(self):
        buttons = [self.runButton, self.clearButton, self.saveButton]
        for button in buttons:
            button.setStyleSheet(
                                "QPushButton" "{"
                                    "border-radius: 6px;"
                                    "color: white;"
                                    "border: none;"
                                "}"
                                "QPushButton::hover" "{"
                                    "background-color: rgb(40, 46, 52);"
                                "}"
                                )

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()