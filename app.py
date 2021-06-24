"""
autor: 
fecha:
descripción: 
Lista de requerimientos
programa que toma la edad de una persona y decide si tiene más de 18 años y menos de 30 años e ingresa el pass correcto

"""
#*******  mensaje de bienvenida *******
print(" -- Bienvenido al programa de identificación X")

#*******  instrucciones al usuario ******
print("Ingresa tu edad")
edad = input()
edad = int(edad)

print("Ahora ingresa el password")
passw = input()
tamPassw = len(passw)
msj = ""
#*******  validar los datos  ************
if edad >= 18:
    if edad <= 30:
        if passw == "admin1234":
            if len(passw) <= 6:
                msj = "Acceso Permitido!"
            else:
                msj = "Acceso No Permitido por len()!"
        else:
            msj = "Acceso No Permitido por passw!"
else:
    msj = "Acceso No Permitido!"

if msj == "":
    pass

#********  presentar un resultado *******
print(msj)




