import sqlite3
from parser import parse_inputs


def get_min_max(currency: str, start_date: str, end_date) -> list:
    with sqlite3.connect('daily_currency_rates.db') as connection:
        cursor = connection.cursor()
        ins = '''SELECT MIN(rate), MAX(rate)
                FROM currency_rates
                WHERE currency_name=? AND
                date BETWEEN ? AND ?;'''
        return cursor.execute(ins, (currency, start_date, end_date)).fetchone()


def minmax(inputs: list[str]) -> dict:
    currency, start_date, end_date = parse_inputs(inputs)
    min_rate, max_rate = get_min_max(currency, start_date, end_date)
    return {"min": min_rate, "max": max_rate}


def console_minmax(inputs: list[str]) -> None:
    temp = minmax(inputs)
    print(f'MIN = {temp.get("min")}\nMAX = {temp.get("max")}')
