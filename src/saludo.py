from datetime import datetime
hora_actual = datetime.now().hour
nombre=input("Introduce tu nombre")
if hora_actual<12:
    print(f"Buenos días{nombre}")
elif 12<= hora_actual <=20:
    print(f"Buenas trades {nombre}")
else:
    print(f"Buenas noches {nombre}")