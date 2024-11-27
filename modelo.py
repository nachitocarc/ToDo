class Tarea:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__completada = False

    def marcar_completada(self):
        self.__completada = True

    def obtener_nombre(self):
        return self.__nombre


class GestorDeTareas:
    def __init__(self):
        self.__tareas = []

    def agregar_tarea(self, nombre):
        tarea = Tarea(nombre)
        self.__tareas.append(tarea)

    def eliminar_tarea(self, nombre):
        tarea = next((t for t in self.__tareas if t.obtener_nombre() == nombre), None)
        if tarea:
            self.__tareas.remove(tarea)

    def obtener_tareas(self):
        return self.__tareas

    def marcar_completada(self, nombre):
        tarea = next((t for t in self.__tareas if t.obtener_nombre() == nombre), None)
        if tarea:
            tarea.marcar_completada()
