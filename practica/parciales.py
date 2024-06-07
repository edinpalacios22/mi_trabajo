def calcular_nota_final(nota1, nota2, nota3):
    primer_parcial = 0.25
    segundo_parcial = 0.25
    parcial_final = 0.55


    
    return nota1 * primer_parcial + nota2 * segundo_parcial + nota3 * parcial_final


def validar():
 while True:
    
    alumno = input("Ingrese su nombre por favor:\n")
    asignatura = input("Ingrese la asignatura por favor:\n")
    # cedula = input("Ingrese el numero de cedula por favor:\n")

  
    nota_1 = float(input("Ingrese su nota del primer parcial por favor:\n"))
    if nota_1 > 5.0:
        print("nota incorrecta. La nota debe ser menor o igual a 5.0")
        return

    nota_2 = float(input("Ingrese su nota del segundo parcial por favor:\n"))
    if nota_2 > 5.0:
        print("nota incorrecta. La nota debe ser menor o igual a 5.0")
        return

    nota_3 = float(input("Ingrese su nota del parcial final por favor:\n"))
    if nota_3 > 5.0:
        print("nota incorrecta. La nota debe ser menor o igual a 5.0")
        return

    nota_final = calcular_nota_final(nota_1, nota_2, nota_3)
    if nota_final > 5.0:
        print("nota incorrecta. La nota debe ser menor o igual a 5.0")
        return
    detener=int (input("desea cerrar 1: si 2: no"))
    if detener == 1:
    
        print("La nota final de %s en la asignatura %s es %.2f" % (alumno, asignatura, nota_final))
    break

validar()

