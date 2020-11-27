FROM python:latest

WORKDIR /usr/local/bin

COPY jira.py .
COPY requirements.txt .
COPY .env .

RUN pip install -r requirements.txt \
&& chmod 755 /usr/local/bin/*.py \
&& rm requirements.txt

CMD ["python", "jira.py"]
