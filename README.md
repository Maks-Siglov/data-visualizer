# Data Visualizer

A FastAPI application for visualizing CSV data as interactive bar charts using Plotly.

## Overview

This project provides a REST API that reads data from CSV files and generates interactive visualizations. It uses dependency injection for clean architecture and supports multiple output formats (HTML and JSON).


## Tech Stack

- **FastAPI** - Modern web framework
- **Plotly** - Interactive visualization library
- **Pandas** - Data manipulation
- **Pydantic Settings** - Configuration management
- **Dependency Injector** - Dependency injection container

## Requirements

- Python 3.13+
- Poetry (for dependency management)

## Installation

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/Maks-Siglov/data-visualizer.git
cd data-visualizer
```

2. Install dependencies:
```bash
poetry install
```

3. Create `.env` file in the project root:
```env
APP_HOST=0.0.0.0
APP_PORT=8000
APP_DEBUG=true

CSV_FILE_PATH=src/data/input_data.csv
CSV_ENCODING=utf-8
```

4. Run the application:
```bash
# Using Python module
python3 -m src.main

# Or using Poetry
poetry run python3 -m src.main

# Or using uvicorn directly
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
```

### Docker

1. Build the Docker image:
```bash
docker build -t data-visualizer .
```

2. Run the container:
```bash
# Using .env file
docker run -p 8000:8000 --env-file .env data-visualizer

```


## Project Structure

```
data-visualizer/
├── src/
│   ├── api/
│   │   └── v1/
│   │       ├── __init__.py
│   │       └── visualization.py      # API endpoints
│   ├── core/
│   │   ├── __init__.py
│   │   └── exceptions.py             # Custom exceptions
│   ├── data/
│   │   └── input_data.csv            # Sample CSV data
│   ├── data_source/
│   │   ├── __init__.py
│   │   ├── base.py                   # DataSource interface
│   │   └── csv.py                    # CSV implementation
│   ├── services/
│   │   ├── __init__.py
│   │   └── visualization.py          # Visualization service
│   ├── system/
│   │   ├── __init__.py
│   │   └── resources.py              # DI container
│   ├── __init__.py
│   ├── config.py                     # Configuration
│   └── main.py                       # FastAPI app entry point
├── .dockerignore
├── .env                              # Environment variables
├── Dockerfile
├── pyproject.toml                    # Dependencies
├── poetry.lock
└── README.md
```

## Configuration

All configuration is managed through environment variables defined in `.env`:


## Development

### Code Style

The project uses Ruff for linting:

```bash
poetry run ruff check src/
```

## Usage

Once the application is running, access:

- **API Documentation**: http://localhost:8000/docs
- **Alternative Docs**: http://localhost:8000/redoc
- **Root Endpoint**: http://localhost:8000

### API Endpoints

#### Create Bar Chart
```
GET /api/v1/visualize/bar-chart
```

**Query Parameters:**
- `title` (optional) - Chart title (default: "Bar Chart")
- `top_n` (optional) - Show only top N records
- `sort_by` (optional) - Sort by "value" or "name" (default: "value")
- `output_format` (optional) - "html" or "json" (default: "html")