from datetime import datetime

print("="*70)
print("              MI EMPRESA .       FACTURA DE COMPRA")
print("="*70)
cliente = input("Ingrese el nombre del cliente: ")
fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
print(f"Cliente: {cliente}")
print(f"Fecha:   {fecha}")
print("NIT: XXXXXX")
print("="*70)

productos = []   #listas
cantidades = []
precios = []
ivas = []
totales = []

# Ingreso de productos
while True:
    producto = input("\nIngrese el nombre del producto (o 'fin' para terminar): ")
    if producto.lower() == "fin":
        break
    cantidad = int(input("Ingrese la cantidad: "))
    precio = float(input("Ingrese el precio unitario: "))

    subtotal = cantidad * precio
    iva = subtotal * 0.19
    total = subtotal + iva

    productos.append(producto) #append agrega
    cantidades.append(cantidad)
    precios.append(precio)
    ivas.append(iva)
    totales.append(total)

# esta parte me muestra la factura
print("\n" + "="*70)
print("{:<20} {:<10} {:<15} {:<15} {:<15}".format("Producto", "Cantidad", "Precio", "IVA", "Total"))
print("-"*70)

total_general = 0
for i in range(len(productos)):
    print("{:<20} {:<10} {:<15} {:<15} {:<15}".format(
        productos[i][:20],
        cantidades[i],
        f"{precios[i]:,.0f}".replace(",", "."),
        f"{ivas[i]:,.0f}".replace(",", "."),
        f"{totales[i]:,.0f}".replace(",", ".")
    ))
    total_general += totales[i]

print("-"*70)
print(f"{'TOTAL A PAGAR':<60} ${total_general:,.0f}".replace(",", "."))
print("="*70)
print("¡Gracias por su compra!")
