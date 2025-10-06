from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
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

@app.post("/estudantes", response_model=schemas.EstudanteResponse)
def create_student(
    student: schemas.EstudanteCreate, 
    db: Session = Depends(get_db)
):
    # Criando uma entidade de estudantes apartir dos dados vindo da requisição
    db_student = models.Estudante(**student.model_dump())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@app.get("/estudantes/", response_model= List[schemas.EstudanteResponse])
def find_all_student(db: Session = Depends(get_db)):
    return db.query(models.Estudante).all() 