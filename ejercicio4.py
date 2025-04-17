monto_cuenta = float(input("Ingrese el monto total de la cuenta: "))
porcentaje_propina = float(input("Ingrese el porcentaje de propina que desea dejar: "))

propina = monto_cuenta * (porcentaje_propina / 100)
total = monto_cuenta + propina


print(f"La propina es: {propina}")
print(f"El total a pagar es: {total}")
