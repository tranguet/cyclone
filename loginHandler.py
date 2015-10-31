import sys
import cyclone.web

from twisted.internet import reactor
from twisted.python import log

class LoginHandler(cyclone.web.RequestHandler):
    def get(self):
        self.render("Login.html")
    username='tranguet'
    password='iloveuet'
        
    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password')

	if((username==username) and (password==password)):
	    self.redirect("/")
        else:
            self.redirect("/login")

class HelloHandler(cyclone.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

application = cyclone.web.Application([
    (r"/", HelloHandler),
    (r"/login", LoginHandler)
])

if __name__ == "__main__":
    log.startLogging(sys.stdout)
    reactor.listenTCP(8888, application, interface="127.0.0.1")
    reactor.run()


        
