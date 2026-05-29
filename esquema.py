import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
# =========================================================
# CONFIGURACIÓN
# =========================================================

st.set_page_config(
    page_title="Metodologías de Minería de Datos",
    page_icon="📊",
    layout="wide"
)

# =========================================================
# ENCABEZADO
# =========================================================
       
# =========================================================
# ENCABEZADO INSTITUCIONAL
# =========================================================
st.image("logo.png", width=400)

st.markdown("""
<div style='text-align: center;'>

<h1 style='color:#0B5394;'>
Metodologías para el Proceso de Minería de Datos
</h1>

<h3>
Proyecto Comparativo
</h3>

<hr style='border:1px solid #D3D3D3;'>

<h4>
Instituto Superior Tecnológico del Azuay
</h4>

<h4>
Periodo Académico 31-2026-1P
</h4>

<h4>
Carrera de Tecnología Superior en Big Data
</h4>

</div>
""", unsafe_allow_html=True)

# =========================================================
# INFORMACIÓN ACADÉMICA
# =========================================================

col1, col2 = st.columns(2)

with col1:

    st.info("""
    ### Docente
    
    Ing. Verónica Chimbo
    """)

with col2:

    st.info("""
    ### Asignatura
    
    Minería de Datos I
    """)

# =========================================================
# DATOS DE ESTUDIANTES
# =========================================================

st.markdown("## 👨‍🎓 Datos del estudiante")
st.write("""
**Nombre: Juan Francisco       
**Apellido: Peña Buri    
**Correo electrónico: juan.pena.est@tecazuay.edu.ec
""")
st.divider()    

# =========================================================
# INTRODUCCIÓN
# =========================================================

st.markdown("""
## Introducción

En este proyecto se analizarán diferentes metodologías
de minería de datos y ciencia de datos.

Los estudiantes deberán completar la información correspondiente
a cada metodología y desarrollar una pequeña aplicación práctica
utilizando datos reales.
""")

st.divider()

# =========================================================
# MENÚ LATERAL
# =========================================================

st.sidebar.title("📚 Menú")

opcion = st.sidebar.radio(
    "Seleccione una metodología",
    [
        "Inicio",
        "KDD",
        "CRISP-DM",
        "SEMMA",
        "TDSP",
        "Comparativa"
    ]
)

# =========================================================
# INICIO
# =========================================================

if opcion == "Inicio":

    st.header("Bienvenido")

    st.markdown("""
    ## Objetivo

    Analizar y comparar metodologías utilizadas
    en proyectos de minería de datos.

    ## Actividades

    ✅ Completar descripción  
    ✅ Investigar fases  
    ✅ Identificar ventajas  
    ✅ Identificar desventajas  
    ✅ Investigar empresas  
    ✅ Desarrollar aplicación práctica
    """)

# =========================================================
# KDD
# =========================================================

