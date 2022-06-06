from minmax import minmax
from list import list_notes

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class CurrencyRequest(BaseModel):
    currency: str
    start_date: str
    end_date: str


@app.get("/")
def welcome_page():
    return ""


@app.get("/minmax")
def api_minmax(request: CurrencyRequest):
    """'r = requests.get(
    "http://127.0.0.1:8000/minmax",
    json={"currency": "RUB",
          "start_date": "03.05.2022",
          "end_date": "01.06.2022"})"""
    return minmax([request.currency, request.start_date, request.end_date])


@app.get("/list")
def api_list_notes(request: CurrencyRequest):
    """'r = requests.get(
        "http://127.0.0.1:8000/list",
        json={"currency": "RUB",
              "start_date": "03.05.2022",
              "end_date": "01.06.2022"})"""
    temp = list_notes([request.currency, request.start_date, request.end_date])

    response = {"count": len(temp)}
    timeseries = {counter: rate[0] for counter, rate in enumerate(temp)}
    response.update({"timeseries": timeseries})

    return response
