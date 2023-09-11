# Project Name

Brief description of your project.


[Include a screenshot or demo GIF here if applicable]

## Table of Contents

- [Project Name](Library)
  - [Table of Contents](#table-of-contents)
  - [Description]

    This documentation provides a clear structure for explaining the project, its features, how to get started with it, and other important details. 

    Flask is the main class used to create a Flask application.
    render_template is used to render HTML templates.
    request is used to handle HTTP requests.
    redirect and url_for are used for URL redirection.

    Two empty lists, books and customers, are created to store information about books and customers.

    Two classes, Book and Customer, are defined to represent book and customer objects, respectively. These classes have constructors to initialize their attributes.

    / (index) route corresponds to the home page. It renders an HTML template (index.html) and passes lists of books and customers to be displayed on the page.

    /add_book route corresponds to the home page. It renders an HTML template (index.html) and passes lists of books and customers to be displayed on the page.

    /add_customer route similar to adding a book, it is used to add a new customer. 
    It retrieves customer information from a form, creates a new Customer object, and adds it to the customers list. Then, it redirects back to the home page.

    /borrow_book route handles borrowing a book. 
    It retrieves the customer ID and book title from a form, finds the customer and book by their respective attributes, and updates the lists accordingly. 
    It also checks if there are available copies of the book.

    /return_book route handles returning a book. It works similarly to the borrow_book route but in reverse. It finds the customer and book and returns the book to the library.

    if __name__ == '__main__':
    app.run(debug=True)
    This block of code checks if the script is the main application and then starts the Flask web server in debug mode if it is. 
    Debug mode provides helpful error messages and auto-reloads the server when you make changes to the code during development.


  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Usage]
    1. Access the Web Interface:
    The librarian should open a web browser and navigate to the URL where the library management system is hosted. 
    By default, it's often http://localhost:5000/.

    2. View Existing Books:
    On the home page of the library management system, the librarian can see a list of existing books in the library. 
    This list displays book titles, authors, and the number of copies available.

    3. Add a New Book:
    The librarian can find a section labeled "Add a New Book." 
    This section typically includes input fields for the book's title, author, and the number of copies available.
    The librarian should fill out these fields with the relevant information for the new book they want to add.

    4. Submit the Book Details:
    After entering the book's information, the librarian should click the "Add Book" or "Submit" button, which will initiate a form submission.

    5. Confirmation and Update:
    Upon successful submission, the system should add the new book to the list of books in the library, including the title, author, and the specified number of copies.
    The librarian will usually receive a confirmation message, such as "Book added successfully."

    6. View Updated Book List:
    The librarian can now see the updated list of books, including the newly added book.

    7. Repeat as Needed:
    If the librarian needs to add more books, they can repeat the process by going back to the "Add a New Book" section and entering the details for each additional book.

    8. Log Out:
    Once the librarian has finished adding books, they can log out or simply close the web browser.
    
    
  - [Features]
    The librarian's interaction with the system is through the user-friendly web interface you've created, which simplifies the process of adding books to the library's collection. 
    The system takes care of storing the book details and updating the list of available books accordingly.
  - [Contributing](#contributing)
  - [Testing](#testing)
  - [Deployment](#deployment)
  - [Built With](#built-with)
  - [License](#license)
  - [Acknowledgments](#acknowledgments)

## Description

Provide a clear and concise overview of your project. Explain what it does and why it's useful or interesting. Include any important context or background information.

## Getting Started

Explain how to get started with your project, including any prerequisites and installation instructions. Make it easy for someone to set up and use your project.

### Prerequisites

List any software, libraries, or tools that users need to have installed before they can use your project.

### Installation

Provide step-by-step instructions for installing your project. Include any configuration or setup required.

## Usage

Show examples of how to use your project. Provide code snippets, screenshots, or a demo if possible. Make it easy for users to understand how your project works.

## Features

List the main features or functionality of your project. Highlight what sets it apart from others.

## Contributing

Explain how others can contribute to your project. Include guidelines for submitting bug reports, feature requests, or code contributions. Be clear about your expectations for contributions.

## Testing

Set Up a Virtual Environment (Optional):

It's a good practice to create a virtual environment to isolate your project's dependencies. You can create a virtual environment using the following commands:

# Create a virtual environment (optional)
python -m venv venv

# Activate the virtual environment (on Windows)
venv\Scripts\activate

# Activate the virtual environment (on macOS/Linux)
source venv/bin/activate

install Flask and Required Dependencies:

Inside your virtual environment (if you created one), install Flask and any other required dependencies using pip:

pip install Flask

Save the Application Code:

Save your Flask application code in a Python file (e.g., app.py) in a directory of your choice.

Run the Flask Application:

In your command prompt or terminal, navigate to the directory containing your Flask application (app.py) and run the application:

python app.py

You should see output indicating that the Flask development server is running.

Access the Application:

Open a web browser and visit http://localhost:5000 (or the URL specified in your Flask application if you customized it). You should be able to access and interact with your library management system.

Test the Application:

You can use your web browser to test the functionality by adding books, adding customers, borrowing books, and returning books through the web interface.

Shutdown the Application:

To stop the Flask application, press Ctrl+C in the terminal where the Flask server is running.

Remember that this is a basic test environment for your Flask application. 
In a production environment, you would typically use a production web server (e.g., Gunicorn) and consider deploying your application to a hosting platform like Heroku or a cloud service like AWS or Google Cloud. Additionally, for a production system, you should use a database to store data persistently rather than relying on in-memory data structures as demonstrated in your code.


## Deployment

Remember to have Flask and any required dependencies installed in your Python environment to run this application successfully.

The exact requirements are as follows:

blinker==1.6.2
certifi==2023.7.22
charset-normalizer==3.2.0
click==8.1.7
colorama==0.4.6
distlib==0.3.7
docutils==0.20.1
filelock==3.12.2
Flask==2.3.3
idna==3.4
itsdangerous==2.1.2
Jinja2==3.1.2
Kivy==2.2.1
kivy-deps.angle==0.3.3
kivy-deps.glew==0.3.1
kivy-deps.sdl2==0.6.0
Kivy-Garden==0.1.5
MarkupSafe==2.1.3
Pillow==10.0.0
platformdirs==3.10.0
Pygments==2.16.1
pypiwin32==223
pywin32==306
requests==2.31.0
urllib3==2.0.4
virtualenv==20.24.3
Werkzeug==2.3.7

## Built With

1. Passion

2. In the provided Python Flask application, several technologies, frameworks, and libraries are used. Here's a list of them:

Flask: Flask is a micro web framework for Python. 
It's used to create web applications and provides tools and libraries for building web applications, including handling routing, HTTP requests, and more.

Jinja2: Jinja2 is a templating engine for Python. It's integrated with Flask and is used for rendering HTML templates with dynamic content.

HTML (HyperText Markup Language): HTML is the standard markup language used for creating web pages. The application uses HTML templates to structure and display web content.

HTTP (Hypertext Transfer Protocol): HTTP is the protocol used for communication between web browsers and web servers. The request object from Flask is used to handle incoming HTTP requests.

Python: Python is the programming language in which the entire application is written.

These are the core technologies and frameworks used in the application.

## License

This project is licensed under the Strict License - see the Unusially Strict License for details.

## Acknowledgments

In our pursuit of knowledge and professional growth, we would like to extend our heartfelt appreciation to John Bryce Tel Aviv and its esteemed team of talented lecturers. 
Their dedication and expertise have played an integral role in shaping our educational journey, and we are deeply grateful for their commitment to excellence.
John Bryce Tel Aviv has consistently demonstrated a commitment to providing high-quality education and training programs that empower individuals to thrive in their respective fields. 
The institution's unwavering dedication to fostering a culture of continuous learning and innovation is truly commendable.
Equally praiseworthy are the lecturers who have shared their wisdom, industry insights, and expertise with us. 
Their passion for teaching, coupled with their real-world experience, has enriched our learning experiences and equipped us with the skills and knowledge needed to excel in our careers.
We would like to express our gratitude for the unwavering support, guidance, and mentorship provided by John Bryce Tel Aviv and its lecturers. 
Their contributions have not only enhanced our professional capabilities but have also inspired us to strive for excellence in all our endeavors.
In conclusion, it is with deep respect and appreciation that we acknowledge John Bryce Tel Aviv and its dedicated lecturers for their invaluable contributions to our educational and professional development. 
Their commitment to nurturing talent and fostering growth sets a benchmark for excellence that we will carry forward throughout our careers.
Thank you, John Bryce Tel Aviv, and the remarkable lecturers who have been instrumental in our journey towards success.