elif opcion == "KDD":

    st.header("Metodología KDD")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "Descripción",
        "Fases",
        "Ventajas",
        "Desventajas",
        "Empresas",
        "Aplicación"
    ])

    # -----------------------------------------------------

    with tab1:

        st.subheader("Descripción")

        st.write("""
        Es un proceso estructurado e iterativo diseñado para identificar patrones válidos, 
        novedosos, potencialmente útiles y comprensibles dentro de grandes volúmenes de datos
        """)

    # -----------------------------------------------------

    with tab2:

        st.subheader("Fases")

        fases = pd.DataFrame({

            "Fase": [
                "SELECCIÓN",
                "PROCESAMIENTO",
                "TRANSFORMACIÓN",
                "MINERÍA DE DATOS",
                "EVALUACIÓN",
                "PRESENTACIÓN DEL CONOCIMIENTO"
            ],

            "Descripción": [
                "Se seleccionan los datos relevantes de las fuentes disponibles para el objetivo del proyecto.",
                "Se limpian y transforman los datos para mejorar su calidad y facilitar el análisis.",
                "Se transforman los datos en formas adecuadas para la minería de datos.",
                "Se aplican técnicas y algoritmos para descubrir patrones y modelos en los datos.",
                "Se evalúan los patrones y modelos encontrados para verificar su validez y utilidad.",
                "Se presenta el conocimiento descubrimiento de forma comprensible para la toma de decisiones."
            ]
        })

        st.dataframe(fases, use_container_width=True)

    # -----------------------------------------------------

    with tab3:

        st.subheader("Ventajas")
        
        

        st.markdown("""
 ✔ **Ventaja 1 | Toma de decisiones precisa:** Fundamenta estrategias empresariales en datos reales y cuantificables, reduciendo los riesgos derivados de la intuición o conjeturas.

 ✔ **Ventaja 2 | Ventaja competitiva:** Permite descubrir tendencias de consumo y anticipar comportamientos futuros del mercado mediante análisis predictivo.

 ✔ **Ventaja 3 | Proceso iterativo:** Facilita la mejora continua.
""")

    # -----------------------------------------------------

    with tab4:

        st.subheader("Desventajas")
        
        st.markdown("""
✘ **Desventajas 1 | Alto Costo y Complejidad:** Requiere una inversión considerable en infraestructura y almacenamiento, además de conocimientos especializados para su ejecución.

✘ **Desventajas 2 | Dependencia de la Calidad de los Datos:** Si los datos iniciales son erróneos, el preprocesamiento exigirá demasiado tiempo y los resultados finales estarán viciados.

✘ **Desventajas 3 | Preocupaciones de Privacidad:** Al analizar volúmenes masivos de información (a menudo de usuarios), surgen riesgos éticos y de seguridad de los datos personales.
""")

        

    # -----------------------------------------------------

    with tab5:

        st.subheader("Empresas")

        empresas = pd.DataFrame({

            "Empresa": ["Neflix", "Amazon", "Mastercard"],
            "Uso": [ "Optimización del motor de recomendaciones y creación de series originales basadas en gustos.", 
        "Predicción de compras para anticipar el stock en almacenes locales antes de que se haga el pedido.", 
        "Minería de patrones de transacciones en tiempo real para la detección temprana de fraudes con tarjetas."]
        })

        st.table(empresas)

    # -----------------------------------------------------
    with tab6:
     st.subheader("Aplicación Práctica")

     st.write("""
        El objetivo de esta aplicación es unificar datos educativos...
    """)

     st.title("Proyecto KDD con Datos de Estudiantes")

     st.markdown("Nombre: Juan Francisco Peña B.")
     st.markdown("Curso: M2A")
     st.markdown("Materia: Minería de Datos ")
     st.markdown("Tema: Comparativa de Metodologías ")

     st.markdown("## 1. Selección")
     st.write("Objetivo: Analizar características de los estudiantes...")

     archivo1 = st.file_uploader("Subir archivo Excel 1", type=["xls","xlsx"])
     archivo2 = st.file_uploader("Subir archivo Excel 2", type=["xls","xlsx"])

     if archivo1 and archivo2:
        df1 = pd.read_excel(archivo1)
        df2 = pd.read_excel(archivo2)

        df = pd.concat([df1, df2], ignore_index=True)

        st.markdown("## 2. Procesamiento")

        st.subheader("Vista previa")
        st.dataframe(df.head())

        st.subheader("Información general")
        st.write(df.shape)
        st.write(df.dtypes)

        st.subheader("Valores nulos")
        st.write(df.isnull().sum())

        st.markdown("## 3. Transformación")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Distribución por sexo")
            fig, ax = plt.subplots()
            df["sexo"].value_counts().plot(kind="bar", ax=ax)
            st.pyplot(fig)

        with col2:
            st.subheader("Tipo de colegio")
            fig2, ax2 = plt.subplots()
            df["tipo_colegio"].value_counts().plot(kind="bar", ax=ax2)
            st.pyplot(fig2)

        st.subheader("Carreras con más estudiantes")
        fig3, ax3 = plt.subplots(figsize=(10,5))
        df["nombre_carrera"].value_counts().head(10).plot(kind="bar", ax=ax3)
        st.pyplot(fig3)

        st.markdown("## 4. Mineria de Datos")

        datos = df.copy()
        columnas = ["sexo","tipo_colegio","etnia","provincia_residencia","tipo_estudiante"]

        le = LabelEncoder()

        for col in columnas:
            datos[col] = datos[col].astype(str)
            datos[col] = le.fit_transform(datos[col])

        datos = datos.fillna(0)

        X = datos[["sexo","tipo_colegio","etnia","provincia_residencia"]]
        y = datos["tipo_estudiante"]

        st.write("Variables predictoras:", X.columns.tolist())

        st.markdown("## 5. Modelado")

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.3, random_state=42
        )

        modelo = RandomForestClassifier()
        modelo.fit(X_train, y_train)

        pred = modelo.predict(X_test)

        st.markdown("## 6. Evaluación")

        acc = accuracy_score(y_test, pred)
        st.metric("Accuracy", round(acc,2))

        st.subheader("Matriz de Confusión")
        st.write(confusion_matrix(y_test, pred))

        st.success("Proyecto KDD ejecutado correctamente.")
       

            # AQUÍ  COMPLETAR

