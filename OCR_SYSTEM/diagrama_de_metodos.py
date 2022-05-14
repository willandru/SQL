
#DEFINICION DE LOS MÉTODOS
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#2 CONSULTAR LISTA DE CARROS
def consultarListaCarros():
	carros_para_renta=[]

	for car in carros:
		if car['disponible'] == True:
			print('Este carros esta disponible para la renta')
			carros_para_renta.append(car)
	return carros_para_renta


#3 CONSULTAR LISTA DE DENOMINACION DE BILLETES
def consultarListaBilletes():
	tipo_billetes_aceptados= ['50.0000', '100.000']
	return tipo_billetes_aceptados


#4 CREAR UNA NUEVA RENTA
renta:{
	'fecha y hora':'date',
	{'Lineas_renta_actual': 'linea1','linea2'...},
	{'Billetes_de_la_renta_actual': 'billete1', 'billete2'...}
}
def crearRenta(renta):
	
	carros = consultarListaCarros()#g.
	tipoBIlletes= consultarListaBilletes() # h.

	disponibles= #HACER CONSULTA  'NOSQL' SOBRE carros_para_renta # b.

	if disponibles == [] # Si no hay existen unidades disponnibles  de ningun carro para la renta
		print('No se puede crear una nueva renta')
	else:
		- INSERT renta_actual INTO renta # c.
		- SELECT * FROM renta # d.


#5 AGREGAR LINEA EN LA RENTA ACTUAL
linea:{
	placa:string,
	cantidad:int,
	numero_Asientos:int
}
def agregarLinea(linea):
	carro_en_linea=linea.carro

	#a. VERIFICAR CARRO EN CATALOGO
	carros = SELECT * FROM carro WHERE carro.disponible=='TRUE'
	if carro_en_linea not in carros:
		print('MENSAJE_ERROR:El carro que quiere agregar ya no está disponible')

	#b. VERIFICAR EXISTENCIAS CARRO
	# i. .. el sistema verifica que el carro que llega como parametro está en el catálogo
	existencias_carro= SELECT unidadesDisponibles FROM carro WHERE carro.id==carro_en_linea.id
	if carro_en_linea not in existencias_carro:
		print('MENSAJE_ERROR:El carro que quiere agregar NO tiene UNIDADES (existencia) disponibles')
	# ii. .. Si un carro ya existe en la renta_Actual, se acumula la cantidad existente con la solicitada
	#.. Se debe consultar si la renta ya tiene en una línea el carro que se pretende agregar
	buscar_linea_por_placa = SELECT * FROM lineas WHERE rentaId=renta_actual AND lineas.PLACA == carro_en_linea.PLACA
	#.. Si ya existe una línea con ese carro se debe realizar una actualizacion a la linea de la renta, en la tabla respectiva.
	if buscar_linea_por_placa:
		id= buscar_linea_por_placa.id
		CC=buscar_linea_por_placa.cantidad
		UPDATE lineas.cantidad WHERE lineas.id==id (SET CC+linea.cantidad)


	#CREAR LINEA

	subtotal= linea.cantidad * carro_en_linea.valor













