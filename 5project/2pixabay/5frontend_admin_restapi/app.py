from flask import Flask, jsonify, send_from_directory, url_for, request

app = Flask(__name__)

images = [
    {"filename":"cat1.jpg", "keywords": ["cat", "animal", "cute"]},
    {"filename":"cat2.jpg", "keywords": ["cat", "pet", "cute"]},
    {"filename":"cat3.jpg", "keywords": ["cat", "kitty", "cute"]},
    {"filename":"dog1.jpg", "keywords": ["dog", "pet", "park"]},
    {"filename":"panda1.jpg", "keywords": ["panda", "zoo", "bear"]}
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
    