# =========================================================
# CRISP-DM
# =========================================================

elif opcion == "CRISP-DM":

    st.header("Metodología CRISP-DM")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "Descripción",
        "Fases",
        "Ventajas",
        "Desventajas",
        "Empresas",
        "Aplicación"
    ])

    # -----------------------------------------------------

    with tab1:

        st.subheader("Descripción")

        st.write("""
        La metodología CRISP-DM fue creada para proporcionar un proceso estructurado, 
        flexible y reutilizable que permita transformar datos en conocimiento útil para la toma de decisiones.
        """)

    # -----------------------------------------------------

    with tab2:

        st.subheader("Fases")

        fases = pd.DataFrame({

            "Fase": [
                "COMPRENSIÓN DEL NEGOCIO",
                "COMPRENSIÓN DE LOS DATOS",
                "PREPARACIÓN DE LOS DATOS",
                "MODELADO",
                "EVALUACIÓN",
                "DESPLIEGUE"
            ],

            "Descripción": [
                "Entender el problema y los objetivos del negocio para definir el alcance del proyecto.",
                "Recolectar los datos iniciales y explorarlos para familiarizarse con ellos.",
                "Transformar los datos en un formato adecuado y de calidad para el modelo.",
                "Aplicar técnicas de minería de datos o aprendizaje automático para construir modelos.",
                "Evaluar los modelos y verificar si cumplen con los objetivos del negocio.",
                "Implementar los resultados del modelo en el entorno real para generar valor."
            ]
        })

        st.dataframe(fases, use_container_width=True)

    # -----------------------------------------------------

    with tab3:

        st.subheader("Ventajas")
        st.markdown("""
 ✔ **Ventaja 1 | Metodología Flexible:** Puede adaptarse a diferentes tipos de proyectos.

 ✔ **Ventaja 2 | Proceso Iterativo:** Permite regresar a fases anteriores para mejorar resultados.

 ✔ **Ventaja 3 | Facilita la Toma de Decisiones:** Transforma datos en conocimiento útil para el negocio.
""")

       

    # -----------------------------------------------------

    with tab4:

        st.subheader("Desventajas")
        
        st.markdown("""
✘ **Desventajas 1 | Consume mucho Tiempo:** La preparación y limpieza de datos puede representar más del 70% del proyecto.

✘ **Desventajas 2 | Requiere conocimiento Técnico:** Se necesitan habilidades en: Estadística, Base de Datos, Programación.

✘ **Desventajas 3 | Puede generar mucha Documentación:** Algunas fases requieren reportes y análisis.
""")


    # -----------------------------------------------------

    with tab5:

        st.subheader("Empresas")

        empresas = pd.DataFrame({

            "Empresa": ["Amazon", "Neflix", "Uber"],
            "Uso": ["Recomendación de productos", "Sistema de recomendación de películas/series.", "Predicción de demanda."]
        })

        st.table(empresas)

    # -----------------------------------------------------

    with tab6:

      st.subheader("Aplicación Práctica")
      st.write("""
        El objetivo de esta aplicación es unificar datos educativos...
     """)

      st.title("Proyecto CRISP-DM con Datos de Estudiantes")

      st.markdown("Nombre: Juan Francisco Peña B.")
      st.markdown("Curso: M2A")
      st.markdown("Materia: Minería de Datos ")
      st.markdown("Tema: Comparativa de Metodologías ")

      st.markdown("## 1. Comprensión del Negocio")
      st.write("Objetivo: Analizar características de los estudiantes...")

      archivo1 = st.file_uploader("Subir archivo Excel 1", type=["xls","xlsx"])
      archivo2 = st.file_uploader("Subir archivo Excel 2", type=["xls","xlsx"])

      if archivo1 and archivo2:
        df1 = pd.read_excel(archivo1)
        df2 = pd.read_excel(archivo2)

        df = pd.concat([df1, df2], ignore_index=True)

        st.markdown("## 2. Comprensión de los Datos")

        st.subheader("Vista previa")
        st.dataframe(df.head())

        st.subheader("Información general")
        st.write(df.shape)
        st.write(df.dtypes)

        st.subheader("Valores nulos")
        st.write(df.isnull().sum())

        st.markdown("## 3. Visualización")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Distribución por sexo")
            fig, ax = plt.subplots()
            df["sexo"].value_counts().plot(kind="bar", ax=ax)
            st.pyplot(fig)

        with col2:
            st.subheader("Tipo de colegio")
            fig2, ax2 = plt.subplots()
            df["tipo_colegio"].value_counts().plot(kind="bar", ax=ax2)
            st.pyplot(fig2)

        st.subheader("Carreras con más estudiantes")
        fig3, ax3 = plt.subplots(figsize=(10,5))
        df["nombre_carrera"].value_counts().head(10).plot(kind="bar", ax=ax3)
        st.pyplot(fig3)

        st.markdown("## 4. Preparación de Datos")

        datos = df.copy()
        columnas = ["sexo","tipo_colegio","etnia","provincia_residencia","tipo_estudiante"]

        le = LabelEncoder()

        for col in columnas:
            datos[col] = datos[col].astype(str)
            datos[col] = le.fit_transform(datos[col])

        datos = datos.fillna(0)

        X = datos[["sexo","tipo_colegio","etnia","provincia_residencia"]]
        y = datos["tipo_estudiante"]

        st.write("Variables predictoras:", X.columns.tolist())

        st.markdown("## 5. Modelado")

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.3, random_state=42
        )

        modelo = RandomForestClassifier()
        modelo.fit(X_train, y_train)

        pred = modelo.predict(X_test)

        st.markdown("## 6. Evaluación")

        acc = accuracy_score(y_test, pred)
        st.metric("Accuracy", round(acc,2))

        st.subheader("Matriz de Confusión")
        st.write(confusion_matrix(y_test, pred))

        st.success("Proyecto CRISP-DM ejecutado correctamente.")   


            # AQUÍ COMPLETAR

