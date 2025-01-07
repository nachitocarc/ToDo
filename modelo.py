class Tarea:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__completada = False

    def marcar_completada(self):
        self.__completada = True

    def obtener_nombre(self):
        return self.__nombre

    def esta_completada(self):
        return self.__completada


class GestorDeTareas:
    def __init__(self):
        self.__tareas = []

    def agregar_tarea(self, nombre):
        nueva_tarea = Tarea(nombre)
        self.__tareas.append(nueva_tarea)

    def eliminar_tarea(self, nombre):
        self.__tareas = [tarea for tarea in self.__tareas if tarea.obtener_nombre() != nombre]

    def marcar_completada(self, nombre):
        for tarea in self.__tareas:
            if tarea.obtener_nombre() == nombre:
                tarea.marcar_completada()
                break

    def obtener_tareas(self):
        return [
            {"nombre": tarea.obtener_nombre(), "completada": tarea.esta_completada()}
            for tarea in self.__tareas]
