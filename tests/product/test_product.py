from inventory_report.product import Product
import pytest


@pytest.fixture
def default_product():
    id = "12345"
    product_name = "Product Name"
    company_name = "Company Name"
    manufacturing_date = "2024-01-01"
    expiration_date = "2024-12-31"
    serial_number = "ABCDE12345"
    storage_instructions = "Store in a cool, dry place."

    return Product(
        id=id,
        product_name=product_name,
        company_name=company_name,
        manufacturing_date=manufacturing_date,
        expiration_date=expiration_date,
        serial_number=serial_number,
        storage_instructions=storage_instructions
    )


def test_create_product(default_product) -> None:
    product = default_product
    assert product.id == "12345"
    assert product.product_name == "Product Name"
    assert product.company_name == "Company Name"
    assert product.manufacturing_date == "2024-01-01"
    assert product.expiration_date == "2024-12-31"
    assert product.serial_number == "ABCDE12345"
    assert product.storage_instructions == "Store in a cool, dry place."
