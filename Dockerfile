FROM python:3
ADD request_dumper.py /
ADD requirements.txt /

RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "-u", "./request_dumper.py"]