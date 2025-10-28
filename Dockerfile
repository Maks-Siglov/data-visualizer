FROM python:3.13-slim

# Set working directory
WORKDIR /app


RUN pip install poetry

# Copy dependency files
COPY pyproject.toml poetry.lock* ./

# Install project dependencies
RUN poetry config virtualenvs.create false
RUN poetry install --only main --no-root

# Copy project files
COPY . .

# Expose port
EXPOSE 8000

# Run the application
CMD ["python3", "-m", "src.main"]