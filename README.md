
# TODOAPP

## Description
This is a simple Flask-based server with a client script to check the server route.  
It is containerized with Docker and uses a Python virtual environment for dependencies.

## Technologies
- Python 3.11
- Flask 3.1.2
- Requests (for client)
- Docker
- Git/GitHub

## Requirements
- Python 3.11
- Docker
- Virtual environment (optional but recommended)

## Setup

1. **Clone repository**
```bash
git clone https://github.com/CzlowiekMilosz/TODOAPP.git
cd TODOAPP-1
```

2. **Create virtual environment (optional)**
```bash
python -m venv .venv
source .venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

## Running the server with Docker
```bash
docker build -t todoapp .
docker run -p 5002:5000 todoapp
```

- Server will be accessible at `http://127.0.0.1:5002/`  
- You should see:
```json
{"message": "Server is running!"}
```

## Running the client
In a new terminal (with virtual environment activated):
```bash
python client.py
```

- Expected output:
```
Status code: 200
Response: {'message': 'Server is running!'}
```

## Logs
- Docker container logs are visible in the terminal where you run:
```bash
docker run -p 5002:5000 todoapp
```
- Client prints response directly to the terminal.

## Notes
- This setup is for development purposes. Do not use Flask development server in production.
- Port mapping (`5002:5000`) may be changed if the host port is already in use.
