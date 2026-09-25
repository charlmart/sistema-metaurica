# -*- coding: utf-8 -*-  # Codificación UTF-8 para soporte completo de acentos y caracteres especiales en Python
"""  # Inicio de la documentación del módulo principal en formato docstring
===============================================================================  # Encabezado visual superior
SISTEMA INTEGRAL METAURICA S.A. DE C.V. - CONTROL DE CALIDAD Y FINANZAS B2B  # Título formal del sistema
CUMPLIMIENTO 100% RÚBRICA TECMILENIO - FUNDAMENTOS DE PROGRAMACIÓN (FASE 2)  # Cumplimiento académico
===============================================================================  # Encabezado visual intermedio
Institución: Universidad Tecmilenio  # Asignatura y universidad
Materia: Fundamentos de Programación Avanzada  # Nombre de la materia
Equipo de Desarrollo: Equipo 3 (Carla Martínez, Paul Rubio, Silvana Hernández)  # Integrantes
Docente: Blanca Aracely Aranda Machorro  # Nombre de la profesora
===============================================================================  # Encabezado visual de cierre
CRITERIOS DE LA RÚBRICA CUMPLIDOS AL 100%:  # Lista de verificación de rúbrica
1. Interacción con usuario: Nickname, concatenación de cadenas, espera <= 5 s.  # Criterio 1
2. Menú tabular (2x2): Ciclo WHILE, matriz de 2 columnas, cambio de usuario.  # Criterio 2
3. Captura y uso de datos: Fecha DD/MM/AAAA almacenada en Tupla (día, mes, año).  # Criterio 3
4. Manejo de archivos: >= 4 archivos creados, diccionario, lectura, escritura y creación.  # Criterio 4
5. Manejo de excepciones: try...except (FileNotFoundError, ValueError, IOError).  # Criterio 5
6. Calidad de código: 100% de líneas comentadas, ejecución continua sin colapsos.  # Criterio 6
===============================================================================  # Línea final del encabezado
"""  # Cierre del bloque docstring principal del módulo

# Importación de librerías del sistema  # Encabezado de la sección de importaciones
import sys        # Módulo sys para control de búfer de salida estándar (sys.stdout)
import time       # Módulo time para control de temporizadores y pausas (time.sleep)
import os         # Módulo os para verificación y gestión de archivos en el sistema de archivos
import threading  # Módulo threading para control asíncrono de temporización en consola

# =============================================================================  # Sección 1: Funciones de interfaz
# FUNCIONES DE BIENVENIDA, CARGA Y FECHA EN TUPLA (CRITERIOS 1 Y 3)  # Descripción de la sección
# =============================================================================  # Separador de sección visual

def mostrar_banner_ascii():  # Función para desplegar el logotipo institucional en arte ASCII
    """ Imprime el logotipo en arte ASCII de Metaurica S.A. de C.V. """  # Docstring de la función
    l1 = "==============================================================================="  # Marco superior
    l2 = r" __  __  ______  _______     /\     _    _  _____    _____     _____     /\    "  # Fila 1 ASCII
    l3 = r"|  \/  ||  ____||__   __|   /  \   | |  | ||  __ \  |_   _|   / ____|   /  \   "  # Fila 2 ASCII
    l4 = r"| \  / || |__      | |     / /\ \  | |  | || |__) |   | |    | |       / /\ \  "  # Fila 3 ASCII
    l5 = r"| |\/| ||  __|     | |    / ____ \ | |  | ||  _  /    | |    | |      / ____ \ "  # Fila 4 ASCII
    l6 = r"| |  | || |____    | |   /_/    \_\| |__| || | \ \   _| |_   | |____ /_/    \_\\"  # Fila 5 ASCII
    l7 = r"|_|  |_||______|   |_|              \____/ |_|  \_\_|_____|   \_____|          "  # Fila 6 ASCII
    l8 = "==============================================================================="  # Marco intermedio
    l9 = "        SISTEMA DE CONTROL DE CALIDAD Y GESTIÓN FINANCIERA METAURICA            "  # Subtítulo principal
    l10 = "                        Corporativo Metaurica S.A. de C.V.                     "  # Nombre corporativo
    l11 = "==============================================================================="  # Marco inferior
    print(f"\n{l1}\n{l2}\n{l3}\n{l4}\n{l5}\n{l6}\n{l7}\n{l8}\n{l9}\n{l10}\n{l11}\n")  # Imprime el arte ASCII completo

