from sqlalchemy import select, String, delete, Float
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import create_engine
import sqlalchemy


Base = declarative_base()

class Waste(Base):
    __tablename__ = "waste"

    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    name: Mapped[str] = mapped_column(String(30))
    amount: Mapped[float] = mapped_column(Float)
    def __repr__(self) -> str:
        return f"Waste(id={self.name!r} name={self.name!r}, amount={self.fullname!r})"


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(bind=engine)