# Request Dumper


This python script based on [Tornado](https://www.tornadoweb.org/en/stable/) creates a mock server that always returns a 200 OK response and logs the request.

The code is based on this [stackexchange comment](https://unix.stackexchange.com/a/57939)

For instance:
```
[BEGIN REQUEST]
127.0.0.1 HTTP/1.1 POST http://127.0.0.1:8080/
HEADERS
  Accept: */*
  Content-Length: 26
  Content-Type: application/x-www-form-urlencoded
  Host: 127.0.0.1:8080
  User-Agent: curl/7.64.1
BODY
{
  "message": "Hello World"
}
[END REQUEST]
```

___DISCLAIMER: Why Python? I'm not keen on untyped languages but this solution meets the "use just a script" requirement___

## Supported methods
- GET
- POST
- PUT
- PATCH
- DELETE

## Run it
### Docker
```bash
docker build . -t request_dumper
docker run -p 80:8080 request_dumper
```

### Py
```bash
pip install -r requirements.txt
python -u ./request_dumper.py
```

## Set Server port
### Docker instance
Bind the port you want to `8080` port when running the container.
### Local instance
Use the`REQUEST_DUMPER_PORT` environment variable to set the port.


```bash
export REQUEST_DUMPER_PORT=8081
```

## Contribute

PRs are more than welcome.

## TODO
- [ ] Docker publish script 
- [ ] Allow hex dumps 
