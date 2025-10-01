# GA Python Template

[![CI](https://github.com/gaelhuot/ga-python-template/actions/workflows/ci.yml/badge.svg)](https://github.com/gaelhuot/ga-python-template/actions/workflows/ci.yml)
[![Security Scan](https://github.com/gaelhuot/ga-python-template/actions/workflows/security.yml/badge.svg)](https://github.com/gaelhuot/ga-python-template/actions/workflows/security.yml)
[![Docker](https://github.com/gaelhuot/ga-python-template/actions/workflows/cd.yml/badge.svg)](https://github.com/gaelhuot/ga-python-template/actions/workflows/cd.yml)

A simple Python FastAPI template project for testing GitHub Actions and personal development purposes.

## 📋 Project Description

This project is a template for a Python FastAPI project that includes GitHub Actions for CI/CD, security scanning, and deployment. It is designed to be a starting point for new projects and to help developers test GitHub Actions and personal development purposes.

## 🚀 Features

- **FastAPI** - Modern, fast web framework for building APIs
- **Type Hints** - Full type annotation support for better code quality
- **Unit Testing** - Comprehensive test suite using pytest
- **Code Quality Tools** - Black, isort, flake8, and mypy for code formatting and linting
- **Configuration Management** - Environment-based configuration using Pydantic
- **API Documentation** - Automatic OpenAPI/Swagger documentation
- **CORS Support** - Cross-Origin Resource Sharing middleware
- **Health Checks** - Built-in health check endpoints
- **GitHub Actions CI/CD** - Automated testing, linting, security scanning, and deployment
- **Docker Support** - Containerized application with multi-stage builds
- **Dependabot** - Automated dependency updates
- **Security Scanning** - Automated security vulnerability detection

## 🏗️ Project Structure

```
ga-python-template/
├── app/                          # Main application package
│   ├── __init__.py
│   ├── main.py                   # FastAPI application entry point
│   ├── core/                     # Core configuration and utilities
│   │   ├── __init__.py
│   │   └── config.py             # Application settings
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
├── requirements.txt              # Python dependencies
├── pytest.ini                   # Pytest configuration
├── pyproject.toml               # Project configuration and tool settings
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
# Using uvicorn directly
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Or using the Python module
python -m uvicorn app.main:app --reload
```

### Production Server

```bash
# Using gunicorn with uvicorn workers
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
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

- `GET /` - Root endpoint with welcome message
- `GET /health` - Health check endpoint

### API v1 Endpoints

- `GET /api/v1/hello/world` - Hello world endpoint

### Example Response

```json
{
  "message": "Hello, World!",
  "status": "success"
}
```

## 🛠️ Development Tools

### Code Formatting

```bash
# Format code with Black
black app tests

# Sort imports with isort
isort app tests
```

### Linting

```bash
# Run flake8 linter
flake8 app tests

# Run mypy type checker
mypy app
```

### Run All Quality Checks

```bash
# Format, sort, and lint
black app tests && isort app tests && flake8 app tests && mypy app
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

- `PROJECT_NAME` - Project name (default: "GA Python Template")
- `PROJECT_DESCRIPTION` - Project description
- `VERSION` - Application version (default: "0.1.0")
- `API_V1_STR` - API v1 prefix (default: "/api/v1")
- `BACKEND_CORS_ORIGINS` - CORS allowed origins (default: "*")
- `HOST` - Server host (default: "0.0.0.0")
- `PORT` - Server port (default: 8000)
- `DEBUG` - Debug mode (default: false)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Gael** - *Initial work* - [GitHub Profile](https://github.com/gaelhuot)

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - The web framework used
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation and settings management
- [pytest](https://pytest.org/) - Testing framework
- [Black](https://black.readthedocs.io/) - Code formatter
- [isort](https://pycqa.github.io/isort/) - Import sorter

---

**Note:** This is a test development project for personal purposes.
