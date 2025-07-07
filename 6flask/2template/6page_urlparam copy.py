from flask import Flask, render_template
app= Flask(__name__)

users=[
    {'id':i,'name':f'User{i}','age':20+i%10,'phone':f'010-0000-{str(i).zfill(4)}'} for i in range(1,101)
]
users_per_page=10

# http://localhost:5000/pages/1
@app.route('/page/<int:page>')
def index(page):
    # Ensure the page is at least 1, otherwise set it to 1
    if page < 1:
        page = 1
    
    start = (page-1)*users_per_page
    end= start + users_per_page

    users_on_page=users[start:end]

    total_pages = len(users) // users_per_page + (1 if len(users) % users_per_page > 0 else 0)

    return render_template('users2.html', users=users_on_page, page=page, total_pages=total_pages)

if __name__=='__main__':
    app.run(debug=True)