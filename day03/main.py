from json_utils import read_json, write_json

orders = [
    {"customer": "Amy", "amount": 1200},
    {"customer": "Bob", "amount": 800},
    {"customer": "Leo", "amount": 2600}
]

def summary_data(orders_data):
   total = 0
   count = len(orders_data)

   for order in orders_data:
       total += order["amount"]

   return {"total_amount": total,"order_count": count}

if __name__ == "__main__":
    input_path = "data/orders.json"
    write_json(input_path, orders)
    new_orders = read_json(input_path)

    if new_orders is not None:
        summary_dict = summary_data(new_orders)
        write_json("data/summary.json", summary_dict)
