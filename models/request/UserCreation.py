from models.base.UserBase import UserBase

class UserCreation(UserBase):
    pass

    # @validator("password")
    # def validate_password(cls, v):
    #   if len(v) < 12:
    #      raise ValueError('Place 12 or more characters')
    # return v