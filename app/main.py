from fastapi import FastAPI
from routers import users, supplier, orders, products
from navigation import pages

app = FastAPI()

# intities
app.include_router(users.router, tags=["users"])
app.include_router(supplier.router, tags=["suppliers"])
app.include_router(orders.router, tags=["orders"])
app.include_router(products.router, tags=["products"])
app.include_router(pages.admin_router, tags=["admin"])

# navigation
app.include_router(pages.router, tags=["navigation"])