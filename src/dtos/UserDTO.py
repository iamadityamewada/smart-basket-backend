from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional

# Request DTO for creating a new user
class CreateUserDTO(BaseModel):
    name: str
    email: EmailStr
    password: str


# Response DTO for retrieving user details (excluding password)
class UserDTO(BaseModel):
    id: Optional[int]
    name: str
    email: EmailStr

    # In Pydantic v2, you need to use `ConfigDict` for orm_mode
    model_config = ConfigDict(from_attributes=True)
