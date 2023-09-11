from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Create empty data structures to store books and customers
books = []
customers = []

class Book:
    def __init__(self, title, author, copies, year_published):
        self.title = title
        self.author = author
        self.copies = copies
        self.year_published = year_published

class Customer:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.borrowed_books = []

# Home page
@app.route('/')
def index():
    # Render the HTML template and pass the lists of books and customers
    return render_template('index.html', books=books, customers=customers)

# Add a new book
@app.route('/add_book', methods=['POST'])
def add_book():
    # Retrieve book information from the form
    title = request.form['title']
    author = request.form['author']
    copies = int(request.form['copies'])
    year_published = int(request.form['year_published'])  # Retrieve the year of publication
    # Create a new book object and add it to the books list
    new_book = Book(title, author, copies, year_published)  # Include the year of publication
    books.append(new_book)
    # Redirect back to the home page
    return redirect(url_for('index'))

# Add a new customer
@app.route('/add_customer', methods=['POST'])
def add_customer():
    # Retrieve customer information from the form
    id = request.form['id']
    name = request.form['name']
    # Create a new customer object and add it to the customers list
    new_customer = Customer(id, name)
    customers.append(new_customer)
    # Redirect back to the home page
    return redirect(url_for('index'))

# Borrow a book
@app.route('/borrow_book', methods=['POST'])
def borrow_book():
    # Retrieve customer ID and book title from the form
    customer_id = request.form['customer_id']
    book_title = request.form['book_title']
    # Find the customer by ID
    for customer in customers:
        if customer.id == customer_id:
            # Find the book by title and check if there are available copies
            for book in books:
                if book.title == book_title and book.copies > 0:
                    # Add the borrowed book to the customer's list and update the copies
                    customer.borrowed_books.append(book)
                    book.copies -= 1
                    # Redirect back to the home page
                    return redirect(url_for('index'))
    # If the book or customer is not found, display an error message
    return "Book not found or customer not registered."

# Return a book
@app.route('/return_book', methods=['POST'])
def return_book():
    # Retrieve customer ID and book title from the form
    customer_id = request.form['customer_id']
    book_title = request.form['book_title']
    # Find the customer by ID
    for customer in customers:
        if customer.id == customer_id:
            # Find the borrowed book by title and return it
            for book in customer.borrowed_books:
                if book.title == book_title:
                    # Remove the book from the customer's list and update the copies
                    customer.borrowed_books.remove(book)
                    book.copies += 1
                    # Redirect back to the home page
                    return redirect(url_for('index'))
    # If the book or customer is not found, display an error message
    return "Book not found or customer not registered."

if __name__ == '__main__':
    app.run(debug=True)
