# controlador.py
from PySide6.QtWidgets import QWidget, QMessageBox
from vista import UiListaDeTareas
from modelo import GestorDeTareas


class ListaDeTareasApp(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = UiListaDeTareas()
        self.ui.ventana_ui(self)

        self.gestor_tareas = GestorDeTareas()

        self.ui._boton_agregar.clicked.connect(self.agregar_tarea)
        self.ui._boton_eliminar.clicked.connect(self.eliminar_tarea)
        self.ui._boton_completar.clicked.connect(self.marcar_completada)

    def agregar_tarea(self):
        tarea_nombre = self.ui._line_edit.text()
        if tarea_nombre:
            self.gestor_tareas.agregar_tarea(tarea_nombre)
            self.ui._list_widget.addItem(tarea_nombre)
            self.ui._line_edit.clear()
        else:
            QMessageBox.warning(self, "Advertencia", "Ingresa una tarea.")

    def eliminar_tarea(self):
        selected_items = self.ui._list_widget.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Advertencia", "Selecciona una tarea si queres eliminar")
            return

        for item in selected_items:
            tarea_nombre = item.text()
            self.gestor_tareas.eliminar_tarea(tarea_nombre)
            self.ui._list_widget.takeItem(self.ui._list_widget.row(item))

    def marcar_completada(self):
        selected_items = self.ui._list_widget.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Advertencia", "Selecciona una tarea para marcar como completada.")
            return

        for item in selected_items:
            font = item.font()
            font.setStrikeOut(True)
            item.setFont(font)

            for tarea in self.gestor_tareas.obtener_tareas():
                if tarea.nombre == item.text():
                    tarea.marcar_completada()


