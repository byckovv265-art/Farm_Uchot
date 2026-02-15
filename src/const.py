from enum import Enum


class typesEnum(str, Enum):
    chicken='chicken'
    cow='cow'
    sheep='sheep'
    pig='pig'
    dog='dog'

class sexEnum(str, Enum):
    male = "male"
    famale = "famale"
    
class stateEnum(str,Enum):
    heatly = 'heatly'
    ill = 'ill'
    vaccinated = 'vaccinated'
    dont_vaccinated = 'донт vaccinated'
