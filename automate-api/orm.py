from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("mysql+pymysql://automate:Automate750*@160.238.242.80/automate")
Base = declarative_base()


class Fretes(Base):
    __tablename__ = "fretes"
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    produto = Column(String(255), nullable=False)
    origem_1 = Column(String(255), nullable=False)
    origem_2 = Column(String(255), nullable=False)
    destino_1 = Column(String(255), nullable=False, default="INDIFERENTE")
    destino_2 = Column(String(255), nullable=False, default="INDIFERENTE")
    valor_acima_de = Column(Integer, nullable=False, default=0)

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