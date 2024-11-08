FROM python:3.11-slim-buster

WORKDIR /usr/src/controlpanel-python
ENV    PYTHONDONTWRITEBYTECODE 1 
ENV    PYTHONUNBUFFERED 1 

COPY ./requirements.txt /usr/src/controlpanel-python/requirements.txt

RUN pip install --upgrade pip setuptools wheel \
    && pip install -r requirements.txt \
    && rm -rf /root/.cache/pip


CMD ["streamlit", "run", "main.py"]