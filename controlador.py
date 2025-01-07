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
        self.__actualizar_vista()

    def __actualizar_vista(self):
        tareas = self.gestor_tareas.obtener_tareas()
        self.ui.actualizar_lista_tareas(tareas)

    def __agregar_tarea(self):
        tarea_nombre = self.ui.obtener_texto_tarea()
        if tarea_nombre:
            self.gestor_tareas.agregar_tarea(tarea_nombre)
            self.__actualizar_vista()
            self.ui.limpiar_entrada()
        else:
            QMessageBox.warning(self, "Advertencia", "Ingresa una tarea.")

    def __eliminar_tarea(self):
        tareas_seleccionadas = self.ui.obtener_tareas_seleccionadas()
        if not tareas_seleccionadas:
            QMessageBox.warning(self, "Advertencia", "Selecciona una tarea para eliminar.")
            return

        for tarea_nombre in tareas_seleccionadas:
            self.gestor_tareas.eliminar_tarea(tarea_nombre)
        self.__actualizar_vista()

    def __marcar_completada(self):
        tareas_seleccionadas = self.ui.obtener_tareas_seleccionadas()
        if not tareas_seleccionadas:
            QMessageBox.warning(self, "Advertencia", "Selecciona una tarea para marcar como completada.")
            return

        for tarea_nombre in tareas_seleccionadas:
            self.gestor_tareas.marcar_completada(tarea_nombre)
        self.__actualizar_vista()
