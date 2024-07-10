var_nombre = input("¿Cúal es tu nombre? -> ")
var_ventas = float(input("¿Tu cantidad de ventas? -> "))

var_comisión = 0.13*var_ventas

var_pago = round(var_comisión, 2)

print(f"Ok {var_nombre}. este mes ganaste {var_pago}")