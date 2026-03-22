# Use a minimal Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Environment variables for better Python behavior
# - Disable .pyc files
# - Enable unbuffered logs (important for Docker logs)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies (CA certificates for SSL)
# Clean apt cache to keep image small
RUN apt-get update && apt-get install -y \
    ca-certificates \
    && update-ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Create a non-root user for security (best practice)
RUN useradd -m appuser

# Copy only requirements first to leverage Docker cache
COPY requirements.txt .

# Upgrade pip and install dependencies
# Using trusted-host to bypass SSL issues (dev/proxy environments)
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir \
    --trusted-host pypi.org \
    --trusted-host files.pythonhosted.org \
    --trusted-host pypi.python.org \
    -r requirements.txt

# Copy application code
COPY app ./app
COPY scripts ./scripts
COPY orders.db ./orders.db
COPY .env.example ./.env.example
COPY README.md ./README.md

# Set proper permissions for scripts
RUN chmod +x ./scripts/start.sh

# Change ownership to non-root user
RUN chown -R appuser:appuser /app

# Switch to non-root user (security best practice)
USER appuser

# Expose application port
EXPOSE 8000

# Start the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

