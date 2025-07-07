from flask import Flask, request

app = Flask(__name__)

@app.route('/search') # /serach?q=apple&page=2
def search():
    query=request.args.get('q')
    page=request.args.get('page')
    page=request.args.get('page',default=1, type=int) #query 구문에 해당키 없어도 디폴트값 있음

    print(query,page)
    return 'hello'

if __name__=='__main__':
    app.run(debug=True)