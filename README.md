# Request Dumper


This python script based on [Tornado](https://www.tornadoweb.org/en/stable/) creates a mock server that always returns a 200 OK response and logs the request.

The code is based on this [stackexchange comment](https://unix.stackexchange.com/a/57939)

Log examples from curl
```
curl -X POST  127.0.0.1:8080 -d '{"id":1234, "message": "Hello World"}'
```

Json log
```
[BEGIN REQUEST]
127.0.0.1 HTTP/1.1 POST http://127.0.0.1:8080/
HEADERS
  Accept: */*
  Content-Length: 37
  Content-Type: application/x-www-form-urlencoded
  Host: 127.0.0.1:8080
  User-Agent: curl/7.64.1
BODY
{
  "id": 1234,
  "message": "Hello World"
}
[END REQUEST]
```

Hex dump log
```
[BEGIN REQUEST]
127.0.0.1 HTTP/1.1 POST http://127.0.0.1:8080/
HEADERS
  Accept: */*
  Content-Length: 37
  Content-Type: application/x-www-form-urlencoded
  Host: 127.0.0.1:8080
  User-Agent: curl/7.64.1
BODY
00000000: 7B 22 69 64 22 3A 31 32  33 34 2C 20 22 6D 65 73  {"id":1234, "mes
00000010: 73 61 67 65 22 3A 20 22  48 65 6C 6C 6F 20 57 6F  sage": "Hello Wo
00000020: 72 6C 64 22 7D                                    rld"}
[END REQUEST]
```
_DISCLAIMER: Why Python? I'm not keen on untyped languages but this solution meets the "use just a script" requirement_

## Supported HTTP methods
- GET
- POST
- PUT
- PATCH
- DELETE

## Arguments
```
python request_dumper.py --h

usage: request_dumper.py [-h] [--port PORT]
                         [--body-print-format {json,hex_dump}]

optional arguments:
  -h, --help            show this help message and exit
  --port PORT           server port. Default value is 8080.
  --body-print-format {json,hex_dump}
                        request body print format.
```

## Run it
### Docker
```bash
docker run -p80:8080  agrev/request_dumper:latest --body-print-format=json
```


### Docker Local
```bash
docker build . -t request_dumper
docker run -p 80:8080 request_dumper
```

### Py
```bash
pip install -r requirements.txt
python -u ./request_dumper.py
```


## Contribute

PRs are more than welcome.
