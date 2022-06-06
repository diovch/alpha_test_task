### Установка окружения и зависимостей

```python -m venv env```

```source env/bin/activate```

```pip install -r requirements.txt```

### Первый уровень
- База содержит данные по ценам валют с 03.05.2022 по 03.06.2022
суткам (напр., USDMKD|2022-05-26|57.420705)
- Запрос к базе для получения максимальной и минимальной цены 
находится в файле **sql_request.txt**

### Второй уровень
- Консольное приложение **currency.py** с двумя типами запросов

```python currency.py minmax RUB 10.05.2022 02.06.2022```

```python currency.py list RUB 15.05.2022 02.06.2022 --limit=3```

### Третий уровень
- API сделан с помощью FastAPI и uvicorn

- Запуск сервера

```uvicorn currency_server:app --reload```

- Примеры запросов

```body = {"currency": "RUB", "start_date": "03.05.2022", "end_date": "01.06.2022"}```

```requests.get("http://127.0.0.1:8000/minmax", json=body)```

```requests.get("http://127.0.0.1:8000/list", json=body)```