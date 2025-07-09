from flask import Flask, render_template, redirect, url_for, request
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename

# pip install flask-cors

app = Flask(__name__)
CORS(app)  # 나의 서버에 누구든지 와서 정보를 요청할수 있음.

images = [
    {"filename":"dog1.jpg", "keywords": ["dog", "sheep", "black"]},
    {"filename":"dog2.jpg", "keywords": ["dog", "lake", "cute"]},
    {"filename":"dog3.jpg", "keywords": ["dog", "field", "black"]},
    {"filename":"dog4.jpg", "keywords": ["dog", "field", "cute"]},
]

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}  # add more if needed
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/search')
def search():
    query = request.args.get("q", "").lower()
    results = []
    
    for item in images:
        # found = False
        # for keyword in item["keywords"]:
        #     if query in keyword:
        #         found = True
        #         # break # 이미지 하나만 찾고 말거다.
        # if found:
        #     image_url = url_for('static', filename=f'img/{item["filename"]}')
        #     results.append(image_url)
        
        # pythonic하게 한줄로...
        if any(query in keyword for keyword in item["keywords"]):
            image_url = url_for('static', filename=f'img/{item["filename"]}')
            results.append(image_url)
    
    # return jsonify({"url": results})  # 순수 BE개발자는 여기까지...
    return render_template("results.html", query=query, results=results)

@app.route('/admin')
def admin():
    img_folder = os.path.join(app.static_folder, "img")
    existing_files = set(os.listdir(img_folder))

    filtered_images = [
        img for img in images
        if img['filename'] in existing_files and img['filename'].lower().endswith('.jpg')
    ]

    return render_template("admin.html", images=filtered_images)



@app.route('/update_keywords', methods=['POST'])
def update_keywords():
    filename = request.form['filename']
    new_keywords = request.form['keywords'].strip().lower().split(',')
    new_keywords = [kw.strip() for kw in new_keywords if kw.strip()]

    for img in images:
        if img['filename'] == filename:
            img['keywords'] = new_keywords
            break

    return redirect(url_for('admin'))

@app.route('/delete_image', methods=['POST'])
def delete_image():
    filename = request.form['filename']

    # Remove from images list
    global images
    images = [img for img in images if img['filename'] != filename]

    # Optionally, delete actual image file from static/img/
    img_path = os.path.join(app.static_folder, 'img', filename)
    if os.path.exists(img_path):
        os.remove(img_path)

    return redirect(url_for('admin'))

@app.route('/add_image', methods=['GET', 'POST'])
def add_image():
    if request.method == 'POST':
        file = request.files.get('file')
        keywords = request.form.get('keywords', '').strip().lower().split(',')
        keywords = [kw.strip() for kw in keywords if kw]

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)

            # Check if filename already exists in images
            if any(img['filename'] == filename for img in images):
                # Already exists, redirect or handle as you like
                return redirect(url_for('admin'))

            # Save file to static/img folder
            file.save(os.path.join(app.static_folder, 'img', filename))

            # Add to images list
            images.append({
                'filename': filename,
                'keywords': keywords
            })

            return redirect(url_for('admin'))

        # If no file or not allowed, just redirect (or flash error)
        return redirect(url_for('admin'))

    # If GET, just redirect to admin page
    return redirect(url_for('admin'))


if __name__ == "__main__":
    app.run(debug=True)