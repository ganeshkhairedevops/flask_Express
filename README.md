# Flask Frontend + Express Backend (with Docker)

This is a simple web application with a **Flask frontend** and an **Express.js backend**, communicating via REST API. The whole setup runs using Docker and Docker Compose.

---
## 📁 Project Structure
project/
├── backend/
│ ├── Dockerfile
│ ├── index.js
│ └── package.json
├── frontend/
│ ├── Dockerfile
│ ├── app.py
│ ├── requirements.txt
│ ├── templates/
│ │ └── index.html
│ └── static/
│ └── script.js
└── docker-compose.yml

Access the App:
Frontend (Flask): http://localhost:5000

Backend (Express API): http://localhost:3001/api/data


📦 Tech Stack
Frontend: Flask (Python)

Backend: Express.js (Node.js)

Containerization: Docker + Docker Compose