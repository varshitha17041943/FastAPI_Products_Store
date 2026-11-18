# Product Store Web Application

A full-stack product catalog web application built with **Python**, **FastAPI**, **SQLAlchemy ORM**, **MySQL**, and **Jinja2** templates. The application enables users to add products via validated HTML forms, browse the sorted product catalog, and manage inventory through RESTful routes.

---

## Features

- **Product Catalog Management:** View all available products sorted by `product_id`, displaying product names, prices (₹), and product images.
- **Add New Products:** Submit new items through an HTML form with server-side validation for non-empty product names and valid `http://` / `https://` image URLs.
- **Product Deletion:** Remove existing products by name with structured `404 Not Found` HTTP exception handling.
- **ORM Database Integration:** Uses SQLAlchemy ORM (`Product` model) for clean schema definition and MySQL database operations.
- **Interactive API Docs:** Automatically generated Swagger UI (`/docs`) and ReDoc (`/redoc`) endpoints provided by FastAPI.

---

## Tech Stack

- **Backend Framework:** Python, FastAPI
- **Frontend & Templating:** HTML5, Jinja2 Templates
- **Database & ORM:** MySQL, SQLAlchemy ORM, `mysql-connector-python`
- **Server:** Uvicorn

---

## Project Structure

```text
product_store_fastapi_project/
├── database.py               # SQLAlchemy engine and session configuration
├── model.py                  # Product ORM model definition
├── main.py                   # FastAPI routes, form validation, and error handling
└── templates/
    ├── home.html             # Landing page with navigation links
    ├── products.html         # Form interface to add new products
    └── products_list.html    # Dynamic product catalog display
```

---

## API & Web Routes

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` | Renders the store landing page (`home.html`) |
| `GET` | `/addproducts` | Renders the form page to add a new product (`products.html`) |
| `POST` | `/add_product` | Validates form inputs, saves the product to MySQL, and redirects to `/products` |
| `GET` | `/products` | Queries all products ordered by ID and renders `products_list.html` |
| `DELETE` | `/delete_products` | Deletes a matching product by `product_name` or returns a `404` error |

---

## Database Schema (`products` Table)

Defined in `model.py` using SQLAlchemy:

| Column | Type | Constraints |
| :--- | :--- | :--- |
| `product_id` | `Integer` | Primary Key, Indexed |
| `product_name` | `String(100)` | Not Null |
| `product_price` | `Float(10, 2)` | Not Null |
| `product_image_url` | `String(500)` | Nullable |

---

## Setup & Installation

### 1. Clone the Repository
```bash
git clone [https://github.com/varshitha17041943/FastAPI_Products_Store.git](https://github.com/varshitha17041943/FastAPI_Products_Store.git)
cd FastAPI_Products_Store
```

### 2. Create & Activate a Virtual Environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install fastapi uvicorn sqlalchemy mysql-connector-python jinja2 python-multipart
```

### 4. Configure MySQL Database
1. Start your local MySQL server and create the database:
   ```sql
   CREATE DATABASE productfastapi;
   ```
2. Update your database connection string in `database.py`:
   ```python
   url = "mysql+mysqlconnector://<username>:<password>@localhost:3306/productfastapi"
   ```

### 5. Run the Application
```bash
uvicorn main:app --reload
```

Open your browser and navigate to:
- **Web App:** `http://127.0.0.1:8000/`
- **Swagger API Docs:** `http://127.0.0.1:8000/docs`

---

## Author

**Varshitha Reddy**  
- GitHub: [@varshitha17041943](https://github.com/varshitha17041943)  
- LinkedIn: [N Varshitha](https://www.linkedin.com/in/n-varshitha)
