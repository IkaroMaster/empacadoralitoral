def renderizado(posicion, tamano):
	estilos = {}
	clases = {}

	for i in range(1, tamano + 1):
		estilos['o' + str(i)] = 'display: none'
		clases['o' + str(i)] = ''

	estilos['o' + str(posicion)] = ''
	clases['o' + str(posicion)] = 'active'

	return estilos, clases