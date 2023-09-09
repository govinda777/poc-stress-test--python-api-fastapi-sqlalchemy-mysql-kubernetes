from dependency_injector import containers, providers
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from infrastructure.database import Database
from user.user_controller import UserController
from user.user_repository import UserRepository
from user.user_service import UserService

DATABASE_URL = "sqlite:///./test.db"

class Container(containers.DeclarativeContainer):
    """Container de Injeção de Dependência."""

    # Configuração do banco de dados
    engine = providers.Singleton(create_engine, DATABASE_URL)
    SessionLocal = providers.Singleton(sessionmaker, bind=engine)
    database = providers.Factory(Database, SessionLocal=SessionLocal)

    # Configuração para UserRepository
    user_repository = providers.Factory(
        UserRepository,
        database=database
    )

    # Configuração para UserService
    user_service = providers.Factory(
        UserService,
        repository=user_repository
    )

    # Configuração para UserController
    user_controller = providers.Factory(
        UserController,
        service=user_service
    )