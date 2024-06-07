def calcular_pago_laboral(dias_trabajados):
    valor_dia_trabajo = 136000
    pago_emplead = dias_trabajad * valor_dia_trabajo
    incentivo = 0

    # Verificar bono por salario mayor o igual a $1.088.000

    if pago_emplead >= 1088000:
       incentivo += 60000

    # Verificar bono por días laborados mayores a 15

    if dias_trabajad > 15:
        incentivo += 0.10 * pago_empleado

    # Verificar bono por mes laborado completo (asumimos que el mes completo es 30 días)

    if dias_trabajad == 30:
       incentivo += 0.20 * pago_empleado

    pago_empleado = pago_empleado + incentivo
    return pago_empleado, incentivo, pago_empleado

# Ejemplo de uso:

dias_trabajad = int(input("Ingrese la cantidad de días laborados:\n "))
pago_empleado,incentivo, salario_total = calcular_pago_laboral(dias_trabajad)

print(f"Salario: ${pago_empleado:f}")
print(f"incentivo de 10% o 20%: ${incentivo:f}")
print(f"pago total dias trabajados: ${pago_empleado:f}")