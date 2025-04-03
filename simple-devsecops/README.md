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
3. Run the application:
   ```
   python -m app.app
   ```
4. Run tests:
   ```
   pytest tests/
   ```

### Running Security Checks Locally

1. SAST scanning:
   ```
   bandit -r app/
   ```
2. Dependency scanning:
   ```
   safety check -r requirements.txt
   ```

### Building and Running with Docker

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