from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uuid import uuid4
from typing import List, Dict

app = FastAPI()

# In-memory storage for receipts
receipts: Dict[str, int] = {}

# Data models
class Item(BaseModel):
    shortDescription: str
    price: str

class Receipt(BaseModel):
    retailer: str
    purchaseDate: str
    purchaseTime: str
    items: List[Item]
    total: str

# Function to calculate points based on rules
def calculate_points(receipt: Receipt) -> int:
    points = 0

    # Rule 1: 1 point per alphanumeric character in retailer name
    points += sum(c.isalnum() for c in receipt.retailer)

    # Rule 2: 50 points if total is a whole number
    if receipt.total.endswith(".00"):
        points += 50

    # Rule 3: 25 points if total is multiple of 0.25
    if float(receipt.total) % 0.25 == 0:
        points += 25

    # Rule 4: 5 points per two items
    points += (len(receipt.items) // 2) * 5

    # Rule 5: If description length is a multiple of 3, award price * 0.2 points
    for item in receipt.items:
        if len(item.shortDescription.strip()) % 3 == 0:
            points += round(float(item.price) * 0.2)

    # Rule 6: 6 points if purchase date is an odd day
    if int(receipt.purchaseDate.split("-")[-1]) % 2 == 1:
        points += 6

    # Rule 7: 10 points if purchase time is between 2 PM and 4 PM
    hour = int(receipt.purchaseTime.split(":")[0])
    if 14 <= hour < 16:
        points += 10

    return points

@app.post("/receipts/process")
def process_receipt(receipt: Receipt):
    receipt_id = str(uuid4())
    points = calculate_points(receipt)
    receipts[receipt_id] = points
    return {"id": receipt_id}

@app.get("/receipts/{receipt_id}/points")
def get_points(receipt_id: str):
    if receipt_id not in receipts:
        raise HTTPException(status_code=404, detail="Receipt not found")
    return {"points": receipts[receipt_id]}