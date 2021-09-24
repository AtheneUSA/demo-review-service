import asyncio
import random
from typing import Optional
from pydantic.fields import Field
from sqlmodel.sql.expression import select
import uvicorn
from typing import List, Optional
from fastapi import Depends, FastAPI
from pydantic import BaseSettings
from sqlmodel import Field, SQLModel, Session, create_engine

class Settings(BaseSettings):
    database_uri: str = "sqlite:///./reviews.db"

class ReviewBase(SQLModel):
    isbn: str
    score: int = Field(ge=0, le=5, description="The score must be between 0 and 5 inclusive.")
    body: Optional[str]

class Review(ReviewBase, table=True):
    __tablename__ = "reviews"
    id: Optional[int] = Field(default=None, primary_key=True)

class ReviewCreate(ReviewBase):
    pass

class ReviewRead(ReviewBase):
    id: int

random.seed()

settings = Settings()
app = FastAPI()

connect_args = {"check_same_thread": False}
engine = create_engine(settings.database_uri, echo=True, connect_args=connect_args)

def get_db_session():
    with Session(engine) as session:
        yield session

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/reviews", response_model=ReviewRead)
async def create_review(review: ReviewCreate, session: Session = Depends(get_db_session)):
    db_review = Review.from_orm(review)
    session.add(db_review)
    session.commit()
    session.refresh(db_review)
    return db_review

@app.get("/reviews/{isbn}", response_model=List[ReviewRead])
async def list_reviews(isbn: str, session: Session = Depends(get_db_session)):
    statement = select(Review).where(Review.isbn == isbn)
    reviews = session.exec(statement).all()
    # Add random latency for demo purposes
    if random.randrange(10) == 0:
        await asyncio.sleep(5)
    else:
        await asyncio.sleep(random.gauss(0.2, 0.08))
    return reviews

def start():
    uvicorn.run("review_service.main:app", host="0.0.0.0", port=8001, reload=True)

if __name__ == "__main__":
    start()
