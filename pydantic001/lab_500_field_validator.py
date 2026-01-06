from pydantic import BaseModel, Field, field_validator


class UserSignup(BaseModel):
    """
    A model representing user signup data with validation for username and password.
    """
    username: str = Field(..., min_length=3)
    password: str = Field(..., min_length=8)

    @field_validator("username")
    @classmethod
    def no_spaces_in_username(cls, v: str) -> str:
        if " " in v:
            raise ValueError("Username must not contain spaces")
        return v

    @field_validator("password")
    @classmethod
    def password_complexity(cls, v: str) -> str:
        if v.isdigit() or v.isalpha():
            raise ValueError("Password must contain letters and numbers")
        return v


print(UserSignup(username="saurabh", password="abc12345"))
print("---Go username ----")
try:
    UserSignup(username="my user", password="abc12345")
except Exception as e:
    print("\nUsername error:")
    print(e)

try:
    UserSignup(username="saurabh", password="password")
except Exception as e:
    print("\nPassword error:")
    print(e)
