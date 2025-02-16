from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("mysql+pymysql://automate:Automate750*@154.38.180.78/automate")
Base = declarative_base()


class Fretes(Base):
    __tablename__ = "fretes"
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    produto = Column(String(255), nullable=False)
    origem_1 = Column(String(255), nullable=False)
    origem_2 = Column(String(255), nullable=False)
    destino_1 = Column(String(255), nullable=False)
    destino_2 = Column(String(255), nullable=False)
    valor_acima_de = Column(Integer, nullable=False)
    observacao = Column(String(255), nullable=False)

    def to_dict(self):
        return {
            column.name: getattr(self, column.name) for column in self.__table__.columns
        }


class Status(Base):
    __tablename__ = "status"
    id = Column(Integer, primary_key=True, unique=True)
    status = Column(Integer, nullable=False, unique=True)

    def to_dict(self):
        return {
            column.name: getattr(self, column.name) for column in self.__table__.columns
        }


def get_fretes():
    Session = sessionmaker(bind=engine)
    session = Session()

    fretes = session.query(Fretes).all()
    session.close_all()
    return [frete.to_dict() for frete in fretes]


def get_status():
    Session = sessionmaker(bind=engine)
    session = Session()

    status = session.query(Status).all()
    session.close_all()
    return [state.to_dict() for state in status][0]