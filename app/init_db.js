db = db.getSiblingDB("myRetail");
db.product.drop();

db.product.insertMany([
    {
        "id": 13860428,
        "name": "The Big Lebowski (Blu-ray) (Widescreen)",
        "current_price": {
            "value": 13.49,
            "currency_code": "USD"
        }
    },
    {
        "id": 12345678,
        "name": "Prod",
        "current_price": {
            "value": 99.99,
            "currency_code": "USD"
        }
    },
    {
        "id": 46598254,
        "name": "Test",
        "current_price": {
            "value": 9.99,
            "currency_code": "WON"
        }
    },
    {
        "id": 46137954,
        "name": "Dev",
        "current_price": {
            "value": 0.99,
            "currency_code": "WON"
        }
    },
]);