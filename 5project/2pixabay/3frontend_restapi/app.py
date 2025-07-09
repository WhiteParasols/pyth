from flask import Flask, jsonify, send_from_directory, url_for, request
from flask_cors import CORS
# pip install flask-cors

app = Flask(__name__)
CORS(app)  # 나의 서버에 누구든지 와서 정보를 요청할수 있음.

images = [
    {"filename":"dog1.jpg", "keywords": ["dog", "sheep", "black"]},
    {"filename":"dog2.jpg", "keywords": ["dog", "lake", "cute"]},
    {"filename":"dog3.jpg", "keywords": ["dog", "field", "black"]},
    {"filename":"dog4.jpg", "keywords": ["dog", "field", "cute"]},
]

@app.route('/')
def index():
    return send_from_directory(app.static_folder, "index.html")

@app.route('/api/search')
def search():
    query = request.args.get("q", "").lower()
    results = []
    
    for item in images:
        if any(query in keyword for keyword in item["keywords"]):
            image_url = url_for('static', filename=f'img/{item["filename"]}')
            results.append(image_url)
    
    return jsonify({"url": results})  # 순수 BE개발자는 여기까지...

if __name__ == "__main__":
    app.run(debug=True)
    