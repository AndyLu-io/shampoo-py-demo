
from flask import Flask
from flask import render_template



app = Flask(__name__)



@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

# 定义根路由
@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
