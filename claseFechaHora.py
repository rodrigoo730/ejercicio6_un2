
class FechaHora:
    __segundo=0
    __minuto=0
    __hora=0
    __dia = 0
    __mes=0
    __anio=0
    def __init__(self,dia=1,mes=1,anio=2020,hora=0,minuto=0,segundo=0):

        if self.validarDato(dia,mes,anio,hora,minuto,segundo): # si devuelve true se ejecuta
            self.__segundo = segundo
            self.__minuto = minuto
            self.__hora = hora
            self.__dia = dia
            self.__mes = mes
            self.__anio = anio
            print('Fecha valida')
        else:
            self.__anio = 2020
            self.__mes = 1
            self.__dia = 1
            print('Fecha invalida, devuelve valor por defecto')


    def validarDato(self,dia,mes,anio,hora,minuto,segundo):
        bandera = False
        if segundo in range(0,60):
            if minuto in range(0,60):
                if hora in range(0,24):
                    if anio > 0:
                        if mes in range(1,13):
                            if mes == 2:
                                bisiesto = self.anioBisiesto(anio)
                                if not bisiesto:
                                    if dia in range(1,29):
                                        bandera = True
                                elif dia in range(1,30):
                                    bandera = True
                            if mes in [1, 3, 5, 7, 8, 10, 12]:
                                if dia in range(1, 32):
                                    bandera = True
                            if mes in [4,6,9,11]:
                                if dia in range(1,31):
                                    bandera = True
        return bandera




    def ajustarFecha(self):
        bandera= False
        bandera = self.anioBisiesto(self.__anio)
        if self.__segundo >= 60:
            entero = self.__segundo // 60
            resto = self.__segundo % 60

            self.__minuto += entero
            self.__segundo = resto
        if self.__minuto >= 60:
            entero = self.__minuto // 60
            resto = self.__minuto % 60
            self.__hora += entero
            self.__minuto = resto
        if self.__hora >= 24:
            entero = self.__hora // 24
            resto = self.__hora % 24
            self.__dia += entero
            self.__hora = resto
        if self.__mes in [1,3,5,7,8,10,12]:
            if self.__dia > 31:
                self.__mes+=1
                self.__dia -= 31
        if self.__mes in [4,6,9,11]:
            if self.__dia > 30:
                self.__mes +=1
                self.__dia -=30

        if self.__mes == 2:
            if not bandera:
                if self.__dia > 28:
                    self.__mes +=1
                    self.__dia -=28
            elif self.__dia > 29:
                self.__mes += 1
                self.__dia -= 29

        if self.__mes > 12:
            entero = self.__mes // 12
            resto = self.__mes % 12
            self.__anio += entero
            self.__mes = resto


    def Mostrar(self):
        print('La hora es {}:{}:{} con fecha {}/{}/{} '.format(self.__hora,self.__minuto,self.__segundo,self.__dia,self.__mes,self.__anio))

    def PonerEnHora(self,hora=0,minuto=0,segundo=0):
        self.__hora = hora
        self.__minuto = minuto
        self.__segundo = segundo

    def anioBisiesto(self,anio):
        if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
            #print('Es año biciesto')
            return True

            #print('No es año biciesto')

    def AdelantarHora(self,hora=0,minuto=0,segundo=0):
        self.__hora += hora
        self.__minuto += minuto
        self.__segundo += segundo

    def getAnio(self):
        return self.__anio
    def getMes(self):
        return self.__mes
    def getDia(self):
        return self.__dia
    def getHora(self):
        return self.__hora
    def getMinuto(self):
        return self.__minuto
    def getSegundo(self):
        return self.__segundo

    def getDatos(self):
        return [self.__segundo,self.__minuto,self.__hora,self.__dia,self.__mes,self.__anio]

    def __add__(self, other):
        if type(other) == FechaHora:
            fecha = FechaHora(self.__dia,self.__mes,self.__anio,self.__hora,self.__minuto,self.__segundo)
            fecha.__anio += other.getAnio()
            fecha.__mes += other.getMes()
            fecha.__dia += other.getDia()
            fecha.__hora += other.getHora()
            fecha.__minuto += other.getMinuto()
            fecha.__segundo += other.getSegundo()
            fecha.ajustarFecha()
            return fecha
        else:
            print('Error de tipo de objeto')


    def __gt__(self, other):
        if type(other) == FechaHora:
            bandera = False
            if self.__anio > other.getAnio():
                bandera = True
            elif self.__anio < other.getAnio():
                bandera = False
            elif self.__mes > other.getMes():
                bandera = True
            elif self.__mes < other.getMes():
                bandera = False
            elif self.__dia > other.getDia():
                bandera = True
            elif self.__dia < other.getDia():
                bandera = False
            elif self.__hora > other.getHora():
                bandera = True
            elif self.__hora < other.getHora():
                bandera = False
            elif self.__minuto > other.getMinuto():
                bandera = True
            elif self.__minuto < other.getMinuto():
                bandera = False
            elif self.__segundo > other.getSegundo():
                bandera = True
            elif self.__segundo < other.getSegundo():
                bandera = False
            return bandera
        else:
            print('Error de tipo de objeto')


    def __sub__(self, other):
        if type(other) == FechaHora:

            mayor = self > other

            if mayor:
                fechamayor= FechaHora(self.__dia,self.__mes,self.__anio,self.__hora,self.__minuto,self.__segundo)
                fechamenor= FechaHora(other.getDia(),other.getMes(),other.getAnio(),other.getHora(),other.getMinuto(),other.getSegundo())
            else:
                fechamayor = FechaHora(other.getDia(),other.getMes(),other.getAnio(),other.getHora(),other.getMinuto(),other.getSegundo())
                fechamenor = FechaHora(self.__dia,self.__mes,self.__anio,self.__hora,self.__minuto,self.__segundo)

            resto_segundo = fechamayor.__segundo - fechamenor.__segundo
            #print('segundo {}'.format(resto_segundo))
            if resto_segundo < 0 :
                resto_segundo += 60
                fechamayor.__minuto -= 1
            fechamayor.__segundo = resto_segundo
            resto_minuto = fechamayor.__minuto - fechamenor.__minuto
            if resto_minuto < 0 :
                resto_minuto += 60
                fechamayor.__hora -= 1
            fechamayor.__minuto = resto_minuto
            resto_hora = fechamayor.__hora - fechamenor.__hora
            if resto_hora < 0:
                resto_hora += 24
                fechamayor.__dia -= 1
            fechamayor.__hora = resto_hora
            resto_dia = fechamayor.__dia - fechamenor.__dia
            #print('dia {} '.format(resto_dia))
            if resto_dia < 0:
                if fechamayor.__mes in [1,3,5,7,8,10,12]:
                    resto_dia +=31
                    fechamayor.__mes -= 1
                elif fechamayor.__mes in [4,6,9,11]:
                    resto_dia +=30
                    fechamayor.__mes -= 1
                elif fechamayor.__mes == 2:
                    bisiesto = fechamayor.anioBisiesto(fechamayor.__anio)
                    if not bisiesto:
                        resto_dia += 28

                    else:
                        resto_dia += 29
                    fechamayor.__mes -= 1
            fechamayor.__dia = resto_dia
            resto_mes = fechamayor.__mes - fechamenor.__mes
            if resto_mes < 0:
                resto_mes += 12
                fechamayor.__anio -= 1
            fechamayor.__mes = resto_mes
            fechamayor.__anio -= fechamenor.__anio
            segundos = fechamayor.PasarSegundos()
            return segundos
        else:
            print('Error de tipo de objeto')


    def PasarSegundos(self):
        segundos = 0
        segundos = self.__segundo + (self.__minuto * 60) + (self.__hora * 3600) + (self.__dia * 86400)
        self.__mes += 1
        if self.__mes == 2:
            bandera = self.anioBisiesto(self.__anio)
            if bandera:
                segundos += 29 * 86400
            else:
                segundos += 28 * 86400
        elif self.__mes == 3:
            segundos += 59 * 86400
        elif self.__mes == 4:
            segundos += 89 * 86400
        elif self.__mes == 5:
            segundos += 120 * 86400
        elif self.__mes == 6:
            segundos += 150 * 86400
        elif self.__mes == 7:
            segundos += 181 * 86400
        elif self.__mes == 8:
            segundos += 212 * 86400
        elif self.__mes == 9:
            segundos += 242 * 86400
        elif self.__mes == 10:
            segundos += 273 * 86400
        elif self.__mes == 11:
            segundos += 303 * 86400
        elif self.__mes == 12:
            segundos += 334 * 86400
        segundos += self.__anio * 365 * 86400
        return segundos









