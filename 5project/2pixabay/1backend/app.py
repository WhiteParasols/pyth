from flask import Flask,jsonify,url_for
import random

app = Flask(__name__)
dog_images=[
    'dog1.jpg',
    'dog2.jpg',
    'dog3.jpg',
    'dog4.jpg',
]

@app.route('/random-dog')
def random_dog():
    random_img=random.choice(dog_images)
    image_url = url_for('static',filename=f'img/{random_img}')
    return jsonify({'url':random_img})

if __name__=='__main__':
    app.run(debug=True)