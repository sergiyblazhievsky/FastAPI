"""FastAPI application main module."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.version,
    debug=settings.debug,
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # В production використовуйте конкретні домени
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(router, prefix="/api/v1")


@app.get("/")
async def root() -> dict:
    """Root endpoint."""
    return {
        "message": f"Welcome to {settings.app_name}",
        "version": settings.version,
        "docs": "/docs"
    }


  # Цей блок виконується тільки якщо файл запущено напряму, наприклад:
  #     python -m app.main
  # Коли модуль імпортується з іншого місця (наприклад під час тестування),
  # код у цій умові не виконається — це запобігає автозапуску сервера.
  # Запускаємо сервер Uvicorn, передаємо об'єкт `app`.
  # - host="0.0.0.0" робить додаток доступним на всіх мережевих інтерфейсах
  #   (корисно для Docker або віддаленого запуску).
  # - port=8000 встановлює порт для прослуховування HTTP-запитів.
if __name__ == "__main__":
  import uvicorn  # ASGI-сервер для запуску FastAPI додатка
  uvicorn.run(app, host="0.0.0.0", port=8000)