from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

posts_db = [{"id": 1, "title": "Первый пост", "content": "Привет, мир!", "likes": 0}]
class PostCreate(BaseModel):
    title: str
    content: str

@app.post("/posts")
def create_post(post_data: PostCreate):
    new_post = post_data.model_dump()
    new_post["id"] = len(posts_db) + 1
    new_post["likes"] = 0
    posts_db.append(new_post)
    return new_post
@app.get("/posts/{post_id}")
def read_post(post_id: int):
    for post in posts_db:
        if post["id"] == post_id:
            return post

