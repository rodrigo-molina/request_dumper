#!/usr/bin/env python

import os
import json
import tornado.web


class RequestDumperHandler(tornado.web.RequestHandler):
  def get(self):
    self.__log_request(self.request)

  def post(self):
    self.__log_request(self.request)

  def put(self):
    self.__log_request(self.request)

  def delete(self):
    self.__log_request(self.request)

  def patch(self):
    self.__log_request(self.request)

  def __log_request(self, request):
    print('[BEGIN REQUEST]')
    print('%s %s %s %s' % (request.remote_ip, request.version, request.method, request.full_url()))

    print('HEADERS')
    for (k, v) in sorted(request.headers.get_all()):
      print('  %s: %s' % (k, v))

    print('BODY')
    if request.body == b'':
      print("[Empty Body]")
    else:
      try:
        parsed = json.loads(request.body)
        print(json.dumps(parsed, indent=2, sort_keys=True))
      except:
        print('(Body is not a json object)')
        print(request.body)

    print('[END REQUEST]')


if __name__ == "__main__":
  PORT = os.getenv('REQUEST_DUMPER_PORT', 8080)

  print('Request Dumper Starting at %s' % PORT)
  tornado.web.Application([(r"/.*", RequestDumperHandler), ]).listen(PORT)
  tornado.ioloop.IOLoop.instance().start()
