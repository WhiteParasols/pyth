from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <head>
    </head>
    <body>
        <ul>
            <li></li>
            <li></li>
        </u1>
    </body>
    
    </html>
    '''
if __name__=="__main__":
    app.run(debug=True)