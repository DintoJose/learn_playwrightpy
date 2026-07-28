# Playwright Python Test Generation Rules

## Language and Framework
- Python 3.14 with Playwright sync API (playwright.sync_api)
- Test framework: pytest with pytest-playwright
- Never use async/await — always use the sync API
- Never generate TypeScript or JavaScript, only Python scripts

## Project Structure
- Page classes live in pages/ — one file per page
- Test files live in tests/ — one file per feature or user flow
- Shared fixtures live in conftest.py at project root
- Test data (credentials, files) lives in test_data/
- Name page classes as AE<PageName>Page (e.g. AELoginPage, AECartPage)
- Name test files as test_AE<Feature>.py (e.g. test_AELogin.py)

## Page Object Model
- Every page class follows this exact pattern:
  from playwright.sync_api import Page
  
  class AE<PageName>Page:
      def __init__(self, page: Page):
          self.page = page
          self.element = page.get_by_role(...)
      
      def action(self):
          self.element.click()
- Locators defined in __init__, actions in methods
- Tests never call .click(), .fill() directly on locators — always through page class methods
- Every new page class needs a corresponding fixture in conftest.py

## Locators
- Always prefer get_by_role(), get_by_placeholder(), get_by_text(), get_by_label()
- Use exact=True when multiple similar elements exist on the same page
- Use page.locator() with stable attributes (name, id, data-testid) when semantic locators aren't available
- Never use CSS class selectors like page.locator('div.some-class')
- Never use XPath unless no other option exists

## Fixtures
- All page object fixtures live in conftest.py
- Follow this pattern for every new page class:
  @pytest.fixture
  def ae_<name>(page: Page):
      return AE<Name>Page(page)
- page fixture is overridden in conftest.py with ad-blocking route handler — do not modify it
- Use @pytest.mark.headed_only for any test that fails in headless mode due to Cloudflare blocking

## Waits and Timing
- Never use page.wait_for_timeout() or fixed delays
- Use wait_for_load_state('networkidle') after form submissions or navigations
- Register event listeners (page.on(), page.route()) before the action that triggers them
- Playwright auto-waits for element interactions — explicit waits only for page-level events and when necessary for flaky elements

## Test Data
- Credentials and reusable data live in test_data/test_credentials.py
- Use **kwargs unpacking to pass credentials into page methods
- Never hardcode credentials directly in test files
- Each test must be independent — never depend on state from a previous test

## Assertions
- Use Playwright's expect() for all assertions — never plain Python assert
- Prefer to_be_visible(), to_have_title(), to_have_text(), to_have_url()
- Use exact=True in assertions when partial matches could cause false positives
- Assert the final outcome, not intermediate states

## Browser Events
- Use page.on("dialog") for browser dialogs — register before the triggering action
- Use page.on("popup") for new browser windows — use page.expect_popup() when you need the popup object
- Use page.route() for network interception — register before the triggering action
- Use page.unroute() to remove route handlers after they are no longer needed

## CI/CD Awareness
- pytest.ini is configured for headless CI execution — never add --headed or --slowmo to pytest.ini
- Tests that require headed mode must be marked with @pytest.mark.headed_only
- GitHub Actions workflow exists in .github/workflows/playwright.yml