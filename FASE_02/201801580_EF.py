import psycopg2 as p
flag = True

PSQL_HOST = "localhost"
PSQL_PORT = "5432"
PSQL_USER = "postgres"
PSQL_PASS = "201801580"
PSQL_DB   = "williamhernandez"

address = """ host=%s port=%s user=%s password=%s dbname=%s 
"""% (PSQL_HOST, PSQL_PORT, PSQL_USER, PSQL_PASS, PSQL_DB)

try:

	connection = p.connect(address)
	cursor = connection.cursor()
	
	print("¡LA CONEXIÓN CON LA BASE DE DATOS FUE EXITOSA!")
	

except:

	print("#¡NO SE LOGRÓ HACER LA CONEXIÓN CON LA BASE DATOS, INTENTELO NUEVAMENTE!#")

while flag == True:

	print("")
	print("           LOGIN          ")
	print("")
	user = input ("INGRESE EL NOMBRE DE USUARIO: ")
	psw = input("INGRSE LA CONTRASEÑA: ")
	print("")

	if user == "William_Hdz" and psw == "201801580":

		flag1 = True

		while flag1 == True:

			print("     BIENVENIDO WILLIAM HERNÁNDEZ       ")
			print("")
			print("               OPCIONES                 ")
			print("")
			print("########################################")
			print("#  1. AGREGAR USUARIO ----------- (a)  #")
			print("#  2. ELIMINAR USUARIO ---------- (d)  #")
			print("#  3. SALIR --------------------- (e)  #")
			print("########################################")
			print("")

			opcion = input("INGRESE UNA OPCIÓN: ")
			opt = opcion.lower()

			if opt == "a":

				nm1 = input("INGRESE EL PRIMER NOMBRE: ")
				nm2 = input("INGRESE EL SEGUNDO NOMBRE: ")
				ap1 = input("INGRESE EL PRIMER APELLIDO: ")
				ap2 = input("INGRESE EL SEGUNDO APELLIDO: ")
				usu = input("INGRESE EL NOMBRE DE USUARIO: ")
				pas = input("INGRESE LA CONTRASEÑA: ")

				SQL = "INSERT INTO usuarios(primer_nombre,segundo_nombre,primer_apellido,segundo_apellido,nombre_usuario,contraseña) VALUES ("'%s'","'%s'","'%s'","'%s'","'%s'","'%s'")"
				datos = (nm1,nm2,ap1,ap2,usu,pas)
				cursor.execute(SQL,datos)
				connection.commit()
			
			elif opt == "d":

				usu1 = input("INGRESE EL NOMBRE DEL USUARIO QUE DESEA ELIMINAR: ")
				SQL3 = "DELETE FROM usuarios where nombre_usuario = %s;"
				cursor.execute(SQL3,(usu1,))
				connection.commit()
				print("Usuario eliminado")

			elif opt == "e":

				flag = False

			else:

				print("######################################")
				print("# USTED NO INGRESÓ UNA OPCIÓN VALIDA #")
				print("######################################")

	else:

		cursor.execute("SELECT primer_nombre, primer_apellido, nombre_usuario, contraseña FROM usuarios where nombre_usuario = %(user)s",{'user':user})
		datos = cursor.fetchone()

		nom = datos[0]
		ape = datos[1]
		user2 = datos[2]
		psw2 = datos[3]

		if user2 == user and psw2 == psw:

			flag2 = True

			print("BIENVENIDO/A", datos[0].upper())
			print("")

			total = int(0)
			subt = int(0)
			subt2 = int(0)
			subt3 = int(0)
			ser = int(0)
			ser2 = int(0)
			ser3 = int(0)
			des2 = False

			while flag2 == True:

				print("      VENTA DE BOLETOS AEROLINEA     ")
				print("")
				print("#####################################")
				print("#  1. PRIMERA CLASE ----------- (p) #")
				print("#  2. SEGUNDA CLASE ----------- (s) #")
				print("#  3. TERCERA CLASE ----------- (t) #")
				print("#  4. FINALIZAR COMPRA -------- (e) #")
				print("#####################################")
				print("")

				opcion2 = input("INGRESE EL TIPO TIPO DE CLASE:" )
				opt2 = opcion2.lower()

				if opt2 == "p":

					print("#################")
					print("# PRIMERA CLASE #")
					print("#################")

					boletos = int(input("¿QUE CANTIDAD DE BOLETOS DE ESTA CLASE DESEA COMPRAR? "))
					if boletos == 0:
						comida = int(0) 
						bebida = int(0)
						peli   = int(0)
					else:
						comida = int(input("¿QUE CANTIDAD DE COMIDA DESEA AGREGAR? "))
						bebida = int(input("¿QUE CANTIDAD DE BEBIDAS DESEA AGREGAR? "))
						peli = int(input("¿QUE CANTIDAD DE PELICULAS DESEA AGREGAR? "))

					subt = ((comida * 50) + (bebida * 35) + (peli *  70))*boletos
					ser = comida + bebida + peli

					if comida > 0 and bebida >0 and peli > 0:
						des2 = True
					else:
						des2 = False

				elif opt2 == "s":

					print("#################")
					print("# SEGUNDA CLASE #")
					print("#################")

					boletos = int(input("¿QUE CANTIDAD DE BOLETOS DE ESTA CLASE DESEA COMPRAR? "))
					if boletos == 0:
						comida = int(0) 
						bebida = int(0)
						peli   = int(0)
					else:
						comida = int(input("¿QUE CANTIDAD DE COMIDA DESEA AGREGAR? "))
						bebida = int(input("¿QUE CANTIDAD DE BEBIDAS DESEA AGREGAR? "))
						peli = int(input("¿QUE CANTIDAD DE PELICULAS DESEA AGREGAR? "))

					subt2 = ((comida * 40) + (bebida * 25) + (peli *  55))*boletos
					ser2 = comida + bebida + peli

				elif opt2 == "t":

					print("#################")
					print("# TERCERA CLASE #")
					print("#################")

					boletos = int(input("¿QUE CANTIDAD DE BOLETOS DE ESTA CLASE DESEA COMPRAR? "))
					if boletos == 0:
						comida = int(0) 
						bebida = int(0)
						peli   = int(0)
					else:
						comida = int(input("¿QUE CANTIDAD DE COMIDA DESEA AGREGAR? "))
						bebida = int(input("¿QUE CANTIDAD DE BEBIDAS DESEA AGREGAR? "))
						peli = int(input("¿QUE CANTIDAD DE PELICULAS DESEA AGREGAR? "))

					subt3 = ((comida * 25) + (bebida * 10) + (peli *  25))*boletos
					ser3 = comida +  bebida + peli

				elif opt2 == "f":

					print("####################")
					print("# FINALIZAR COMPRA #")
					print("####################")

					subtotal = subt + subt2 + subt3
					servicios = ser + ser2 + ser3

					if servicios > 10:

						desc = subtotal * 0.1

					else:

						desc = 0

					if des2 == True:

						desc1 = subtotal * 0.05

					else:

						desc1 = int(0)

					descuento = desc + desc1
					total = subtotal - descuento 

					print("EL SUBTOTAL DE LA COMPRA ES: ",subtotal)
					print("EL DESCUENTO PARA ESTA COMPRA ES DE: ",descuento)
					print("EL TOTAL DE LA COMPRA ES DE:",total)

					SQL2 = "INSERT INTO ventas(nombre_usuario,subtotal,descuento,total) VALUES ("'%s'",'%s','%s','%s')"
					datos2 = (datos[2],subtotal,descuento,total)
					cursor.execute(SQL2,datos2)
					connection.commit()	

					flag2 = False

				else: 

					print("######################################")
					print("# USTED NO INGRESÓ UNA OPCIÓN VALIDA #")
					print("######################################")