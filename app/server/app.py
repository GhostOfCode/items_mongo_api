from fastapi import FastAPI

from .routes.item import router as ItemRouter


app = FastAPI(title="Items_API", version='0.0.1')


#  Main methods of API (routes) with tag "Items"
app.include_router(ItemRouter, tags=["Items"], prefix="/item")


#  Welcome
@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this test CRUD app!"}
