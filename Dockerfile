FROM python:3.6-buster
WORKDIR /
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "pp.py"]
