# Metaurica: Sistema Integral de Control de Ingeniería y Gestión Financiera B2B


---

## 1\. Descripción del Proyecto

**Metaurica S.A. de C.V.** es una empresa mexicana de ingeniería especializada en diseño metal-mecánico, manufactura de precisión y consultoría industrial.

El **Sistema Integral Metaurica** es una solución informática robusta desarrollada en **Python** y **PSeInt** diseñada para sustituir procesos manuales propensos a error por un entorno automatizado, estructurado y trazable. El sistema integra dos módulos operativos fundamentales:

1. **Módulo Técnico de Control de Calidad Dimensional:** Valida las cotas físicas de planos mecánicos contra el estándar internacional **ISO 2768 Clase Fina** (tolerancia crítica de $\\pm 0.05\\text{ mm}$) y verifica el catálogo de materiales normados (**Acero ASTM A36** y **Aluminio ASTM B221**), emitiendo dictámenes automáticos de *Aprobado para Manufactura* o *Rechazado*.
2. **Módulo Administrativo y Financiero B2B:** Calcula con precisión la liquidación de comisiones comerciales (15% por regla de negocio) para agentes externos y proyectistas, determina el rendimiento neto de la consultoría y realiza el seguimiento del estatus fiscal y de cobranza (`PAGADO` / `PENDIENTE`).

---

##  2\. Características Técnicas y Estructura del Código

El software cumple estrictamente con los criterios de excelencia de la rúbrica de evaluación académica de **Universidad Tecmilenio** para la asignatura *Fundamentos de Programación Avanzada*:

* ** Menú Matricial Tabular ($2 \\times 2$):** Diseñado dentro de un bucle `while` interactivo en consola con bordes tabulares visuales. Permite la navegación flexible mediante coordenadas de celda `[0,0]`, `[0,1]`, `[1,0]`, `[1,1]` o selección numérica directa (`1` a `4`).
* ** Almacenamiento de Fecha mediante Tupla Inmutable:** Captura la fecha de trabajo del usuario en formato calendárico y la almacena en una tupla inmutable de tres elementos: `Fecha = (día, mes, año)` (ej. `(21, 9, 2026)`). Esta tupla se utiliza para estampar la auditoría de fecha en todos los registros del sistema.
* ** Gestión Dinámica de Archivos de Texto (`.txt`) vía Diccionario:** Administración de un catálogo en memoria persistente mapeado en una estructura de diccionario (`{ID: (nombre_archivo, descripción)}`). Soporta las operaciones de:  
  * **Lectura** de documentos preexistentes (`plano_flecha_ISO2768.txt`, `factura_proyecto_metaurica.txt`, etc.).
  * **Modificación/Anexo** en modo *append* (`'a'`) sin sobreescribir el historial previo.
  * **Creación y registro dinámico** de nuevos archivos `.txt` en el catálogo.
* ** Manejo de Excepciones (`try...except`):** Encapsulamiento defensivo para capturar excepciones como `ValueError` (ingreso de caracteres no numéricos en campos de tolerancia/montos) y `FileNotFoundError` (consultas a documentos inexistentes), garantizando que el programa nunca colapse y retorne de manera segura al menú principal.
* ** Interfaz e Interacción con el Usuario:**  
  * Banner corporativo en **Arte ASCII** alineado.
  * Saludo personalizado formateado dinámicamente con operadores de cadena (`+`, `*`, `.upper()`, `.center()`).
  * Pantalla de carga animada con temporizador configurado en $\\le 5\\text{ segundos}$ (`sys.stdout.flush()`).
  * Pausa de seguridad al cierre (`input()`) para prevenir el cierre intempestivo de la consola en Windows.

---

##  3\. Guía de Uso e Instalación

### Requisitos Previos

* **Python 3.10** o superior instalado en el sistema.
* (Opcional) **Streamlit** para ejecutar la versión web interactiva.
* **Git** para clonar el repositorio.

### Paso 1: Clonar el Repositorio

Abre tu terminal o símbolo del sistema (CMD) y ejecuta:

```
git clone https://github.com/tu-usuario/metaurica-control-system.git
cd metaurica-control-system

```

### Paso 2: Ejecución del Script de Consola (Python)

Para ejecutar la versión interactiva nativa en terminal de comandos:

```
python metaurica_fase2-v3.py

```

### Paso 3: Ejecución de la Aplicación Web (Streamlit)

Si deseas probar la interfaz web con componentes gráficos:

```
# Instalar Streamlit (si no lo tienes instalado)
pip install streamlit

# Ejecutar la aplicación web
streamlit run metaurica_streamlit.py

```

---

##  4\. Estructura del Repositorio

```
metaurica-control-system/
├── README.md                              # Carta de presentación del proyecto
├── metaurica_fase2-v3.py                  # Script principal en Python (Consola)
├── metaurica_streamlit.py                 # Aplicación Web Interactiva con Streamlit
├── metaurica_gui.py                       # Interfaz Gráfica de Escritorio (Tkinter)
├── metaurica_control-v5.psc               # Pseudocódigo ejecutable en PSeInt
├── docs/
│   ├── reporte_proyecto_metaurica_fase2-v6.docx   # Tesina y Reporte Técnico Final
│   ├── codigo_metaurica_fase2-v4.docx            # Código fuente 100% comentado
│   └── referencias_bibliograficas_apa_metaurica.docx # 100 Referencias en APA 7
└── assets/
    ├── diagrama_de_flujo_metaurica.png    # Diagrama de flujo ANSI/ISO
    └── figura1_radar_temario.png          # Gráficas de análisis y evaluación

```

---

##  5\. Equipo de Desarrollo (Equipo #3)

* **Carla Yuliana Martinez Quiroz**
* **Paul Ramses Rubio Alanis**
* **Silvana Hernández Montalvo**

*Universidad Tecmilenio — Fundamentos de Programación*