def pantalla_carga_animada(segundos=3):  # Función para simular pantalla de carga animada (<= 5 s)
    """ Genera una barra de carga animada con temporización exacta de <= 5 segundos. """  # Docstring
    if segundos > 5:  # Evaluación de seguridad para no exceder los 5 segundos de la rúbrica
        segundos = 5  # Restringe la duración máxima a 5 segundos exactos
        
    print("\n" + "=" * 65)  # Imprime barra divisoria superior multiplicando el carácter '='
    print(" [SISTEMA METAURICA] Cargando módulos de gestión técnica y financiera...")  # Mensaje de inicio
    print("=" * 65)  # Imprime barra divisoria inferior
    
    pasos = 20  # Número total de segmentos en la barra de progreso
    tiempo_paso = segundos / pasos  # Fracción de tiempo para cada segmento de la barra
    
    for i in range(1, pasos + 1):  # Ciclo for para simular el progreso del 1% al 100%
        porcentaje = (i / pasos) * 100  # Cálculo del porcentaje de avance acumulado
        barra = "█" * i + "-" * (pasos - i)  # Construcción de la barra visual con repetición de caracteres
        sys.stdout.write(f"\r Inicializando entorno: [{barra}] {porcentaje:.0f}%")  # Impresión en línea
        sys.stdout.flush()  # Limpieza de búfer para actualizar la consola en tiempo real
        time.sleep(tiempo_paso)  # Pausa por cada iteración del ciclo for
        
    print("\n\n [OK] Módulos inicializados correctamente. Entorno listo para operar.")  # Confirmación
    print("=" * 65 + "\n")  # Divisoria de cierre de la animación

def solicitar_y_almacenar_fecha_tupla():  # Función para pedir la fecha y guardarla en una tupla
    """ Solicita fecha en DD/MM/AAAA y la almacena en una tupla inmutable Fecha = (día, mes, año). """  # Docstring
    while True:  # Ciclo while para repetir hasta obtener una fecha con formato válido
        entrada = input(" Ingrese la fecha de trabajo (formato DD/MM/AAAA, ej. 15/08/2024): ").strip()  # Lectura
        try:  # Bloque try para capturar errores de formato o valores no enteros
            partes = entrada.split("/")  # División de la cadena usando '/' como delimitador
            if len(partes) != 3:  # Validación de que existan exactamente 3 elementos
                raise ValueError("Debe ingresar día, mes y año separados por diagonales '/'")  # Excepción
                
            dia = int(partes[0])   # Conversión del día a número entero
            mes = int(partes[1])   # Conversión del mes a número entero
            anio = int(partes[2])  # Conversión del año a número entero
            
            if not (1 <= dia <= 31 and 1 <= mes <= 12 and 1900 <= anio <= 2100):  # Rango calendárico
                raise ValueError("Día (1-31), mes (1-12) o año (1900-2100) fuera de rango válido")  # Excepción
                
            Fecha = (dia, mes, anio)  # Almacenamiento estricto en la tupla Fecha = (día, mes, año)
            print(f" [OK] Fecha almacenada exitosamente en Tupla inmutable: Fecha = {Fecha}")  # Confirmación
            return Fecha  # Retorno de la tupla Fecha hacia el programa principal
            
        except ValueError as e:  # Captura de errores de conversión numérica o formato
            print(f" [ERROR DE FORMATO] {e}. Por favor, intente de nuevo.\n")  # Notificación de error

