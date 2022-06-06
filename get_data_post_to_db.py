import requests
import json
import sqlite3

url = "https://api.apilayer.com/currency_data/timeframe?start_date=2022-05-03&end_date=2022-06-03"

payload = {}
headers = {
    "apikey": "HWb1HaCSSUlTjwyqs9dOy7NcTBeYLG8Q"
}

response = requests.request("GET", url, headers=headers, data=payload)

status_code = response.status_code
result = response.text

data = json.loads(result)
with sqlite3.connect('daily_currency_rates.db') as db_connection:
    curs = db_connection.cursor()
    for date, rate_info in data["quotes"]:
        for currency, rate in rate_info:
            curs.execute(f"""INSERT INTO currency_rates(currency_name, date, rate)
                        VALUES ({currency}, {date}, {rate})""")
