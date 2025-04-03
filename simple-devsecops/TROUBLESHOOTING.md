# Troubleshooting Guide

## Common Issues and Solutions

### Application Won't Start

1. **Module not found errors**:
   - Make sure you're running commands from the project root directory
   - Verify that the `app` directory contains `__init__.py`
   - Try installing dependencies again: `pip install -r requirements.txt`

2. **Port already in use**:
   - Change the port in `run.py` or use environment variable: `PORT=8080 python run.py`
   - Kill the process using the port: `lsof -i :5000` then `kill -9 PID`

### Tests Failing

1. **Import errors in tests**:
   - Make sure you have `__init__.py` in both `app` and `tests` directories
   - Run tests from the project root directory
   - Try with the `-s` flag for more verbose output: `pytest -s`

2. **Flask app context issues**:
   - Verify that the test fixture is correctly set up
   - Check that you're using the test client correctly

### Security Checks Failing

1. **Bandit errors**:
   - Review the specific security issues reported
   - Fix the issues or add appropriate comments to ignore false positives

2. **Safety check failures**:
   - Update dependencies to secure versions
   - If you can't update, consider adding mitigations

### Docker Issues

1. **Build failures**:
   - Check that Docker is installed and running
   - Verify that the Dockerfile syntax is correct
   - Make sure all required files are in the correct locations

2. **Container won't start**:
   - Check logs: `docker logs <container_id>`
   - Verify port mappings: `docker ps`
   - Make sure the application is configured to listen on 0.0.0.0

## Getting Help

If you continue to experience issues:

1. Check the project documentation
2. Look for similar issues in the project repository
3. Reach out to the project maintainers