from pydantic import BaseModel

class Student(BaseModel):
    name:str
    id:int
    dept:str

s1= Student(name="Hameez",id=14,dept="DS")
s2= Student(name="Giri",id=6,dept="Mech")
s3= Student(name="Hari",id=7,dept="IT")
print(s1)



