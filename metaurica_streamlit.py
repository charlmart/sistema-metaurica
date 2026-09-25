"""
================================================================================
SISTEMA INTEGRAL METAURICA S.A. DE C.V. - APLICACIÓN WEB STREAMLIT
================================================================================
Alineado a la Rúbrica Oficial Tecmilenio y Estándares ISO 2768 / ASTM
Desarrollado por: Equipo #3 (Carla Martinez, Paul Rubio, Silvana Hernández)
================================================================================
"""

import streamlit as st
import datetime

# ------------------------------------------------------------------------------
# CONFIGURACIÓN DE PÁGINA STREAMLIT
# ------------------------------------------------------------------------------
st.set_page_config(
    page_title="Metaurica S.A. de C.V. - Control & Finanzas",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------------------------------------------------------------------
# INICIALIZACIÓN DE VARIABLES DE SESIÓN (PERSISTENCIA DE DATOS)
# ------------------------------------------------------------------------------
if "diccionario_archivos" not in st.session_state:
    st.session_state["diccionario_archivos"] = {
        1: ("plano_flecha_ISO2768.txt", "Flecha Cilíndrica de Transmisión Principal"),
        2: ("plano_buje_ASTM.txt", "Buje Guía en Aluminio ASTM B221"),
        3: ("cotizacion_servicios_B2B.txt", "Cotización de Servicio de Ingeniería B2B"),
        4: ("factura_proyecto_metaurica.txt", "Factura de Consultoría de Diseño Mecánico")
    }

if "contenido_archivos" not in st.session_state:
    st.session_state["contenido_archivos"] = {
        "plano_flecha_ISO2768.txt": "DOCUMENTO TÉCNICO: Plano Flecha Cilíndrica\nCota Nominal: 50.00 mm | Tolerancia: ISO 2768 Fina (±0.05 mm)\nMaterial: Acero ASTM A36\nEstatus: Aprobado para Manufactura\n",
        "plano_buje_ASTM.txt": "DOCUMENTO TÉCNICO: Plano Buje Guía\nCota Nominal: 25.00 mm | Tolerancia: ISO 2768 Fina (±0.05 mm)\nMaterial: Aluminio ASTM B221\nEstatus: Aprobado para Manufactura\n",
        "cotizacion_servicios_B2B.txt": "REGISTRO FINANCIERO: Cotización B2B #1042\nCliente: Grupo Industrial Metalmecánico S.A.\nMonto Total: $50,000.00 MXN | Anticipo: $25,000.00 MXN\nComisión Agente (15%): $7,500.00 MXN\n",
        "factura_proyecto_metaurica.txt": "REGISTRO FINANCIERO: Factura B2B #8891\nCliente: Componentes Industriales del Norte\nMonto Total: $120,000.00 MXN | Estatus: PAGADO\nRendimiento Neto Empresa: $102,000.00 MXN\n"
    }

if "estadisticas" not in st.session_state:
    st.session_state["estadisticas"] = {
        "total_evaluados": 0,
        "aprobados": 0,
        "rechazados": 0,
        "monto_acumulado": 0.0
    }

# ------------------------------------------------------------------------------
# ENCABEZADO Y BANNER CORPORATIVO
# ------------------------------------------------------------------------------
st.title("⚙️ METAURICA S.A. DE C.V.")
st.caption("Sistema Integral de Control de Calidad Dimensional y Gestión Financiera B2B")
st.markdown("---")

# ------------------------------------------------------------------------------
# BARRA LATERAL (SIDEBAR) - REGISTRO DE USUARIO Y TUPLA DE FECHA
# ------------------------------------------------------------------------------
st.sidebar.header("👤 Control de Sesión")
nickname = st.sidebar.text_input("Ingrese su Nickname / Nombre:", value="Ingeniero_Metaurica")

st.sidebar.subheader("📅 Captura de Fecha (Tupla Inmutable)")
col_d, col_m, col_a = st.sidebar.columns(3)
with col_d:
    dia = st.number_input("Día", min_value=1, max_value=31, value=21)
with col_m:
    mes = st.number_input("Mes", min_value=1, max_value=12, value=9)
with col_a:
    anio = st.number_input("Año", min_value=2020, max_value=2030, value=2026)

# Creación de la Tupla Inmutable de Fecha requerida por la Rúbrica Tecmilenio
tupla_fecha = (int(dia), int(mes), int(anio))
st.sidebar.info(f"📌 **Tupla de Fecha Activa:** `{tupla_fecha}`")

# Saludo personalizado procesado con operadores de cadena
saludo_formateado = f"¡BIENVENIDO(A) {nickname.upper()} AL SISTEMA METAURICA!"
st.sidebar.success(saludo_formateado)

# ------------------------------------------------------------------------------
# NAVEGACIÓN PRINCIPAL POR PESTAÑAS (MÓDULOS DEL SISTEMA)
# ------------------------------------------------------------------------------
tab1, tab2, tab3, tab4 = st.tabs([
    "📐 Módulo Técnico (ISO 2768)",
    "💰 Módulo Financiero B2B",
    "📁 Gestión de Archivos (.txt)",
    "📊 Resumen Ejecutivo Estadístico"
])

# ==============================================================================
# PESTAÑA 1: MÓDULO TÉCNICO DE CALIDAD DIMENSIONAL (ISO 2768 / ASTM)
# ==============================================================================
with tab1:
    st.header("📐 Inspección Dimensional bajo Norma ISO 2768 Clase Fina")
    st.markdown("""
    Este módulo valida las cotas físicas de planos mecánicos. La norma **ISO 2768** exige un límite estricto de **±0.05 mm** respecto a la tolerancia permitida.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        codigo_plano = st.text_input("Folio / Código del Plano Mecánico:", value="PLN-2026-001")
        medida_real = st.number_input("Medida Real Obtenida en Taller (mm):", min_value=0.0, value=50.03, format="%.4f")
    with col2:
        tolerancia_permitida = st.number_input("Tolerancia / Cota Nominal (mm):", min_value=0.0, value=50.00, format="%.4f")
        tipo_material = st.selectbox(
            "Material Certificado en Catálogo:",
            [
                "1 - Acero ASTM A36 (Estructural)",
                "2 - Aluminio ASTM B221 (Maquinado)",
                "3 - Material No Certificado / Genérico"
            ]
        )

    if st.button("🔍 Evaluar Tolerancia y Emitir Dictamen"):
        try:
            # Procesamiento algorítmico de desviaciones (Procesos 2 y 3)
            difA = medida_real - tolerancia_permitida
            difB = tolerancia_permitida - medida_real
            
            st.markdown("### 📋 Resultado de la Evaluación Técnica")
            st.write(f"**Desviación Superior (`difA`):** `{difA:+.4f} mm`")
            st.write(f"**Desviación Inferior (`difB`):** `{difB:+.4f} mm`")
            
            # Evaluación booleana de decisiones (Decisión 1 y Decisión 2)
            excede_tolerancia = (difA > 0.05) or (difB > 0.05)
            material_valido = tipo_material.startswith("1") or tipo_material.startswith("2")
            
            st.session_state["estadisticas"]["total_evaluados"] += 1
            
            if excede_tolerancia:
                st.error("❌ DICTAMEN: RECHAZADO POR ERROR DE MEDIDA DIMENSIONAL")
                st.warning("⚠️ La desviación detectada excede el límite crítico de ±0.05 mm establecido por la norma ISO 2768 Clase Fina.")
                st.session_state["estadisticas"]["rechazados"] += 1
            elif not material_valido:
                st.error("❌ DICTAMEN: RECHAZADO POR MATERIAL NO CERTIFICADO")
                st.warning("⚠️ El material seleccionado no cumple con los estándares ASTM A36 o ASTM B221 exigidos en la especificación.")
                st.session_state["estadisticas"]["rechazados"] += 1
            else:
                st.success("✅ DICTAMEN: ¡APROBADO PARA MANUFACTURA / PRODUCCIÓN!")
                st.info(f"La pieza con folio **{codigo_plano}** cumple con todas las especificaciones geométricas y de material.")
                st.session_state["estadisticas"]["aprobados"] += 1

        except Exception as e:
            st.error(f"Ocurrió un error en el cálculo dimensional: {e}")

# ==============================================================================
# PESTAÑA 2: MÓDULO ADMINISTRATIVO Y FINANCIERO B2B
# ==============================================================================
with tab2:
    st.header("💰 Calculadora de Comisiones y Rendimiento Financiero B2B")
    st.markdown("""
    Calcula de forma exacta la comisión neta asignada al proyectista externo (15% por regla de negocio) y el rendimiento neto operativo conservado por Metaurica S.A. de C.V.
    """)
    
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        nombre_cliente = st.text_input("Razón Social / Nombre del Cliente B2B:", value="Grupo Industrial Metalmecánico S.A.")
        monto_total = st.number_input("Monto Total Facturado del Proyecto ($ MXN):", min_value=0.0, value=50000.0, step=1000.0, format="%.2f")
    with col_f2:
        porcentaje_comision = st.number_input("Porcentaje de Comisión del Agente (%):", min_value=0.0, max_value=100.0, value=15.0, step=1.0)
        estado_cobro = st.selectbox("Estatus de Cobranza de la Factura:", ["PAGADO", "PENDIENTE DE PAGO"])

    if st.button("💰 Calcular Comisión Financiera B2B"):
        try:
            # Procesamiento de cálculos comerciales (Proceso 4 y Proceso 5)
            monto_comision = (monto_total * porcentaje_comision) / 100.0
            rendimiento_neto = monto_total - monto_comision
            
            st.session_state["estadisticas"]["monto_acumulado"] += monto_total
            
            st.markdown("### 📊 Resumen Financiero Generado")
            col_res1, col_res2, col_res3 = st.columns(3)
            with col_res1:
                st.metric("Monto Total Facturado", f"${monto_total:,.2f} MXN")
            with col_res2:
                st.metric(f"Comisión Agente ({porcentaje_comision:.0f}%)", f"${monto_comision:,.2f} MXN")
            with col_res3:
                st.metric("Rendimiento Neto Empresa", f"${rendimiento_neto:,.2f} MXN")
                
            if estado_cobro == "PAGADO":
                st.success(f"✅ La factura de **{nombre_cliente}** está marcada como **PAGADA**. Se autoriza la liberación de la comisión de ${monto_comision:,.2f} MXN.")
            else:
                st.warning(f"⏳ La factura de **{nombre_cliente}** está **PENDIENTE DE PAGO**. La comisión se liberará tras saldar la cuenta.")
                
        except Exception as e:
            st.error(f"Error al procesar la transacción financiera: {e}")

# ==============================================================================
# PESTAÑA 3: GESTIÓN DE ARCHIVOS DE TEXTO PLANO (.TXT) VÍA DICCIONARIO
# ==============================================================================
with tab3:
    st.header("📁 Gestor de Archivos y Documentación Persistente")
    st.markdown("""
    Administra el catálogo de documentos institucionales almacenados en un **diccionario**. Permite leer, anexar notas en modo *append* (`'a'`) y registrar nuevos archivos `.txt`.
    """)
    
    opcion_gestion = st.radio(
        "Seleccione la operación a realizar:",
        ["1 - Leer Archivo del Catálogo", "2 - Anexar Nota / Modificar Archivo", "3 - Crear y Registrar Nuevo Archivo .txt"]
    )
    
    dict_archivos = st.session_state["diccionario_archivos"]
    
    if opcion_gestion.startswith("1"):
        st.subheader("📖 Lectura de Documentos")
        opciones_lista = [f"ID {k}: {v[0]} ({v[1]})" for k, v in dict_archivos.items()]
        archivo_sel = st.selectbox("Seleccione el archivo que desea consultar:", opciones_lista)
        
        if st.button("📄 Mostrar Contenido"):
            clave_id = int(archivo_sel.split(":")[0].replace("ID", "").strip())
            nombre_archivo = dict_archivos[clave_id][0]
            contenido = st.session_state["contenido_archivos"].get(nombre_archivo, "El archivo está vacío.")
            
            st.info(f"**Archivo Seleccionado:** `{nombre_archivo}`")
            st.text_area("Contenido Actual del Archivo:", value=contenido, height=200)

    elif opcion_gestion.startswith("2"):
        st.subheader("✍️ Anexar Nota Técnica en Modo Append ('a')")
        opciones_lista = [f"ID {k}: {v[0]} ({v[1]})" for k, v in dict_archivos.items()]
        archivo_sel = st.selectbox("Seleccione el archivo a actualizar:", opciones_lista)
        nota_anexa = st.text_input("Ingrese la nota o actualización técnica a incluir:")
        
        if st.button("📝 Guardar Actualización en Archivo"):
            if nota_anexa.strip() != "":
                clave_id = int(archivo_sel.split(":")[0].replace("ID", "").strip())
                nombre_archivo = dict_archivos[clave_id][0]
                
                # Estampa con la Tupla Inmutable de Fecha y el Nickname del usuario
                linea_anexa = f"\n[ACTUALIZACIÓN {tupla_fecha[0]}/{tupla_fecha[1]}/{tupla_fecha[2]} BY {nickname.upper()}]: {nota_anexa}"
                st.session_state["contenido_archivos"][nombre_archivo] += linea_anexa
                
                st.success(f"✅ ¡Nota agregada exitosamente al archivo `{nombre_archivo}`!")
                st.text_area("Contenido Actualizado:", value=st.session_state["contenido_archivos"][nombre_archivo], height=200)
            else:
                st.warning("Escriba un texto válido antes de guardar.")

    elif opcion_gestion.startswith("3"):
        st.subheader("➕ Crear Nuevo Archivo .txt y Registrar en Diccionario")
        nuevo_nombre = st.text_input("Nombre del Nuevo Archivo (ej. reporte_inspeccion.txt):", value="reporte_nuevo_inspeccion.txt")
        nueva_desc = st.text_input("Descripción del Documento:", value="Reporte Especial de Control de Calidad")
        nuevo_contenido = st.text_area("Contenido Inicial del Documento:", value="ENCABEZADO DE DOCUMENTO METAURICA S.A. DE C.V.\nFecha de Alta: " + str(tupla_fecha))
        
        if st.button("💾 Crear y Registrar Documento"):
            if nuevo_nombre.strip() != "":
                nueva_clave = max(dict_archivos.keys()) + 1
                dict_archivos[nueva_clave] = (nuevo_nombre, nueva_desc)
                st.session_state["contenido_archivos"][nuevo_nombre] = nuevo_contenido
                
                st.success(f"✅ ¡Archivo `{nuevo_nombre}` registrado en el Diccionario con la Clave ID {nueva_clave}!")

# ==============================================================================
# PESTAÑA 4: RESUMEN EJECUTIVO ESTADÍSTICO
# ==============================================================================
with tab4:
    st.header("📊 Resumen Ejecutivo Estadístico de la Sesión")
    st.markdown("Indicadores acumulados en tiempo real durante la operación del sistema:")
    
    stats = st.session_state["estadisticas"]
    
    col_st1, col_st2, col_st3, col_st4 = st.columns(4)
    with col_st1:
        st.metric("Total Planos Evaluados", stats["total_evaluados"])
    with col_st2:
        st.metric("Planos Aprobados", stats["aprobados"])
    with col_st3:
        st.metric("Planos Rechazados", stats["rechazados"])
    with col_st4:
        st.metric("Monto Total Procesado", f"${stats['monto_acumulado']:,.2f} MXN")
        
    st.markdown("---")
    st.caption("Metaurica Control & Financial System v3.0 | Proyecto Final Fundamentos de Programación Avanzada Tecmilenio")
