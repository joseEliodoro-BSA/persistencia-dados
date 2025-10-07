from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
#  
from typing import List
# dependências criadas por mim
from database import SessionLocal, engine
import models
import schemas 

# Cria as tabelas no banco caso elas não existam
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()

@app.post("/estudantes", response_model=schemas.Estudante)
def create_student(
    student: schemas.EstudanteCreate, 
    db: Session = Depends(get_db)
):
    # Criando uma entidade de estudantes apartir dos dados vindo da requisição
    db_student = models.Estudante(
        nome=student.nome, 
        email=student.email,
        perfil= models.Perfil(**student.perfil.model_dump())
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@app.get("/estudantes/", response_model= List[schemas.Estudante])
def find_all_student(db: Session = Depends(get_db)):
    estudantes =  db.query(models.Estudante).options(
        joinedload(models.Estudante.perfil)
    ).all()
    return estudantes

@app.get("/estudantes/{id_student}", response_model= schemas.Estudante)
def find_all_student(id_student: int, db: Session = Depends(get_db)):
    estudante = db.query(models.Estudante).where(models.Estudante.id==id_student)
    if (estudante.count() == 0):
        raise HTTPException(404, detail={"error": "Estudante não encontrado"})
    return estudante.first()