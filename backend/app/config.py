"""
Configuration settings for the Dating Conversation Assistant API
"""

import os
from typing import List
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # OpenAI Configuration
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    
    # Database Configuration
    database_url: str = os.getenv("DATABASE_URL", "postgresql://localhost:5432/dating_assistant")
    redis_url: str = os.getenv("REDIS_URL", "redis://localhost:6379")
    
    # Application Configuration
    secret_key: str = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
    debug: bool = os.getenv("DEBUG", "True").lower() == "true"
    environment: str = os.getenv("ENVIRONMENT", "development")
    
    # API Configuration
    api_host: str = os.getenv("API_HOST", "0.0.0.0")
    api_port: int = int(os.getenv("API_PORT", "8000"))
    
    # CORS Configuration
    allowed_origins: List[str] = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000,http://localhost:3001").split(",")
    
    # Logging
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    
    class Config:
        env_file = ".env"
        case_sensitive = False

# Global settings instance
settings = Settings()

# Validate OpenAI API key
if not settings.openai_api_key:
    print("⚠️  WARNING: OPENAI_API_KEY not found in environment variables")
    print("Please set your OpenAI API key in the .env file")
    print("Get your API key from: https://platform.openai.com/api-keys")
else:
    print("✅ OpenAI API key configured")