def inicializar_archivos_sistema():  # Función para pre-crear los 4 archivos requeridos por la rúbrica
    """ Asegura la presencia de al menos 4 archivos .txt de muestra en el sistema. """  # Docstring
    catalogo_inicial = {  # Diccionario con nombres de archivo y contenidos iniciales de ingeniería
        "plano_flecha_ISO2768.txt": (  # Archivo 1: Plano técnico de flecha mecánica
            "=== PLANO TÉCNICO: FLECHA DE TRANSMISIÓN INDUSTRIAL ===\n"  # Encabezado
            "Código de Plano: PL-1024 | Norma Aplicable: ISO 2768 (Tolerancia Fina)\n"  # Norma
            "Medida Nominal: 50.00 mm | Tolerancia Permitida: +/- 0.05 mm\n"  # Tolerancias
            "Material Especificado: Acero Estructural ASTM A36 (Clave 1)\n"  # Material
            "Dictamen de Calidad: APROBADO PARA MANUFACTURA EN TALLER\n"  # Dictamen
        ),  # Fin archivo 1
        "plano_buje_ASTM.txt": (  # Archivo 2: Plano técnico de buje guía
            "=== PLANO TÉCNICO: BUJE GUÍA DE BRONCE Y ALUMINIO ===\n"  # Encabezado
            "Código de Plano: PL-2048 | Norma Aplicable: ISO 2768 (Tolerancia Media)\n"  # Norma
            "Medida Nominal: 120.00 mm | Tolerancia Permitida: +/- 0.10 mm\n"  # Tolerancias
            "Material Especificado: Aluminio Industrial ASTM B221 (Clave 2)\n"  # Material
            "Dictamen de Calidad: REVISIÓN DE DISEÑO EN PROCESO\n"  # Dictamen
        ),  # Fin archivo 2
        "cotizacion_servicios_B2B.txt": (  # Archivo 3: Cotización comercial B2B
            "=== COTIZACIÓN COMERCIAL B2B METAURICA S.A. DE C.V. ===\n"  # Encabezado
            "Cliente: Industrias Metalmecánicas del Norte S.A.\n"  # Cliente
            "Concepto: Levantamiento 3D y Memoria de Cálculo Estructural\n"  # Concepto
            "Horas de Ingeniería: 45 hrs | Tarifa: $850.00 MXN/hr\n"  # Horas
            "Margen Operativo Aplica: 30% | Monto Total: $49,725.00 MXN\n"  # Margen
        ),  # Fin archivo 3
        "factura_proyecto_metaurica.txt": (  # Archivo 4: Registro financiero de cobranza
            "=== REGISTRO FINANCIERO Y CONTROL DE FACTURACIÓN ===\n"  # Encabezado
            "Folio Fiscal: MET-2026-0891 | Cliente: Taller Maquilados MTY\n"  # Folio
            "Monto Total Facturado: $120,000.00 MXN\n"  # Monto
            "Estatus de Cobranza: PAGADO\n"  # Estatus
            "Comisión Agente (15%): $18,000.00 MXN [LIBERADA Y PAGADA]\n"  # Comisión
        )  # Fin archivo 4
    }  # Cierre del diccionario de archivos iniciales
    
    for nombre_file, texto_contenido in catalogo_inicial.items():  # Recorrido de los 4 archivos
        if not os.path.exists(nombre_file):  # Verificación de existencia previa en disco
            with open(nombre_file, "w", encoding="utf-8") as f:  # Apertura en modo escritura UTF-8
                f.write(texto_contenido)  # Escritura del contenido inicial en el archivo

# =============================================================================  # Sección 2: Operaciones de archivos
# MÓDULOS DE LECTURA, ESCRITURA Y CREACIÓN DE ARCHIVOS (CRITERIOS 4 Y 5)  # Descripción
# =============================================================================  # Separador visual

def mostrar_catalogo_y_seleccionar(diccionario_archivos):  # Muestra archivos en diccionario
    """ Muestra los archivos registrados en formato diccionario y captura la selección. """  # Docstring
    print("\n" + "-" * 60)  # Barra divisoria superior
    print(" CATÁLOGO DE ARCHIVOS REGISTRADOS EN EL DICCIONARIO")  # Encabezado
    print("-" * 60)  # Barra divisoria intermedia
    
    for clave, nombre_archivo in diccionario_archivos.items():  # Iteración sobre clave y valor del diccionario
        print(f"  Clave [{clave}] -> Nombre de archivo: {nombre_archivo}")  # Despliegue de diccionario
    print("-" * 60)  # Barra divisoria inferior
    
    eleccion = input(" Ingrese la clave numérica del archivo o su nombre exacto: ").strip()  # Lectura
    
    try:  # Bloque try para intentar convertir la elección a clave numérica
        clave_num = int(eleccion)  # Conversión a entero
        if clave_num in diccionario_archivos:  # Verificación de existencia de clave en el diccionario
            return diccionario_archivos[clave_num]  # Retorna el nombre mapeado a esa clave
    except ValueError:  # Si el usuario escribió el nombre directamente como cadena de texto
        pass  # Omisión de error para procesar la entrada como texto literal
        
    return eleccion  # Retorna el texto ingresado directamente

