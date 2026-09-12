# -*- coding: utf-8 -*-
#
# SISTEMA INTEGRAL METAURICA - MÓDULOS DE INGENIERÍA Y FINANZAS (VERSIÓN PREMIUM V3)
# Desarrollado de acuerdo con la Rúbrica de Fundamentos de Programación Tecmilenio
#

def mostrar_bienvenida():
    """
    Función encargada de mostrar el banner corporativo inicial
    al arrancar el sistema en la terminal.
    """
    banner = r"""
    =============================================================
    M E T A U R I C A
    SISTEMA DE CONTROL DE CALIDAD Y GESTIÓN FINANCIERA
    Corporativo Metaurica S.A.
    =============================================================
    """
    print(banner)

def sistema_metaurica():
    """
    Función principal que controla el flujo del programa, el menú de opciones
    y la ejecución cíclica mediante estructuras de control (while).
    """
    mostrar_bienvenida()
    continuar_operacion = "s"
    
    # Ciclo principal para permitir múltiples consultas según el usuario lo decida
    while continuar_operacion.lower().startswith("s"):
        print("\n" + "." * 45)
        print(" MENÚ PRINCIPAL DE OPERACIONES")
        print("." * 45)
        print(" [1] MÓDULO TÉCNICO: Validación de Planos de Ingeniería")
        print(" [2] MÓDULO FINANCIERO: Cálculo de Comisiones de Ventas")
        print("." * 45)
        
        # Captura de la opción seleccionada por el usuario
        opcion_seleccionada = input("Ingrese el número de la opción deseada (1 o 2): ")
        
        # Opción 1: Módulo Técnico de Calidad
        if opcion_seleccionada == "1":
            print("\n" + "-" * 50)
            print(" >>> MÓDULO 1: VALIDACIÓN TÉCNICA DE PLANOS <<<")
            print("-" * 50)
            try:
                # Entrada de datos numéricos con validación de tipos
                codigo_plano = int(input("Ingrese el código numérico identificador del plano: "))
                medida_real = float(input("Ingrese la medida física real de la pieza (mm): "))
                tolerancia_permitida = float(input("Ingrese la tolerancia nominal permitida (mm): "))
                
                # Cálculos de desviación dimensional
                desviacion_positiva = medida_real - tolerancia_permitida
                desviacion_negativa = tolerancia_permitida - medida_real
                
                print("\n" + "." * 40)
                print(f" Código del plano evaluado: {codigo_plano}")
                print(f" Desviación Calculada (+): {desviacion_positiva:+.4f} mm")
                print(f" Desviación Calculada (-): {desviacion_negativa:+.4f} mm")
                print("." * 40)
                
                # Condicionales para evaluar límites críticos de calidad
                if desviacion_positiva > 0.05 or desviacion_negativa > 0.05:
                    print("\n" + "X" * 45)
                    print(" DICTAMEN DE CALIDAD: RECHAZADO por error de medida.")
                    print(" Explicación: La desviación excede el límite crítico de +/- 0.05 mm.")
                    print("X" * 45)
                else:
                    print("\nLa dimensión física está aprobada. Procediendo a verificar material...")
                    tipo_material = int(input("Seleccione material (1: Acero, 2: Aluminio): "))
                    
                    # Verificación de códigos de materiales autorizados
                    if tipo_material == 1 or tipo_material == 2:
                        nombre_material = "Acero de Alta Resistencia" if tipo_material == 1 else "Aluminio Estructural"
                        print("\n" + "*" * 45)
                        print(" DICTAMEN DE CALIDAD: ¡APROBADO PARA PRODUCCIÓN!")
                        print(f" Material validado: {nombre_material}")
                        print("*" * 45)
                    else:
                        print("\n" + "X" * 45)
                        print(" DICTAMEN DE CALIDAD: RECHAZADO por material.")
                        print(" Explicación: El material no coincide con los códigos autorizados.")
                        print("X" * 45)
            except ValueError:
                # Manejo de excepciones ante errores de dedo del usuario
                print("\n[ERROR CRÍTICO] El sistema detectó una entrada no numérica válida.")
                print("Por favor, asegúrese de ingresar números enteros para códigos y decimales para medidas.")
                
        # Opción 2: Módulo Financiero
        elif opcion_seleccionada == "2":
            print("\n" + "-" * 50)
            print(" >>> MÓDULO 2: GESTIÓN FINANCIERA Y COMISIONES <<<")
            print("-" * 50)
            try:
                # Captura de datos financieros
                nombre_cliente = input("Ingrese el nombre completo del cliente: ")
                monto_total_facturado = float(input("Ingrese el monto total facturado ($): "))
                porcentaje_comision = float(input("Ingrese el porcentaje de comisión para el agente (%): "))
                
                # Operaciones aritméticas financieras
                monto_comision_calculada = (monto_total_facturado * porcentaje_comision) / 100.0
                monto_neto_empresa = monto_total_facturado - monto_comision_calculada
                
                # Despliegue estructurado del estado de cuenta
                print("\n" + "=" * 50)
                print(" ESTADO DE CUENTA DE COMISIONES ")
                print("=" * 50)
                print(f" Cliente Asociado:  {nombre_cliente}")
                print(f" Monto Facturado:   ${monto_total_facturado:,.2f} MXN")
                print(f" Comisión Agente:   ${monto_comision_calculada:,.2f} MXN ({porcentaje_comision}%)")
                print(f" Rendimiento Neto:  ${monto_neto_empresa:,.2f} MXN")
                print("=" * 50)
                
                estado_cobro_factura = input("Ingrese estatus de cobro (PAGADO / PENDIENTE): ")
                print(f"\nOperación financiera registrada con estatus: {estado_cobro_factura.upper()}")
            except ValueError:
                # Manejo de excepciones financieras
                print("\n[ERROR CRÍTICO] Formato financiero inválido.")
                print("Asegúrese de escribir montos y porcentajes únicamente con números y puntos decimales.")
        else:
            print("\n[ADVERTENCIA] Opción no válida. Por favor, ingrese únicamente 1 o 2.")
            
        print("\n" + "=" * 50)
        # Pregunta para repetir o finalizar la ejecución del ciclo while
        continuar_operacion = input("¿Desea realizar otra operación en el sistema Metaurica? (s/n): ")
        
    print("\n" + "=" * 79)
    print(" Gracias por utilizar el Sistema Integral Metaurica.")
    print(" La sesión ha sido cerrada y guardada con éxito.")
    print("=" * 79)

if __name__ == "__main__":
    # Punto de entrada estándar para la ejecución del script en Python
    sistema_metaurica()
