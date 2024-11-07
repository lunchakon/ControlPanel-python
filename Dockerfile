FROM python:3.11-slim-buster

WORKDIR /controlpanel-python

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["streamlit", "run", "main.py"]