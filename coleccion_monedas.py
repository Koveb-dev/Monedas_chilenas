import time
import os
# Comentario 1: Me falto agregar una opcion(simbolo) aparte para la moneda de 10 pesos ya que esta cuenta con 2 simbolos, no use el "angel libertad"
# Comentario 2: Por ultimo en los simbolos se puede ver que obligo de alguna forma al usuario a ingresar números para agregar las opciones de los simbolos según la moneda, no pude solucionar esa parte
# ya que no se como hacer para agregar de forma ordenada el indice correspondiente de la tupla el cual pertenece este. Por lo que se me facilito hacer que el usuario ingresara el numero del indice
# de la tupla(simbolos) donde se encontraba el valor del simbolo correspondiente.

print('Bienvenido a la App Colección De Monedas Chilenas!')
time.sleep(1)
os.system('cls')

tipos_monedas = ('Moneda de $1 peso', 'Moneda de $5 pesos',
                 'Moneda de $10 pesos', 'Moneda de $50 pesos', 'Moneda de $100 pesos', 'Moneda de $500')

simbolos = ('Angel libertad', 'Bernardo Ohiggins', 'Escudo Nacional',
            'Mapuche', 'Cardenal Raul Silva Henriquez')

monedas = []

while True:
    os.system('cls')
    print('App monedas chilenas\n\t 1. Agregar moneda\n\t 2. Ver monedas\n\t 3. Eliminar moneda\n\t 4. Salir')
    while True:
        try:
            opc = int(input('Ingrese una opción: '))
            if opc in (1, 2, 3, 4):
                break
            else:
                print(
                    'ERROR! debe ingresar una opcíón valida, opciones validas(1,2,3,4)!')
        except:
            print('ERROR! debe ingresar números enteros!')

    if opc == 1:
        print('Agregar moneda!')
        time.sleep(1)
        os.system('cls')
        while True:
            try:
                tipo = int(input(
                    'Ingrese el tipo de moneda(1: $1 peso, 2: $5 pesos, 3: $10 pesos, 4: $50 pesos, 5: $100 pesos, 6: $500 pesos ): '))
                if tipo in (1, 2, 3, 4, 5, 6):
                    print('Se registro el tipo de moneda de forma exitosa!')
                    time.sleep(1)
                    os.system('cls')
                    break
                else:
                    print(
                        'ERROR! debe ingresar un tipo de moneda valido, tipos(1,2,3,4,5,6)!')
                time.sleep(1)
                os.system('cls')
            except:
                print('ERROR! debe ingresar números enteros!')

        if tipo in (1, 2, 3, 4):
            while True:
                print('Monedas con el simbolo de Bernardo Ohiggins $1 $5 $10 $50 ')
                time.sleep(2)
                os.system('cls')
                try:
                    simbolo = int(
                        input('Ingrese simbolo de la moneda(1: Bernando Ohiggins): '))
                    if simbolo == 1:
                        print('Se registro el simbolo!')
                        time.sleep(1)
                        os.system('cls')
                        break
                    else:
                        print(
                            'ERROR! debe ingresar una opción valida, opcion valida(1)')
                    time.sleep(1)
                    os.system('cls')
                except:
                    print('ERROR! debe ingresar un número entero!')
        elif tipo == 5:
            while True:
                print(
                    'Monedas de $100 pesos!')
                time.sleep(1)
                os.system('cls')
                try:
                    simbolo = int(
                        input('Ingrese simbolo de la moneda $100 (2: $100 escudo nacional, 3: $100 mapuche): '))
                    if simbolo in (2, 3):
                        print('Se registro el simbolo!')
                        time.sleep(1)
                        os.system('cls')
                        break
                    else:
                        print(
                            'ERROR! debe ingresar una opción valida, opciones validas(2,3)!')
                    time.sleep(1)
                    os.system('cls')
                except:
                    print('ERROR! debe ingresar un número entero!')
        else:
            simbolo = 4
            break

        while True:
            print('Año moneda!')
            time.sleep(1)
            os.system('cls')
            try:
                año_mon = int(input('Ingrese el año de la moneda: '))
                if año_mon >= 1990 and año_mon <= 2024:
                    print('Se registro el año de la moneda!')
                    time.sleep(1)
                    os.system('cls')
                    break
                else:
                    print(
                        'ERROR! debe ingresar un año valido, el año de la moneda debe estar dentro de los años 1990 a 2024!')
            except:
                print('ERROR! debe ingresar números enteros!')

        moneda = {
            "nro": len(monedas) + 1,
            "tipo": tipos_monedas[tipo-1],
            "simbolo": simbolos[simbolo],
            "año": año_mon
        }
        monedas.append(moneda)
        print('MONEDA AGREGADA!')

    elif opc == 2:
        print('Ver monedas!')
        time.sleep(1)
        os.system('cls')
        if len(monedas) >= 1:
            while True:
                for x in monedas:
                    print("nro:", x["nro"], "\ttipo:",
                          x["tipo"], "\tsimbolo:", x["simbolo"], "\taño:", x["año"])
                opc = int(
                    input('¿Deseas salir? ingrese (1: salir), ingrese (0: redigir a lista de monedas) : '))
                if opc == 1:
                    print('Saliendo de lista de monedas.')
                    time.sleep(1)
                    os.system('cls')
                    break
                else:
                    print('Redirigiendo a lista de monedas!')
                time.sleep(1)
                os.system('cls')
        else:
            print('NO HAY MONEDAS REGISTRADAS!')
        time.sleep(1)

    elif opc == 3:
        print('Eliminar monedas!')
        if len(monedas) >= 1:
            while True:
                for x in monedas:
                    print("nro:", x["nro"], "\ttipo:",
                          x["tipo"], "\tsimbolo:", x["simbolo"], "\taño:", x["año"])
                mensaje = str(input(
                    'Deseas eliminar alguna moneda, ingrese("S": eliminar moneda o "N": salir sin hacer cambios): '))
                if mensaje.upper() == "S":
                    try:
                        nro_eliminar = int(
                            input('Ingrese el nro a eliminar de moneda: '))
                        for m in monedas:
                            if m["nro"] == nro_eliminar:
                                monedas.remove(m)
                                print('Moneda eliminada!')
                                time.sleep(1)
                                os.system('cls')
                                break
                            else:
                                print(
                                    'No se encuentra ningun número de moneda registrado!')
                            time.sleep(1)
                            os.system('cls')
                    except:
                        print('ERROR! debe ingresar números enteros!')
                elif mensaje.upper() == 'N':
                    print('Saliendo!')
                    time.sleep(1)
                    os.system('cls')
                    break
                else:
                    print(
                        'ERROR! debe ingresar un caracter valido, caracteres validos "S" o "N"!')
        else:
            print('NO HAY MONEDAS PARA ELIMINAR ACTUALMENTE!')
        time.sleep(1)
        os.system('cls')

    else:
        for f in range(1, 4):
            print('Saliendo de app monedas!', ("."*f))
            time.sleep(1)
            os.system('cls')
        break
