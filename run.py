__author__ = 'The Gibs'

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

from smiteapp import app


def main():
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(5554)

    IOLoop.instance().start()


if __name__ == "__main__":
    main()