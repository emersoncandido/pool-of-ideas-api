FROM python:3.9

WORKDIR /pool-of-ideas-api

COPY ./requirements.txt /pool-of-ideas-api/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /pool-of-ideas-api/requirements.txt

COPY ./app /pool-of-ideas-api/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]

