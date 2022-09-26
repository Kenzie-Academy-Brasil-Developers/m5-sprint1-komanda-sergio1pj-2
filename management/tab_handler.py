from utils import json_handler
from datetime import datetime

def calculate_tab(data: list[dict]) -> dict:
    read = json_handler.read_json("menu.json")
    total = 0
    for p in data:
        list = [x for x in read if x["id"] == p["id"]]
        total += list[0]["price"] * p["amount"] 
    return dict(subtotal=total, created_at=datetime.now().strftime("%d/%m/%Y %H:%M:%S"))