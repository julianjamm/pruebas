factura = [
    "empresa: Mi Empresa",
    "NIT: XXXXXX",
    "Producto: Mouse gamer",
    "inter core i9 ultra",
    "teclado mecanico",
    "auriculares gamer",
    "microfono",
    "luces led 100m",
    "100 teras de almacenamiento",
    "pantalla 1000hz",
    "1 tera de ram",
    "RTX1090",
    "Precio: 20000000",
    "IVA: 19%",
    "Total: 23800000"
]
print("-" * 33)
print("|      FACTURA DE VENTA         |")
print("-" * 33)

for i, listas in enumerate(factura):
    print("| ", i,":", listas)


print("-" * 33)
print("|    Gracias por su compra       |")
print("-" * 33)