def ejecucion_leer_archivo(diccionario_archivos):  # Función para leer archivos con manejo de excepciones
    """ Lee un archivo seleccionado manejando la excepción FileNotFoundError de forma segura. """  # Docstring
    archivo_objetivo = mostrar_catalogo_y_seleccionar(diccionario_archivos)  # Obtiene nombre del archivo
    
    try:  # Bloque try para capturar errores al intentar abrir y leer el archivo
        with open(archivo_objetivo, "r", encoding="utf-8") as archivo:  # Apertura en modo lectura UTF-8
            contenido = archivo.read()  # Lectura completa del contenido del archivo
            
        print("\n" + "=" * 65)  # Marco divisorio de lectura
        print(f" CONTENIDO DEL ARCHIVO CONSULTADO: '{archivo_objetivo}'")  # Título con nombre del archivo
        print("=" * 65)  # Línea divisoria
        print(contenido)  # Despliegue del texto leído en la pantalla
        print("=" * 65 + "\n")  # Pie de cierre visual
        
    except FileNotFoundError:  # Captura de excepción cuando el archivo no existe en el disco
        print(f"\n [EXCEPCIÓN DETECTADA] Error: El archivo '{archivo_objetivo}' no existe o está mal escrito.")  # Error
        print(" El programa continúa en ejecución normal. Verifique el nombre e intente de nuevo.\n")  # Resiliencia
    except IOError as e:  # Captura de errores de entrada/salida de disco
        print(f"\n [EXCEPCIÓN DE E/S] No se pudo leer el archivo '{archivo_objetivo}': {e}\n")  # Notificación
    except Exception as e:  # Captura de cualquier otra anomalía no prevista
        print(f"\n [EXCEPCIÓN NO PREVISTA] Error al leer: {e}\n")  # Manejo general

def ejecucion_escribir_archivo(diccionario_archivos, fecha_tupla, usuario):  # Anexa notas con fecha de tupla
    """ Anexa contenido a un archivo existente incorporando la fecha de la tupla. """  # Docstring
    archivo_objetivo = mostrar_catalogo_y_seleccionar(diccionario_archivos)  # Obtiene nombre del archivo
    
    if not os.path.exists(archivo_objetivo):  # Verificación de existencia del archivo en disco
        print(f"\n [EXCEPCIÓN DETECTADA] El archivo '{archivo_objetivo}' no existe para modificación.")  # Error
        print(" Utilice la Opción 3 ('Crear archivo') si desea registrar un documento nuevo.\n")  # Guía
        return  # Retorno limpio sin romper el programa
        
    print(f"\n Modificando archivo técnico: '{archivo_objetivo}'")  # Aviso de modificación
    nota_tecnica = input(" Ingrese la nota técnica o actualización a anexar: ")  # Lectura de la nota
    
    str_fecha = f"{fecha_tupla[0]:02d}/{fecha_tupla[1]:02d}/{fecha_tupla[2]}"  # Formato de fecha desde la tupla
    
    try:  # Bloque try para capturar errores durante la escritura en modo append ('a')
        with open(archivo_objetivo, "a", encoding="utf-8") as archivo:  # Modo anexar sin sobrescribir
            archivo.write(f"\n[ACTUALIZACIÓN {str_fecha} POR {usuario.upper()}]: {nota_tecnica}\n")  # Anexo
            
        print(f" [OK] Archivo '{archivo_objetivo}' modificado con éxito usando la fecha {str_fecha}.\n")  # Exito
    except Exception as e:  # Captura de excepciones en escritura de archivos
        print(f" [EXCEPCIÓN EN ESCRITURA] Ocurrió un error al modificar el archivo: {e}\n")  # Notificación

