class Microondas:
    def __init__(self):
        self.estado = "APAGADO"

    def mostrar_estado(self):
        print("\nEstado actual:", self.estado)

    def procesar_evento(self, evento):
        if self.estado == "APAGADO":
            if evento == "abrir":
                self.estado = "PUERTA_ABIERTA"

        elif self.estado == "PUERTA_ABIERTA":
            if evento == "cerrar":
                self.estado = "LISTO"

        elif self.estado == "LISTO":
            if evento == "iniciar":
                self.estado = "COCINANDO"
            elif evento == "abrir":
                self.estado = "PUERTA_ABIERTA"

        elif self.estado == "COCINANDO":
            if evento == "pausar":
                self.estado = "PAUSADO"
            elif evento == "terminar":
                self.estado = "LISTO"

        elif self.estado == "PAUSADO":
            if evento == "terminar":
                self.estado = "LISTO"


# 🔥 IMPORTANTE: este while es lo que hace que funcione
m = Microondas()

while True:
    m.mostrar_estado()
    print("Eventos: abrir, cerrar, iniciar, pausar, terminar, salir")
    evento = input("Ingresa evento: ").lower()

    if evento == "salir":
        print("Programa terminado")
        break

    m.procesar_evento(evento)
