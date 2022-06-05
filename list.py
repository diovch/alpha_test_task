import sqlite3
from parser import parse_inputs


def get_notes_from_table(currency: str, start_date: str, end_date: str, count: int = None) -> list:
    with sqlite3.connect('daily_currency_rates.db') as connection:
        cursor = connection.cursor()
        ins = '''SELECT rate
                FROM currency_rates
                WHERE currency_name=? AND
                date BETWEEN ? AND ?;'''
        if count:
            return cursor.execute(ins, (currency, start_date, end_date)).fetchmany(size=count)
        return cursor.execute(ins, (currency, start_date, end_date)).fetchall()


def get_notes_count(inp: str) -> int:
    return int(inp.lstrip('--limit='))


def list_notes(inputs: list[str]) -> list:
    currency, start_date, end_date = parse_inputs(inputs[:3])

    notes = get_notes_from_table(currency, start_date, end_date, get_notes_count(inputs[-1])) \
        if len(inputs) == 4 else \
        get_notes_from_table(currency, start_date, end_date)

    return notes


def console_list_notes(inputs: list[str]) -> None:
    notes = list_notes(inputs)

    print(f'Count = {len(notes)}')
    for i, note in enumerate(notes, start=1):
        print(f'{i}. {round(float(note[0]), 2)}')
