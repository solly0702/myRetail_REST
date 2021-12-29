from api.product.model import Product


def test_model():
    product = Product()

    assert product.collection_name == "product"

    product_fields = list(product.product_model._schema["properties"].keys())
    assert product_fields.sort() == [
        "id, name, current_price"].sort()

    current_price_field = list(
        product.current_price_model._schema["properties"].keys())
    assert current_price_field.sort() == [
        "value", "currency_code"].sort()
