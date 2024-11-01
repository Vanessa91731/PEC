import re
import pymysql

class CBD():

    def __init__(self):
        try:
            #Crea una conexion con los datos que se recolectaron de XAMPP
            self.conn = pymysql.connect(host='localhost', user=self.usuarioXampp, passwd='', port=self.puertoXampp, db="rh3")
            self.cursor = self.conn.cursor()
            print("\nConexión exitosa\n")

        except pymysql.Error as err:
            self.conn = pymysql.connect(host='localhost', user=self.usuarioXampp, passwd='', port=self.puertoXampp)
            self.cursor = self.conn.cursor()
            self.cursor.execute("CREATE DATABASE IF NOT EXISTS pec")
            self.cursor.execute("USE pec")
            print("\nCreación exitosa\n")
        

    # Detectar puerto y usuario de XAMPP
    def detectarPuertosXampp(rutaXampp='C:/xampp/mysql/bin/my.ini'):
        try:
            with open(rutaXampp, 'r') as archivo:
                contenido = archivo.read()

            # el re.search sirve para detectar los numeros del 0 al 9 con la sentencia de \d
            resultado_puerto = re.search(r'port[ ]*=[ ]*(\d+)', contenido)
            if resultado_puerto:
                puerto = int(resultado_puerto.group(1))  

            else:
                print("No hay puerto predeterminado")
                puerto =  None
            
            # el re.search sirve para detectar los caracteres alfanumericos con la sentencia de \w
            # En caso de no encontrar un usuario se llenara con un root
            resultado_usuario = re.search(r'user[ ]*=[ ]*(\w+)', contenido)
            if resultado_usuario:
                usuario = resultado_usuario.group(1)
            else:
                print("\nNo se encontró un nombre de usuario")
                usuario = "root"

            return puerto, usuario

        # Por si no se encontro el archivo en la ruta mencionada 
        except FileNotFoundError:
            print(f"No se encontro Xampp en la ruta {rutaXampp}")
            return None, None


    puertoXampp, usuarioXampp = detectarPuertosXampp()
    if puertoXampp:
        print(f"\nEl puerto de MySQL es {puertoXampp}")
        print(f"El nombre de usuario de MySQL es {usuarioXampp}")
    else:
        print("No se pudo encontrar el puerto de Xampp")

    def crearTabladonadores(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS `donadores` (`iddonador` int(11) NOT NULL AUTO_INCREMENT,`nombre` varchar(50) NOT NULL,`apellido` varchar(50) NOT NULL,`email` varchar(50) NOT NULL,`telefono` varchar(15) NOT NULL,`pago` varchar(30) NOT NULL,`comentarios` varchar(500) NOT NULL;")

    def conectar(self):
        try:
            self.crearTabladonadores()
        except pymysql.Error as err: 
            print ("\nError al intentar la conexión: {0}".format(err))
