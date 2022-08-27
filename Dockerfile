
FROM arm32v7/python:3.9-buster

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code/app
RUN ls -lah
RUN ls -lah ./app
RUN ls -lah ./app/models
WORKDIR /code/app
RUN ls -lah

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
