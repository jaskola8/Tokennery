FROM python:3.6.5

WORKDIR /app

ADD . /app

RUN pip install --upgrade pip setuptools
RUN pip install -r requirements.txt
EXPOSE 80

CMD ["python", "main.py"]


