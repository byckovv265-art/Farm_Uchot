from pydantic import BaseModel, Field
from src.const import typesEnum, sexEnum, stateEnum


class LivestockCreate(BaseModel):
    name: str = Field(description="Имя животного")
    type: typesEnum = Field(description="Тип животного")
    sex: sexEnum | None = Field(description="Пол животного", default = None)
    state: stateEnum | None = Field(description="Статус животного", default = None)
    weight: float = Field(description="Вес животного, кг.")
    
class LivestockChange(BaseModel):
    name: str | None = Field(description="Имя животного", default = None)
    type: typesEnum | None = Field(description="Тип животного", default = None)
    sex: sexEnum | None = Field(description="Пол животного", default = None)
    state: stateEnum | None = Field(description="Статус животного", default = None)
    weight: float | None = Field(description="Вес животного, кг.", default = None)

class LivestockFilter(BaseModel):
    string_search: str | None = Field(description="Поиск по тексту", default = None)
    type: typesEnum | None = Field(description="Поиск по типу", default = None)
    state: stateEnum | None = Field(description="Статус животного", default = None)
