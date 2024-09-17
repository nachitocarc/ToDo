class Tarea:
    def __init__(self, nombre):
        self.nombre = nombre
        self.completada = False

    def marcar_completada(self):
        self.completada = True

class GestorDeTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, nombre):
        tarea = Tarea(nombre)
        self.tareas.append(tarea)

    def eliminar_tarea(self, nombre):
        tarea = next((t for t in self.tareas if t.nombre == nombre), None)
        if tarea:
            self.tareas.remove(tarea)

    def obtener_tareas(self):
        return self.tareas