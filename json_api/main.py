from fastapi import FastAPI
from database.repository import get_all_news


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the news aggregator!"}


@app.get("/news")
async def get_news():
    news = await get_all_news()
    return news
