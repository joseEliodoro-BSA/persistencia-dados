from sqlalchemy import Column, Integer, String, ForeignKey, String
from sqlalchemy.orm import relationship
from database import Base

class Estudante(Base):
    __tablename__ = "estudantes"
    id = Column(
        Integer, 
        primary_key=True, 
        index=True
    )
    email = Column(String(255))
    nome = Column(String(255))
    perfil = relationship(
        "Perfil", 
        back_populates="estudante", 
        uselist=False, 
        cascade="all, delete-orphan" 
        # primeiro parâmetro refere-se a todos os estudantes,
        # o segundo refere-se que não devem ter um estudante sem um pai
        )

class Perfil(Base):
    __tablename__ = "perfis"
    id = Column(
        Integer, 
        primary_key=True, 
        index=True
    )
    idade = Column(Integer)
    endereco = Column(String(255))
    id_student = Column(Integer, ForeignKey("estudantes.id"), unique=True)
    estudante = relationship("Estudante", back_populates='perfil')