import pytest
from inventory_report.product import Product


@pytest.fixture
def product_instance():
    product_data = {
        "id": "12345",
        "product_name": "Farinha",
        "company_name": "Farinini",
        "manufacturing_date": "01-05-2021",
        "expiration_date": "02-06-2023",
        "serial_number": "TY68409CJJ43ASD1PL2F",
        "storage_instructions": (
            "precisa ser armazenado em local protegido "
            "da luz."
        )
    }

    return Product(**product_data)


def test_product_report(product_instance):
    product = product_instance

    # Testando cada trecho da frase gerada pelo método __str__
    assert "The product 12345 - Farinha" in str(product)
    assert "with serial number TY68409CJJ43ASD1PL2F" in str(product)
    assert "manufactured on 01-05-2021" in str(product)
    assert "by the company Farinini" in str(product)
    assert "valid until 02-06-2023" in str(product)
    assert "must be stored according to the following instructions: precisa " \
        "ser armazenado em local protegido da luz." in str(product)
