# Sistema de Gestión de Flota y Resolución de Normalización BD
**Instituto Profesional INACAP — Informática y Ciberseguridad**  
**Asignatura:** Desarrollo Backend & Bases de Datos  
**Profesor:** Marcelo Alvarado  
**Entrega de Proyecto Final en Formato VS Code**

---

## 📁 Estructura del Entregable

```
Trabajo Receta/
│
├── INFORME_FINAL_ENTREGA_PROFESOR.pdf      # [PDF] Informe académico consolidado
├── RESOLUCION_EJERCICIO_NORMALIZACION.pdf  # [PDF] Resolución formal Diapositiva 24
├── RESOLUCION_NORMALIZACION.sql            # [SQL] Script DDL y DML en 3FN
├── generate_reports.py                     # [Python] Script generador de PDFs
│
├── flota/flota/                            # [PROYECTO DJANGO REST FRAMEWORK]
│   ├── .vscode/                            # Configuración de F5 y entorno VS Code
│   │   ├── launch.json
│   │   └── settings.json
│   ├── flota_app/                          # Aplicación de Flota & Web Templates
│   │   ├── models.py                       # Modelos Camion y Chofer (ORM)
│   │   ├── serializers.py                  # Serializadores DRF con validación RUT
│   │   ├── views.py                        # ViewSets DRF + Vistas de Templates
│   │   ├── urls.py                         # Enrutamiento de API y frontend
│   │   ├── tests.py                        # 15 Pruebas Unitarias (100% OK)
│   │   └── templates/                      # Plantillas HTML con Bootstrap 5
│   │       ├── base.html                   # Navbar, footer y sistema de toasts
│   │       ├── home.html                   # Inicio con métricas en tiempo real
│   │       ├── about.html                  # Quiénes Somos (Misión / Visión)
│   │       ├── services.html               # Servicios + Botones a /api/ y /admin/
│   │       ├── contact.html                # Formulario de contacto interactivo
│   │       ├── choferes.html               # CRUD Choferes CON BOTÓN Y FLUJO EDITAR
│   │       ├── camiones.html               # CRUD Camiones CON BOTÓN Y FLUJO EDITAR
│   │       └── login.html                  # Inicio de sesión estilizado
│   ├── flota_project/                      # Configuración Django
│   │   ├── settings.py
│   │   └── urls.py
│   ├── venv/                               # Entorno Virtual Python 3.12 configurado
│   ├── db.sqlite3                          # Base de datos SQLite migrada y poblada
│   ├── manage.py
│   ├── requirements.txt                    # Dependencias congeladas
│   ├── seed_data.py                        # Poblador automático de datos de prueba
│   └── Usuarios_BD.txt                     # Credenciales de acceso para evaluación
│
├── CONSULTA_IA_WEB_TEMPLATE/               # Carpeta original de insumos y templates
└── Instrucciones_RECETA_DRF_BACKEND.pdf    # Guía original del proyecto
```

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
1. Abrir la carpeta `flota/flota` en Visual Studio Code.
2. Presionar **`F5`** (o ir a la pestaña *Ejecutar y Depurar* y seleccionar **"Django: Iniciar Servidor"**).
3. El servidor se iniciará automáticamente en `http://127.0.0.1:8000/`.

### Opción 2: Por Terminal PowerShell
```powershell
cd "C:\Users\laboratorio8\Desktop\Trabjo Receta\flota\flota"
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

## 🌟 Funcionalidades Destacadas

1. **Requerimiento Crítico Implementado: Botón y Flujo Completo de Edición**
   - Se incorporó el botón **"Editar"** en las tablas de Choferes y Camiones.
   - Precarga automática de datos en el formulario mediante JavaScript asíncrono.
   - Conmutación dinámica a *Modo Edición* con botón *Guardar Cambios* y *Cancelar*.
   - Petición HTTP `PUT`/`PATCH` hacia los endpoints `/api/choferes/{id}/` y `/api/camiones/{id}/`.
   - Notificaciones flotantes (Toasts) de confirmación y refresco reactivo de nómina.

2. **Vistas Web Corporativas (`CONSULTA_IA_WEB_TEMPLATE`)**
   - `Inicio (/)`: Banner principal y tarjetas de resumen.
   - `Quiénes Somos (/quienes-somos/)`: Perfil empresarial.
   - `Servicios (/servicios/)`: Acceso directo mediante botones a `/api/` y `/admin/`.
   - `Contacto (/contacto/)`: Formulario de consulta con retroalimentación inmediata.

3. **Resolución de Normalización de Base de Datos (Diapositiva 24)**
   - Desglose formal de 1FN, 2FN y 3FN.
   - Script SQL DDL y DML listo para ejecutar (`RESOLUCION_NORMALIZACION.sql`).
   - Documento PDF monográfico generado (`RESOLUCION_EJERCICIO_NORMALIZACION.pdf`).
