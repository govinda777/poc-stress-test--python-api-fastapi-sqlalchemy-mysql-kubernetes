from sqlalchemy.orm import sessionmaker, Session

class Database:
    def __init__(self, SessionLocal: sessionmaker):
        """
        Inicializa a classe Database.

        Args:
            SessionLocal (sessionmaker): Uma fábrica de sessões do SQLAlchemy.
        """
        self.SessionLocal = SessionLocal
        self.session: Session = None

    def __enter__(self) -> "Database":
        """
        Inicia uma nova sessão do SQLAlchemy ao entrar no contexto.

        Returns:
            Database: Retorna a instância atual da classe.
        """
        self.session = self.SessionLocal()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Fecha a sessão do SQLAlchemy ao sair do contexto.
        """
        self.session.close()

    def add(self, entity):
        """
        Adiciona e comita uma entidade ao banco de dados.

        Args:
            entity: A entidade a ser adicionada.
        """
        with self as db:
            db.session.add(entity)
            db.session.commit()

    def update(self, entity):
        """
        Atualiza e comita uma entidade no banco de dados.

        Args:
            entity: A entidade a ser atualizada.
        """
        with self as db:
            db.session.merge(entity)
            db.session.commit()

    def delete(self, entity):
        """
        Exclui e comita uma entidade do banco de dados.

        Args:
            entity: A entidade a ser excluída.
        """
        with self as db:
            db.session.delete(entity)
            db.session.commit()

    def query(self, entity, filter=None):
        """
        Consulta entidades no banco de dados com base em um filtro opcional.

        Args:
            entity: O tipo de entidade a ser consultado.
            filter (dict, optional): Um filtro para a consulta. Defaults to None.

        Returns:
            list: Uma lista de entidades que correspondem à consulta.
        """
        with self as db:
            if filter:
                result = db.session.query(entity).filter_by(**filter).all()
            else:
                result = db.session.query(entity).all()
        return result
