from pydantic import BaseModel

class Iris_model(BaseModel):
    SepalLengthCm : float
    SepalWidthCm : float
    PetalLengthCm : float
    PetalWidthCm : float

class Petient_model(BaseModel):
    Age : int
    Height : int
    Weight : int

    #["Age","Height","Weight"]