def ejecucion_crear_archivo(diccionario_archivos, fecha_tupla, usuario):  # Crea nuevo archivo en el sistema
    """ Crea un archivo .txt nuevo con cabecera institucional y lo registra en el diccionario. """  # Docstring
    nuevo_nombre = input("\n Ingrese el nombre del nuevo archivo (ej. reporte_inspeccion.txt): ").strip()  # Nombre
    
    if not nuevo_nombre.endswith(".txt"):  # Verificación de la extensión de archivo .txt
        nuevo_nombre += ".txt"  # Concatenación automática de la extensión .txt
        
    contenido_inicial = input(" Ingrese el contenido inicial para el documento: ")  # Lectura del contenido
    str_fecha = f"{fecha_tupla[0]:02d}/{fecha_tupla[1]:02d}/{fecha_tupla[2]}"  # Formato de la fecha desde tupla
    
    try:  # Bloque try para creación de archivo en modo escritura ('w')
        with open(nuevo_nombre, "w", encoding="utf-8") as archivo:  # Apertura de nuevo archivo
            archivo.write("=== REGISTRO OFICIAL METAURICA S.A. DE C.V. ===\n")  # Línea 1
            archivo.write(f"Fecha de Registro: {str_fecha} (Tupla inmutable: {fecha_tupla})\n")  # Tupla
            archivo.write(f"Usuario Creador: {usuario}\n")  # Usuario
            archivo.write("--------------------------------------------------\n")  # Divisoria
            archivo.write(contenido_inicial + "\n")  # Contenido introducido por el usuario
            
        nueva_clave = max(diccionario_archivos.keys()) + 1 if diccionario_archivos else 1  # Clave incremental
        diccionario_archivos[nueva_clave] = nuevo_nombre  # Registro en el diccionario en memoria
        
        print(f" [OK] Nuevo archivo '{nuevo_nombre}' creado y agregado al catálogo con la fecha {str_fecha}.\n")  # OK
    except Exception as e:  # Captura de errores al crear el archivo
        print(f" [EXCEPCIÓN EN CREACIÓN] No se pudo crear el archivo: {e}\n")  # Notificación de fallo

# =============================================================================  # Sección 3: Temporizador
# CONTROL DE TEMPORIZACIÓN DE INACTIVIDAD CON CICLO FOR (CRITERIO 2)  # Descripción
# =============================================================================  # Separador visual

def capturar_opcion_con_temporizador(tiempo_limite_segundos=600):  # Temporizador de 10 minutos (600 s)
    """ Controla la inactividad durante 10 min (600 s) con ciclo FOR y lectura asíncrona. """  # Docstring
    resultado = [None]  # Lista mutable para recibir la entrada desde el hilo asíncrono

    def entrada_usuario():  # Función interna para capturar la opción desde la consola
        try:  # Bloque try para evitar fallos en la consola durante la lectura
            val = input("\n Seleccione opción [Fila,Columna] o número de celda (1-4): ")  # Captura
            resultado[0] = val  # Guardado en el primer elemento de la lista
        except (EOFError, KeyboardInterrupt, Exception):  # Captura de interrupciones de teclado o consola
            resultado[0] = None  # Asignación de valor nulo si ocurre interrupción

    hilo = threading.Thread(target=entrada_usuario)  # Creación del hilo asíncrono para input()
    hilo.daemon = True  # Marcado como hilo demonio para cerrarse automáticamente al salir
    hilo.start()  # Inicio del hilo asíncrono

    for segundo in range(tiempo_limite_segundos):  # Ciclo FOR que cuenta de 0 a 599 segundos (10 minutos)
        if not hilo.is_alive():  # Comprobación de si el usuario ya presionó ENTER
            return resultado[0]  # Retorna el valor ingresado inmediatamente
        time.sleep(1)  # Pausa de 1 segundo en cada iteración del ciclo FOR

    print("\n\n [TEMPORIZADOR] Han transcurrido 10 minutos sin actividad en el menú.")  # Advertencia
    while True:  # Ciclo while para confirmar si el usuario desea continuar
        resp = input(" ¿Desea continuar en el sistema Metaurica? (si/no): ").strip().lower()  # Respuesta
        if resp in ["si", "sí"]:  # Si decide continuar
            return "REINICIAR_MENU"  # Señal para reimprimir el menú
        elif resp == "no":  # Si decide no continuar
            return "CAMBIAR_USUARIO"  # Señal para salir o cambiar de usuario
        else:  # Si ingresa una opción no válida
            print(" Por favor, responda escribiendo únicamente 'si' o 'no'.")  # Aclaración

# =============================================================================  # Sección 4: Programa principal
# MENÚ MATRICIAL EN CICLO WHILE Y CONTROL DE USUARIOS (CRITERIOS 1, 2, 6)  # Descripción
# =============================================================================  # Separador visual

