from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped, mapped_column

from database import Base

class Livro(Base):
    __tablename__ = "livros"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    titulo: Mapped[str] = mapped_column(String(200), nullable=False)
    autor_id: Mapped[int] = mapped_column(ForeignKey("autores.id"))
    autor: Mapped["Autor"] = relationship(back_populates="livros")

class Autor(Base):
    __tablename__ = "autores"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    livros: Mapped[list["Livro"]] = relationship(back_populates="autor")