#!/bin/bash
echo "Starting CI/CD Framework App..."

# Start FastAPI backend in background
cd /app/backend
uvicorn app.main:app --host 0.0.0.0 --port 8000 &

# Wait for backend to start
sleep 2

# Remove default nginx config
rm -f /etc/nginx/sites-enabled/default

# Start Nginx in foreground
echo "Starting Nginx..."
nginx -g 'daemon off;' &

# Wait and check
sleep 2
echo "All services started!"

# Keep container alive
wait
