from flask import Flask, render_template, url_for, request, redirect
from forms import AuthorForm, BookForm, GenreForm, session
from engine_db import engine
from models import Author, Genre, Book
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)


def create_form_handler(form_class, model_class, title):
    form = form_class()
    success = False
    if request.method == "POST":
        form = form_class(request.form)
        if form.validate():
            temp_object = model_class()
            form.populate_obj(temp_object)  # добавляем обхект автора
            session.add(temp_object)
            session.commit()
            success = True
    return render_template(
        'add_object.html', **{
            'form': form,
            'title': title,
            'success': success
        }
    )


@app.route('/add_book/', methods=['GET', 'POST'])
def add_book():
    return create_form_handler(BookForm, Book, 'Add Book')


@app.route('/add_author/', methods=['GET', 'POST'])
def add_author():
    return create_form_handler(AuthorForm, Author, 'Add Author')


@app.route('/add_genre/', methods=['GET', 'POST'])
def add_genre():
    return create_form_handler(GenreForm, Genre, 'Add Genre')


@app.route('/<int:id>/update', methods=['GET', 'POST'])
def book_update(id):
    form = BookForm()
    success = False
    if request.method == "POST":
        form = BookForm(request.form)
        if form.validate():
            temp_object = Book()
            form.populate_obj(temp_object)  # добавляем обхект автора
            session.add(temp_object)
            session.commit()
            success = True
        return render_template(
            'add_object.html', **{
                'form': form,
                'title': "Book Update",
                'success': success
            }
        )
    if request.method == "GET":
        book = session.query(Book).get(id)
        return render_template("book_update.html", book=book)


@app.route('/')
def home():
    books = session.query(Book).all()
    return render_template(
        'index.html', **{
            'books': books
        }
    )


@app.route('/<int:id>')
def book_detail(id):
    book = session.query(Book).get(id)
    return render_template(
        'book_detail.html', **{
            'book': book
        }
    )


@app.route('/<int:id>/del')
def book_delete(id):
    book = session.query(Book).get(id)

    try:
        session.delete(book)
        session.commit()
        return redirect('/')
    except:
        return "При удалении книги произошла ошибка"





@app.route('/genre/<int:id>', methods=['GET', 'POST'])
def genre():
    if request.method == "GET":
        books = session.query(Book).all()
    if request.method == "POST":
        book_id = request.form['book_id']
        books = session.query(Book).get(book_id)
        # books = session.query(Book).filter(Book.genre == book_id)
    return render_template(
        'genre.html', **{
            'books': books
        }
    )


@app.route('/book_year/')
def year():
    books = session.query(Book).filter()
    return render_template(
        'index.html', **{
            'books': books
        }
    )


if __name__ == '__main__':
    app.run(debug=True)