# =========================================================
# SEMMA
# =========================================================

elif opcion == "SEMMA":

    st.header("Metodología SEMMA")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "Descripción",
        "Fases",
        "Ventajas",
        "Desventajas",
        "Empresas",
        "Aplicación"
    ])

    # -----------------------------------------------------

    with tab1:

        st.subheader("Descripción")

        st.write("""
        La metodología SEMMA es un enfoque desarrollado por SAS Institute para proyectos de 
        minería de datos. Su nombre proviene de cinco etapas clave: Sample, Explore, Modify, 
        Model, Assess.
        """)

    # -----------------------------------------------------

    with tab2:

        st.subheader("Fases")

        fases = pd.DataFrame({

            "Fase": [
                "SAMPLE(Muestreo)",
                "EXPLORE(Exploración)",
                "MODIFY(Modificación)",
                "MODEL(Modelado)",
                "ASSESS(Evaluación)"
            ],

            "Descripción": [
                "Se selecciona un subconjunto representativo de los datos para trabajar de manera eficiente.",
                "Se analizan los datos para entender su comportamiento, patrones, relaciones y detectar anomalías.",
                "Se preparan y transforman los datos para mejorar su calidad y adecuarlos para el modelado.",
                "Se aplican técnicas de minería de datos para construir modelos que expliquen o predigan el comportamiento.",
                "Se evalúan los modelos desarrollados para asegurar su rendimiento, utilidad y confiabilidad."
            ]
        })

        st.dataframe(fases, use_container_width=True)

    # -----------------------------------------------------

    with tab3:

        st.subheader("Ventajas")
        st.markdown("""
     ✔  Ventaja 1 | Enfoque estructurado: Ofrece un proceso ordenado y secuencial que guía todas las etapas del proyecto de minería de datos.

     ✔ Ventaja 2 | Mejora la calidad de los datos:Incluye pasos para analizar y preparar los datos, asegurando que estén limpios y listos para el modelado.

     ✔ Ventaja 3 | Reduce riesgos:Permite identificar problemas desde etapas tempranas, evitando errores costosos más adelante.
     """)
        
    # -----------------------------------------------------

    with tab4:

        st.subheader("Desventajas")
                
        st.markdown("""
     ✘ Desventajas 1 | Consume tiempo:** Seguir todas las etapas puede tomar bastante tiempo, especialmente con grandes volúmenes de datos.

     ✘ Desventajas 2 | Requiere datos de calidad:** Si los datos iniciales son malos o incompletos, el resultado del proceso se ve afectado.. 

     ✘ Desventajas 3 | Depende de la experiencia:** Los resultados dependen del conocimiento y habilidades del equipo que aplica la metodología.
     """)

    # -----------------------------------------------------

    with tab5:

        st.subheader("Empresas")

        empresas = pd.DataFrame({

            "Empresa": ["SAS", "IBM", "Oracle"],
            "Uso": ["Desarrollo de modelos analíticos con herramientas como SAS Enterprise Miner.", "Integración de metodologías similares en analítica avanzada.", "Procesos de análisis de datos en sus plataformas."]
        })

        st.table(empresas)

    # -----------------------------------------------------

    with tab6:

      st.subheader("Aplicación Práctica")
      st.write("""
        El objetivo de esta aplicación es unificar datos educativos...
     """)

      st.title("Proyecto SEMMA con Datos de Estudiantes")

      st.markdown("Nombre: Juan Francisco Peña B.")
      st.markdown("Curso: M2A")
      st.markdown("Materia: Minería de Datos ")
      st.markdown("Tema: Comparativa de Metodologías ")

      st.markdown("## 1. Sample(Muestreo)")
      st.write("Objetivo: Analizar características de los estudiantes...")

      archivo1 = st.file_uploader("Subir archivo Excel 1", type=["xls","xlsx"])
      archivo2 = st.file_uploader("Subir archivo Excel 2", type=["xls","xlsx"])

      if archivo1 and archivo2:
        df1 = pd.read_excel(archivo1)
        df2 = pd.read_excel(archivo2)

        df = pd.concat([df1, df2], ignore_index=True)

        st.markdown("## 2. Exploración")

        st.subheader("Vista previa")
        st.dataframe(df.head())

        st.subheader("Información general")
        st.write(df.shape)
        st.write(df.dtypes)

        st.subheader("Valores nulos")
        st.write(df.isnull().sum())

        st.markdown("## 3. Modificación")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Distribución por sexo")
            fig, ax = plt.subplots()
            df["sexo"].value_counts().plot(kind="bar", ax=ax)
            st.pyplot(fig)

        with col2:
            st.subheader("Tipo de colegio")
            fig2, ax2 = plt.subplots()
            df["tipo_colegio"].value_counts().plot(kind="bar", ax=ax2)
            st.pyplot(fig2)

        st.subheader("Carreras con más estudiantes")
        fig3, ax3 = plt.subplots(figsize=(10,5))
        df["nombre_carrera"].value_counts().head(10).plot(kind="bar", ax=ax3)
        st.pyplot(fig3)

        st.markdown("## 4.  Modify")

        datos = df.copy()
        columnas = ["sexo","tipo_colegio","etnia","provincia_residencia","tipo_estudiante"]

        le = LabelEncoder()

        for col in columnas:
            datos[col] = datos[col].astype(str)
            datos[col] = le.fit_transform(datos[col])

        datos = datos.fillna(0)

        X = datos[["sexo","tipo_colegio","etnia","provincia_residencia"]]
        y = datos["tipo_estudiante"]

        st.write("Variables predictoras:", X.columns.tolist())

        st.markdown("## 5. Modelado")

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.3, random_state=42
        )

        modelo = RandomForestClassifier()
        modelo.fit(X_train, y_train)

        pred = modelo.predict(X_test)

        st.markdown("## 6. Asses")

        acc = accuracy_score(y_test, pred)
        st.metric("Accuracy", round(acc,2))

        st.subheader("Matriz de Confusión")
        st.write(confusion_matrix(y_test, pred))

        st.success("Proyecto SEMMA ejecutado correctamente.")   
 
            # AQUÍ COMPLETAR

