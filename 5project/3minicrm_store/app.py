from flask import Flask, render_template, request
import database as db

app = Flask(__name__)

@app.route('/')
def index():
    name = request.args.get('name','').strip()

    if name:
        stores=db.get_stores_by_name(name)
    else: 
        stores = db.get_stores()
    print(stores)

    return render_template('index.html',stores=stores, search=name)

if __name__ == '__main__':
    app.run(debug=True)