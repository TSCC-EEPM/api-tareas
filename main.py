# main.py
from fastapi import FastAPI
from routers.product_router import router as product_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="API REST  - Tareas")

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],  # Permitir todos los encabezados
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)

app.include_router(product_router)

# Si quieres algo de prueba:
@app.get("/")
def root():
    return {"message": "API de productos funcionando"}
