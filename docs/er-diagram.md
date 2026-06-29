# Finova ER Diagram

## Version 1.0 Database Model

```mermaid
erDiagram
    USERS ||--o{ CATEGORIES : owns
    USERS ||--o{ OPERATIONS : creates
    USERS ||--o{ BUDGETS : owns
    USERS ||--o{ FINANCIAL_GOALS : owns

    CATEGORIES ||--o{ OPERATIONS : classifies
    CATEGORIES ||--o{ BUDGETS : limits

    USERS {
        int id PK
        string email
        string password_hash
        datetime created_at
    }

    CATEGORIES {
        int id PK
        string name
        string category_type
        string icon
        string color
        int user_id FK
        datetime created_at
    }

    OPERATIONS {
        int id PK
        float amount
        string operation_type
        string description
        date operation_date
        int user_id FK
        int category_id FK
        datetime created_at
        datetime updated_at
    }

    BUDGETS {
        int id PK
        float limit_amount
        int user_id FK
        int category_id FK
        date start_date
        date end_date
        datetime created_at
        datetime updated_at
    }

    FINANCIAL_GOALS {
        int id PK
        string name
        float target_amount
        float current_amount
        date target_date
        int user_id FK
        datetime created_at
        datetime updated_at
    }