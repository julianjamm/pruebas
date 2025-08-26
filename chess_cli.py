from datetime import datetime

print("="*70)
print("              MI EMPRESA .       FACTURA DE COMPRA")
print("="*70)
cliente = "Julian Monroy"   # Nombre del cliente
fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
print(f"Cliente: {cliente}")
print(f"Fecha:   {fecha}")
print("NIT: XXXXXX")
print("="*70)

# Listas con datos
productos = [
    "Mouse gamer",
    "Inter Core i9 Ultra",
    "Teclado mecánico",
    "Auriculares gamer",
    "Micrófono",
    "Luces LED 100m",
    "100 TB almacenamiento",
    "Pantalla 1000hz",
    "1 TB RAM",
    "RTX 1090"
]

cantidades = [1, 1, 1, 2, 1, 1, 1, 2, 1, 1]

# Precios sugeridos (unitarios)
precios = [
    150000,     # Mouse gamer
    5000000,    # Inter Core i9 Ultra
    400000,     # Teclado mecánico
    300000,     # Auriculares gamer
    200000,     # Micrófono
    50000,      # Luces LED 100m
    10000000,   # 100 TB almacenamiento
    2000000,    # Pantalla 1000hz
    800000,     # 1 TB RAM
    3000000     # RTX 1090
]

# IVA por producto (19%)
ivas = []
subtotales = []
totales = []

# Calcular IVA, subtotal y total por producto
for i in range(len(productos)):
    subtotal = cantidades[i] * precios[i]
    iva = precios[i] * 0.19
    total = subtotal + (iva * cantidades[i])

    subtotales.append(subtotal)
    ivas.append(iva)
    totales.append(total)

# Mostrar factura
print("{:<20} {:<10} {:<15} {:<15} {:<15}".format("Producto", "Cantidad", "Precio", "IVA", "Total"))
print("-"*70)

total_general = 0
for i in range(len(productos)):
    print("{:<20} {:<10} {:<15} {:<15} {:<15}".format(
        productos[i][:20], 
        cantidades[i],
        f"{precios[i]:,}".replace(",", "."),
        f"{ivas[i]:,.0f}".replace(",", "."),
        f"{totales[i]:,.0f}".replace(",", ".")
    ))
    total_general += totales[i]

print("-"*70)
print(f"{'TOTAL A PAGAR':<60} ${total_general:,.0f}".replace(",", "."))
print("="*70)
print("¡Gracias por su compra!")
