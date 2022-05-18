import json
from datetime import datetime


def write_order_to_json(item: str,
                        quantity: int,
                        price: float,
                        buyer: str,
                        date: datetime) -> 'write order to json':
    orders_dict = {
        "orders": [
            {
                "item": item,
                "quantity": quantity,
                "price": price,
                "buyer": buyer,
                "date": str(date),
            }
        ]
    }

    with open('orders.json', 'w', encoding='utf-8') as f:
        json.dump(orders_dict, f, sort_keys=True, indent=4, ensure_ascii=False)


write_order_to_json('Кресло', 5, 5200.5, 'ООО "Гиик"', datetime.now())
