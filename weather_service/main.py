from fastapi import FastAPI
app=FastAPI()
@app.get("/weather/current")
async def current(city:str):
    return {"city":city}
@app.get("/weather/forecast")
async def forecast(city:str):
    return {"city":city}