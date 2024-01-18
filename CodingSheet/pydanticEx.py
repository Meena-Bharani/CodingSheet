import requests
from rich import print  # helps to align the json data
from pydantic import BaseModel, field_validator

class Variant(BaseModel):  #pydantic
    title: str
    sku: str
    price: str
    grams: int

    @field_validator('sku')
    def check_sku_length(cls, value):
        required_length = 10
        if len(value) != required_length:
            raise  ValueError('sku must be 10 chars long')
        return value

class Product(BaseModel):  # pydantic
    id: int
    title: str
    variants: list[Variant]

def get_data():
    response = requests.get('https://www.allbirds.co.uk/products.json')
    return response.json()['products']
def main():
    products = get_data()
    for product in products:
        item = Product(**product)   # pydantic
        print(item.dict())
        # print(item)

if __name__ == '__main__':
    main()