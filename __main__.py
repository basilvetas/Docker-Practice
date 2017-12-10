import tornado.ioloop
import tornado.web

## REST API that accepts a query for a GET request like ?user=username
class MainHandler(tornado.web.RequestHandler):
	def get(self):
		user = self.get_argument('user', "World")
		self.write("Hello, " + user + "\n")

if __name__ == "__main__":
	application = tornado.web.Application([
		(r"/", MainHandler),
	])
	application.listen(8888)
	tornado.ioloop.IOLoop.current().start()