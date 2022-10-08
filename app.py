from flask import Flask

app = Flask(__name__)
app.debug = True
app.secret_key = 'c0v1-d1sp4p3l3s#2022' #os.urandom(24)  #'Hola mundo'

if __name__ =='__main__':  
    app.run()


@app.route('/')
def index():
    return "Hola mundo"