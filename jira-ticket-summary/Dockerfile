FROM python:latest

WORKDIR /usr/local/bin

COPY jira.py .
copy requirements.txt .

RUN pip install -r requirements.txt \
&& chmod 755 /usr/local/bin/*.py \
&& rm requirements.txt

CMD ["python", "jira.py"]
