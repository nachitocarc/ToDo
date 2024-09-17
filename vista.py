# vista.py
from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QGridLayout, QPushButton, QLabel, QLineEdit, QListWidget, QSpacerItem, QSizePolicy

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

        self._grid_layout = QGridLayout(lista_de_tareas)
        self._grid_layout.setObjectName(u"grid_layout")

        self._boton_eliminar = QPushButton(lista_de_tareas)
        self._boton_eliminar.setObjectName(u"boton_eliminar")
        self._boton_eliminar.setStyleSheet("color: #ffffff;")
        self._grid_layout.addWidget(self._boton_eliminar, 3, 2, 1, 2)

        self._label = QLabel(lista_de_tareas)
        self._label.setObjectName(u"label")
        self._grid_layout.addWidget(self._label, 1, 0, 1, 1)
        self._label.setStyleSheet("border-color: #444444;")

        self._line_edit = QLineEdit(lista_de_tareas)
        self._line_edit.setObjectName(u"line_edit")
        self._line_edit.setPlaceholderText("Escriba su tarea...")
        self._line_edit.setStyleSheet("background-color: #444444; color: #ffffff;")
        self._grid_layout.addWidget(self._line_edit, 1, 1, 1, 1)

        self._boton_agregar = QPushButton(lista_de_tareas)
        self._boton_agregar.setObjectName(u"boton_agregar")
        self._boton_agregar.setStyleSheet("color: #ffffff;")
        self._grid_layout.addWidget(self._boton_agregar, 1, 2, 1, 1)

        self._horizontal_spacer = QSpacerItem(50, 50, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self._grid_layout.addItem(self._horizontal_spacer, 3, 0, 1, 1)

        self._boton_completar = QPushButton(lista_de_tareas)
        self._boton_completar.setObjectName(u"boton_completar")
        self._boton_completar.setStyleSheet("color: #ffffff;")
        self._grid_layout.addWidget(self._boton_completar, 3, 1, 1, 1)

        self._list_widget = QListWidget(lista_de_tareas)
        self._list_widget.setObjectName(u"list_widget")
        self._list_widget.setStyleSheet("background-color: #333333; color: #ffffff;")
        self._grid_layout.addWidget(self._list_widget, 2, 0, 1, 3)

        self.interfaz(lista_de_tareas)

    def interfaz(self, lista_de_tareas):
        lista_de_tareas.setWindowTitle(QCoreApplication.translate("lista_de_tareas", u"Lista de Tareas", None))
        self._boton_eliminar.setText(QCoreApplication.translate("lista_de_tareas", u"Eliminar", None))
        self._label.setText(QCoreApplication.translate("lista_de_tareas", u"Lista de tareas", None))
        self._boton_agregar.setText(QCoreApplication.translate("lista_de_tareas", u"Agregar tarea", None))
        self._boton_completar.setText(QCoreApplication.translate("lista_de_tareas", u"Completada", None))
