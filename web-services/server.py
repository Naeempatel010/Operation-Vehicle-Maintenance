import tornado
import tornado.ioloop
import tornado.web
import os, uuid
import logging
import tornado.escape
import tornado.options
import tornado.websocket
import os.path
import uuid
import urllib
import json
from tornado.options import define, options

define("port", default=8889, help="run on the given port", type=int)


__UPLOADS__ = "uploads/"

import tornado.httpserver, tornado.ioloop, tornado.options, tornado.web, os.path, random, string



    #body = urllib.parse.urlencode(response)

class Upload(tornado.web.RequestHandler):
    def post(self):
        print("connection found")
        fileinfo = self.request.files['filearg'][0]
        print ("fileinfo is", fileinfo)
        fname = fileinfo['filename']
        extn = os.path.splitext(fname)[1]
        cname = str(uuid.uuid4()) + extn
        fh = open(__UPLOADS__ + cname, 'wb')
        #fh.write(fileinfo['body'])  
        response = { 'boolean':'true'} 
        self.write(response)
        

application = tornado.web.Application([
        (r"/upload", Upload),
        (r"/images/(.*)",tornado.web.StaticFileHandler, {"path": "/uploads"})
        ], debug=True)


if __name__ == "__main__":
    application.listen(8889)
    tornado.ioloop.IOLoop.instance().start()