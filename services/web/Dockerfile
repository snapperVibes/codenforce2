# Launches devolpment server
FROM python:3.8
WORKDIR /app
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
# Unneeded since we link the volumes
# COPY ./app .
CMD ["python", "codenforce/main.py"]
