FROM python:3
ADD request_dumper.py /
ADD requirements.txt /

RUN pip install -r requirements.txt

ENV REQUEST_DUMPER_PORT 8080
EXPOSE ${REQUEST_DUMPER_PORT}

CMD [ "python", "-u", "./request_dumper.py"]