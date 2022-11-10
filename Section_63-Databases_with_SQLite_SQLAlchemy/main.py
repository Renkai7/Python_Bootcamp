from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-collection.db'
db = SQLAlchemy(app)


# all_books = []


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'


db.create_all()


@app.route('/')
def home():
    all_books = db.session.query(Book).all()

    return render_template('index.html', books=all_books)


@app.route('/add', methods=['POST', 'GET'])
def add():
    # book_name = request.form['name']
    if request.method == 'POST':
        # data = {
        #     "title": request.form['name'],
        #     "author": request.form['author'],
        #     "rating": request.form['rating']
        # }
        # all_books.append(data)
        new_book = Book(title=request.form['name'], author=request.form['author'], rating=request.form['rating'])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route('/edit', methods=['POST', 'GET'])
def edit():
    if request.method == 'POST':
        book_id = request.form['id']
        book_to_update = Book.query.get(book_id)
        book_to_update.rating = request.form['rating']
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    selected_book = Book.query.get(book_id)
    return render_template('edit.html', book=selected_book)


@app.route('/delete', methods=['POST', 'GET'])
def delete():
    book_id = request.args.get('id')
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
