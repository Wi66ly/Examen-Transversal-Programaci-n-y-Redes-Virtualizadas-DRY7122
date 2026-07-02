#script:verificar_vlan.py

print("====================================")
print("     VERIFICADOR DE RANGOS VLAN     ")
print("====================================")

try:
    # Solicita al usuario ingresar el número de VLAN
    vlan_input = input("Por favor, ingrese el número de VLAN: ")
    vlan = int(vlan_input)

    # Validación de los rangos
    if 1 <= vlan <= 1005:
        print(f"-> La VLAN {vlan} corresponde al RANGO NORMAL.")
    elif 1006 <= vlan <= 4094:
        print(f"-> La VLAN {vlan} corresponde al RANGO EXTENDIDO.")
    elif vlan == 0 or vlan == 4095:
        print(f"-> La VLAN {vlan} es una VLAN RESERVADA y no se puede utilizar.")
    else:
        print("-> Error: El número ingresado está fuera del rango válido de VLANs (0 - 4095).")

except ValueError:
    print("-> Error: Por favor, ingrese un número entero válido.")
