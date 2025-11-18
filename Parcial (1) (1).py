# ============================================================
# SISTEMA DE GESTIÓN ACADÉMICA - ARCHIVO COMPLETO ACTUALIZADO
# Contiene: Estudiantes, Profesores, Cursos, Inscripciones, Calificaciones
# ============================================================

# ---------------------------
# MÓDULO: GESTIÓN DE ESTUDIANTES
# ---------------------------

# Lista donde se almacenarán los estudiantes
estudiantes = []

# ----------------------------------------------------------
# FUNCIÓN: buscar_indice_estudiante
# Busca un estudiante en la lista usando el código.
# Si lo encuentra devuelve su posición, si no devuelve -1.
# ----------------------------------------------------------
def buscar_indice_estudiante(codigo):
    for i in range(len(estudiantes)):
        if estudiantes[i]['codigo'] == codigo:
            return i
    return -1

# ----------------------------------------------------------
# FUNCIÓN: registrar_estudiante
# Crea un nuevo estudiante y lo agrega a la lista
# ----------------------------------------------------------
def registrar_estudiante(codigo, nombre, programa, semestre, creditos_cursados=0):
    if buscar_indice_estudiante(codigo) != -1:
        print("Ya existe un estudiante con ese código.")
        return False

    estudiante = {
        'codigo': codigo,
        'nombre': nombre,
        'programa': programa,
        'semestre': semestre,
        'creditos_cursados': creditos_cursados,
        # historial: lista de diccionarios con claves:
        # 'curso' (codigo), 'nota' (nota definitiva, 0 si sin nota),
        # 'estado' ('inscrito','aprobado','reprobado'), opcional campos de componentes
        'historial': []
    }

    estudiantes.append(estudiante)
    print("Estudiante registrado correctamente.")
    return True

# ----------------------------------------------------------
# FUNCIÓN: actualizar_estudiante
# Permite modificar nombre, programa o semestre
# ----------------------------------------------------------
def actualizar_estudiante(codigo, nombre=None, programa=None, semestre=None):
    idx = buscar_indice_estudiante(codigo)

    if idx == -1:
        print("No existe un estudiante con ese código.")
        return False

    if nombre is not None and nombre != "":
        estudiantes[idx]['nombre'] = nombre

    if programa is not None and programa != "":
        estudiantes[idx]['programa'] = programa

    if semestre is not None and semestre != "":
        try:
            estudiantes[idx]['semestre'] = int(semestre)
        except:
            print("Semestre ingresado inválido. No se cambió ese campo.")

    print("Estudiante actualizado correctamente.")
    return True

# ----------------------------------------------------------
# FUNCIÓN: mostrar_estudiantes
# Muestra todos los estudiantes registrados
# ----------------------------------------------------------
def mostrar_estudiantes():
    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
        return

    print("\nLISTA DE ESTUDIANTES REGISTRADOS:")
    print("----------------------------------")

    for est in estudiantes:
        print(f"Código: {est['codigo']}")
        print(f"Nombre: {est['nombre']}")
        print(f"Programa: {est['programa']}")
        print(f"Semestre: {est['semestre']}")
        print(f"Créditos cursados: {est['creditos_cursados']}")
        print("----------------------------------")

# ----------------------------------------------------------
# MENÚ DEL MÓDULO DE ESTUDIANTES
# ----------------------------------------------------------
def menu_estudiantes():
    while True:
        print("\n===== MENÚ DE GESTIÓN DE ESTUDIANTES =====")
        print("1. Registrar estudiante")
        print("2. Actualizar estudiante")
        print("3. Ver lista de estudiantes")
        print("4. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n--- REGISTRO DE ESTUDIANTE ---")
            codigo = input("Código del estudiante: ")
            nombre = input("Nombre completo: ")
            programa = input("Programa académico: ")
            try:
                semestre = int(input("Semestre actual (número): "))
            except:
                print("Semestre inválido. Se usará 1 por defecto.")
                semestre = 1
            try:
                creditos = int(input("Créditos cursados (número, 0 si es nuevo): "))
            except:
                print("Créditos inválidos. Se usará 0 por defecto.")
                creditos = 0

            registrar_estudiante(codigo, nombre, programa, semestre, creditos)

        elif opcion == "2":
            print("\n--- ACTUALIZAR ESTUDIANTE ---")
            codigo = input("Código del estudiante a actualizar: ")

            print("Deja un campo vacío si NO deseas modificarlo.")
            nuevo_nombre = input("Nuevo nombre: ")
            nuevo_programa = input("Nuevo programa: ")
            nuevo_semestre = input("Nuevo semestre (número): ")

            actualizar_estudiante(codigo, nuevo_nombre, nuevo_programa, nuevo_semestre)

        elif opcion == "3":
            mostrar_estudiantes()

        elif opcion == "4":
            break

        else:
            print("Opción incorrecta.")