# =========================================================
# TDSP
# =========================================================

elif opcion == "TDSP":

    st.header("Metodología TDSP")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "Descripción",
        "Fases",
        "Ventajas",
        "Desventajas",
        "Empresas",
        "Aplicación"
    ])

    # -----------------------------------------------------

    with tab1:

        st.subheader("Descripción")

        st.write("""
        Su objetivo es transformar datos en soluciones útiles para el negocio, 
        siguiendo fases como la comprensión del problema, análisis de datos, modelado, despliegue y validación de resultados.
        """)

    # -----------------------------------------------------

    with tab2:

        st.subheader("Fases")

        fases = pd.DataFrame({

            "Fase": [
                "COMPRENSIÓN DEL NEGOCIO",
                "ADQUISICIÓN Y COMPRENSIÓN DE DATOS",
                "MODELADO",
                "DESPLIEGUE",
                "ACEPTACIÓN DEL CLIENTE"
            ],

            "Descripción": [
                "Entender los objetivos del negocio, definir el problema y los criterios de éxito del proyecto.",
                "Recolectar, explorar y entender los datos disponibles para determinar su utilidad.",
                "Preparar los datos y aplicar técnicas y algoritmos para construir y evaluar modelos.",
                "Implementar el modelo en un entorno productivo e integrarlo con los procesos existentes.",
                "Validar los resultados con el cliente y asegurar que se cumplan los objetivos del negocio."
            ]
        })

        st.dataframe(fases, use_container_width=True)

    # -----------------------------------------------------

    with tab3:

        st.subheader("Ventajas")
        st.markdown("""
     ✔ Ventaja 1 | Define fases bien establecidas (negocio, datos, modelado, despliegue).

     ✔ Ventaja 2 | Pensado para equipos multidisciplinarios.

     ✔ Ventaja 3 | Facilita despliegue en la nube.
     """)


    # -----------------------------------------------------

    with tab4:

        st.subheader("Desventajas")
        
        st.markdown("""
     ✘ Desventajas 1 | Puede ser compleja para principiantes.

     ✘ Desventajas 2 | Está muy ligada a herramientas de Microsoft

     ✘ Desventajas 3 | No es ideal para proyectos rápidos o pequeños.
     """)
    # -----------------------------------------------------

    with tab5:

        st.subheader("Empresas")

        empresas = pd.DataFrame({

            "Empresa": ["Microsoft", "Accenture", "IBM"],
            "Uso": ["Desarrollo de soluciones de IA, análisis en Azure Machine Learning.", "Consultoría en analítica y transformación digital", "Aunque usan CRISP-DM, integran prácticas similares a TDSP"]
        })

        st.table(empresas)

    # -----------------------------------------------------

    with tab6:

      st.subheader("Aplicación Práctica")
      st.write("""
        El objetivo de esta aplicación es unificar datos educativos...
     """)
      
      st.title("Proyecto TDSP con Datos de Estudiantes")

      st.markdown("Nombre: Juan Francisco Peña B.")
      st.markdown("Curso: M2A")
      st.markdown("Materia: Minería de Datos ")
      st.markdown("Tema: Comparativa de Metodologías ")

      st.markdown("## 1. Comprensión del Negocio")
      st.write("Objetivo: Analizar características de los estudiantes...")

      archivo1 = st.file_uploader("Subir archivo Excel 1", type=["xls","xlsx"])
      archivo2 = st.file_uploader("Subir archivo Excel 2", type=["xls","xlsx"])

      if archivo1 and archivo2:
        df1 = pd.read_excel(archivo1)
        df2 = pd.read_excel(archivo2)

        df = pd.concat([df1, df2], ignore_index=True)

        st.markdown("## 2. Adquisición y Comprensión de Datos")

        st.subheader("Vista previa")
        st.dataframe(df.head())

        st.subheader("Información general")
        st.write(df.shape)
        st.write(df.dtypes)

        st.subheader("Valores nulos")
        st.write(df.isnull().sum())

        st.markdown("### Visualización")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Distribución por sexo")
            fig, ax = plt.subplots()
            df["sexo"].value_counts().plot(kind="bar", ax=ax)
            st.pyplot(fig)

        with col2:
            st.subheader("Tipo de colegio")
            fig2, ax2 = plt.subplots()
            df["tipo_colegio"].value_counts().plot(kind="bar", ax=ax2)
            st.pyplot(fig2)

        st.subheader("Carreras con más estudiantes")
        fig3, ax3 = plt.subplots(figsize=(10,5))
        df["nombre_carrera"].value_counts().head(10).plot(kind="bar", ax=ax3)
        st.pyplot(fig3)

        st.markdown("## 3.  Modelo")

        datos = df.copy()
        columnas = ["sexo","tipo_colegio","etnia","provincia_residencia","tipo_estudiante"]

        le = LabelEncoder()

        for col in columnas:
            datos[col] = datos[col].astype(str)
            datos[col] = le.fit_transform(datos[col])

        datos = datos.fillna(0)

        X = datos[["sexo","tipo_colegio","etnia","provincia_residencia"]]
        y = datos["tipo_estudiante"]

        st.write("Variables predictoras:", X.columns.tolist())

        st.markdown("## 4. Despliegue")

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.3, random_state=42
        )

        modelo = RandomForestClassifier()
        modelo.fit(X_train, y_train)

        pred = modelo.predict(X_test)

        st.markdown("## 5. Aceptación del Cliente")

        acc = accuracy_score(y_test, pred)
        st.metric("Accuracy", round(acc,2))

        st.subheader("Matriz de Confusión")
        st.write(confusion_matrix(y_test, pred))

        st.success("Proyecto SEMMA ejecutado correctamente.")   


            # AQUÍ COMPLETAR

