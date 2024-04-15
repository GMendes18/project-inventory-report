from typing import List
from datetime import datetime
from inventory_report.reports.report import Report
from inventory_report.inventory import Inventory


class SimpleReport(Report):
    def __init__(self):
        self._inventories: List[Inventory] = []

    def add_inventory(self, inventory: Inventory) -> None:
        self._inventories.append(inventory)

    def generate(self) -> str:
        all_products = [
            product for inventory in self._inventories
            for product in inventory.data]
        current_date = datetime.now().date()

        valid_products = [
            product for product in all_products
            if datetime.fromisoformat(product.expiration_date).date() >
            current_date
        ]

        oldest_manufacturing_date = min(
            valid_products,
            key=lambda product: datetime.fromisoformat(
                product.manufacturing_date)
        ).manufacturing_date

        closest_expiration_date = min(
            valid_products,
            key=lambda product: datetime.fromisoformat(product.expiration_date)
        ).expiration_date

        company_inventory = {}
        for product in valid_products:
            company_inventory[product.company_name] = company_inventory.get(
                product.company_name, 0) + 1
        largest_inventory_company = max(
            company_inventory, key=lambda key: company_inventory[key])

        report = (
            f"Oldest manufacturing date: {oldest_manufacturing_date}\n"
            f"Closest expiration date: {closest_expiration_date}\n"
            f"Company with the largest inventory: {largest_inventory_company}"
        )
        return report
