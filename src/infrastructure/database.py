# infrastructure.database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

class Database:
    def __init__(self, connection_string: str):
        self.engine = create_engine(connection_string)
        self.SessionLocal = sessionmaker(bind=self.engine)
        self.session = None

    def __enter__(self):
        self.session = self.SessionLocal()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

    def add(self, entity):
        with self as db:
            db.session.add(entity)
            db.session.commit()

    def update(self, entity):
        with self as db:
            db.session.merge(entity)
            db.session.commit()

    def delete(self, entity):
        with self as db:
            db.session.delete(entity)
            db.session.commit()

    def query(self, entity, filter=None):
        with self as db:
            if filter:
                result = db.session.query(entity).filter_by(**filter).all()
            else:
                result = db.session.query(entity).all()
        return result
