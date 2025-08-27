from sqlalchemy import Datetime, Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from workout_API.contrib.models import BaseModel, AtletaModel

class CategoriaModel(BaseModel):
    __tablename__ = 'categorias'
    
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    atleta: Mapped['AtletaModel'] = relationship(back_populates='atleta') 

    