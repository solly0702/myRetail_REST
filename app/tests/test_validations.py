import pytest
from factory.validation import Validator
from api.product.model import Product


def test_validations():
    product = Product()
    validator = Validator()

    fields = product.product_model._schema["properties"]
    fields["current_price"] = product.current_price_model._schema["properties"]

    payload = {
        "id": 13860428,
        "name": "The Big Lebowski (Blu-ray) (Widescreen)",
        "current_price": {
            "value": 13.49,
            "currency_code": "USD"
        }
    }

    assert validator.validate(payload, fields) == True

    fail_payload = {
        "id": 13860428,
        "name": "The Big Lebowski (Blu-ray) (Widescreen)",
        "current_price": {
            "value": "13.49",
            "currency_code": "USD"
        }
    }

    with pytest.raises(ValueError):
        validator.validate(fail_payload, fields)
