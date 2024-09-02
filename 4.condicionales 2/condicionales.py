'''Vamos a crear un app que nos va apreguntar la edad del usuario en el caso que 
el usario sea mayor de edad y cunete con licencia de consucir le va a mostra un mensaje
que le informe que puede conducir, en el caso que sea mayor de edad pero no tenga 
licencia que no puede conducir porque no tiene licencia y en el caso que sea
menor de edad le informará que no puede conducir por este motivo'''

edad = int(input("Ingrese su edad: "))


if edad >= 18:

    tiene_licencia = int(input("¿Tiene licencia de conducir? (1 para sí, 0 para no): "))

    if tiene_licencia == 1:
        print("Puede conducir")
    else:
        print("No puede conducir")
else:
    print("Eres menor de edad, no puedes conducir")
