# Performance Lab Backend (FastAPI)

A lightweight but robust API designed to serve as a data provider for the **React Performance Lab**. This backend focuses on simulating real-world engineering scenarios where high-frequency data and large payloads are common.

## 🛠 Features

- **FastAPI Core:** Leveraging asynchronous endpoints for non-blocking I/O.
- **Large Dataset Simulation:** Endpoints capable of generating 100k+ records for virtualization testing.
- **CORS Configured:** Pre-configured for seamless integration with modern frontend development servers (Vite).
- **Type Safety:** Full Python type hinting for better maintainability.

## 🚀 Quick Start

1. Create a virtual environment: `python -m venv venv`
2. Activate it: `source venv/bin/activate` (or `venv\Scripts\activate` on Windows)
3. Install dependencies: `pip install fastapi uvicorn`
4. Run the server: `uvicorn main:app --reload`

## 📡 Key Endpoints

- `GET /`: Health check and system status.
- `GET /data`: Returns a simulated heavy payload for frontend optimization tests.
