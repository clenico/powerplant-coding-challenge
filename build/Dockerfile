FROM python:3.10

WORKDIR /install
COPY requirements.txt .
RUN pip install -r requirements.txt
WORKDIR /app
COPY . .
# TODO refactor in multi stage build
#COPY run.py .
#COPY app ./app
ENV PYTHONPATH=/app

ENTRYPOINT [ "python3", "/app/run.py" ]
