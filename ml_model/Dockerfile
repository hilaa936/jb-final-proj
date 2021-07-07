FROM python:3.8.3

WORKDIR /app/
COPY requirements.txt /app/
RUN pip install -r requirements.txt
ADD ./ml_model /app/

ENTRYPOINT python /app/model_train.py