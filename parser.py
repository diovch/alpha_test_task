def format_date(date: str) -> str:
    day, month, year = date.split('.')
    return f'{year}-{month}-{day}'


def format_currency(currency: str) -> str:
    return f"USD{currency}"


def parse_inputs(inputs: list[str]) -> tuple:
    currency, start_date, end_date = inputs
    return format_currency(currency), format_date(start_date), format_date(end_date)