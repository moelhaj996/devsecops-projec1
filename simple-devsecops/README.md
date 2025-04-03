# Simple DevSecOps Project

This project demonstrates a basic implementation of DevSecOps principles with a simple Flask web application and a CI/CD pipeline with integrated security checks.

## Features

- Simple Flask web API with secure coding practices
- Automated testing with pytest
- Security scanning integrated into CI/CD pipeline:
  - Static Application Security Testing (SAST) with Bandit
  - Dependency scanning with Safety
  - Container scanning with Trivy
- Secure Docker configuration

## Getting Started

### Prerequisites

- Python 3.9+
- Docker
- Git

### Local Development

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the application (choose one method):
   ```
   # Method 1: Using the run.py script
   python run.py
   
   # Method 2: Directly with the module
   python -m app.app
   
   # Method 3: Using Flask CLI
   export FLASK_APP=app.app
   flask run --host=0.0.0.0 --port=5000
   ```
4. Run tests:
   ```
   # Make sure you're in the project root directory
   pytest
   ```

### Running Security Checks Locally

1. Make the script executable:
   ```
   chmod +x run_security_checks.sh
   ```

2. Run all security checks at once:
   ```
   ./run_security_checks.sh
   ```

Or run individual checks:

1. SAST scanning:
   ```
   bandit -r app/
   ```
2. Dependency scanning:
   ```
   safety check -r requirements.txt
   ```

### Building and Running with Docker

1. Make the script executable:
   ```
   chmod +x docker_run.sh
   ```

2. Build and run with one command:
   ```
   ./docker_run.sh
   ```

Or manually:

```
docker build -t secure-app .
docker run -p 5000:5000 secure-app
```

## CI/CD Pipeline

The GitHub Actions workflow in `.github/workflows/ci-cd.yml` automatically runs:

1. Security scanning (SAST and dependency checks)
2. Unit tests with coverage
3. Docker build and container scanning

## Security Features

- Input validation to prevent injection attacks
- No sensitive data exposure
- Secure configuration management
- Running as non-root user in Docker
- Dependency vulnerability scanning
- Container security scanning

## Next Steps

To enhance this project, consider adding:

1. Dynamic Application Security Testing (DAST)
2. Secret management
3. Infrastructure as Code (IaC) security scanning
4. Compliance checks
5. Automated deployment with security gates

## Troubleshooting

If you encounter any issues, please refer to the [Troubleshooting Guide](TROUBLESHOOTING.md).