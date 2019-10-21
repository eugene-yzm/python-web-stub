import tornado.httpserver
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def setup_routes():
    return tornado.web.Application(
        [
            (r"/", MainHandler),
        ],
    debug=True)

def main():
    print("Starting service")
    app = setup_routes()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(5000)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
