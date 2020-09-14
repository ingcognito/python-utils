FROM python:3.7-alpine

WORKDIR /usr/local/bin

COPY . /usr/local/bin

RUN pip install -r requirements.txt \
&& chmod 755 /usr/local/bin/*.py \
&& rm requirements.txt

CMD ["python", "qr-code.py"]
