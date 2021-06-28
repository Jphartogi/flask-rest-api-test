FROM python:3.7.10-alpine3.13
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN cp env.example .env

CMD [ "python", "main.py" ]