# =========================================================
# COMPARATIVA
# =========================================================

elif opcion == "Comparativa":

    st.header("Comparativa General")

    comparativa = pd.DataFrame({

        "Aspecto": [
            "Cantidad de fases",
            "Orientación",
            "Uso empresarial",
            "Nivel técnico",
            "Flexibilidad"
        ],

        "KDD": ["5 fases", "Descubrimiento de conocimiento", "Medio", "Alto", "Media"],

        "CRISP-DM": ["6 fases", "Negocio + datos", "Alto (muy usado en empresas)", "Medio", "Alta"],

        "SEMMA": ["5 fases", "Modelado y análisis", "Medio (SAS principalmente)", "Alto", "Baja - Media"],

        "TDSP": ["5 fases", "Solución completa (end-to-end)", "Alto (Microsoft y proyectos reales)", "Medio - Alto", "Alta"]
    })

    st.dataframe(comparativa, use_container_width=True)

    st.subheader("Conclusión")

    st.write("""
    Las metodologías tienen enfoques diferentes pero complementarios. 
    CRISP-DM es la más equilibrada y utilizada en empresas porque conecta bien el negocio con los datos. KDD es más teórica y enfocada en el descubrimiento de conocimiento. 
    SEMMA es técnica y centrada en el modelado, ideal para análisis estadístico. Por último, TDSP es más moderna y práctica, diseñada para proyectos completos de ciencia de datos en entornos reales.

    En general, si buscas algo empresarial y flexible → CRISP-DM o TDSP, mientras que si el enfoque es más técnico o académico → KDD o SEMMA..
    """)

# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "Proyecto académico desarrollado con Streamlit."
)