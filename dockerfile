FROM ubuntu:latest
RUN apt update && apt upgrade -y
RUN apt install -y -q build-essential python3-pip python3-dev
RUN pip3 install -U pip setuptools wheel
RUN pip3 install gunicorn uvloop httptools
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "app:app --host 0.0.0.0 --port 8000 --reload"]
