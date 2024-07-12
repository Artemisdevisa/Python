def prueba(num1, num2, *args, **kwargs):
    print(f"El primera valor es {num1}")
    print(f"El segundo valor es {num2}")

    for arg in args:
        print(f"arg = {arg}")

    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")

args = [100, 200, 300, 400]
kwards = {'x':'uno', 'y':'dos', 'z':'tres'}
prueba(15, 50, *args, **kwards)