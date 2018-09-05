import webapp2

class HomePage(webapp2.RequestHandler):
    
    def get(self):
        self.request.headers['Content-Type'] = 'text/html'
        self.response.write('<h1>Hello, AppEngine!</h1><br/><p>Cool things could be made!</p>')

app = webapp2.WSGIApplication([('/', HomePage), debug=True])
