# STAGE 1: BUILD FRONTEND
FROM node:18-alpine AS frontend-build

WORKDIR /app/frontend
COPY frontend/package.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build


# STAGE 2: BUILD BACKEND + COMBINE EVERYTHING
FROM python:3.11-slim

# Install Nginx
RUN apt-get update && apt-get install -y nginx && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Backend Setup
COPY backend/requirements.txt ./backend/
RUN pip install --no-cache-dir -r backend/requirements.txt
COPY backend/ ./backend/

# Frontend Setup
COPY --from=frontend-build /app/frontend/dist ./dist

# Write nginx config using Python to avoid shell escaping issues
RUN python3 -c "
config = '''server {
    listen 80;
    location / {
        root /app/dist;
        index index.html;
        try_files \$uri \$uri/ /index.html;
    }
    location /api {
        proxy_pass http://localhost:8000;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
    }
}'''
open('/etc/nginx/conf.d/default.conf', 'w').write(config)
"

# Remove default nginx config
RUN rm -f /etc/nginx/sites-enabled/default

# Startup Script
COPY startup.sh ./
RUN chmod +x startup.sh

EXPOSE 80
EXPOSE 8000

CMD ["./startup.sh"]