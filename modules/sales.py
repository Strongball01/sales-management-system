# modules/sales.py
# Manejo de ventas por sucursal y vendedor

sales = []  

def add_sale(branch, vendor, amount):
    """Agrega una venta a la lista"""
    sales.append({
        "branch": branch,
        "vendor": vendor,
        "amount": amount
    })
    print(f"Venta registrada: {vendor} - {branch} - ${amount}")

def show_sales():
    """Muestra todas las ventas registradas"""
    if not sales:
        print("No hay ventas registradas aún.")
        return

    print("\n=== Ventas Registradas ===")
    for sale in sales:
        print(f"Sucursal: {sale['branch']} | Vendedor: {sale['vendor']} | Monto: ${sale['amount']}")

def sales_by_branch(branch_name):
    """Filtra ventas por sucursal"""
    branch_sales = [s for s in sales if s["branch"] == branch_name]
    total = sum(s["amount"] for s in branch_sales)
    print(f"\nVentas en sucursal {branch_name}: ${total}")
    return total
