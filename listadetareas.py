import sys
from PySide6.QtWidgets import QApplication
from controlador import ListaDeTareasApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ListaDeTareasApp()
    window.show()
    sys.exit(app.exec())
