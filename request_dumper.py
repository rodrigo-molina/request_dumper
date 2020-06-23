#!/usr/bin/env python

import json
import hexdump
import argparse
import tornado.web


class RequestDumperHandler(tornado.web.RequestHandler):
  def initialize(self):
    self.body_print_format = self.application.settings.get('body_print_format')

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
    elif self.body_print_format == 'json':
      self.__print_json(request.body)
    elif self.body_print_format == 'hex_dump':
      self.print_hex_dump(request.body)
    else:
      print('Unsupported print format value %s' % self.body_print_format)

    print('[END REQUEST]')

  def __print_json(self, body):
    try:
      parsed = json.loads(body)
      print(json.dumps(parsed, indent=2, sort_keys=True))
    except:
      print('(Body is not a json object)')
      print(body)

  def print_hex_dump(self, body):
    for row in hexdump.dumpgen(body):
      print(row)


def process_arguments():
  parser = argparse.ArgumentParser()
  parser.add_argument('--port', default=8080, type=int, help='server port. Default value is 8080.')
  parser.add_argument('--body-print-format', choices=['json', 'hex_dump'], default='json',
                      help='request body print format.')

  return parser.parse_args()


if __name__ == "__main__":
  config = process_arguments()
  PORT = config.port
  BODY_PRINT_FORMAT = config.body_print_format

  print('Request Dumper Starting at %s' % PORT)
  tornado.web.Application([(r"/.*", RequestDumperHandler)], body_print_format=BODY_PRINT_FORMAT).listen(PORT)
  tornado.ioloop.IOLoop.instance().start()
