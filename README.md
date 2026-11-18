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
