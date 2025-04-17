num1 = int(input("primer número: "))
num2 = int(input("segundo número: "))
num3 = int(input("tercer número: "))

if num1 == num2 == num3:
    print("los números son iguales.")
else:
    nummayor = max(num1, num2, num3)
    print(f"El número mayor es: {nummayor}")