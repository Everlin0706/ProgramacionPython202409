#enviar mensaje a whatsApp
codigo_bloqueo="123456789"

codigo=input("ingrese su codigo de bloqueo de celular: ")
contacto1="Everlin Osorio"
contacto2="Camila"
contacto3="Najely"
contacto4="Matias"
if codigo_bloqueo.lower()==codigo.lower():
    print("Ingreso correctamente")
    app=input("Ingrese la app a revisar: ")
    print(f"el {app} abierto correctamente")
    contacto_enviar=input("Ingrese el contacto a chatear: ")
    contacto_confirmado=True
    mensaje=""
    if contacto_enviar.lower()==contacto1.lower():
        mensaje=input("Ingrese el mensaje: ")
    elif contacto_enviar.lower()==contacto2.lower():
        mensaje=input("Ingrese el mensaje: ")
    elif contacto_enviar.lower()==contacto3.lower():
        mensaje=input("Ingrese el mensaje: ")
    elif contacto_enviar.lower()==contacto4.lower():
        mensaje=input("Ingrese el mensaje: ")
    else:
        contacto_confirmado=False
        print("no tiene ese contacto")
    if contacto_confirmado:
        confirmacion=input("Desea enviar el mensaje: (si/no)")
        if 'SI'.upper() == confirmacion.upper():
             print(f"se envio el mensaje correctamente")
             print(f'{contacto_enviar} =>{mensaje}')
        else:
            print("Gracias")
else:
    print("El codigo es incorrecto")