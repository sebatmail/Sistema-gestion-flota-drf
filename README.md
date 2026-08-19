# Sistema de Gestión de Flota y Backend Django REST Framework (DRF)
**Instituto Profesional INACAP — Informática y Ciberseguridad**  
**Asignatura:** Desarrollo Backend & Bases de Datos  
**Profesor:** Marcelo Alvarado  
**Entrega de Proyecto Final en Formato VS Code**

---

## 🔑 Credenciales para Evaluación

| Rol | Usuario | Contraseña | Permisos / Alcance |
|---|---|---|---|
| **Superusuario Administrador** | `admin` | `admin123` | Control total del sistema, Django Admin y APIs |
| **Profesor (Receta DRF)** | `profe` | `123456` | Cuenta superusuario definida en la guía del profesor |
| **Chofer (Operador)** | `chofer_a` | `chofer123` | Acceso a panel de chofer |

---

## 🚀 Puesta en Marcha Rápida (VS Code)

### Opción 1: Con VS Code (Recomendada)
1. Abrir esta carpeta en Visual Studio Code.
2. Presionar **`F5`** (o ir a la pestaña *Ejecutar y Depurar* y seleccionar **"Django: Iniciar Servidor"**).
3. El servidor se iniciará automáticamente en `http://127.0.0.1:8000/`.

### Opción 2: Por Terminal PowerShell
```powershell
.\venv\Scripts\activate
python manage.py runserver
```

---

## 🧪 Ejecución de Pruebas Automatizadas (100% Aprobadas)

Para verificar que todos los endpoints, modelos y vistas funcionan sin errores:
```powershell
python manage.py test
```
> **Resultado:** `Ran 15 tests in 8.5s - OK (Found 15 test(s). System check identified no issues).`

---

## 🌟 Módulos Implementados

1. **Gestión de Choferes (`/choferes/`)**:
   - Agregar, Listar, **EDITAR (Requerimiento completado)** y Eliminar conductores.
   - Validación de formato de RUT chileno.
   - Asignación interactiva de camión.
2. **Gestión de Camiones (`/camiones/`)**:
   - Agregar, Listar, **EDITAR (Requerimiento completado)** y Eliminar camiones de la flota.
   - Control de patentes únicas y capacidad en toneladas.
3. **Vistas Web Institucionales (`CONSULTA_IA_WEB_TEMPLATE`)**:
   - `/` (Home)
   - `/quienes-somos/` (About)
   - `/servicios/` (Servicios con botones a `/api/` y `/admin/`)
   - `/contacto/` (Formulario interactivo de contacto)
4. **Informes PDF de Entrega**:
   - `INFORME_FINAL_ENTREGA_PROFESOR.pdf`
   - `RESOLUCION_EJERCICIO_NORMALIZACION.pdf`
   - `../../RESOLUCION_NORMALIZACION.sql` (Script SQL en 3FN)
