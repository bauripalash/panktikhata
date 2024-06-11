from PySide6.QtWidgets import QApplication
from ui.mainwin import Ui_MainWindow


def main():
    app = QApplication()
    win = Ui_MainWindow()
    win.show()
    app.exec()


if __name__ == "__main__":
    main()
