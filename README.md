# RESTful Booker API Test Automation

![Python](https://img.shields.io/badge/python-3.x-blue)
![Pytest](https://img.shields.io/badge/tested%20with-pytest-green)
![API Testing](https://img.shields.io/badge/testing-API-orange)
![CI](https://img.shields.io/badge/CI-GitHub%20Actions-blue)
![Status](https://img.shields.io/badge/build-passing-brightgreen)
![Tests](https://github.com/KacperBlok1/restful-booker-api-test/actions/workflows/tests.yml/badge.svg)

Automated API test suite for the demo application:
https://restful-booker.herokuapp.com

This project demonstrates how to design and implement a **small but production-like API test automation framework** using **Python and pytest**.

The framework covers core REST API scenarios including authentication, CRUD operations, health checks, and negative testing, while also integrating **continuous integration via GitHub Actions**.

---

# 📊 Example Test Report

![Test Report](docs/report-example.png)

---

# 🚀 Tech Stack

| Tool           | Purpose                      |
| -------------- | ---------------------------- |
| Python 3.x     | Programming language         |
| pytest         | Test framework               |
| requests       | HTTP client for API calls    |
| pytest-html    | Generating HTML test reports |
| GitHub Actions | Continuous Integration       |

---

# 📁 Project Structure

```text
restful-booker-api-tests/

├── tests/
│   ├── auth/
│   │   └── test_auth.py
│   │
│   ├── bookings/
│   │   ├── test_bookings.py
│   │   └── test_crud_bookings.py
│   │
│   └── health/
│       └── test_health.py
│
├── utils/
│   └── config.py
│
├── reports/
│   └── report.html
│
├── conftest.py
├── requirements.txt
├── pytest.ini
│
└── .github/
    └── workflows/
        └── tests.yml
```

### Directory Overview

**tests/**
Contains all automated test cases grouped by feature.

**auth/**
Authentication tests including valid and invalid login scenarios.

**bookings/**
Tests for booking operations including list retrieval and full CRUD workflow.

**health/**
Basic API health verification.

**utils/**
Utility modules such as configuration and base URL settings.

**reports/**
Generated HTML reports from pytest runs.

**conftest.py**
Shared pytest fixtures (session handling, authentication tokens, base URL).

**GitHub Actions workflow**
CI pipeline configuration.

---

# 🧪 Test Design

The suite focuses on key areas of the **Restful Booker API**.

## Healthcheck

Endpoint:

```
GET /ping
```

Purpose:

* Verify that the API is available
* Basic smoke test for environment availability

---

## Authentication

Endpoint:

```
POST /auth
```

Covered scenarios:

* Valid login credentials
* Invalid username
* Invalid password
* Invalid credentials combination

---

## Bookings

Endpoints:

```
GET /booking
GET /booking/{id}
POST /booking
PUT /booking/{id}
DELETE /booking/{id}
```

### Booking listing

Retrieve all bookings using:

```
GET /booking
```

---

### Full CRUD workflow

The framework verifies a complete booking lifecycle.

**1️⃣ Create booking**

```
POST /booking
```

Create a booking with valid payload.

---

**2️⃣ Read booking**

```
GET /booking/{id}
```

Verify that the stored data matches the original request.

---

**3️⃣ Update booking**

```
PUT /booking/{id}
```

Update booking details using an authentication token.

---

**4️⃣ Delete booking**

```
DELETE /booking/{id}
```

Remove the booking and verify that it no longer exists.

---

# 🏷 Test Markers

Tests are organized using **pytest markers**.

| Marker     | Purpose                                              |
| ---------- | ---------------------------------------------------- |
| smoke      | Critical fast tests verifying main API functionality |
| regression | Extended scenarios such as full CRUD workflow        |
| negative   | Invalid inputs and error handling scenarios          |

Example:

```
pytest -m smoke
```

---

# ⚡ Running Tests Locally

## 1. Clone the repository

```
git clone https://github.com/KacperBlok1/restful-booker-api-test.git
cd restful-booker-api-test
```

---

## 2. (Optional) Create a virtual environment

```
python -m venv venv
```

Activate it:

Windows:

```
venv\Scripts\activate
```

Mac/Linux:

```
source venv/bin/activate
```

---

## 3. Install dependencies

```
pip install -r requirements.txt
```

---

## 4. Run all tests

```
pytest
```

---

## 5. Run only smoke tests

```
pytest -m smoke
```

---

## 6. Generate HTML report

```
pytest --html=reports/report.html --self-contained-html
```

Open:

```
reports/report.html
```

in your browser to view detailed test results.

---

# 🔁 Continuous Integration

This repository includes a **GitHub Actions CI pipeline**.

Workflow location:

```
.github/workflows/tests.yml
```

### Pipeline steps

Triggered on:

* push
* pull_request to main branch

Pipeline actions:

1. Sets up Python environment
2. Installs dependencies from requirements.txt
3. Runs the full pytest test suite
4. Generates HTML test report
5. Uploads the report as a build artifact

You can view the latest runs in the **Actions tab** of the repository.

---

# 👨‍💻 Author

**Kacper Blok**

Automation QA / Software Testing Portfolio Project
