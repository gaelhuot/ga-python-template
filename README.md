# GA Python Template

[![CI](https://github.com/gaelhuot/ga-python-template/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/gaelhuot/ga-python-template/actions/workflows/ci.yml)
[![Security Scan](https://github.com/gaelhuot/ga-python-template/actions/workflows/security.yml/badge.svg?branch=master)](https://github.com/gaelhuot/ga-python-template/actions/workflows/security.yml)
[![Docker](https://github.com/gaelhuot/ga-python-template/actions/workflows/cd.yml/badge.svg?branch=master)](https://github.com/gaelhuot/ga-python-template/actions/workflows/cd.yml)

A simple Python FastAPI template project for testing GitHub Actions and personal development purposes.

## 📋 Project Description

This project is a template for a Python FastAPI project that includes GitHub Actions for CI/CD, security scanning, and deployment. It is designed to be a starting point for new projects and to help developers test GitHub Actions and personal development purposes.

## 🚀 Features

### Core Framework
- **FastAPI** - Modern, fast web framework for building APIs
- **Pydantic** - Data validation and settings management
- **Type Hints** - Full type annotation support for better code quality
- **Async Support** - Full async/await support with proper resource management

### Production-Ready Features
- **Application Lifespan** - Proper startup/shutdown with shared resources (HTTP clients, etc.)
- **Structured Logging** - Request correlation with unique request IDs
- **Error Handling** - Global exception handlers with structured JSON responses
- **Health Checks** - Separate liveness (`/health`) and readiness (`/health/ready`) probes
- **Metrics** - Prometheus metrics endpoint (`/metrics`) for monitoring
- **CORS Security** - Production-ready CORS configuration with environment-based restrictions
- **Service Layer** - Clean architecture with separated business logic

### API & Documentation
- **OpenAPI 3.0** - Rich API documentation with metadata (contact, license, servers)
- **Swagger UI** - Interactive API documentation at `/docs`
- **ReDoc** - Alternative documentation at `/redoc`
- **Response Models** - Typed request/response schemas for all endpoints

### Development & Quality
- **Unit Testing** - Comprehensive test suite using pytest with 100% coverage
- **Code Quality Tools** - Black, isort, flake8, and mypy for code formatting and linting
- **Configuration Management** - Environment-based configuration using Pydantic
- **Makefile** - Convenient commands for development and production

### DevOps & Deployment
- **GitHub Actions CI/CD** - Automated testing, linting, security scanning, and deployment
- **Docker Support** - Multi-stage containerized application with security best practices
- **Dependabot** - Automated dependency updates
- **Security Scanning** - Automated security vulnerability detection with safety and bandit

## 🏗️ Project Structure

```
ga-python-template/
├── app/                          # Main application package
│   ├── __init__.py
│   ├── main.py                   # FastAPI application with lifespan & middleware
│   ├── core/                     # Core configuration and utilities
│   │   ├── __init__.py
│   │   ├── config.py             # Application settings with environment detection
│   │   ├── resources.py          # Shared resources management (HTTP clients, etc.)
│   │   ├── middleware.py         # Request logging and correlation middleware
│   │   └── exceptions.py         # Global exception handlers
│   ├── schemas/                  # Pydantic models for API
│   │   ├── __init__.py
│   │   ├── common.py             # Common response schemas
│   │   └── hello.py              # Hello endpoint schemas
│   ├── services/                 # Business logic layer
│   │   ├── __init__.py
│   │   └── hello.py              # Hello world service
│   └── api/                      # API package
│       ├── __init__.py
│       └── v1/                   # API version 1
│           ├── __init__.py
│           ├── router.py         # Main API router
│           └── endpoints/        # API endpoints
│               ├── __init__.py
│               └── hello.py      # Hello world endpoint
├── tests/                        # Test package
│   ├── __init__.py
│   ├── conftest.py              # Pytest configuration and fixtures
│   ├── test_main.py             # Main application tests
│   └── test_hello.py            # Hello endpoint tests
├── .github/                      # GitHub Actions workflows
│   └── workflows/
│       ├── ci.yml               # Continuous Integration
│       ├── cd.yml               # Continuous Deployment
│       └── security.yml         # Security scanning
├── requirements.txt              # Python dependencies
├── pytest.ini                   # Pytest configuration
├── pyproject.toml               # Project configuration and tool settings
├── Makefile                     # Development and production commands
├── Dockerfile                   # Multi-stage Docker configuration
├── .gitignore                   # Git ignore rules
├── env.example                  # Environment variables example
└── README.md                    # This file
```

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd ga-python-template
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables (optional):**
   ```bash
   cp env.example .env
   # Edit .env with your preferred settings
   ```

## 🚀 Running the Application

### Development Server

```bash
# Using Makefile (recommended)
make dev

# Or using uvicorn directly
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Or using the Python module
python -m uvicorn app.main:app --reload
```

### Production Server

```bash
# Using Makefile (recommended)
make prod

# Or using gunicorn with uvicorn workers
gunicorn -w 2 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000 --keep-alive 5 --graceful-timeout 20 --access-logfile - --error-logfile - app.main:app
```

### Available Make Commands

```bash
make help          # Show all available commands
make install       # Install dependencies
make dev          # Run development server
make prod         # Run production server
make test         # Run tests
make test-cov     # Run tests with coverage
make lint         # Run linting (flake8, mypy)
make format       # Format code (black, isort)
make all-checks   # Run all quality checks
make clean        # Clean temporary files
```

## 🧪 Testing

### Run All Tests

```bash
pytest
```

### Run Tests with Coverage

```bash
pytest --cov=app
```

### Run Specific Test Files

```bash
pytest tests/test_hello.py
pytest tests/test_main.py
```

## 📚 API Documentation

Once the application is running, you can access:

- **Interactive API Documentation (Swagger UI):** http://localhost:8000/docs
- **Alternative API Documentation (ReDoc):** http://localhost:8000/redoc
- **OpenAPI JSON Schema:** http://localhost:8000/api/v1/openapi.json

## 🔗 Available Endpoints

### Main Endpoints

- `GET /` - Root endpoint with API information
- `GET /health` - Liveness probe (simple health check)
- `GET /health/ready` - Readiness probe (checks dependencies)
- `GET /metrics` - Prometheus metrics endpoint

### API v1 Endpoints

- `GET /api/v1/hello/world` - Hello world endpoint with service layer

### Documentation Endpoints

- `GET /docs` - Interactive Swagger UI documentation
- `GET /redoc` - Alternative ReDoc documentation
- `GET /api/v1/openapi.json` - OpenAPI 3.0 JSON schema

### Example Responses

**Root Endpoint:**
```json
{
  "message": "Welcome to GA Python Template API",
  "version": "0.1.0",
  "docs_url": "/docs"
}
```

**Health Check:**
```json
{
  "status": "healthy",
  "timestamp": "2024-01-01T12:00:00.000Z"
}
```

**Readiness Check:**
```json
{
  "status": "ready",
  "checks": {
    "http_client": "healthy",
    "application": "healthy"
  },
  "timestamp": "2024-01-01T12:00:00.000Z"
}
```

**Hello World:**
```json
{
  "message": "Hello, World!",
  "status": "success",
  "timestamp": "2024-01-01T12:00:00.000Z"
}
```

## 🛠️ Development Tools

### Code Quality

```bash
# Format code with Black
make format

# Run linting (flake8, mypy)
make lint

# Run all quality checks (format, lint, test)
make all-checks
```

### Individual Tools

```bash
# Format code with Black
black app tests

# Sort imports with isort
isort app tests

# Run flake8 linter
flake8 app tests

# Run mypy type checker
mypy app --ignore-missing-imports
```

## 🚀 GitHub Actions

This project includes comprehensive GitHub Actions workflows for CI/CD:

### Workflows

1. **CI Workflow** (`.github/workflows/ci.yml`)
   - Runs on every push and pull request
   - Tests across Python 3.8-3.12
   - Code formatting checks (Black, isort)
   - Linting (flake8, mypy)
   - Security scanning (safety, bandit)
   - Coverage reporting
   - Package building

2. **CD Workflow** (`.github/workflows/cd.yml`)
   - Runs on pushes to main/master branches
   - Builds and pushes Docker images to GitHub Container Registry
   - Creates GitHub releases for tags
   - Ready for cloud deployment

3. **Security Workflow** (`.github/workflows/security.yml`)
   - Weekly security scans
   - Dependency vulnerability checks
   - Code security analysis with Semgrep
   - Bandit security linting

### Dependabot

- Automated dependency updates for Python packages
- GitHub Actions updates
- Weekly schedule with Monday morning updates
- Automatic pull request creation

### Docker Support

The project includes Docker configuration:
- Multi-stage Dockerfile for optimized builds
- Health checks and security best practices
- Non-root user execution
- Production-ready configuration

## ⚙️ Configuration

The application uses Pydantic for configuration management. Key settings can be configured via environment variables:

### Core Settings
- `PROJECT_NAME` - Project name (default: "GA Python Template")
- `PROJECT_DESCRIPTION` - Project description
- `VERSION` - Application version (default: "0.1.0")
- `API_V1_STR` - API v1 prefix (default: "/api/v1")
- `HOST` - Server host (default: "0.0.0.0")
- `PORT` - Server port (default: 8000)
- `DEBUG` - Debug mode (default: false)

### Security & CORS
- `BACKEND_CORS_ORIGINS` - CORS allowed origins (default: "*", restricted in production)
- `ENVIRONMENT` - Environment (development/production, affects CORS and logging)

### API Documentation (Optional)
- `CONTACT_NAME` - API contact name
- `CONTACT_EMAIL` - API contact email
- `CONTACT_URL` - API contact URL
- `LICENSE_NAME` - API license name
- `LICENSE_URL` - API license URL
- `TERMS_OF_SERVICE` - Terms of service URL

### Production Features
- **Request Correlation**: Automatic request ID generation and logging
- **Metrics**: Prometheus metrics collection at `/metrics`
- **Health Checks**: Separate liveness and readiness probes
- **Error Handling**: Structured JSON error responses with correlation IDs
- **Resource Management**: Proper HTTP client pooling and connection management

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**gaelhuot** - *Initial work* - [GitHub Profile](https://github.com/gaelhuot)

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - The web framework used
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation and settings management
- [pytest](https://pytest.org/) - Testing framework
- [Black](https://black.readthedocs.io/) - Code formatter
- [isort](https://pycqa.github.io/isort/) - Import sorter
- [Prometheus](https://prometheus.io/) - Metrics collection
- [httpx](https://www.python-httpx.org/) - HTTP client library

## 🏆 Production Ready Features

This template includes enterprise-grade features:

- ✅ **Application Lifespan Management** - Proper startup/shutdown with resource cleanup
- ✅ **Structured Logging** - Request correlation with unique IDs for debugging
- ✅ **Global Error Handling** - Consistent JSON error responses
- ✅ **Health Monitoring** - Separate liveness and readiness probes for Kubernetes
- ✅ **Metrics Collection** - Prometheus metrics for monitoring and alerting
- ✅ **Security** - Production-ready CORS configuration and security headers
- ✅ **Clean Architecture** - Service layer separation for maintainable code
- ✅ **Type Safety** - Full type annotations with mypy validation
- ✅ **Testing** - Comprehensive test suite with 100% coverage
- ✅ **CI/CD** - Automated testing, linting, security scanning, and deployment

---

**Note:** This is a test development project for personal purposes.
