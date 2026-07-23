# learn_playwrightpy

A test automation portfolio project built with **Playwright + Python**, demonstrating end-to-end UI testing using the Page Object Model (POM) design pattern.

Built as part of a self-directed transition from manual testing to test automation.

**NOTE: CI runs are blocked by Cloudflare bot protection on automationexercise.com. Tests pass fully in local execution.**

---

## 🧪 What This Project Tests

The project automates test scenarios on [Automation Exercise](https://automationexercise.com) — a practice e-commerce site — covering:

- User login (valid and invalid credentials)
- Homepage element visibility
- Product browsing and cart interactions
- Data-driven testing with parametrized test scenarios

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| [Playwright](https://playwright.dev/python/) | Browser automation |
| [pytest](https://docs.pytest.org/) | Test framework |
| [pytest-playwright](https://pypi.org/project/pytest-playwright/) | Playwright pytest integration |
| Python 3.14 | Programming language |

---

## 📁 Project Structure

```
learn_playwrightpy/
├── pages/                  # Page Object Model classes
│   ├── __init__.py
│   ├── AE_Loginpage.py     # Login page actions and locators
│   ├── AE_Homepage.py      # Home page actions and locators
│   ├── AE_Cartpage.py      # Cart page actions and locators
│   └── AE_Productspage.py  # Products page actions and locators
├── test_data/              # External test data
│   ├── __init__.py
│   └── test_credentials.py # Test credentials (valid and invalid users)
├── tests/                  # Test files
│   ├── test_AELogin.py
│   ├── test_AEHome.py
│   ├── test_AECart.py
│   └── test_AEProducts.py
├── conftest.py             # Shared pytest fixtures
├── requirements.txt        # Project dependencies
└── README.md
```

---

## 🔐 Test Scenarios

### Login Tests (`test_AELogin.py`)

Uses `@pytest.mark.parametrize` to run multiple credential sets from a single test function:

| Scenario | Credentials | Expected Result |
|---|---|---|
| Valid login | Valid email + password | "Logged in as {username}" visible |
| Invalid login | Invalid email + password | Login fails gracefully |

Test data is stored externally in `test_data/test_credentials.py` and passed into tests using `**kwargs` unpacking — keeping test logic clean and data easy to maintain.

### Home Page Tests (`test_AEHome.py`)
- Verifies key homepage elements are visible after login

### Products Tests (`test_AEProducts.py`)
- Verifies product listing and browsing functionality

### Cart Tests (`test_AECart.py`)
- Verifies cart interactions

---

## ⚙️ Setup and Installation

### Prerequisites
- Python 3.10+
- Git

### Steps

1. **Clone the repository**
```bash
git clone https://github.com/DintoJose/learn_playwrightpy.git
cd learn_playwrightpy
```

2. **Create and activate a virtual environment**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Install Playwright browsers**
```bash
playwright install
```

---

## ▶️ Running Tests

Run all tests:
```bash
pytest
```

Run a specific test file:
```bash
pytest tests/test_AELogin.py
```

Run in headed mode (see the browser):
```bash
pytest --headed
```

Run with detailed output:
```bash
pytest -v
```

Run with printed output visible:
```bash
pytest -s --verbose
```

---

## 🧠 Key Concepts Demonstrated

- **Page Object Model (POM)** — separates page locators and actions from test logic, making tests maintainable and scalable
- **Parametrized testing** — `@pytest.mark.parametrize` runs the same test with multiple data sets (valid + invalid login)
- **Data-driven testing** — test data stored externally in `test_data/` and passed into tests using `**kwargs` unpacking
- **pytest fixtures** — shared browser/page setup via `conftest.py`, keeping tests DRY
- **Playwright assertions** — using `expect()` for robust, auto-retrying element-level assertions
- **Negative testing** — explicitly testing failure scenarios alongside happy path tests
- **Clean project structure** — pages, tests, and data each in their own layer with clear separation of concerns

---

## 👤 Author

**Dinto Jose**
- GitHub: [@DintoJose](https://github.com/DintoJose)
- 3 years of manual QA experience, transitioning into test automation
