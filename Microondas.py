class Microondas:
    def __init__(self):
        self.estado = "APAGADO"

    def abrir_puerta(self):
        if self.estado != "COCINANDO":
            self.estado = "PUERTA_ABIERTA"
        print("Estado:", self.estado)

    def cerrar_puerta(self):
        if self.estado == "PUERTA_ABIERTA":
            self.estado = "LISTO"
        print("Estado:", self.estado)

    def iniciar(self):
        if self.estado == "LISTO":
            self.estado = "COCINANDO"
        print("Estado:", self.estado)

    def pausar(self):
        if self.estado == "COCINANDO":
            self.estado = "PAUSADO"
        print("Estado:", self.estado)

    def terminar(self):
        if self.estado in ["COCINANDO", "PAUSADO"]:
            self.estado = "LISTO"
        print("Estado:", self.estado)


# Prueba del autómata
m = Microondas()
m.abrir_puerta()
m.cerrar_puerta()
m.iniciar()
m.pausar()
m.terminar()
