"""
Demonstrates serialization and deserialization of Pydantic models.
"""
import json
from pydantic import BaseModel


class BlogPost(BaseModel):
    """
    A model representing a blog post with ID, title, and tags.
    """
    id: int
    title: str
    tags: list[str]


post = BlogPost(id=1, title="Hello Pydantic", tags=["python", "validation"])

# Model → dict
post_dict = post.model_dump()
print("Dict:", post_dict, type(post_dict))

# Model → JSON string
post_json = post.model_dump_json()
print("JSON:", post_json, type(post_json))

# JSON string → Model
data_from_json = json.loads(post_json)
post2 = BlogPost.model_validate(data_from_json)
print("Post2:", post2)
