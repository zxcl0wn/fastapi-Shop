from pydantic import BaseModel, Field


class CartItemBase(BaseModel):
    product_id: int = Field(..., description="Product ID")
    quantity: int = Field(..., gt=0, description="Quantity must be greater than 0")


class CartItemCreate(CartItemBase):
    ...


class CartItemUpdate(BaseModel):
    product_id: int|None = Field(None, description="Product ID")
    quantity: int|None = Field(None, gt=0, description="Quantity must be greater than 0")


class CartItem(BaseModel):
    product_id: int
    name: str = Field(..., description="Product name")
    price: float = Field(..., gt=0, description="Product price")
    quantity: int = Field(..., gt=0, description="Quantity must be greater than 0")
    subtotal: float = Field(..., description="Total price for this item (price * quantity)")
    image_url: str|None = Field(None, description="Product image url")


class CartResponse(BaseModel):
    items: list[CartItem] = Field(..., description="List of items in the cart")
    total: float = Field(..., description="Total price of all items in the cart")
    items_count: int = Field(..., description="Number of items in the cart")