# ---------------------------
# MÓDULO: GESTIÓN DE PROFESORES
# ---------------------------

# Diccionario para guardar profesores
profesores = {}

# ------------------------------------------------------------
# FUNCIÓN: registrar_profesor
# ------------------------------------------------------------
def registrar_profesor():
    print("\n=== REGISTRO DE PROFESOR ===")
    
    id_profesor = input("Ingrese el ID del profesor: ")
    nombre = input("Ingrese el nombre del profesor: ")
    departamento = input("Ingrese el departamento al que pertenece: ")

    profesor = {
        "id": id_profesor,
        "nombre": nombre,
        "departamento": departamento,
        "cursos_asignados": []
    }

    profesores[id_profesor] = profesor
    print("\n>>> Profesor registrado correctamente.")

# ------------------------------------------------------------
# FUNCIÓN: asignar_curso_profesor
# ------------------------------------------------------------
def asignar_curso_profesor():
    print("\n=== ASIGNAR CURSO A PROFESOR ===")

    id_profesor = input("Ingrese el ID del profesor: ")

    if id_profesor not in profesores:
        print("ERROR: El profesor no está registrado.")
        return

    codigo_curso = input("Ingrese el código del curso a asignar: ")

    profesor = profesores[id_profesor]

    if codigo_curso in profesor["cursos_asignados"]:
        print("El profesor ya tiene este curso asignado.")
        return

    profesor["cursos_asignados"].append(codigo_curso)

    print("\n>>> Curso asignado exitosamente al profesor.")

# ------------------------------------------------------------
# FUNCIÓN: calcular_carga_profesor
# ------------------------------------------------------------
def calcular_carga_profesor(profesor, cursos):
    total_creditos = 0

    for codigo in profesor["cursos_asignados"]:
        if codigo in cursos:
            creditos = cursos[codigo]["creditos"]
            total_creditos += creditos

    return total_creditos

# ------------------------------------------------------------
# FUNCIÓN: mostrar_profesor
# ------------------------------------------------------------
def mostrar_profesor(cursos):
    print("\n=== CONSULTAR PROFESOR ===")
    id_profesor = input("Ingrese el ID del profesor: ")

    if id_profesor not in profesores:
        print("ERROR: No existe un profesor con ese ID.")
        return

    profesor = profesores[id_profesor]

    carga = calcular_carga_profesor(profesor, cursos)

    print("\n--- INFORMACIÓN DEL PROFESOR ---")
    print("Nombre:", profesor["nombre"])
    print("Departamento:", profesor["departamento"])
    print("Cursos asignados:", profesor["cursos_asignados"])
    print("Carga académica total (créditos):", carga)

