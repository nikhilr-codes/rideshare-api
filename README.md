# Ridex Backend API 🚕

A simple Ride Sharing Backend API built using Django REST Framework.

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```
git clone https://github.com/nikhilr-codes/rideshare.git

```

### 2. Create Virtual Environment (optional but recommended)

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Apply Migrations

```
python manage.py migrate
```

### 5. Run Server

```
python manage.py runserver
```

Server will run at:

```
http://127.0.0.1:8000/
```

---

## 📌 API Endpoints

| Method | Endpoint                       | Description                 |
| ------ | ------------------------------ | --------------------------- |
| GET    | /api/rides/                    | List all rides              |
| POST   | /api/rides/                    | Create a ride               |
| GET    | /api/rides/{id}/               | Get ride details            |
| POST   | /api/rides/{id}/accept_driver/ | Assign driver & accept ride |
| PATCH  | /api/rides/{id}/change_status/ | Update ride status          |

---

## 🔄 Ride Flow

1. Create Ride → `requested`
2. Accept Ride → `accepted`
3. Update Status → `started / completed / cancelled`

---

## 📊 Status Values

* requested
* accepted
* started
* completed
* cancelled

---

## 🧠 Notes

* Rider is automatically assigned when creating a ride.
* Driver is assigned when accepting the ride.
* Status is automatically set to **accepted** during ride acceptance.
* Status can be updated manually using the update endpoint.

---

## 🛠 Tech Stack

* Python
* Django
* Django REST Framework

---

## 👨‍💻 Author

Nikhil
