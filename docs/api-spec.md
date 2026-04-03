# API Specification

## Authentication
All endpoints require Bearer JWT token in Authorization header.

## Endpoints

### GET /api/v1/health
Health check — returns 200 with {"status": "ok"}

### GET /api/v1/projects
List all projects for the authenticated user.
Query params: page (default 1), pageSize (default 20)

### POST /api/v1/projects
Create a new project.
Body: {"title": "string", "description": "string"}

### GET /api/v1/projects/{id}
Get project by ID. Returns 404 if not found.