from claseMenu import Menu
from  claseFechaHora import FechaHora

def test():
    print('test')
    r1 = FechaHora(23, 2, 2051, 4, 10, 2)
    r1.Mostrar()
    r2 = FechaHora(23, 0, 2050, 5, 11, 28)
    r2.Mostrar()
    input()
if __name__ == '__main__':
    p = input('Desea ejecutar test: 1:si  2:no   :')
    if p =='1':
        test()
    print('Ingrese dos objetos tipo fecha para operar')

    print('1er fecha:')
    
    d = int(input("Ingrese Dia: "))

    mes = int(input("Ingrese Mes: "))

    a = int(input("Ingrese Año: "))

    h = int(input("Ingrese Hora: "))

    m = int(input("Ingrese Minutos: "))

    s = int(input("Ingrese Segundos: "))

    r1 = FechaHora(d,mes,a,h,m,s)

    print('2da fecha:')

    d = int(input("Ingrese Dia: "))

    mes = int(input("Ingrese Mes: "))

    a = int(input("Ingrese Año: "))

    h = int(input("Ingrese Hora: "))

    m = int(input("Ingrese Minutos: "))

    s = int(input("Ingrese Segundos: "))

    r2 = FechaHora(d, mes, a, h, m, s)

    menu = Menu()
    bandera = False
    while not bandera:
        print(
            "\n------------Menu------------\n1. Sumar dos fechas \n2. Restar dos fechas \n3. Distinguir entre dos fechas cual es mayor \n4. Salir")
        op = int(input('Ingrese una opcion: '))
        menu.opcion(op, r1, r2)
        if op == 4:
            bandera = True
