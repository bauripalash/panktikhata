import sys
from PySide6.QtWidgets import QApplication, QStyleFactory
from ui.mainwin import Ui_MainWindow


def main():
    app = QApplication()
    app.setStyle(QStyleFactory.create("Fusion"))
    win = Ui_MainWindow()
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
