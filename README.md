# API REST Básica de Tareas (FastAPI)

Este proyecto implementa una API REST mínima para gestionar tareas en
memoria.\
La estructura sigue el patrón de **3 capas**:

-   **models/**: Definición de esquemas (Pydantic).
-   **services/**: Lógica de negocio y almacenamiento en memoria.
-   **routers/**: Endpoints y controladores HTTP.
-   **main.py**: Punto de entrada, monta los routers.


------------------------------------------------------------------------

## 1. Estructura del proyecto

    .
    ├── main.py
    ├── models/
    │   └── task_models.py
    ├── services/
    │   └── task_service.py
    └── routers/
        ├── health_router.py
        └── tasks_router.py

------------------------------------------------------------------------

## 2. Descripción general del funcionamiento

### Almacenamiento en memoria

`TaskService` mantiene una lista interna de tareas y un contador
incremental de IDs.\
Esto significa que los datos **no son persistentes**; reiniciar el
servidor borra toda la información.

### Flujo

1.  Los **routers** reciben solicitudes HTTP.
2.  Realizan validaciones básicas (existencia de la tarea, status code,
    errores).
3.  Llaman a los métodos del **service**.
4.  Los servicios manipulan los modelos definidos en **models**.
5.  Los routers devuelven la respuesta al cliente con los modelos
    correctos.

------------------------------------------------------------------------

## 3. Endpoints principales

### Health

  -----------------------------------------------------------------------
  Método            Ruta                     Descripción
  ----------------- ------------------------ ----------------------------
  GET               `/health`                Verifica estado del
                                             servicio, uptime y timestamp

  -----------------------------------------------------------------------

### Tasks

  Método   Ruta            Descripción
  -------- --------------- ---------------------
  GET      `/tasks`        Listar tareas
  POST     `/tasks`        Crear tarea
  GET      `/tasks/{id}`   Obtener tarea
  PUT      `/tasks/{id}`   Actualizar completa
  PATCH    `/tasks/{id}`   Actualizar parcial
  DELETE   `/tasks/{id}`   Eliminar tarea

------------------------------------------------------------------------

## 4. Cómo ejecutar el proyecto

A continuación se muestra un procedimiento estándar en Linux/macOS.\
(En Windows, sustituye `python3` por `python` donde corresponda.)

------------------------------------------------------------------------

### 4.1 Crear entorno virtual

``` bash
python3 -m venv .venv
```

Activar:

**Linux/macOS**

``` bash
source .venv/bin/activate
```

**Windows**

``` bash
.venv\Scripts\activate
```

------------------------------------------------------------------------

### 4.2 Instalar dependencias

    pip install fastapi uvicorn

------------------------------------------------------------------------

### 4.3 Ejecutar la aplicación

Dentro del entorno virtual:

``` bash
uvicorn main:app --reload --port 3021
```

La API estará disponible en:

-   **http://localhost:3000**
-   **Documentación automática Swagger**: http://localhost:3021/docs
-   **Documentación Redoc**: http://localhost:3021/redoc

------------------------------------------------------------------------

## 5. Detener el servidor

Presiona:

    CTRL + C
