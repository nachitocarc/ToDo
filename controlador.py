from PySide6.QtWidgets import QWidget, QMessageBox
from vista import UiListaDeTareas
from modelo import GestorDeTareas


class ListaDeTareasApp(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = UiListaDeTareas()
        self.ui.ventana_ui(self)

        self.gestor_tareas = GestorDeTareas()

        self.ui.boton_agregar.clicked.connect(self.__agregar_tarea)
        self.ui.boton_eliminar.clicked.connect(self.__eliminar_tarea)
        self.ui.boton_completar.clicked.connect(self.__marcar_completada)

    def __agregar_tarea(self):
        tarea_nombre = self.ui.obtener_texto_tarea()
        if tarea_nombre:
            self.gestor_tareas.agregar_tarea(tarea_nombre)
            self.ui.agregar_tarea_a_lista(tarea_nombre)
            self.ui.limpiar_entrada()
        else:
            QMessageBox.warning(self, "Advertencia", "Ingresa una tarea.")

    def __eliminar_tarea(self):
        tareas_seleccionadas = self.ui.obtener_tarea_seleccionada()
        if not tareas_seleccionadas:
            QMessageBox.warning(self, "Advertencia", "Selecciona una tarea si queres eliminar")
            return

        for tarea_nombre in tareas_seleccionadas:
            self.gestor_tareas.eliminar_tarea(tarea_nombre)
        self.ui.eliminar_tarea_seleccionada()

    def __marcar_completada(self):
        tareas_seleccionadas = self.ui.obtener_tarea_seleccionada()
        if not tareas_seleccionadas:
            QMessageBox.warning(self, "Advertencia", "Selecciona una tarea para marcar como completada.")
            return

        for tarea_nombre in tareas_seleccionadas:
            self.ui.marcar_tarea_completada(tarea_nombre)
            self.gestor_tareas.marcar_completada(tarea_nombre)

