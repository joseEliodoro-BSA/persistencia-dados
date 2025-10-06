from pydantic import BaseModel

class EstudanteBase(BaseModel):
    name: str
    age: int

    
class EstudanteCreate(EstudanteBase):
    pass

class EstudanteResponse(EstudanteBase):
    id: int
    class Config:
        from_attributes = True
    
class MatriculaBase(BaseModel):
    name: str
    id_student: int

    
class MatriculaCreate(MatriculaBase):
    pass

class MatriculaResponse(MatriculaBase):
    id: int
    class Config:
        from_attributes = True
    
