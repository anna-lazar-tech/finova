# Finova Architecture

## Overview

Finova is a modern Personal Finance Management Platform designed using Clean Architecture principles.

The application is separated into independent layers that simplify development, testing, and future scalability.

---

# System Architecture

Frontend

↓

React + Vite

↓

REST API

↓

FastAPI

↓

Service Layer

↓

Repository Layer

↓

SQLAlchemy ORM

↓

SQLite (PostgreSQL in future)

---

# Backend Layers

## API Layer

Responsibilities

- Receive HTTP requests
- Validate input
- Return responses
- Call services

Location

app/api

---

## Service Layer

Responsibilities

- Business logic
- Validation
- Financial calculations
- Orchestration

Location

app/services

---

## Repository Layer

Responsibilities

- Database access
- CRUD operations
- Queries

Location

app/repositories

---

## Model Layer

Responsibilities

- Database entities
- Relationships
- Constraints

Location

app/models

---

## Schema Layer

Responsibilities

- Request validation
- Response serialization

Location

app/schemas

---

## Core Layer

Responsibilities

- Configuration
- Database
- Security
- Common utilities

Location

app/core

---

# Current Domain Model

User

↓

Categories

↓

Operations

↓

Budgets

↓

Financial Goals

---

# Entity Relationships

User

├── Categories

├── Operations

├── Budgets

└── Financial Goals

Category

└── Operations

Operation

├── User

└── Category

Budget

├── User

└── Category

Goal

└── User

---

# Request Flow

Client

↓

FastAPI Router

↓

Service

↓

Repository

↓

Database

↓

Repository

↓

Service

↓

Response

---

# Design Principles

Finova follows:

- Clean Architecture
- SOLID
- DRY
- KISS
- REST API Design
- Separation of Concerns
- Type Safety
- Scalability
- Maintainability

---

# Future Extensions

The architecture is prepared for:

- PostgreSQL
- Docker
- Authentication (JWT)
- Refresh Tokens
- Redis
- Celery
- Background Jobs
- Email Notifications
- AI Services
- Mobile Application

---

# Technology Stack

Backend

- Python
- FastAPI
- SQLAlchemy
- Alembic
- SQLite

Frontend

- React
- Vite
- Axios
- Chart.js

Deployment

- Docker
- Nginx
- GitHub Actions

---

# Development Philosophy

Finova is not built as a simple expense tracker.

The goal is to create a scalable financial platform that helps users understand, manage, and improve their financial life.

Every feature should provide meaningful financial insights rather than simply displaying data.