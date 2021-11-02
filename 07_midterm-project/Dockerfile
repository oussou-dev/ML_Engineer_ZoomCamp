FROM ubuntu:latest

RUN pip install --upgrade pip
RUN apt-get -y update
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install -r requirements.txt

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt


# Expose the required port
EXPOSE 5000

# Run
CMD ["python","./app.py"]
# CMD gunicorn main:app