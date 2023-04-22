# Online Marketplace

An online marketplace web application where users can browse and filter items by categories, add reviews and ratings to items, and manage their profiles. Administrators can manage users and items, including adding and deleting users and items.

## Deployment URL

https://e-commerce-service-8eqv.onrender.com/

## Design Decisions

### Programming Language and Frameworks

- Python: Chosen for its simplicity, readability, and a vast number of libraries and frameworks.
- Flask: A lightweight web framework for Python which allows rapid development, is easy to learn, and is easily deployable to platforms like Render.
- MongoDB: A flexible NoSQL database that can store and manage unstructured data, ideal for handling varying details for different item categories.

## User Guide

### Login as a regular user

To log in as a regular user, use one of the following credentials:

- Username: `bugramatik`
- Password: `Deneme123`

or

- Username: `DenemeUser`
- Password: `deneme`

### Login as an admin user

To log in as an admin user, use the following credentials:

- Username: `admin`
- Password: `admin`

### Regular User Features

1. Browse and filter items by categories.
2. View item details, including reviews and ratings.
3. Add reviews and ratings to items.
4. Viewing their average rating and submitted reviews.

### Admin User Features

1. Perform all regular user actions.
2. Add and delete items.
3. Add and delete users.
4. View a list of all users and items.

## Additional Notes

- The project uses bcrypt for hashing and storing passwords securely.
- The app uses MongoDB as the main database, which allows flexibility in handling data with varying structures.

## Running the Project Locally

1. Clone the repository to your local machine.

2. Create a virtual environment:

```bash
python3 -m venv venv
```

3. Activate the virtual environment:

- For Windows:

```bash
venv\Scripts\activate
```

- For macOS and Linux:

```bash
source venv/bin/activate
```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

5. Set the FLASK_APP environment variable:

- For Windows:

```bash
set FLASK_APP=app.py
```

- For macOS and Linux:

```bash
export FLASK_APP=app.py
```

6. Run the Flask application:

```bash
flask run
```

7. Open your web browser and navigate to `http://127.0.0.1:5000/` to view and interact with the web application.

