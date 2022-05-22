FROM python:3.8-slim-buster

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y python3 python3-pip
RUN python3 -m pip install --no-cache --upgrade pip


ADD . /app/

# create requirement.text file using command "pip freeze > requirement.txt" on cmd
#COPY requirements.txt /app/requirements.txt

RUN pip3 install -r /app/requirements.txt

WORKDIR ./app/

#COPY . /app
#ENTRYPOINT[]

CMD ["python3", "pp.py"]
