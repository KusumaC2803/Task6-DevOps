# Task 6 - Multi-Container Orchestration

## Technologies
- Docker
- Docker Compose
- Python Flask
- Redis

## Features
- Multi-container application
- Service-to-service networking
- Health checks
- Restart policy
- Scaling
- Environment variables using .env

## Run

docker compose up --build

## Scale

docker compose up --scale web=3

## Health Check

http://localhost:5000/health