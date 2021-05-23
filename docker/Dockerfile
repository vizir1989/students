FROM python:3.7

WORKDIR /usr/src/app

COPY poetry.lock .
COPY pyproject.toml .
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install

COPY . .

EXPOSE 8000

CMD PYTHONPATH=. gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0
#CMD while true; do echo 'Hit CTRL+C'; sleep 1; done