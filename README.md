# TripPythonAPI

A REST API built with **Flask**.

## Table of Contents

- [Tech Stack](#tech-stack)
- [Running Locally](#running-locally)
- [Endpoints](#endpoints)

## Tech Stack

- Python 3
- Flask

## Running Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/fczanardo/TripPythonAPI.git
   cd TripPythonAPI
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the application:
   ```bash
   python application.py
   ```

4. Access at: `http://localhost:5000`

## Endpoints

| Method | Route     | Description                  |
|--------|-----------|------------------------------|
| GET    | `/`       | Checks if the API is running |
| GET    | `/health` | Application health check     |

---

Made by **Fabio Zanardo**