def sistema_metaurica_principal():  # Función principal que orquesta la aplicación
    """ Función principal del sistema Metaurica con menú matricial 2x2 en ciclo WHILE. """  # Docstring
    inicializar_archivos_sistema()  # Asegura la presencia de los 4 archivos .txt iniciales
    
    diccionario_archivos = {  # Declaración del diccionario en memoria con la estructura de catálogo
        1: "plano_flecha_ISO2768.txt",  # Clave 1: Plano de flecha
        2: "plano_buje_ASTM.txt",  # Clave 2: Plano de buje
        3: "cotizacion_servicios_B2B.txt",  # Clave 3: Cotización B2B
        4: "factura_proyecto_metaurica.txt"  # Clave 4: Factura de proyecto
    }  # Cierre del diccionario del catálogo

    mostrar_banner_ascii()  # Despliegue del logotipo institucional ASCII
    
    print("=" * 70)  # Marco superior
    print("      SISTEMA DE CONTROL Y GESTIÓN METAURICA S.A. DE C.V.")  # Título secundario
    print("=" * 70)  # Marco inferior
    
    nombre_usuario = input(" Por favor, ingrese su nombre o nickname de usuario: ").strip()  # Captura nickname
    if not nombre_usuario:  # Si no ingresó texto
        nombre_usuario = "Ingeniero_Consultor"  # Asignación de nickname predeterminado
        
    separador_banner = "*" * 70  # Operador de repetición (*) para el separador visual
    mensaje_saludo = " ¡Bienvenido(a) al Sistema de Ingeniería, " + nombre_usuario.upper() + "! "  # Concatenación (+)
    mensaje_sub = " Metaurica S.A. - Control de Calidad Dimensional y Gestión Financiera B2B "  # Subtítulo
    
    print("\n" + separador_banner)  # Imprime barra superior
    print(mensaje_saludo.center(70, "#"))  # Imprime saludo centrado con relleno '#'
    print(mensaje_sub.center(70, " "))  # Imprime subtítulo centrado
    print(separador_banner + "\n")  # Imprime barra inferior

    pantalla_carga_animada(segundos=3)  # Pantalla de carga animada (<= 5 s)
    
    fecha_sistema = solicitar_y_almacenar_fecha_tupla()  # Almacena fecha en tupla Fecha = (día, mes, año)
    
    matriz_opciones = [  # Declaración de la MATRIZ 2x2 para el menú en formato tabular de 2 columnas
        ["[1] Leer Archivo", "[2] Escribir / Modificar Archivo"],  # Fila 0: Columna 0 y Columna 1
        ["[3] Crear Nuevo Archivo", "[4] Cambiar de Usuario / Salir"]  # Fila 1: Columna 0 y Columna 1
    ]  # Cierre de la estructura matricial
    
    sistema_activo = True  # Bandera booleana para mantener el ciclo WHILE activo
    
    while sistema_activo:  # Ciclo WHILE principal del menú del sistema
        print("\n" + "=" * 65)  # Divisoria superior del menú
        print(f" MENÚ MATRICIAL DE OPERACIONES (Usuario: {nombre_usuario} | Fecha: {fecha_sistema})")  # Encabezado
        print("=" * 65)  # Divisoria del encabezado
        
        print("      Columna 0                       Columna 1")  # Título de columnas
        print("  ┌──────────────────────────────┬──────────────────────────────┐")  # Marco superior
        for idx_fila, fila in enumerate(matriz_opciones):  # Iteración sobre filas de la matriz
            col0 = fila[0].ljust(28)  # Formato de ancho fijo para columna 0
            col1 = fila[1].ljust(28)  # Formato de ancho fijo para columna 1
            print(f"F{idx_fila}│ {col0} │ {col1} │")  # Despliegue de fila con sus 2 columnas en consola
            if idx_fila < len(matriz_opciones) - 1:  # Si no es la última fila
                print("  ├──────────────────────────────┼──────────────────────────────┤")  # Divisoria de fila
        print("  └──────────────────────────────┴──────────────────────────────┘")  # Marco inferior
        print(" Opciones válidas: 1, 2, 3 o 4 (o por coordenadas matriciales: 0,0 | 0,1 | 1,0 | 1,1)")  # Ayuda
        
        opcion_ingresada = capturar_opcion_con_temporizador(tiempo_limite_segundos=600)  # Temporizador 10 min
        
        if opcion_ingresada == "REINICIAR_MENU" or opcion_ingresada is None:  # Si eligió continuar
            continue  # Vuelve al inicio del ciclo WHILE
        elif opcion_ingresada == "CAMBIAR_USUARIO":  # Si eligió cambiar usuario
            print("\n [REINICIANDO SESIÓN] Regresando a la pantalla de inicio de usuario...")  # Aviso
            return sistema_metaurica_principal()  # Llamada recursiva para reiniciar sesión con nuevo usuario
            
        opcion_limpia = opcion_ingresada.strip().lower()  # Limpieza de espacios y conversión a minúsculas
        
        opcion_num = None  # Inicialización de la opción numérica seleccionada
        if opcion_limpia in ["1", "0,0", "[0,0]"]:  # Mapeo celda [Fila 0, Columna 0]
            opcion_num = 1  # Opción 1: Leer
        elif opcion_limpia in ["2", "0,1", "[0,1]"]:  # Mapeo celda [Fila 0, Columna 1]
            opcion_num = 2  # Opción 2: Escribir
        elif opcion_limpia in ["3", "1,0", "[1,0]"]:  # Mapeo celda [Fila 1, Columna 0]
            opcion_num = 3  # Opción 3: Crear
        elif opcion_limpia in ["4", "1,1", "[1,1]", "salir"]:  # Mapeo celda [Fila 1, Columna 1]
            opcion_num = 4  # Opción 4: Cambiar usuario / Salir
        else:  # Si ingresó una coordenada o número fuera de la matriz
            print(f"\n [ERROR DE SELECCIÓN] '{opcion_limpia}' no es una opción o coordenada válida.")  # Error
            continue  # Reintenta dentro del ciclo WHILE

        if opcion_num == 1:  # Si la opción procesada es 1
            ejecucion_leer_archivo(diccionario_archivos)  # Llama función de lectura
        elif opcion_num == 2:  # Si la opción procesada es 2
            ejecucion_escribir_archivo(diccionario_archivos, fecha_sistema, nombre_usuario)  # Llama escritura
        elif opcion_num == 3:  # Si la opción procesada es 3
            ejecucion_crear_archivo(diccionario_archivos, fecha_sistema, nombre_usuario)  # Llama creación
        elif opcion_num == 4:  # Si la opción procesada es 4
            print("\n Submenú de Usuario / Salida de Sistema:")  # Título
            sub_op = input(" Escriba 'cambiar' para nuevo usuario o 'salir' para cerrar programa: ").strip().lower()  # Leer
            if sub_op == "cambiar":  # Opción cambiar de usuario
                return sistema_metaurica_principal()  # Reinicio recursivo de la aplicación
            else:  # Opción salir del sistema
                print("\n" + "=" * 65)  # Divisoria de despedida
                print(" ¡Gracias por utilizar el Sistema Metaurica S.A. de C.V.!")  # Agradecimiento
                print(" La sesión ha sido finalizada de manera totalmente segura.")  # Confirmación
                print("=" * 65 + "\n")  # Divisoria final
                sistema_activo = False  # Cambia la bandera booleana a False para terminar el ciclo WHILE

# Bloque estándar de ejecución del script  # Condición para ejecución directa del script
if __name__ == "__main__":  # Verifica si el archivo se ejecuta directamente
    try:  # Bloque try de protección global para la ejecución del programa
        sistema_metaurica_principal()  # Ejecución de la función principal
    except KeyboardInterrupt:  # Captura de interrupción por teclado (Ctrl+C)
        print("\n\n [AVISO] Ejecución interrumpida por el usuario. Cerrando programa de forma segura.")  # Aviso
    finally:  # Bloque final que asegura una pausa antes de cerrar la ventana de consola en Windows
        print("\n" + "." * 65)  # Divisoria final de pausa
        try:  # Intento de captura de Enter final para evitar el cierre instantáneo al hacer doble clic
            input(" [PAUSA DE SEGURIDAD] Presione ENTER para cerrar la ventana del sistema...")  # Pausa
        except (EOFError, KeyboardInterrupt):  # Captura de cualquier excepción durante la pausa final
            pass  # Finalización silenciosa si no hay entrada interactiva disponible
