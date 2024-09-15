from datetime import datetime
import json
from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

from Model import Model
from Field import *
from Database import Database

Model.db = Database('database.sqlite')  # تحديد قاعدة البيانات التي نرغب بإنشائها
Model.connection = Model.db.connect()  # الاتصال بها

PORT = 8000


class Post(Model):  # في قاعدة البيانات وسنضيف بعض الأعمدة إليه يمكن تعريف الجداول هكذا post يمثل هذا الصنف الجدول
    title = CharField()
    body = TextField()
    created_at = DateTimeField()
    published = BooleanField()


class User(Model):
    first_name = CharField()
    last_name = CharField(max_length=255)
    age = IntegerField()


if __name__ == '__main__':

    class MyHandler(SimpleHTTPRequestHandler):
        def do_GET(self):
            if self.path == '/':
                return SimpleHTTPRequestHandler.do_GET(self)

            elif self.path == '/posts':
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(Post.all()).encode('utf-8'))
            else:
                post_id = int(self.path.split('/')[-1])
                result = Post.get(post_id)
                if result is False:
                    self.send_response(404)
                    self.end_headers()
                    self.wfile.write(b'Not Found')
                    return
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(Post.get(post_id)).encode('utf-8'))

        def do_POST(self):
            length = int(self.headers.get('Content-length'))
            body = self.rfile.read(length)
            string = urlparse(body)
            post = parse_qs(string.path.decode('utf-8'))
            Post.create(title=post['title'][0], body=post['body'][0], created_at=datetime.now(), published=False)
            self.send_response(301)
            self.send_header('Location', 'localhost: 8000')
            self.end_headers()

    with HTTPServer(("", PORT), MyHandler) as httpd:
        print("Serving at port", PORT)
        httpd.serve_forever()


