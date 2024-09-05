import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *

class UiListaDeTareas(object):
    def ventana_ui(self, lista_de_tareas):
        lista_de_tareas.setStyleSheet("""
            background-color: #2b2b2b;
            color: #ffffff;
            border-color: #444444;
        """)
        if not lista_de_tareas.objectName():
            lista_de_tareas.setObjectName(u"lista_de_tareas")
        lista_de_tareas.resize(614, 331)
        self.gridLayout = QGridLayout(lista_de_tareas)
        self.gridLayout.setObjectName(u"gridLayout")

        self.boton_eliminar = QPushButton(lista_de_tareas)
        self.boton_eliminar.setObjectName(u"boton_eliminar")
        self.boton_eliminar.setStyleSheet("color: #ffffff;")
        self.gridLayout.addWidget(self.boton_eliminar, 3, 2, 1, 2)

        self.label = QLabel(lista_de_tareas)
        self.label.setObjectName(u"label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label.setStyleSheet("border-color: #444444;")

        self.lineEdit = QLineEdit(lista_de_tareas)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setPlaceholderText("Escriba su tarea...")
        self.lineEdit.setStyleSheet("background-color: #444444; color: #ffffff;")
        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.boton_agregar = QPushButton(lista_de_tareas)
        self.boton_agregar.setObjectName(u"boton_agregar")
        self.boton_agregar.setStyleSheet("color: #ffffff;")
        self.gridLayout.addWidget(self.boton_agregar, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(50, 50, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(self.horizontalSpacer, 3, 0, 1, 1)

        self.boton_completar = QPushButton(lista_de_tareas)
        self.boton_completar.setObjectName(u"boton_completar")
        self.boton_completar.setStyleSheet("color: #ffffff;")
        self.gridLayout.addWidget(self.boton_completar, 3, 1, 1, 1)

        self.listWidget = QListWidget(lista_de_tareas)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setStyleSheet("background-color: #333333; color: #ffffff;")
        self.gridLayout.addWidget(self.listWidget, 2, 0, 1, 3)

        self.interfaz(lista_de_tareas)

    def interfaz(self, lista_de_tareas):
        lista_de_tareas.setWindowTitle(QCoreApplication.translate("lista_de_tareas", u"Lista de Tareas", None))
        self.boton_eliminar.setText(QCoreApplication.translate("lista_de_tareas", u"Eliminar", None))
        self.label.setText(QCoreApplication.translate("lista_de_tareas", u"Lista de tareas", None))
        self.boton_agregar.setText(QCoreApplication.translate("lista_de_tareas", u"Agregar tarea", None))
        self.boton_completar.setText(QCoreApplication.translate("lista_de_tareas", u"Completada", None))

class ListaDeTareasApp(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = UiListaDeTareas()
        self.ui.ventana_ui(self)

        self.ui.boton_agregar.clicked.connect(self.agregar_tarea)
        self.ui.boton_eliminar.clicked.connect(self.eliminar_tarea)
        self.ui.boton_completar.clicked.connect(self.marcar_completada)

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