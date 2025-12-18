from pydantic import (
    BaseModel,
    ConfigDict,
    )


class UsersSchema(BaseModel):
    useraname: str
    foo: int
    bar: int


class UsersCreate(UsersSchema):
    pass


class UsersReaf(UsersSchema):
    model_config = ConfigDict(
        from_attributes=True,
    )
    
    id: int
