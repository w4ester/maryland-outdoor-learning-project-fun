# OLP Backend - Lightweight Python Container
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .
COPY faq_data.py .

# Non-root user for security
RUN useradd -m -u 1000 olp && chown -R olp:olp /app
USER olp

EXPOSE 5000

CMD ["python", "app.py"]
