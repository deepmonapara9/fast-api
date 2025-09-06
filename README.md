# Basic FastAPI Template

This is a basic FastAPI template that includes a simple product API with CRUD functionality. It uses SQLAlchemy for database interactions and is configured to work with a React frontend.

## Features

*   FastAPI backend with automatic API documentation
*   SQLAlchemy for database ORM
*   Basic CRUD endpoints for products
*   CORS middleware for frontend development
*   Database initialization with sample data
*   React frontend integration ready

## Project Structure

```
├── main.py              # FastAPI application entry point
├── models.py            # Pydantic models for API validation
├── database_models.py   # SQLAlchemy database models
├── config.py            # Database configuration
├── pyproject.toml       # Python dependencies
├── frontend/            # React frontend application
│   ├── src/
│   ├── public/
│   └── package.json
└── README.md
```

## Setup Instructions

### Backend (FastAPI)

#### Option 1: Using uv (Recommended)

1. Install uv (if not already installed):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. Create and activate a virtual environment with dependencies:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   uv pip install -e .
   ```

3. Run the FastAPI server:
   ```bash
   uv run uvicorn main:app --reload
   ```

#### Option 2: Using pip

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -e .
   ```

3. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

4. Access the API documentation at: http://localhost:8000/docs

### Frontend (React)

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

4. Access the frontend at: http://localhost:3000

## API Endpoints

### Products

- `GET /products` - Get all products
- `GET /products/{id}` - Get a specific product by ID
- `POST /products` - Create a new product
- `PUT /products/{id}` - Update a product by ID
- `DELETE /products/{id}` - Delete a product by ID

## Sample Product Data

The API comes pre-loaded with sample products:
- Phone (ID: 1) - ₹58,499
- Laptop (ID: 2) - ₹83,499
- Pen (ID: 3) - ₹166
- Table (ID: 4) - ₹16,699

## Dependencies

This project uses `pyproject.toml` for dependency management. Main dependencies include:

- **FastAPI** (>=0.104.0) - Modern web framework for building APIs
- **Uvicorn** (>=0.24.0) - ASGI server for running FastAPI applications
- **SQLAlchemy** (>=2.0.0) - Database ORM for Python
- **Pydantic** (>=2.0.0) - Data validation using Python type annotations
- **Python-multipart** (>=0.0.6) - For handling form data and file uploads

### Development Dependencies

- **pytest** (>=7.0.0) - Testing framework
- **pytest-asyncio** (>=0.21.0) - For testing async code
- **httpx** (>=0.25.0) - HTTP client for testing API endpoints

Install development dependencies with:
```bash
uv pip install -e ".[dev]"  # Using uv
# or
pip install -e ".[dev]"     # Using pip
```

## Development Notes

- The database is automatically initialized with sample data on first run
- CORS is enabled for `http://localhost:3000` to support React development
- The API uses dependency injection for database sessions
- SQLAlchemy handles database operations with proper session management
