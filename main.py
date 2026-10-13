from fastapi import FastAPI,Request,Form,HTTPException
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.templating import Jinja2Templates
from model import Product,Base
from database import engine,LocalSession

app=FastAPI()
templates=Jinja2Templates(directory="templates")
Base.metadata.create_all(bind=engine)
@app.get("/",response_class=HTMLResponse)
def home(req:Request):
    return templates.TemplateResponse(
        request=req,
        name="home.html"
    )

@app.get("/addproducts", response_class=HTMLResponse)
def add_product_page(req: Request):
    return templates.TemplateResponse(
        request=req,
        name="products.html"
    )
@app.post("/add_product",response_class=HTMLResponse)
def add_products(req:Request,product_id:int=Form(),product_name:str=Form(),product_price:float=Form(),product_image_url:str=Form("")):
    clean_name =product_name.strip()
    clean_image_url =product_image_url.strip()
    db=LocalSession()
    if not clean_name:
        raise HTTPException(
            status_code=400,
            detail="Product name cannot be empty",
        )
    if clean_image_url and not clean_image_url.startswith(("https://", "http://")):
        raise HTTPException(
            status_code=400,
            detail="Image URL must start with http:// or https://",
        )
    new_product = Product(
        product_id=product_id,
        product_name=clean_name,
        product_price=product_price,
        product_image_url=clean_image_url or None,
    )

    db.add(new_product)
    db.commit()
    return RedirectResponse(
        url="/products",
        status_code=303
    )


@app.get("/products")
def products(req: Request):
    db=LocalSession()
    product_list = db.query(Product).order_by(Product.product_id).all()

    return templates.TemplateResponse(
        request=req,
        name="products_list.html",
        context={"products": product_list},
    )

@app.delete("/delete_products",response_class=HTMLResponse)
def delete_products(req:Request,product_name:str=Form()):
    db=LocalSession()
    product_list=db.query(Product).filter(
            Product.product_name == product_name
        ).first()
    if product_list is None:
        raise HTTPException( status_code=404,detail="Product not found")
    
    db.delete(product_list)
    db.commit()