import tornado.ioloop
import tornado.web

# (1) If you would like extra credit on the mid-term, you can earn back X points by creating a 
# containerized tornado REST API that accepts a query for a GET request like ?user=username and 
# returns "Hello, <username>" as the response. I'll evaluate on a pass/fail basis by cd'ing into 
# the container directory, building the container, running the container, and making an API 
# request to it. You can submit your work by emailing me a github link (and giving me access, if 
# it's private) with the subject line "MLP Extra Credit" sometime before the final. I'll follow 
# the procedure outlined in class to build and run your container. The percentage points you can 
# earn back will be X = 20 * ((100. - G) / G), where G is the grade you earned on the mid-term. 

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