# ------------------------------------------------------------
# MENÚ DEL MÓDULO DE PROFESORES
# ------------------------------------------------------------
def menu_profesores(cursos):
    while True:
        print("\n========== MENÚ DE PROFESORES ==========")
        print("1. Registrar profesor")
        print("2. Asignar curso")
        print("3. Mostrar profesor")
        print("4. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_profesor()
        elif opcion == "2":
            asignar_curso_profesor()
        elif opcion == "3":
            mostrar_profesor(cursos)
        elif opcion == "4":
            break
        else:
            print("Opción inválida, intente de nuevo.")


# ============================================================
#   REQUERIMIENTO 3: GESTIÓN DE CURSOS
# ============================================================

# Diccionario donde se almacenarán los cursos
cursos = {}

# ------------------------------------------------------------
# FUNCIÓN: registrar_curso
# Crea un curso nuevo con código, nombre, créditos y cupos
# ------------------------------------------------------------
def registrar_curso():
    print("\n=== REGISTRO DE CURSO ===")

    codigo = input("Código del curso: ")

    if codigo in cursos:
        print("ERROR: Ya existe un curso con ese código.")
        return

    nombre = input("Nombre del curso: ")
    try:
        creditos = int(input("Número de créditos: "))
    except:
        print("Créditos inválidos. Se usará 1 por defecto.")
        creditos = 1
    try:
        cupos = int(input("Cantidad de cupos disponibles: "))
    except:
        print("Cupos inválidos. Se usará 0 por defecto.")
        cupos = 0

    curso = {
        "nombre": nombre,
        "creditos": creditos,
        "cupos": cupos,
        "prerrequisitos": []
    }

    cursos[codigo] = curso
    print(">>> Curso registrado correctamente.")

# ------------------------------------------------------------
# FUNCIÓN: agregar_prerrequisito
# ------------------------------------------------------------
def agregar_prerrequisito():
    print("\n=== AGREGAR PRERREQUISITO ===")

    codigo = input("Código del curso principal: ")

    if codigo not in cursos:
        print("ERROR: Ese curso no existe.")
        return

    codigo_pre = input("Código del curso prerrequisito: ")

    if codigo_pre not in cursos:
        print("ERROR: El curso prerrequisito no existe.")
        return

    if codigo_pre in cursos[codigo]["prerrequisitos"]:
        print("Ese prerrequisito ya está registrado.")
        return

    cursos[codigo]["prerrequisitos"].append(codigo_pre)

    print(">>> Prerrequisito agregado correctamente.")

# ------------------------------------------------------------
# FUNCIÓN: mostrar_cursos
# ------------------------------------------------------------
def mostrar_cursos():
    print("\n=== LISTA DE CURSOS REGISTRADOS ===")

    if len(cursos) == 0:
        print("No hay cursos registrados.")
        return

    for codigo, info in cursos.items():
        print("------------------------------------")
        print("Código:", codigo)
        print("Nombre:", info["nombre"])
        print("Créditos:", info["creditos"])
        print("Cupos:", info["cupos"])
        print("Prerrequisitos:", info["prerrequisitos"])
    print("------------------------------------")

# ------------------------------------------------------------
# FUNCIÓN: verificar_cupos
# ------------------------------------------------------------
def verificar_cupos():
    print("\n=== VERIFICAR CUPOS ===")

    codigo = input("Código del curso: ")

    if codigo not in cursos:
        print("ERROR: Ese curso no existe.")
        return

    cupos = cursos[codigo]["cupos"]

    if cupos > 0:
        print(f"Sí hay cupos disponibles ({cupos} cupos).")
    else:
        print("NO hay cupos disponibles.")

# ------------------------------------------------------------
# MENÚ DEL MÓDULO DE CURSOS
# ------------------------------------------------------------
def menu_cursos():
    while True:
        print("\n========== MENÚ DE CURSOS ==========")
        print("1. Registrar curso")
        print("2. Agregar prerrequisito")
        print("3. Ver lista de cursos")
        print("4. Verificar cupos")
        print("5. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_curso()
        elif opcion == "2":
            agregar_prerrequisito()
        elif opcion == "3":
            mostrar_cursos()
        elif opcion == "4":
            verificar_cupos()
        elif opcion == "5":
            break
        else:
            print("Opción inválida, intente de nuevo.")


# ============================================================
#   MÓDULO DE SISTEMA DE INSCRIPCIÓN
# ============================================================

# ------------------------------------------------------------
# FUNCIÓN: inscribir_estudiante_en_curso
# ------------------------------------------------------------
def inscribir_estudiante_en_curso():

    print("\n=== INSCRIPCIÓN A CURSO ===")

    codigo_est = input("Código del estudiante: ")
    codigo_curso = input("Código del curso: ")

    # Validar estudiante
    idx_est = buscar_indice_estudiante(codigo_est)
    if idx_est == -1:
        print("ERROR: El estudiante no existe.")
        return

    # Validar curso
    if codigo_curso not in cursos:
        print("ERROR: El curso no existe.")
        return

    estudiante = estudiantes[idx_est]
    curso = cursos[codigo_curso]

    # Validar si ya está inscrito
    for registro in estudiante["historial"]:
        if registro["curso"] == codigo_curso:
            print("ERROR: El estudiante ya está inscrito en este curso.")
            return

    # Validar cupos
    if curso["cupos"] <= 0:
        print("ERROR: NO hay cupos disponibles para este curso.")
        return

    # Validar prerrequisitos
    for pre in curso["prerrequisitos"]:
        aprobado = False

        for reg in estudiante["historial"]:
            if reg["curso"] == pre and reg.get("nota",0) >= 3.0:
                aprobado = True
                break

        if not aprobado:
            print(f"ERROR: No cumple el prerrequisito: {pre}")
            return

    # Registrar inscripción
    curso["cupos"] -= 1  # Reducir cupos del curso

    # Guardamos la inscripción en historial con nota 0.0 y estado 'inscrito'
    estudiante["historial"].append({
        "curso": codigo_curso,
        "nota": 0.0,
        "estado": "inscrito"
    })

    print("\n>>> Estudiante inscrito correctamente.")

# ------------------------------------------------------------
# FUNCIÓN: mostrar_inscripciones
# ------------------------------------------------------------
def mostrar_inscripciones():
    print("\n=== CONSULTA DE INSCRIPCIONES ===")

    codigo_est = input("Código del estudiante: ")
    idx_est = buscar_indice_estudiante(codigo_est)

    if idx_est == -1:
        print("ERROR: Estudiante no encontrado.")
        return

    estudiante = estudiantes[idx_est]

    print(f"\nHistorial académico de {estudiante['nombre']}:")
    print("-------------------------------------------")

    if len(estudiante["historial"]) == 0:
        print("No tiene cursos inscritos.")
        return

    for reg in estudiante["historial"]:
        print(f"Curso: {reg['curso']}  | Nota: {reg.get('nota',0.0)}  | Estado: {reg.get('estado','-')}")
    print("-------------------------------------------")

# ------------------------------------------------------------
# MENÚ DEL MÓDULO DE INSCRIPCIÓN
# ------------------------------------------------------------
def menu_inscripcion():
    while True:
        print("\n========== MÓDULO DE INSCRIPCIÓN ==========")
        print("1. Inscribir estudiante en un curso")
        print("2. Ver cursos inscritos del estudiante")
        print("3. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            inscribir_estudiante_en_curso()
        elif opcion == "2":
            mostrar_inscripciones()
        elif opcion == "3":
            break
        else:
            print("Opción inválida.")


# ============================================================
#   MÓDULO 5: SISTEMA DE CALIFICACIONES
# ============================================================

# ------------------------------------------------------------
# FUNCIÓN: listar_estudiantes_por_curso
# Devuelve una lista de tuplas (indice_estudiante, estudiante, registro_historial)
# para los estudiantes que tienen inscrito el curso (estado 'inscrito' o 'reprobado' o 'aprobado')
# ------------------------------------------------------------
def listar_estudiantes_por_curso(codigo_curso):
    lista = []
    for idx, est in enumerate(estudiantes):
        for reg in est["historial"]:
            if reg["curso"] == codigo_curso:
                lista.append((idx, est, reg))
    return lista

# ------------------------------------------------------------
# FUNCIÓN: registrar_notas_para_un_estudiante
# Pide las notas de parciales, trabajos y examen final (con ponderaciones),
# calcula la nota definitiva y actualiza el historial y créditos si aprueba.
# ------------------------------------------------------------
def registrar_notas_para_un_estudiante(idx_est, estudiante, registro_historial):
    print(f"\n--- Registrar notas para {estudiante['nombre']} (código {estudiante['codigo']}) ---")
    codigo_curso = registro_historial["curso"]

    # Mostrar créditos del curso (si existe)
    creditos_curso = cursos[codigo_curso]["creditos"] if codigo_curso in cursos else 0
    print(f"Créditos del curso: {creditos_curso}")

    # Pedimos las ponderaciones. Para hacerlo simple ofrecemos valores por defecto.
    print("\nIngrese las ponderaciones en porcentaje (sumarán 100). Presione ENTER para usar los valores por defecto:")
    try:
        w_parciales = input("Peso parciales (porcentaje) [por defecto 30]: ")
        w_parciales = float(w_parciales) if w_parciales.strip() != "" else 30.0
        w_trabajos = input("Peso trabajos (porcentaje) [por defecto 30]: ")
        w_trabajos = float(w_trabajos) if w_trabajos.strip() != "" else 30.0
        w_examen = input("Peso examen final (porcentaje) [por defecto 40]: ")
        w_examen = float(w_examen) if w_examen.strip() != "" else 40.0
    except:
        print("Entrada inválida. Se usarán ponderaciones por defecto 30/30/40.")
        w_parciales, w_trabajos, w_examen = 30.0, 30.0, 40.0

    suma_pesos = w_parciales + w_trabajos + w_examen
    if abs(suma_pesos - 100.0) > 0.001:
        print(f"Advertencia: las ponderaciones suman {suma_pesos}, se normalizarán automáticamente.")
        # normalizar para que sumen 100
        w_parciales = w_parciales * 100.0 / suma_pesos
        w_trabajos = w_trabajos * 100.0 / suma_pesos
        w_examen = w_examen * 100.0 / suma_pesos

    # Pedimos las notas (0.0 - 5.0)
    def pedir_nota(texto):
        while True:
            try:
                val = input(texto)
                if val.strip() == "":
                    return 0.0
                n = float(val)
                if 0.0 <= n <= 5.0:
                    return n
                else:
                    print("La nota debe estar entre 0.0 y 5.0.")
            except:
                print("Entrada inválida. Intente de nuevo.")

    nota_parciales = pedir_nota("Ingrese nota promedio de parciales (0-5): ")
    nota_trabajos = pedir_nota("Ingrese nota promedio de trabajos (0-5): ")
    nota_examen = pedir_nota("Ingrese nota del examen final (0-5): ")

    # Calculamos nota definitiva (en escala 0-5)
    nota_def = (nota_parciales * (w_parciales/100.0) +
                nota_trabajos * (w_trabajos/100.0) +
                nota_examen * (w_examen/100.0))

    # Redondeamos a 3 decimales
    nota_def = round(nota_def, 3)

    # Actualizamos el registro en el historial
    registro_historial["nota"] = nota_def
    registro_historial["componentes"] = {
        "parciales": nota_parciales,
        "trabajos": nota_trabajos,
        "examen": nota_examen,
        "pesos": {
            "parciales": w_parciales,
            "trabajos": w_trabajos,
            "examen": w_examen
        }
    }

    # Determinamos si aprobó (>= 3.0)
    if nota_def >= 3.0:
        registro_historial["estado"] = "aprobado"
        # Actualizar créditos cursados si aún no estaban contados
        # Verificar si esos créditos ya fueron sumados: buscamos si existe una bandera 'creditos_sumados'
        if not registro_historial.get("creditos_sumados", False):
            if codigo_curso in cursos:
                estudiantes[idx_est]["creditos_cursados"] += creditos_curso
                registro_historial["creditos_sumados"] = True
    else:
        registro_historial["estado"] = "reprobado"
        # No sumamos créditos si reprobó (y si previamente los había sumado, se debe restar — aquí asumimos que si sumó fue por aprobada antes)
        if registro_historial.get("creditos_sumados", False):
            # Esto es raro: si estaba marcado como sumados pero ahora reprobó, restamos
            if codigo_curso in cursos:
                estudiantes[idx_est]["creditos_cursados"] -= creditos_curso
            registro_historial["creditos_sumados"] = False

    # Mensaje resumen
    print(f"\nNota definitiva registrada: {nota_def}")
    print(f"Estado del curso: {registro_historial['estado']}")
    print(f"Créditos cursados actuales del estudiante: {estudiantes[idx_est]['creditos_cursados']}")

# ------------------------------------------------------------
# FUNCIÓN: registrar_notas_por_curso
# Lista estudiantes inscritos en un curso y permite seleccionar
# uno por uno para registrar sus notas.
# ------------------------------------------------------------
def registrar_notas_por_curso():
    print("\n=== REGISTRAR NOTAS POR CURSO ===")
    codigo_curso = input("Ingrese el código del curso: ")

    if codigo_curso not in cursos:
        print("ERROR: Curso no encontrado.")
        return

    lista = listar_estudiantes_por_curso(codigo_curso)

    if len(lista) == 0:
        print("No hay estudiantes inscritos en este curso.")
        return

    # Mostramos los estudiantes con índice local
    print("\nEstudiantes inscritos:")
    for i, (idx_est, est, reg) in enumerate(lista):
        print(f"{i+1}. {est['codigo']} - {est['nombre']} | Nota actual: {reg.get('nota',0.0)} | Estado: {reg.get('estado','inscrito')}")

    # Pedimos seleccionar uno
    try:
        sel = int(input("Seleccione el número del estudiante para registrar nota (0 para cancelar): "))
    except:
        print("Selección inválida.")
        return

    if sel == 0:
        return
    if sel < 1 or sel > len(lista):
        print("Selección fuera de rango.")
        return

    idx_est, est, reg = lista[sel-1]
    registrar_notas_para_un_estudiante(idx_est, est, reg)

# ------------------------------------------------------------
# FUNCIÓN: calcular_nota_definitiva_directa
# Permite calcular la nota definitiva si ya conoces los componentes sin guardarla.
# (útil para verificar)
# ------------------------------------------------------------
def calcular_nota_definitiva_directa():
    print("\n=== CALCULAR NOTA DEFINITIVA (sin guardar) ===")
    try:
        w_par = float(input("Peso parciales (%) [ej. 30]: "))
        w_tra = float(input("Peso trabajos (%) [ej. 30]: "))
        w_ex = float(input("Peso examen (%) [ej. 40]: "))
    except:
        print("Entrada inválida. Abortando.")
        return
    suma = w_par + w_tra + w_ex
    if abs(suma - 100.0) > 0.001:
        print("Las ponderaciones no suman 100. Normalizando...")
        w_par = w_par * 100.0 / suma
        w_tra = w_tra * 100.0 / suma
        w_ex = w_ex * 100.0 / suma
    try:
        n_par = float(input("Nota parciales (0-5): "))
        n_tra = float(input("Nota trabajos (0-5): "))
        n_ex = float(input("Nota examen (0-5): "))
    except:
        print("Entrada inválida. Abortando.")
        return
    nota_def = n_par*(w_par/100.0) + n_tra*(w_tra/100.0) + n_ex*(w_ex/100.0)
    print(f"Nota definitiva (calculada): {round(nota_def,3)}")

# ------------------------------------------------------------
# MENÚ DEL MÓDULO DE CALIFICACIONES
# ------------------------------------------------------------
def menu_calificaciones():
    while True:
        print("\n========== MENÚ DE CALIFICACIONES ==========")
        print("1. Registrar nota a un estudiante (por curso)")
        print("2. Registrar notas para un estudiante específico (buscar por código)")
        print("3. Calcular nota definitiva sin guardar")
        print("4. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_notas_por_curso()
        elif opcion == "2":
            # Buscar estudiante por código y mostrar sus cursos inscritos
            codigo_est = input("Código del estudiante: ")
            idx = buscar_indice_estudiante(codigo_est)
            if idx == -1:
                print("Estudiante no encontrado.")
            else:
                est = estudiantes[idx]
                # listar cursos en su historial
                inscritos = [reg for reg in est["historial"]]
                if len(inscritos) == 0:
                    print("No tiene cursos inscritos.")
                else:
                    print("Cursos del estudiante:")
                    for i, reg in enumerate(inscritos):
                        print(f"{i+1}. {reg['curso']} | Nota actual: {reg.get('nota',0.0)} | Estado: {reg.get('estado','inscrito')}")
                    try:
                        sel = int(input("Seleccione el número del curso para registrar nota (0 cancelar): "))
                    except:
                        print("Selección inválida.")
                        sel = -1
                    if sel == 0:
                        pass
                    elif 1 <= sel <= len(inscritos):
                        registrar_notas_para_un_estudiante(idx, est, inscritos[sel-1])
                    else:
                        print("Selección fuera de rango.")
        elif opcion == "3":
            calcular_nota_definitiva_directa()
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")


            # ===============================================================
#               MÓDULO DE REPORTES ACADÉMICOS
# ===============================================================

# ---------------------------------------------------------------
# 1. HISTORIAL ACADÉMICO DE UN ESTUDIANTE
# ---------------------------------------------------------------
def reporte_historial_estudiante():
    print("\n=== HISTORIAL ACADÉMICO DEL ESTUDIANTE ===")
    codigo = input("Ingrese el código del estudiante: ")

    idx = buscar_indice_estudiante(codigo)
    if idx == -1:
        print("ERROR: No existe un estudiante con ese código.")
        return

    estudiante = estudiantes[idx]

    print("\n--- DATOS DEL ESTUDIANTE ---")
    print("Nombre: ", estudiante["nombre"])
    print("Programa: ", estudiante["programa"])
    print("Semestre: ", estudiante["semestre"])
    print("Créditos cursados: ", estudiante["creditos_cursados"])

    print("\n--- HISTORIAL DE CURSOS ---")
    if len(estudiante["historial"]) == 0:
        print("No hay cursos registrados.")
        return

    for item in estudiante["historial"]:
        print("-------------------------------------")
        print("Curso:", item["codigo"])
        print("Nombre:", cursos[item["codigo"]]["nombre"])
        print("Nota definitiva:", item["nota_def"])
        print("Estado:", "Aprobado" if item["nota_def"] >= 3.0 else "Reprobado")
    print("-------------------------------------")


# ---------------------------------------------------------------
# 2. CURSOS CON MAYOR TASA DE REPROBACIÓN
# ---------------------------------------------------------------
def reporte_cursos_reprobacion():
    print("\n=== CURSOS CON MAYOR TASA DE REPROBACIÓN ===")

    estadisticas = {}

    for est in estudiantes:
        for item in est["historial"]:
            cod = item["codigo"]
            if cod not in estadisticas:
                estadisticas[cod] = {"aprob": 0, "reprob": 0}
            if item["nota_def"] >= 3.0:
                estadisticas[cod]["aprob"] += 1
            else:
                estadisticas[cod]["reprob"] += 1

    # Ordenar por tasa de reprobados
    ranking = sorted(
        estadisticas.items(),
        key=lambda x: x[1]["reprob"],
        reverse=True
    )

    for cod, info in ranking:
        total = info["aprob"] + info["reprob"]
        tasa = (info["reprob"] / total) * 100 if total > 0 else 0
        print(f"Curso {cod} - Reprobación: {tasa:.2f}% ({info['reprob']} / {total})")


# ---------------------------------------------------------------
# 3. ESTUDIANTES CON MEJOR PROMEDIO POR PROGRAMA
# ---------------------------------------------------------------
def reporte_mejor_promedio():
    print("\n=== ESTUDIANTES CON MEJOR PROMEDIO POR PROGRAMA ===")

    programas = {}

    for est in estudiantes:
        PPA = est.get("PPA", 0)

        prog = est["programa"]
        if prog not in programas:
            programas[prog] = []
        programas[prog].append((est["nombre"], PPA))

    for prog, lista in programas.items():
        lista.sort(key=lambda x: x[1], reverse=True)
        mejor = lista[0]
        print(f"\nPrograma: {prog}")
        print("Mejor estudiante:", mejor[0])
        print("PPA:", mejor[1])


# ---------------------------------------------------------------
# 4. PROFESORES MEJOR EVALUADOS
# (Promedio de las notas de todos los cursos que dicta)
# ---------------------------------------------------------------
def reporte_profesores_mejor_evaluados():
    print("\n=== PROFESORES MEJOR EVALUADOS ===")

    evaluaciones = {}

    for idp, prof in profesores.items():
        notas = []

        for est in estudiantes:
            for item in est["historial"]:
                curso_cod = item["codigo"]
                if curso_cod in prof["cursos_asignados"]:
                    notas.append(item["nota_def"])

        if len(notas) > 0:
            evaluaciones[idp] = sum(notas) / len(notas)
        else:
            evaluaciones[idp] = 0

    ranking = sorted(evaluaciones.items(), key=lambda x: x[1], reverse=True)

    for idp, prom in ranking:
        print(f"Profesor {profesores[idp]['nombre']} - Evaluación promedio: {prom:.2f}")


# ---------------------------------------------------------------
# 5. CORRELACIÓN ENTRE PRERREQUISITOS Y RENDIMIENTO
# ---------------------------------------------------------------
def reporte_correlacion_prerrequisitos():
    print("\n=== ANÁLISIS DE CORRELACIÓN PRERREQUISITOS - RENDIMIENTO ===")

    for cod, curso in cursos.items():
        if len(curso["prerrequisitos"]) == 0:
            continue  # No aplica

        notas_prer = []
        notas_final = []

        for est in estudiantes:
            notas_est = {c["codigo"]: c["nota_def"] for c in est["historial"]}

            # Verificar si cursó los prerrequisitos
            if all(pre in notas_est for pre in curso["prerrequisitos"]):
                # promedio de prerrequisitos
                promedio_pre = sum(notas_est[pre] for pre in curso["prerrequisitos"]) / len(curso["prerrequisitos"])

                # nota del curso principal
                if cod in notas_est:
                    nota_curso = notas_est[cod]
                    notas_prer.append(promedio_pre)
                    notas_final.append(nota_curso)

        if len(notas_prer) == 0:
            continue

        # Calcular correlación (simplificada)
        correlacion = sum(
            (notas_prer[i] - sum(notas_prer) / len(notas_prer)) *
            (notas_final[i] - sum(notas_final) / len(notas_final))
            for i in range(len(notas_prer))
        )

        print(f"\nCurso {cod} ({curso['nombre']})")
        print("Prerrequisitos:", curso["prerrequisitos"])
        print("Correlación rendimiento:", round(correlacion, 2))


# ---------------------------------------------------------------
# MENÚ DE REPORTES
# ---------------------------------------------------------------
def menu_reportes():
    while True:
        print("\n========== MENÚ DE REPORTES ==========")
        print("1. Historial académico de un estudiante")
        print("2. Cursos con mayor tasa de reprobación")
        print("3. Mejor promedio por programa")
        print("4. Profesores mejor evaluados")
        print("5. Correlación prerrequisitos – rendimiento")
        print("6. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            reporte_historial_estudiante()
        elif opcion == "2":
            reporte_cursos_reprobacion()
        elif opcion == "3":
            reporte_mejor_promedio()
        elif opcion == "4":
            reporte_profesores_mejor_evaluados()
        elif opcion == "5":
            reporte_correlacion_prerrequisitos()
        elif opcion == "6":
            break
        else:
            print("Opción inválida.")


# ===============================================================
#                MENÚ PRINCIPAL DEL SISTEMA
# ===============================================================
def menu_principal():
    while True:
        print("\n============ SISTEMA DE GESTIÓN UNIVERSITARIA ============")
        print("Seleccione el módulo que desea gestionar:")
        print("1. Gestión de Estudiantes")
        print("2. Gestión de Profesores")
        print("3. Gestión de Cursos")
        print("4. Gestión de Inscripciones")
        print("5. Calificaciones")
        print("6. Reportes Académicos")
        print("7. Salir del sistema")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            menu_estudiantes()
        elif opcion == "2":
            menu_profesores(cursos)
        elif opcion == "3":
            menu_cursos()
        elif opcion == "4":
            menu_inscripcion()
        elif opcion == "5":
            menu_calificaciones()
        elif opcion == "6":
            menu_reportes()
        elif opcion == "7":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

# Ejecutamos el menú principal cuando se ejecute este archivo
if __name__ == "__main__":
    menu_principal()
    