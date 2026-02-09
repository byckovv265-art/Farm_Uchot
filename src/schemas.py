from pydantic import BaseModel, Field
from src.const import typesEnum, sexEnum, stateEnum


class livestockCreate(BaseModel):
    name: str = Field(description="Имя животного")
    type: typesEnum = Field(description="Тип животного")
    sex: sexEnum | None = Field(description="Тип животного", default = None)
    state: stateEnum | None = Field(description="Тип животного", default = None)
    weight: float = Field(description="Тип животного")
    
class livestockChange(BaseModel):
    name: str | None = Field(description="Имя животного", default = None)
    type: typesEnum | None = Field(description="Тип животного", default = None)
    sex: sexEnum | None = Field(description="Тип животного", default = None)
    state: stateEnum | None = Field(description="Тип животного", default = None)
    weight: float | None = Field(description="Тип животного", default = None)