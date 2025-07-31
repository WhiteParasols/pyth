from flask import Flask, send_file, jsonify
from flask_cors import CORS
#여기다 CORS 라이브러리를 추가해서 해결하거나 프론트엔드를 내가 서빙하거나 

app=Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return send_file('4fetch.html')

@app.route('/data')
def data():
    return jsonify({'result':'success','message':'안녕하세요!'})

if __name__=='__main__':
    app.run(debug=True)