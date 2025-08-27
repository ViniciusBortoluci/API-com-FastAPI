from datetime import datetime
from sqlalchemy import Datetime, ForeignKey, Integer, String, Float 
from sqlalchemy.orm import Mapped, mapped_column, relationship
from workout_API.atleta.model import AtletaModel
from workout_API.categorias.model import CategoriaModel, AtletaModel
from workout_API.contrib.models import BaseModel

class CentroTreinamentoModel(BaseModel):
    __tablename__ = 'centro_treinamento'
    
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    endereco: Mapped[str] = mapped_column(String(60), nullable=False)
    proprietario: Mapped[str] = mapped_column(String(30), nullable=False)
    atleta: Mapped['AtletaModel'] = relationship(back_populates='centro_treinamento')
    