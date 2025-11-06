FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Avoid cache purge by adding requirements first
ADD ./pyproject.toml ./pyproject.toml

RUN pip install uv wheel
RUN uv pip install -e . --system

# Add the rest of the files
COPY . /app
WORKDIR /app

# Set PYTHONPATH to ensure modules can be imported
ENV PYTHONPATH=/app

# Default command (can be overridden by task definition)
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5001"]
