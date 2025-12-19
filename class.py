from pydantic import BaseModel, ValidationError

class User(BaseModel):
    id: int
    name: str
    email: str | None = None

# valid
u = User(id=1, name="Alice")
print(u.id, u.name, u.email)

# invalid
try:
    User(id="not-an-int", name=123)
except ValidationError as e:
    print(e)
