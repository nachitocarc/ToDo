import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *

class Ui_Lista_de_tareas(object):
    def VentanaUi(self, Lista_de_tareas):
        Lista_de_tareas.setStyleSheet("""
            background-color: #2b2b2b;
            color: #ffffff;
            border-color: #444444;
        """)
        if not Lista_de_tareas.objectName():
            Lista_de_tareas.setObjectName(u"Lista_de_tareas")
        Lista_de_tareas.resize(614, 331)
        self.gridLayout = QGridLayout(Lista_de_tareas)
        self.gridLayout.setObjectName(u"gridLayout")

        self.Boton_Eliminar = QPushButton(Lista_de_tareas)
        self.Boton_Eliminar.setObjectName(u"Boton_Eliminar")
        self.Boton_Eliminar.setStyleSheet("color: #ffffff;")
        self.gridLayout.addWidget(self.Boton_Eliminar, 3, 2, 1, 2)

        self.label = QLabel(Lista_de_tareas)
        self.label.setObjectName(u"label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label.setStyleSheet("border-color: #444444;")

        self.lineEdit = QLineEdit(Lista_de_tareas)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setPlaceholderText("Escriba su tarea...")
        self.lineEdit.setStyleSheet("background-color: #444444; color: #ffffff;")
        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.Boton_Agregar = QPushButton(Lista_de_tareas)
        self.Boton_Agregar.setObjectName(u"Boton_Agregar")
        self.Boton_Agregar.setStyleSheet("color: #ffffff;")
        self.gridLayout.addWidget(self.Boton_Agregar, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(50, 50, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(self.horizontalSpacer, 3, 0, 1, 1)

        self.pushButton = QPushButton(Lista_de_tareas)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet("color: #ffffff;")
        self.gridLayout.addWidget(self.pushButton, 3, 1, 1, 1)

        self.listWidget = QListWidget(Lista_de_tareas)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setStyleSheet("background-color: #333333; color: #ffffff;")
        self.gridLayout.addWidget(self.listWidget, 2, 0, 1, 3)

        self.Interfaz(Lista_de_tareas)
        QMetaObject.connectSlotsByName(Lista_de_tareas)

    def Interfaz(self, Lista_de_tareas):
        Lista_de_tareas.setWindowTitle(QCoreApplication.translate("Lista_de_tareas", u"Lista de Tareas", None))
        self.Boton_Eliminar.setText(QCoreApplication.translate("Lista_de_tareas", u"Eliminar", None))
        self.label.setText(QCoreApplication.translate("Lista_de_tareas", u"Lista de tareas", None))
        self.Boton_Agregar.setText(QCoreApplication.translate("Lista_de_tareas", u"Agregar tarea", None))
        self.pushButton.setText(QCoreApplication.translate("Lista_de_tareas", u"Completada", None))

class ListaDeTareasApp(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Lista_de_tareas()
        self.ui.VentanaUi(self)

        self.ui.Boton_Agregar.clicked.connect(self.agregar_tarea)
        self.ui.Boton_Eliminar.clicked.connect(self.eliminar_tarea)
        self.ui.pushButton.clicked.connect(self.marcar_completada)

    def agregar_tarea(self):
        tarea = self.ui.lineEdit.text()
        if tarea:
            self.ui.listWidget.addItem(tarea)
            self.ui.lineEdit.clear()
        else:
            QMessageBox.warning(self, "Advertencia", "Ingresa una tarea.")

    def eliminar_tarea(self):
        for item in self.ui.listWidget.selectedItems():
            self.ui.listWidget.takeItem(self.ui.listWidget.row(item))

    def marcar_completada(self):
        for item in self.ui.listWidget.selectedItems():
            font = item.font()
            font.setStrikeOut(True)
            item.setFont(font)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ListaDeTareasApp()
    window.show()
    sys.exit(app.exec())