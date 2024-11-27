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

        self.boton_eliminar = QPushButton("Eliminar", lista_de_tareas)
        self.boton_eliminar.setObjectName(u"boton_eliminar")
        self.boton_eliminar.setStyleSheet("color: #ffffff;")
        self._grid_layout.addWidget(self.boton_eliminar, 3, 2, 1, 2)

        self._label = QLabel("Lista de tareas", lista_de_tareas)
        self._label.setObjectName(u"label")
        self._grid_layout.addWidget(self._label, 1, 0, 1, 1)
        self._label.setStyleSheet("border-color: #444444;")

        self._line_edit = QLineEdit(lista_de_tareas)
        self._line_edit.setObjectName(u"line_edit")
        self._line_edit.setPlaceholderText("Escriba su tarea...")
        self._line_edit.setStyleSheet("background-color: #444444; color: #ffffff;")
        self._grid_layout.addWidget(self._line_edit, 1, 1, 1, 1)

        self.boton_agregar = QPushButton("Agregar tarea", lista_de_tareas)
        self.boton_agregar.setObjectName(u"boton_agregar")
        self.boton_agregar.setStyleSheet("color: #ffffff;")
        self._grid_layout.addWidget(self.boton_agregar, 1, 2, 1, 1)

        self._horizontal_spacer = QSpacerItem(50, 50, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self._grid_layout.addItem(self._horizontal_spacer, 3, 0, 1, 1)

        self.boton_completar = QPushButton("Completada", lista_de_tareas)
        self.boton_completar.setObjectName(u"boton_completar")
        self.boton_completar.setStyleSheet("color: #ffffff;")
        self._grid_layout.addWidget(self.boton_completar, 3, 1, 1, 1)

        self._list_widget = QListWidget(lista_de_tareas)
        self._list_widget.setObjectName(u"list_widget")
        self._list_widget.setStyleSheet("background-color: #333333; color: #ffffff;")
        self._grid_layout.addWidget(self._list_widget, 2, 0, 1, 3)

    # Métodos encapsulados para interactuar con la vista
    def obtener_texto_tarea(self):
        return self._line_edit.text()

    def limpiar_entrada(self):
        self._line_edit.clear()

    def agregar_tarea_a_lista(self, tarea):
        self._list_widget.addItem(tarea)

    def eliminar_tarea_seleccionada(self):
        for item in self._list_widget.selectedItems():
            self._list_widget.takeItem(self._list_widget.row(item))

    def obtener_tarea_seleccionada(self):
        return [item.text() for item in self._list_widget.selectedItems()]

    def marcar_tarea_completada(self, tarea):
        for index in range(self._list_widget.count()):
            item = self._list_widget.item(index)
            if item.text() == tarea:
                font = item.font()
                font.setStrikeOut(True)
                item.setFont(font)
