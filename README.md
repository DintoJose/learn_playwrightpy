# learn_playwrightpy

A test automation portfolio project built with **Playwright + Python**, demonstrating end-to-end UI testing using the Page Object Model (POM) design pattern, AI-assisted test generation, and CI/CD integration via GitHub Actions.

Built as part of a self-directed transition from manual testing to test automation.

> **Note:** CI runs are blocked by Cloudflare bot protection on automationexercise.com. All tests pass fully in local execution. See [CI/CD](#️-cicd--github-actions) section for details.

---

## 🧪 What This Project Tests

The project automates test scenarios on [Automation Exercise](https://automationexercise.com) — a practice e-commerce site — covering:

- User login with valid and invalid credentials (parametrized)
- Homepage element visibility
- Product browsing and cart interactions
- End-to-end checkout flow (guest and authenticated)
- Contact form submission with file upload and browser dialog handling
- Positive and negative checkout scenarios

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| [Playwright](https://playwright.dev/python/) | Browser automation |
| [pytest](https://docs.pytest.org/) | Test framework |
| [pytest-playwright](https://pypi.org/project/pytest-playwright/) | Playwright pytest integration |
| [pytest-html](https://pypi.org/project/pytest-html/) | HTML test reports |
| [GitHub Copilot + Playwright MCP](https://playwright.dev/docs/mcp) | AI-assisted test and locator generation |
| [pytest-xdist](https://pypi.org/project/pytest-xdist/) | Parallel execution |
| Python 3.13 | Programming language |
| GitHub Actions | CI/CD pipeline |

---

## 📁 Project Structure

```
learn_playwrightpy/
├── .github/
│   └── workflows/
│       └── playwright.yml      # GitHub Actions CI/CD workflow
├── pages/                      # Page Object Model classes
│   ├── __init__.py
│   ├── AE_Homepage.py          # Homepage actions and locators
│   ├── AE_Loginpage.py         # Login page actions and locators
│   ├── AE_Productspage.py      # Products page actions and locators
│   ├── AE_Cartpage.py          # Cart page actions and locators
│   ├── AE_Checkoutpage.py      # Checkout page actions and locators
│   └── AE_Contactpage.py       # Contact form actions and locators
├── test_data/                  # External test data
│   ├── __init__.py
│   ├── test_credentials.py     # Valid and invalid login credentials
│   └── sample.txt              # Sample file for upload tests
├── tests/                      # Test files
│   ├── test_AEHome.py
│   ├── test_AELogin.py
│   ├── test_AEProducts.py
│   ├── test_AECart.py
│   └── test_AEContact.py
├── reports/                    # Generated HTML test reports
├── conftest.py                 # Shared fixtures, custom marks, global handlers
├── pytest.ini                  # Pytest configuration
├── requirements.txt            # Project dependencies
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

Test data is stored externally in `test_data/test_credentials.py` and passed into tests using `**kwargs` unpacking.

### Home Page Tests (`test_AEHome.py`)

- Verifies page title and key homepage elements are visible on load

### Products Tests (`test_AEProducts.py`)

- Verifies product listing navigation and product detail page load

### Cart Tests (`test_AECart.py`)

Three test scenarios covering the full cart and checkout flow:

| Test | Scenario | Expected Result |
|---|---|---|
| `test_cart_remove` | Add item → go to cart → remove item | Back to products link visible |
| `test_checkout_without_login` | Add item → attempt checkout as guest | Register/Login popup appears |
| `test_checkout_after_login` | Login → add item → checkout → place order | Payment page loads |

### Contact Form Tests (`test_AEContact.py`)

- Fills contact form with name, email, subject, and message
- Uploads a file using Playwright's `set_input_files()`
- Handles browser-level dialog (`page.on("dialog")`) triggered on submission
- Asserts success message visibility after form submission

> **Note:** This test is marked `@pytest.mark.headed_only` and skipped automatically in headless mode due to Cloudflare protection blocking form submission. Runs fully in headed mode.

---

## ⚙️ Setup and Installation

### Prerequisites

- Python 3.10+
- Git
- Node.js 18+ (for Playwright MCP)

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

Run all tests (headless by default):
```bash
pytest
```

Run in headed mode (required for contact form test):
```bash
pytest --headed
```

Run a specific test file:
```bash
pytest tests/test_AECart.py
```

Run with detailed output:
```bash
pytest -v -s
```

---

## 🤖 AI-Assisted Test Generation

This project uses **GitHub Copilot with Playwright MCP** (Model Context Protocol) to assist with test and locator generation:

- Playwright MCP connects Copilot to a live browser session, allowing it to read the actual DOM and accessibility tree rather than guessing page structure
- `AE_Contactpage.py` was generated using this workflow — Copilot navigated the contact page, identified elements, and produced the page class following the existing POM pattern
- AI-generated locators are verified against the live site before being committed — one locator (`contact_email`) required `exact=True` to disambiguate from a duplicate field, caught during test execution

---

## ⚠️ CI/CD & GitHub Actions

A GitHub Actions workflow (`.github/workflows/playwright.yml`) is configured to run on every push and pull request to `main`.

**Known issue:** The target site (automationexercise.com) is protected by Cloudflare, which blocks headless browser traffic from GitHub Actions' cloud IP ranges. This causes all tests to timeout in CI with a `"One moment, please..."` Cloudflare challenge page instead of the actual site.

This is an infrastructure constraint, not a code issue — all tests pass in local headed and headless execution. The CI pipeline itself (workflow triggers, dependency installation, browser setup, artifact upload) is correctly configured.

**Workaround documented:** The contact form test uses a custom `@pytest.mark.headed_only` mark with an `autouse` fixture in `conftest.py` to skip automatically in headless environments, demonstrating environment-aware test execution.

---

## 🧠 Key Concepts Demonstrated

- **Page Object Model (POM)** — 6 page classes separating locators and actions from test logic
- **End-to-end testing** — full user journeys across multiple pages and states
- **Parametrized testing** — `@pytest.mark.parametrize` for data-driven login scenarios
- **Pytest fixtures** — shared setup via `conftest.py` with `autouse` and scoped fixtures
- **Custom pytest marks** — `headed_only` mark with runtime environment detection via `request.config.getoption()`
- **Browser event handling** — `page.on("dialog")` for browser dialogs; `page.on("popup")` for ad suppression
- **File upload automation** — `set_input_files()` with hidden input pattern
- **AI-assisted generation** — GitHub Copilot + Playwright MCP for locator and page class generation
- **CI/CD pipeline** — GitHub Actions workflow with dependency caching and artifact upload
- **Negative testing** — explicit failure scenarios alongside happy path coverage

---

## 👤 Author

**Dinto Jose**
- GitHub: [@DintoJose](https://github.com/DintoJose)
- LinkedIn: [linkedin.com/in/dinto-jose-0426b31b5](https://linkedin.com/in/dinto-jose-0426b31b5)
- 3 years of manual QA experience, transitioning into test automation