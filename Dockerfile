FROM python:3.11.5

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONNUNBUFFERED 1

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN  python -m pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

COPY ./entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["bash", "entrypoint.sh"]
