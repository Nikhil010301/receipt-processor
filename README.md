# 🚀 Receipt Processor API - FastAPI Implementation

A FastAPI-based REST API that processes receipts and calculates reward points based on the **Fetch Rewards Receipt Processor Challenge** requirements.

## 📌 Features & Functionality
✅ **`POST /receipts/process`** – Processes a receipt, calculates points, and returns a unique `receipt_id`.  
✅ **`GET /receipts/{receipt_id}/points`** – Retrieves the reward points for a given receipt.  
✅ **Automatic validation** using Pydantic (ensures correct data format).  
✅ **Live API documentation** at `/docs` (Swagger UI).  

---

## 📌 API Endpoints

### **1️⃣ `POST /receipts/process` - Process a Receipt**
#### 📩 Request Body (JSON)
```json
{
  "retailer": "Apple Store",
  "purchaseDate": "2024-02-01",
  "purchaseTime": "14:30",
  "items": [
    {"shortDescription": "MacBook Pro", "price": "1299.00"},
    {"shortDescription": "Magic Mouse", "price": "99.00"}
  ],
  "total": "1398.00"
}
```
✅ **Response (200 OK)**  
```json
{
  "id": "55568eb4-4fe6-471a-85e5-ebb3bb7a2fb8"
}
```
### **2️⃣ `GET /receipts/{receipt_id}/points` - Retrieve Points**


#### 📩 Request URL
```json
GET http://127.0.0.1:8000/receipts/55568eb4-4fe6-471a-85e5-ebb3bb7a2fb8/points
```
✅ **Response (200 OK)**  
```json
{
  "points": 106
}
```

## 📌 Points Calculation Logic

- **Retailer Name** → 1 point per **alphanumeric character**.

- **Total Amount**:
  - ✅ **+50 points** if it’s a **whole number** (e.g., `10.00` → ✅).
  - ✅ **+25 points** if it’s **a multiple of 0.25** (e.g., `7.25`, `8.50` → ✅).

- **Items Purchased**:
  - ✅ **+5 points** per **two items**.
  - ✅ If an **item’s description length is a multiple of 3**, you get **20% of its price as points**.

- **Purchase Date**:
  - ✅ **+6 points** if the **day is odd**.

- **Purchase Time**:
  - ✅ **+10 points** if **between 2 PM - 4 PM**.

---

✅ **Our implementation follows these exact rules!** 🎯


## 📌 Installation & Running the API

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Nikhil010301/receipt-processor.git
cd receipt-processor
```

### 2️⃣ Set Up Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # Assuming Mac/Linux
```
### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Run the API
```bash
uvicorn main:app --reload
```



## 📌 How to Test the API

### 🚀 Swagger UI 
- Open **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**  
- Try out:
  - **`POST /receipts/process`** (to submit a receipt)
  - **`GET /receipts/{receipt_id}/points`** (to retrieve points)

---

### 🛠️ cURL Commands

#### **1️⃣ Process a Receipt (`POST` Request)**
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/receipts/process' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "retailer": "Apple Store",
  "purchaseDate": "2024-02-01",
  "purchaseTime": "14:30",
  "items": [
    {"shortDescription": "MacBook Pro", "price": "1299.00"},
    {"shortDescription": "Magic Mouse", "price": "99.00"}
  ],
  "total": "1398.00"
}'
```

#### **2️⃣ Retrieve Points (`GET` Request)**
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/receipts/{receipt_id}/points' \
  -H 'accept: application/json'
```

#### Replace {receipt_id} with the actual ID returned from the POST request.

## 📌 Author

👤 **Nikhil Tammina**  
🔗 **GitHub:** [Nikhil010301](https://github.com/Nikhil010301)  
📧 **Email:** [tamminanikhil01@gmail.com](mailto:tamminanikhil01@gmail.com)  
