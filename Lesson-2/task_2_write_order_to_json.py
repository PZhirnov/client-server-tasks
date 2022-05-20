import json
from datetime import datetime


def write_order_to_json(item: str,
                        quantity: int,
                        price: float,
                        buyer: str,
                        date: datetime) -> 'write order to json':

    with open('orders.json', 'r', encoding='utf8') as f_out:
        data = json.load(f_out)

    orders = data['orders']
    new_order_item = {
        "item": item,
        "quantity": quantity,
        "price": price,
        "buyer": buyer,
        "date": str(date),
    }
    orders.append(new_order_item)

    with open('orders.json', 'w', encoding='utf-8') as f_in:
        json.dump(data, f_in, sort_keys=True, indent=4, ensure_ascii=False)


write_order_to_json('Кресло', 5, 5200.5, 'ООО "Гиик"', datetime.now())
