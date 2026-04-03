# ADLC Project 1

A full-stack project management application built with Python and FastAPI.

## Architecture

This project follows Clean Architecture principles:

```
src/
├── main.py          # Application entry point
├── config.py        # Configuration management
├── models.py        # Domain models (User, Project)
├── routes/          # REST API endpoints
│   ├── users.py
│   └── projects.py
├── services/        # Business logic layer
│   ├── auth.py
│   └── project.py
└── repositories/    # Data access layer
    ├── user_repo.py
    └── project_repo.py
```

## API Endpoints

### Authentication
| Method | Path | Description |
|--------|------|-------------|
| POST | `/api/v1/auth/login` | Login with email/password |
| POST | `/api/v1/auth/register` | Register new account |
| POST | `/api/v1/auth/refresh` | Refresh JWT token |

### Projects
| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/v1/projects` | List all projects |
| POST | `/api/v1/projects` | Create new project |
| GET | `/api/v1/projects/{id}` | Get project details |
| PUT | `/api/v1/projects/{id}` | Update project |
| DELETE | `/api/v1/projects/{id}` | Delete project |

### Users
| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/v1/users` | List users in org |
| GET | `/api/v1/users/{id}` | Get user profile |
| PUT | `/api/v1/users/{id}` | Update user profile |

## Tech Stack

- **Backend**: Python 3.12, FastAPI, SQLAlchemy 2.0
- **Database**: PostgreSQL 15 with async driver (asyncpg)
- **Cache**: Redis 7 for session management
- **Auth**: JWT with Keycloak integration
- **Testing**: pytest with pytest-asyncio
- **CI/CD**: Azure DevOps Pipelines

## Getting Started

### Prerequisites
- Python 3.12+
- PostgreSQL 15+
- Redis 7+

### Installation

```bash
# Clone the repository
git clone https://github.com/ngdev23/adlc-project-1.git
cd adlc-project-1

# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
alembic upgrade head

# Start the server
uvicorn src.main:app --reload --port 8000
```

### Environment Variables

```env
DATABASE_URL=postgresql+asyncpg://user:pass@localhost:5432/adlc_db
REDIS_URL=redis://localhost:6379/0
JWT_SECRET=your-secret-key
KEYCLOAK_URL=https://keycloak.example.com
```

## Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# Run only unit tests
pytest -m unit

# Run only integration tests
pytest -m integration
```

## Contributing

1. Create a feature branch: `git checkout -b feature/my-feature`
2. Make your changes
3. Run tests: `pytest`
4. Push and create a PR against `develop-adlc`

## License

MIT License - see LICENSE file for details.