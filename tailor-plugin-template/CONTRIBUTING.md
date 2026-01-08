# Contributing to This Plugin

Thank you for considering contributing to this plugin!

## Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-plugin.git
   cd your-plugin
   ```

2. Install development dependencies:
   ```bash
   pip install flake8 pytest pytest-asyncio
   ```

3. Run linting:
   ```bash
   flake8 main.py --max-line-length=100
   ```

4. Run tests:
   ```bash
   pytest tests/ -v
   ```

## Code Style

- Follow PEP 8 with max line length of 100
- Use type hints for all function signatures
- Use `self.logger` instead of `print()`
- Handle errors gracefully with try-except

## Pull Requests

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Make your changes
4. Run linting and tests
5. Commit with a descriptive message
6. Push and open a Pull Request

## Reporting Issues

Please include:
- Tailor version
- Plugin version
- Steps to reproduce
- Expected vs actual behavior
- Relevant logs
