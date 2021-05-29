FROM python:3.7

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1



COPY poetry.lock .
COPY pyproject.toml .
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install

COPY . .

EXPOSE 8000

#CMD PYTHONPATH=. gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0 --reload
CMD PYTHONPATH=. uvicorn app.main:app --reload --workers 1 --host 0.0.0.0 --port 8000
