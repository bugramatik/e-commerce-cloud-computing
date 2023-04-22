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

## MongoDB Structure

The project uses MongoDB as the main database for storing and managing data. The database contains three main collections: users, items, and categories.

## users Collection

The users collection stores information about the users, including their username, admin status, and hashed password.

Example documents:

` { "_id": {"$oid": "64426dc889ae0ac80c59a45c"}, "username": "bugramatik", "is_admin": false, "password": "$2b$12$Oe8HgGI9kyvU/ssK2akAP.TkUfVxO7Q6z580sOB0UrJUEkjKaQ1pq" } `

` { "_id": {"$oid": "64426de089ae0ac80c59a45d"}, "username": "admin", "is_admin": true, "password": "$2b$12$n822RAZri.uBrQ/1dZf9Re5PhvrFySQq/gXm.nXEFjqVu8pIO/Fl6" } `

These documents store user information, such as whether a user is an admin, as well as their securely hashed password. 

### items Collection

The items collection stores information about individual items, including the item's name, category, description, price, seller, image URL, rating, reviews, rates, number of rates, and item-specific details.

Example document:

 `{ "_id": {"$oid": "64436beaa70075e537ba90c1"}, "name": "T-shirt", "category": "6441d8f902031b1dd547d1ac", "description": "Metallica Tshirt", "price": {"$numberDouble": "125.0"}, "seller": "64426dc889ae0ac80c59a45c", "image_url": "https://productimages.hepsiburada.net/s/129/600-800/110000079540660.jpg", "rating": {"$numberDouble": "4.0"}, "reviews": { "bugramatik": "new rewiev 2", "DenemeUser": "Delivery was great", "admin": "admin review" }, "rates": { "bugramatik": {"$numberInt": "4"}, "DenemeUser": {"$numberInt": "3"}, "admin": {"$numberInt": "5"} }, "details": { "size": "M", "colour": "Green" }, "number_of_rates": {"$numberInt": "3"} } `

In the details field, only the relevant attributes for the specific item category are stored. In this example, the item is in the "Clothing" category, so the details field includes the "size" and "colour" attributes. 

### categories Collection

I created categories collection for storing the categories of items and the details specific to each category. This allows the app to dynamically add and delete categories, and also allows the app to handle items with varying details. For this version of app just database admin can add a new category type.

Example documents:

 `{ "_id": {"$oid": "6441d8f902031b1dd547d1ac"}, "name": "Clothing", "specific_to_category": ["colour", "size"] }` 

 `{ "_id": {"$oid": "6441d93202031b1dd547d1ad"}, "name": "Computer Components", "specific_to_category": ["spec"] } ` 

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

