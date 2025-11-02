"""Application configuration."""
# Optional: тип з typing, дозволяє оголошувати атрибути, які можуть бути None (необов'язкові). Це корисно для налаштувань, які не завжди потрібні.
from typing import Optional

# BaseSettings: клас з pydantic_settings, який дозволяє легко працювати з налаштуваннями через змінні середовища та .env файли. Використовується для безпечного та зручного конфігурування додатків.
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""
    
    app_name: str = "FastAPI Project"
    version: str = "0.1.0"
    debug: bool = False
    
    # Database
    database_url: Optional[str] = None
    
    # Security
    # secret_key: секретний ключ для JWT, авторизації тощо. Значення береться з .env або змінних середовища (див. class Config нижче).
    # Приклад: у .env файлі має бути рядок SECRET_KEY=your-production-secret
    secret_key: str  # значення буде підставлено з .env або змінних середовища автоматично через BaseSettings
    # Якщо використовуєте BaseSettings, вам не потрібно вручну діставати secret_key через os.environ:
    # при ініціалізації Settings() всі змінні, оголошені як атрибути класу, автоматично підтягуються з .env або env.
    # Наприклад, якщо у вас у .env є SECRET_KEY=your-production-secret, то Settings().secret_key буде містити це значення.
    
    # Альтернативний спосіб отримати секрет безпосередньо з env (наприклад, якщо не використовуєте BaseSettings):
    # import os
    # SECRET_KEY = os.environ.get("SECRET_KEY")
    access_token_expire_minutes: int = 30
    
    class Config:
        env_file = ".env"


settings = Settings()